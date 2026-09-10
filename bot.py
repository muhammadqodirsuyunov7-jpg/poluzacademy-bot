#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🦉 POLUZACADEMY — POLYAKCHA BOT
Telegram orqali polyak tilini professional va interaktiv o'rganish.
Duolingo uslubida: darslar, testlar, audio talaffuz, BLIK/Karta to'lovlari.
"""

import logging
import sqlite3
import os
import sys
from datetime import date, datetime, timedelta

# Windows konsolida Unicode/emoji (cp1250) xatoliklarini oldini olish
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    ContextTypes, MessageHandler, filters
)
from lessons_a1 import A1_LESSONS
from lessons_a2 import A2_LESSONS
# .env faylni yuklash (agar mavjud bo'lsa)
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

import payments
import tts

# ═══════════════════════════════════════════
# SOZLAMALAR
# ═══════════════════════════════════════════
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8749989883:AAGX0RiQ32ExbIayYbevhxxBkDIxL-QEN0k")
DB_PATH   = "polyakcha.db"
ADMIN_IDS = [int(x.strip()) for x in os.environ.get("ADMIN_IDS", "1628696149,8022251674").split(",") if x.strip().isdigit()]

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ═══════════════════════════════════════════
# DARSLAR TARTIBI
# ═══════════════════════════════════════════
ALL_LESSONS = {**A1_LESSONS, **A2_LESSONS}

LESSON_ORDER = [
    "a1_l01","a1_l02","a1_l03","a1_l04","a1_l05",
    "a1_l06","a1_l07","a1_l08","a1_l09","a1_l10",
    "a1_l11","a1_l12","a1_l13","a1_l14","a1_l15",
    "a1_l16","a1_l17","a1_l18","a1_l19","a1_l20",
    "a2_l01","a2_l02","a2_l03","a2_l04","a2_l05",
    "a2_l06","a2_l07","a2_l08","a2_l09","a2_l10",
    "a2_l11","a2_l12","a2_l13","a2_l14","a2_l15",
    "a2_l16","a2_l17","a2_l18","a2_l19","a2_l20",
]

LEVELS = {
    "A1.1": [f"a1_l{str(i).zfill(2)}" for i in range(1, 11)],
    "A1.2": [f"a1_l{str(i).zfill(2)}" for i in range(11, 21)],
    "A2.1": [f"a2_l{str(i).zfill(2)}" for i in range(1, 11)],
    "A2.2": [f"a2_l{str(i).zfill(2)}" for i in range(11, 21)],
}

# ═══════════════════════════════════════════
# MA'LUMOTLAR BAZASI
# ═══════════════════════════════════════════
def init_db():
    payments.init_payment_db()
    con = sqlite3.connect(DB_PATH)
    con.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            user_id   INTEGER PRIMARY KEY,
            name      TEXT,
            xp        INTEGER DEFAULT 0,
            hearts    INTEGER DEFAULT 5,
            streak    INTEGER DEFAULT 0,
            last_date TEXT,
            reminder  TEXT,
            created_at TEXT
        );
        CREATE TABLE IF NOT EXISTS progress (
            user_id   INTEGER,
            lesson_id TEXT,
            done      INTEGER DEFAULT 0,
            score     INTEGER DEFAULT 0,
            PRIMARY KEY (user_id, lesson_id)
        );
        CREATE TABLE IF NOT EXISTS sessions (
            user_id   INTEGER PRIMARY KEY,
            lesson_id TEXT,
            ex_idx    INTEGER DEFAULT 0,
            lives     INTEGER DEFAULT 3,
            correct   INTEGER DEFAULT 0,
            wrong     INTEGER DEFAULT 0,
            xp_earned INTEGER DEFAULT 0
        );
    """)
    # Avtomatik migratsiya: agar users jadvalida created_at ustuni bo'lmasa, qo'shish
    cur = con.cursor()
    user_cols = [c[1] for c in cur.execute("PRAGMA table_info(users)").fetchall()]
    if "created_at" not in user_cols:
        cur.execute("ALTER TABLE users ADD COLUMN created_at TEXT")
    con.commit()
    con.close()

def db(query, args=(), fetch=None):
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(query, args)
    result = None
    if fetch == "one":
        result = cur.fetchone()
    elif fetch == "all":
        result = cur.fetchall()
    con.commit()
    con.close()
    return result

def get_user(uid):
    row = db("SELECT * FROM users WHERE user_id=?", (uid,), "one")
    return dict(row) if row else None

def ensure_user(uid, name):
    now = datetime.now().isoformat()
    db("INSERT OR IGNORE INTO users (user_id, name, created_at) VALUES (?, ?, ?)", (uid, name, now))

def upd_user(uid, **kw):
    sets = ", ".join(f"{k}=?" for k in kw)
    db(f"UPDATE users SET {sets} WHERE user_id=?", (*kw.values(), uid))

def done_lessons(uid):
    rows = db("SELECT lesson_id FROM progress WHERE user_id=? AND done=1", (uid,), "all")
    return [r["lesson_id"] for r in rows] if rows else []

def can_access_lesson(uid, lid):
    idx = LESSON_ORDER.index(lid) if lid in LESSON_ORDER else -1
    if idx == -1:
        return False, "locked"
    
    # 1. Premium tekshiruvi (dastlabki 5 ta darsdan keyin)
    if not payments.can_access_lesson(uid, lid):
        return False, "premium_required"
        
    # 2. Ketma-ketlik tekshiruvi (oldingi dars o'tilgan bo'lishi kerak)
    if idx == 0:
        return True, "open"
    prev_lid = LESSON_ORDER[idx - 1]
    done = done_lessons(uid)
    if prev_lid not in done:
        return False, "prev_not_done"
    return True, "open"

def mark_done(uid, lid, score):
    db("""INSERT INTO progress(user_id,lesson_id,done,score) VALUES(?,?,1,?)
          ON CONFLICT(user_id,lesson_id) DO UPDATE SET done=1,score=MAX(score,?)""",
       (uid, lid, score, score))

def get_ses(uid):
    row = db("SELECT * FROM sessions WHERE user_id=?", (uid,), "one")
    return dict(row) if row else None

def new_ses(uid, lid):
    # Premium foydalanuvchilar cheksiz yurakka ega (5 ta jon beriladi)
    lives = 5 if payments.is_premium(uid) else 3
    db("""INSERT INTO sessions(user_id,lesson_id,ex_idx,lives,correct,wrong,xp_earned)
          VALUES(?,?,0,?,0,0,0)
          ON CONFLICT(user_id) DO UPDATE SET
          lesson_id=?,ex_idx=0,lives=?,correct=0,wrong=0,xp_earned=0""",
       (uid, lid, lives, lid, lives))

def upd_ses(uid, **kw):
    sets = ", ".join(f"{k}=?" for k in kw)
    db(f"UPDATE sessions SET {sets} WHERE user_id=?", (*kw.values(), uid))

def refresh_streak(uid):
    u = get_user(uid)
    if not u: return
    today = date.today().isoformat()
    if u.get("last_date") == today: return
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    streak = (u.get("streak", 0) + 1) if u.get("last_date") == yesterday else 1
    upd_user(uid, streak=streak, last_date=today)

# ═══════════════════════════════════════════
# YORDAMCHI FUNKSIYALAR
# ═══════════════════════════════════════════
def hbar(lives, max_lives=3):
    return "❤️" * lives + "🖤" * max(0, max_lives - lives)

def pbar(done, total):
    pct = int(done / total * 100) if total else 0
    filled = pct // 10
    return f"`[{'▓'*filled}{'░'*(10-filled)}]` {pct}%"

def stars(lives):
    return "⭐⭐⭐" if lives >= 3 else "⭐⭐" if lives == 2 else "⭐"

def lesson(lid):
    return ALL_LESSONS.get(lid, {})

def level_progress(uid):
    done = done_lessons(uid)
    result = {}
    for lvl, ids in LEVELS.items():
        result[lvl] = sum(1 for i in ids if i in done)
    return result

# ═══════════════════════════════════════════
# KLAVIATURALAR
# ═══════════════════════════════════════════
def kb_main(uid: int = None):
    prem_label = "💎 Premium Obuna"
    if uid and payments.is_premium(uid):
        prem_label = "💎 Premium (Faol ✅)"

    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📚 Darslar",    callback_data="lessons"),
         InlineKeyboardButton("📖 Lug'at",     callback_data="vocab_menu")],
        [InlineKeyboardButton("📊 Progressim", callback_data="progress"),
         InlineKeyboardButton("⏰ Eslatma",    callback_data="reminder_menu")],
        [InlineKeyboardButton(prem_label,      callback_data="premium_menu"),
         InlineKeyboardButton("ℹ️ Kurs haqida", callback_data="about")],
        [InlineKeyboardButton("❓ Yordam",      callback_data="help")],
    ])

def kb_lessons(uid):
    done = done_lessons(uid)
    is_prem = payments.is_premium(uid)
    rows = []
    for lvl, ids in LEVELS.items():
        n_done = sum(1 for i in ids if i in done)
        # Agar bepul bo'lmagan daraja bo'lsa va premium bo'lmasa qulf belgisi
        badge = "💎 " if (lvl != "A1.1" and not is_prem) else "📗 "
        rows.append([InlineKeyboardButton(
            f"{badge}{lvl} — {n_done}/{len(ids)} ✅",
            callback_data=f"level:{lvl}"
        )])
    rows.append([InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")])
    return InlineKeyboardMarkup(rows)

def kb_level(lvl, uid):
    done = done_lessons(uid)
    ids  = LEVELS[lvl]
    is_prem = payments.is_premium(uid)
    rows = []
    for i, lid in enumerate(ids):
        les  = lesson(lid)
        is_free = lid in payments.BEPUL_DARSLAR
        
        if lid in done:
            icon = "✅ "
        elif not is_free and not is_prem:
            icon = "💎🔒 " # Premium dars
        elif i == 0 or LESSON_ORDER[LESSON_ORDER.index(lid)-1] in done:
            icon = "▶️ "  # Ochiq dars
        else:
            icon = "🔒 "  # Oldingi dars o'tilmagan

        free_badge = " [Bepul]" if is_free else ""
        rows.append([InlineKeyboardButton(
            f"{icon}{les.get('emoji','📘')} {les.get('title',lid)}{free_badge}",
            callback_data=f"lesson:{lid}"
        )])
    rows.append([InlineKeyboardButton("◀️ Darslarga", callback_data="lessons")])
    return InlineKeyboardMarkup(rows)

def kb_lesson_detail(lid, uid):
    done = done_lessons(uid)
    rows = [
        [InlineKeyboardButton("🔊 Lug'atni eshitish", callback_data=f"audio_vocab:{lid}"),
         InlineKeyboardButton("📖 Lug'at", callback_data=f"vocab:{lid}")],
        [InlineKeyboardButton("📝 Grammatika", callback_data=f"grammar:{lid}"),
         InlineKeyboardButton("💬 Dialog", callback_data=f"dialog:{lid}")],
        [InlineKeyboardButton("▶️ Darsni boshlash", callback_data=f"go:{lid}")],
    ]
    if lid in done:
        rows.append([InlineKeyboardButton("🔁 Qayta ishlash", callback_data=f"go:{lid}")])
    rows.append([InlineKeyboardButton("◀️ Orqaga", callback_data=f"back_level:{lid}")])
    return InlineKeyboardMarkup(rows)

def kb_exercise(opts, ex_idx):
    letters = ["🅐","🅑","🅒","🅓"]
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(f"{letters[i]}  {opt}",
                              callback_data=f"ans:{ex_idx}:{i}")]
        for i, opt in enumerate(opts)
    ])

def kb_after_lesson(lid):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("▶️ Keyingi dars",   callback_data="lessons")],
        [InlineKeyboardButton("🔁 Qayta ishlash",  callback_data=f"go:{lid}")],
        [InlineKeyboardButton("📚 Darslar",        callback_data="lessons"),
         InlineKeyboardButton("🏠 Bosh menyu",     callback_data="main")],
    ])

def kb_vocab_menu():
    rows = []
    for lvl, ids in LEVELS.items():
        rows.append([InlineKeyboardButton(f"📗 {lvl}", callback_data=f"vocab_level:{lvl}")])
    rows.append([InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")])
    return InlineKeyboardMarkup(rows)

# ═══════════════════════════════════════════
# /START
# ═══════════════════════════════════════════
async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    ensure_user(u.id, u.first_name)

    # To'lovdan qaytgandagi linklarni tekshirish (/start success_oylik_12345 yoki simpay_oylik)
    args = ctx.args
    if args and len(args) > 0:
        arg = args[0]
        if arg.startswith("success_") or arg.startswith("simpay_"):
            parts = arg.split("_")
            plan = parts[1] if len(parts) > 1 else "oylik"
            exp = payments.activate_premium(u.id, plan, f"stripe_{arg}", payments.NARXLAR.get(plan, {}).get("narx", 2499))
            await update.message.reply_text(
                "🎉 *Tabriklaymiz! To'lovingiz muvaffaqiyatli qabul qilindi!*\n\n"
                f"💎 Sizning *{plan.capitalize()}* Premium obunangiz faollashtirildi.\n"
                f"📅 Tugash sanasi: *{exp.strftime('%d.%m.%Y')}*\n\n"
                "Endi barcha 40+ darslar, ovozli talaffuzlar va audio darslar siz uchun ochiq!",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("📚 Darslarni boshlash", callback_data="lessons")]
                ])
            )
            return

    is_prem = payments.is_premium(u.id)
    status_badge = "💎 *Premium Foydalanuvchi*" if is_prem else "🆓 *Dastlabki 5 ta dars bepul!*"

    text = (
        f"🦉 *Assalomu alaykum, {u.first_name}!*\n"
        f"*PolUzAcademy Botiga xush kelibsiz!*\n\n"
        "Bu bot orqali siz *polyak tilini* amaliy hayotda kerak bo'ladigan darajada "
        "interaktiv o'yinlar, testlar va *🔊 jonli polyakcha ovozli talaffuz* orqali o'rganasiz!\n\n"
        f"⭐️ Holatingiz: {status_badge}\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "📚 *Kurs tarkibi:*\n"
        "🟢 *A1.1* — Boshlang'ich muloqot *(10 dars — 1-5 darslar bepul!)*\n"
        "🔵 *A1.2* — Kundalik hayot, Do'kon, Ish *(10 dars)*\n"
        "🟡 *A2.1* — Urząd, Hujjatlar, Ijara *(10 dars)*\n"
        "🔴 *A2.2* — Shifokor, Ish muloqoti, Transport *(10 dars)*\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🎮 *O'yin va O'rganish tizimi:*\n"
        "🔊 *Ovozli talaffuz* — so'z va dialoglarni tinglang\n"
        "⭐ *XP ballar* — har to'g'ri javob uchun +10 ball\n"
        "❤️ *Yuraklar* — xatolar hisoblanadi\n"
        "🔥 *Streak* — ketma-ket o'rganish kunlari\n\n"
        "⬇️ *Quyidagi tugmani bosing va boshlang!*"
    )
    await update.message.reply_text(
        text, parse_mode="Markdown", reply_markup=kb_main(u.id)
    )

# ═══════════════════════════════════════════
# ASOSIY CALLBACK HANDLER
# ═══════════════════════════════════════════
async def on_cb(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q   = update.callback_query
    uid = q.from_user.id
    d   = q.data
    await q.answer()

    # ── To'lov bilan bog'liq callbacklar ────────────
    if d in ["premium_menu", "buy_oylik", "buy_3oylik", "buy_yillik", "premium_renew", "premium_info", "promo_code"]:
        await payments.payment_callback(update, ctx)
        return

    # ── Bosh menyu ──────────────────────────────────
    if d == "main":
        u = get_user(uid) or {}
        lvl_p = level_progress(uid)
        is_prem = payments.is_premium(uid)
        status_txt = "💎 Premium Obunachi ✅" if is_prem else "🆓 Bepul versiya"

        text = (
            f"🦉 *PolUzAcademy — Bosh Menyu*\n\n"
            f"👤 *{q.from_user.first_name}* ({status_txt})\n\n"
            f"🔥 Streak: *{u.get('streak',0)} kun*\n"
            f"⭐ XP: *{u.get('xp',0)}*\n"
            f"❤️ Yuraklar: *{u.get('hearts',5)}/5*\n\n"
            f"📗 A1.1: *{lvl_p.get('A1.1',0)}/10* dars\n"
            f"📘 A1.2: *{lvl_p.get('A1.2',0)}/10* dars\n"
            f"📙 A2.1: *{lvl_p.get('A2.1',0)}/10* dars\n"
            f"📕 A2.2: *{lvl_p.get('A2.2',0)}/10* dars\n\n"
            "Nima qilamiz?"
        )
        await q.edit_message_text(text, parse_mode="Markdown", reply_markup=kb_main(uid))

    # ── Kurs haqida ─────────────────────────────────
    elif d == "about":
        text = (
            "ℹ️ *PolUzAcademy Kursi haqida*\n\n"
            "Bu kurs *Polshada yashovchi, ishlayotgan va o'qiyotgan vatandoshlarimiz*\n"
            "uchun polyak tilini 0 dan erkin muloqot darajasigacha o'rgatish uchun yaratilgan.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📗 *A1.1 — Boshlang'ich muloqot* (10 dars)\n"
            "• Salomlashish, alifbo, talaffuz\n"
            "• Tanishuv, oila, kasblar, sonlar\n"
            "• *(1-5 darslar mutlaqo bepul)*\n\n"
            "📘 *A1.2 — Kundalik hayot* (10 dars)\n"
            "• Ovqat, do'kon, supermarket\n"
            "• Shahar transporti, chiptalar, yo'l so'rash\n"
            "• Bank, valyuta, xaridlar\n\n"
            "📙 *A2.1 — Mustaqil hayot va Hujjatlar* (10 dars)\n"
            "• Urząd (idora) va Karta Pobytu muloqoti\n"
            "• Uy ijarasi va shartnomalar\n"
            "• Ish topish va rezyume topshirish\n\n"
            "📕 *A2.2 — Professional muloqot* (10 dars)\n"
            "• Shifokor va dorixona\n"
            "• Ishxonada rahbariyat bilan muloqot\n"
            "• Muammoli vaziyatlarni hal qilish\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎓 *Har bir darsda:*\n"
            "🔊 15 ta yangi so'z + Jonli audio talaffuz\n"
            "📝 Aniq va sodda grammatika\n"
            "💬 Haqiqiy polyakcha dialog + Audio\n"
            "🧪 10 ta qiziqarli test savoli"
        )
        await q.edit_message_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📚 Darslarni boshlash", callback_data="lessons")],
                [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
            ]))

    # ── Darslar (daraja tanlash) ─────────────────────
    elif d == "lessons":
        text = "📚 *Darslar ro'yxati*\n\nO'rganmoqchi bo'lgan darajangizni tanlang:"
        await q.edit_message_text(text, parse_mode="Markdown", reply_markup=kb_lessons(uid))

    # ── Daraja ichidagi darslar ──────────────────────
    elif d.startswith("level:"):
        lvl = d[6:]
        ids = LEVELS.get(lvl, [])
        done = done_lessons(uid)
        n_done = sum(1 for i in ids if i in done)
        text = (
            f"📗 *{lvl} — Darslar ro'yxati*\n\n"
            f"{pbar(n_done, len(ids))}\n"
            f"Tugatilgan: *{n_done}/{len(ids)}*\n\n"
            "Darsni tanlang:"
        )
        await q.edit_message_text(text, parse_mode="Markdown", reply_markup=kb_level(lvl, uid))

    # ── Alohida dars detali ─────────────────────────
    elif d.startswith("lesson:"):
        lid  = d[7:]
        les  = lesson(lid)
        ok, reason = can_access_lesson(uid, lid)

        # Agar Premium talab qilinsa
        if reason == "premium_required":
            text = (
                "🔒 *Ushbu dars faqat Premium obunachilar uchun!*\n\n"
                "🎉 Siz dastlabki 5 ta bepul darsni ko'rib chiqdingiz.\n"
                "Kursni to'liq davom ettirish va barcha 40+ darslar, "
                "jonli audio talaffuz hamda testlarga ega bo'lish uchun Premium obunani faollashtiring!\n\n"
                "💰 *Tariflar:*\n"
                "• 💳 **1 Oylik:** `24.99 zł / oy`\n"
                "• ⭐ **3 Oylik:** `59.99 zł` _(20% tejash)_\n"
                "• 👑 **1 Yillik:** `179.99 zł` _(40% tejash)_\n\n"
                "To'lov: **BLIK** yoki **Karta** orqali ⚡️"
            )
            await q.edit_message_text(
                text,
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("💎 Premium obunani olish", callback_data="premium_menu")],
                    [InlineKeyboardButton("◀️ Darslarga qaytish", callback_data="lessons")]
                ])
            )
            return

        if reason == "prev_not_done":
            idx = LESSON_ORDER.index(lid)
            prev = lesson(LESSON_ORDER[idx - 1])
            await q.edit_message_text(
                f"🔒 *Bu dars hali qulfli!*\n\n"
                f"Avval bu darsni tugatib keling:\n"
                f"*{prev.get('emoji','')} {prev.get('title','')}* 📚",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(
                        f"▶️ {prev.get('emoji','')} {prev.get('title','')}",
                        callback_data=f"lesson:{LESSON_ORDER[idx-1]}"
                    )],
                    [InlineKeyboardButton("◀️ Orqaga", callback_data="lessons")]
                ])
            )
            return

        done = done_lessons(uid)
        status = "✅ *Tugatilgan!*" if lid in done else "🔓 Boshlashga tayyor"
        text = (
            f"{les.get('emoji','📘')} *{les.get('title',lid)}*\n"
            f"📗 Daraja: *{les.get('level','A1')}*\n\n"
            f"📚 So'zlar: *{len(les.get('vocab',[]))} ta* (Ovozli)\n"
            f"🧪 Testlar: *{len(les.get('exercises',[]))} ta*\n"
            f"⭐ Mukofot: *+{len(les.get('exercises',[]))*10} XP*\n\n"
            f"{status}\n\n"
            "📖 Avval lug'at va grammatikani ko'ring, talaffuzni tinglang,\n"
            "so'ngra darsni boshlang!"
        )
        await q.edit_message_text(text, parse_mode="Markdown", reply_markup=kb_lesson_detail(lid, uid))

    # ── Orqaga (daraja sahifasiga) ───────────────────
    elif d.startswith("back_level:"):
        lid = d[11:]
        lvl = lesson(lid).get("level", "A1.1")
        ids = LEVELS.get(lvl, [])
        done = done_lessons(uid)
        n_done = sum(1 for i in ids if i in done)
        text = (
            f"📗 *{lvl} — Darslar ro'yxati*\n\n"
            f"{pbar(n_done, len(ids))}\n"
            f"Tugatilgan: *{n_done}/{len(ids)}*\n\n"
            "Darsni tanlang:"
        )
        await q.edit_message_text(text, parse_mode="Markdown", reply_markup=kb_level(lvl, uid))

    # ── Grammatika ──────────────────────────────────
    elif d.startswith("grammar:"):
        lid = d[8:]
        les = lesson(lid)
        text = les.get("grammar", "Grammatika mavjud emas.")
        await q.edit_message_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("▶️ Darsni boshlash", callback_data=f"go:{lid}")],
                [InlineKeyboardButton("◀️ Orqaga", callback_data=f"lesson:{lid}")]
            ]))

    # ── Dialog ──────────────────────────────────────
    elif d.startswith("dialog:"):
        lid = d[7:]
        les = lesson(lid)
        text = les.get("dialog", "Dialog mavjud emas.")
        await q.edit_message_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔊 Dialogni audio eshitish", callback_data=f"audio_dialog:{lid}")],
                [InlineKeyboardButton("▶️ Darsni boshlash", callback_data=f"go:{lid}")],
                [InlineKeyboardButton("◀️ Orqaga", callback_data=f"lesson:{lid}")]
            ]))

    # ── Lug'at (alohida dars) ───────────────────────
    elif d.startswith("vocab:"):
        lid  = d[6:]
        les  = lesson(lid)
        vocab = les.get("vocab", [])
        text = f"📖 *{les.get('emoji','')} {les.get('title','')} — Lug'at*\n\n"
        for i, w in enumerate(vocab, 1):
            text += (
                f"*{i}.* 🇵🇱 `{w['pl']}`\n"
                f"    🔊 _{w['ph']}_\n"
                f"    🇺🇿 {w['uz']}\n\n"
            )
        await q.edit_message_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔊 So'zlarni audio eshitish", callback_data=f"audio_vocab:{lid}")],
                [InlineKeyboardButton("📝 Grammatika", callback_data=f"grammar:{lid}"),
                 InlineKeyboardButton("💬 Dialog", callback_data=f"dialog:{lid}")],
                [InlineKeyboardButton("▶️ Darsni boshlash", callback_data=f"go:{lid}")],
                [InlineKeyboardButton("◀️ Orqaga", callback_data=f"lesson:{lid}")]
            ]))

    # ── Audio Talaffuz (TTS) ────────────────────────
    elif d.startswith("audio_vocab:"):
        lid = d[12:]
        les = lesson(lid)
        vocab = les.get("vocab", [])
        if vocab:
            await q.answer("🔊 Audio tayyorlanmoqda...")
            audio_path = await tts.generate_vocab_audio(vocab)
            if audio_path and os.path.exists(audio_path):
                with open(audio_path, "rb") as af:
                    await ctx.bot.send_voice(
                        chat_id=uid,
                        voice=af,
                        caption=f"🦉 *{les.get('emoji','')} {les.get('title','')}* — Lug'at so'zlari talaffuzi (Polyakcha)",
                        parse_mode="Markdown"
                    )
            else:
                await q.answer("Ovoz hosil qilishda xatolik!", show_alert=True)
        else:
            await q.answer("Lug'at topilmadi!", show_alert=True)

    elif d.startswith("audio_dialog:"):
        lid = d[13:]
        les = lesson(lid)
        dialog_text = les.get("dialog", "")
        if dialog_text:
            await q.answer("🔊 Dialog audiosi tayyorlanmoqda...")
            # Dialogdagi faqat polyakcha qismlarni ovozga aylantirish
            lines = [l.split(":", 1)[1].strip() for l in dialog_text.split("\n") if ":" in l and ("🧑" in l or "🏪" in l or "👨" in l or "👩" in l or "🇵🇱" in l)]
            clean_diag = ". ".join(lines) if lines else dialog_text
            audio_path = await tts.generate_speech(clean_diag)
            if audio_path and os.path.exists(audio_path):
                with open(audio_path, "rb") as af:
                    await ctx.bot.send_voice(
                        chat_id=uid,
                        voice=af,
                        caption=f"🦉 *{les.get('emoji','')} {les.get('title','')}* — Dialog talaffuzi",
                        parse_mode="Markdown"
                    )
            else:
                await q.answer("Ovoz hosil qilishda xatolik!", show_alert=True)
        else:
            await q.answer("Dialog topilmadi!", show_alert=True)

    # ── Lug'at menyu ────────────────────────────────
    elif d == "vocab_menu":
        await q.edit_message_text(
            "📖 *Lug'at — Darajani tanlang:*",
            parse_mode="Markdown",
            reply_markup=kb_vocab_menu()
        )

    elif d.startswith("vocab_level:"):
        lvl  = d[12:]
        ids  = LEVELS.get(lvl, [])
        rows = []
        for lid in ids:
            les = lesson(lid)
            rows.append([InlineKeyboardButton(
                f"{les.get('emoji','')} {les.get('title',lid)}",
                callback_data=f"vocab:{lid}"
            )])
        rows.append([InlineKeyboardButton("◀️ Orqaga", callback_data="vocab_menu")])
        await q.edit_message_text(
            f"📖 *{lvl} — Lug'at, darsni tanlang:*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(rows)
        )

    # ── Darsni boshlash ─────────────────────────────
    elif d.startswith("go:"):
        lid = d[3:]
        ok, reason = can_access_lesson(uid, lid)
        if reason == "premium_required":
            await q.edit_message_text(
                "🔒 *Bu dars faqat Premium obunachilar uchun!*\n\n"
                "Davom etish uchun Premium obunani faollashtiring.",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("💎 Premium olish (24.99 zł)", callback_data="premium_menu")],
                    [InlineKeyboardButton("◀️ Orqaga", callback_data="lessons")]
                ])
            )
            return
        if reason == "prev_not_done":
            idx = LESSON_ORDER.index(lid)
            prev = lesson(LESSON_ORDER[idx - 1])
            await q.edit_message_text(
                f"🔒 *Bu dars hali qulfli!*\n\n"
                f"Avval bu darsni tugatib keling:\n"
                f"*{prev.get('emoji','')} {prev.get('title','')}* 📚",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(
                        f"▶️ {prev.get('emoji','')} {prev.get('title','')}",
                        callback_data=f"lesson:{LESSON_ORDER[idx-1]}"
                    )],
                    [InlineKeyboardButton("◀️ Orqaga", callback_data="lessons")]
                ])
            )
            return
        new_ses(uid, lid)
        refresh_streak(uid)
        max_lives = 5 if payments.is_premium(uid) else 3
        await show_ex(q, uid, lid, 0, max_lives)

    # ── Test Javobi ─────────────────────────────────
    elif d.startswith("ans:"):
        _, ex_s, ch_s = d.split(":")
        ex_idx = int(ex_s)
        choice = int(ch_s)

        ses = get_ses(uid)
        if not ses:
            await q.edit_message_text("⚠️ Sessiya topilmadi. /start bosing.")
            return

        lid  = ses["lesson_id"]
        les  = lesson(lid)
        exs  = les.get("exercises", [])

        if ex_idx >= len(exs):
            return

        ex      = exs[ex_idx]
        correct = ex["ans"]
        is_ok   = (choice == correct)

        lives    = ses["lives"]
        corr_cnt = ses["correct"]
        wrng_cnt = ses["wrong"]
        xp_earn  = ses["xp_earned"]
        is_prem  = payments.is_premium(uid)

        if is_ok:
            corr_cnt += 1
            xp_earn  += 10
            result = "✅ *To'g'ri!* +10 ⭐"
        else:
            # Agar Premium bo'lsa jon kamaymaydi yoki ko'proq bo'ladi
            if not is_prem:
                lives -= 1
            wrng_cnt += 1
            result = f"❌ *Xato!*  To'g'ri javob: *{ex['opts'][correct]}*"

        next_idx = ex_idx + 1
        upd_ses(uid, ex_idx=next_idx, lives=lives,
                correct=corr_cnt, wrong=wrng_cnt, xp_earned=xp_earn)

        opts_txt = "\n".join(
            f"{'✅' if i==correct else ('❌' if i==choice and not is_ok else '◾')}  {opt}"
            for i, opt in enumerate(ex["opts"])
        )
        max_h = 5 if is_prem else 3
        res_txt = (
            f"{hbar(lives, max_h)}\n"
            f"{pbar(ex_idx+1, len(exs))}\n\n"
            f"{ex['q']}\n\n"
            f"{opts_txt}\n\n"
            f"{result}"
        )

        # Yuraklar tugadi
        if lives <= 0 and not is_prem:
            u     = get_user(uid)
            new_h = max(0, (u.get("hearts") or 5) - 1)
            upd_user(uid, hearts=new_h)
            final = (
                f"{res_txt}\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"💔 *Yuraklaringiz tugadi!*\n\n"
                f"✅ To'g'ri javoblar: *{corr_cnt}*\n"
                f"❌ Xatolar: *{wrng_cnt}*\n"
                f"⭐ To'plangan ball: *+{xp_earn}*\n\n"
                f"❤️ Qolgan yuraklar: *{new_h}/5*\n\n"
                "💡 *Maslahat:* Premium obuna bilan cheksiz yuraklarga ega bo'ling!"
            )
            await q.edit_message_text(
                final, parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔁 Qayta urinish", callback_data=f"go:{lid}")],
                    [InlineKeyboardButton("💎 Cheksiz yuraklar (Premium)", callback_data="premium_menu")],
                    [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")],
                ])
            )
            return

        # Dars muvaffaqiyatli yakunlandi
        if next_idx >= len(exs):
            pct = int(corr_cnt / len(exs) * 100)
            u   = get_user(uid)
            upd_user(uid, xp=(u.get("xp",0) + xp_earn))
            mark_done(uid, lid, pct)

            final = (
                f"{res_txt}\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"🎉 *Dars muvaffaqiyatli tugadi!*\n\n"
                f"{stars(lives)}\n"
                f"📊 Natija: *{corr_cnt}/{len(exs)}* ({pct}%)\n"
                f"⭐ To'plangan XP: *+{xp_earn}*\n"
                f"🔥 Streak: *{u.get('streak',1)} kun*\n\n"
                f"Barakalla! Keyingi darsga o'ting! 🚀"
            )
            await q.edit_message_text(
                final, parse_mode="Markdown",
                reply_markup=kb_after_lesson(lid)
            )
            return

        # Keyingi savolga o'tish tugmasi
        await q.edit_message_text(
            res_txt, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Keyingi savol ➡️", callback_data=f"next:{lid}:{next_idx}")]
            ])
        )

    # ── Keyingi savol ───────────────────────────────
    elif d.startswith("next:"):
        _, lid, ex_s = d.split(":")
        ex_idx = int(ex_s)
        ses    = get_ses(uid)
        lives  = ses["lives"] if ses else 3
        max_h  = 5 if payments.is_premium(uid) else 3
        await show_ex(q, uid, lid, ex_idx, lives, max_h)

    # ── Progress ────────────────────────────────────
    elif d == "progress":
        u     = get_user(uid) or {}
        done  = done_lessons(uid)
        lvl_p = level_progress(uid)
        is_prem = payments.is_premium(uid)

        text = (
            f"📊 *Mening Progressim*\n\n"
            f"👤 O'quvchi: *{q.from_user.first_name}*\n"
            f"💎 Holat: *{'Premium ✅' if is_prem else 'Bepul 🆓'}*\n"
            f"⭐ Jami XP: *{u.get('xp',0)} ball*\n"
            f"🔥 Streak: *{u.get('streak',0)} kun ketma-ket*\n"
            f"❤️ Yuraklar: *{u.get('hearts',5)}/5*\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"📚 *Darajalar bo'yicha progress:*\n"
            f"📗 A1.1: {pbar(lvl_p.get('A1.1',0),10)} {lvl_p.get('A1.1',0)}/10\n"
            f"📘 A1.2: {pbar(lvl_p.get('A1.2',0),10)} {lvl_p.get('A1.2',0)}/10\n"
            f"📙 A2.1: {pbar(lvl_p.get('A2.1',0),10)} {lvl_p.get('A2.1',0)}/10\n"
            f"📕 A2.2: {pbar(lvl_p.get('A2.2',0),10)} {lvl_p.get('A2.2',0)}/10\n\n"
            f"🎯 Jami tugatilgan darslar: *{len(done)}/{len(LESSON_ORDER)}*"
        )
        await q.edit_message_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📚 Darslarga o'tish", callback_data="lessons")],
                [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
            ]))

    # ── Eslatma Menyu ───────────────────────────────
    elif d == "reminder_menu":
        u = get_user(uid) or {}
        cur_rem = u.get("reminder") or "O'rnatilmagan"
        text = (
            f"⏰ *Kunlik Dars Eslatmasi*\n\n"
            f"Hozirgi eslatma vaqti: *{cur_rem}*\n\n"
            "Har kuni sizga qulay vaqtda dars eslatmasini yuboramiz.\n"
            "Vaqtni tanlang:"
        )
        times = ["08:00","10:00","12:00","15:00","18:00","20:00","21:00","22:00"]
        rows = [
            [InlineKeyboardButton(f"⏰ {times[i]}", callback_data=f"setr:{times[i]}"),
             InlineKeyboardButton(f"⏰ {times[i+1]}", callback_data=f"setr:{times[i+1]}")]
            for i in range(0, len(times), 2)
        ]
        rows.append([InlineKeyboardButton("❌ Eslatmani o'chirish", callback_data="delr")])
        rows.append([InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")])
        await q.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(rows))

    elif d.startswith("setr:"):
        time_str = d[5:]
        upd_user(uid, reminder=time_str)
        await q.edit_message_text(
            f"✅ *Eslatma o'rnatildi! Har kuni {time_str} da dars eslatiladi.*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
            ])
        )

    elif d == "delr":
        upd_user(uid, reminder=None)
        await q.edit_message_text(
            "✅ *Eslatma o'chirildi.*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
            ])
        )

    # ── Yordam ──────────────────────────────────────
    elif d == "help":
        text = (
            "❓ *Yordam va Yo'riqnoma — PolUzAcademy*\n\n"
            "🎮 *Qanday o'rganiladi?*\n"
            "1️⃣ *Darslar* bo'limidan darajani tanlang\n"
            "2️⃣ Darsdagi yangi so'zlarni ko'ring va *🔊 Audio* orqali talaffuzini eshiting\n"
            "3️⃣ Grammatika va dialoglarni o'rganing\n"
            "4️⃣ *Darsni boshlash* tugmasini bosib testlarni ishlang\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "💎 *To'lov va Premium:*\n"
            "• Dastlabki 5 ta dars — barcha uchun bepul\n"
            "• 6-darsdan boshlab — Premium (Oylik 24.99 zł, 3 oylik 59.99 zł, Yillik 179.99 zł)\n"
            "• To'lovlar **BLIK** yoki **Karta** orqali avtomatik qabul qilinadi\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📞 *Qo'llab-quvvatlash va Aloqa:*\n"
            "Bot bo'yicha savol yoki takliflaringiz bo'lsa, adminga yozing."
        )
        await q.edit_message_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💎 Premium obuna", callback_data="premium_menu")],
                [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
            ]))

# ═══════════════════════════════════════════
# MASHQ KO'RSATISH
# ═══════════════════════════════════════════
async def show_ex(q, uid, lid, ex_idx, lives, max_lives=3):
    les = lesson(lid)
    exs = les.get("exercises", [])
    ex  = exs[ex_idx]
    total = len(exs)

    text = (
        f"{hbar(lives, max_lives)}\n"
        f"{pbar(ex_idx, total)}\n\n"
        f"*Savol {ex_idx+1}/{total}*\n\n"
        f"{ex['q']}"
    )
    await q.edit_message_text(
        text, parse_mode="Markdown",
        reply_markup=kb_exercise(ex["opts"], ex_idx)
    )

# ═══════════════════════════════════════════
# KUNLIK ESLATMA
# ═══════════════════════════════════════════
async def daily_reminder(ctx: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().strftime("%H:%M")
    rows = db("SELECT user_id, name FROM users WHERE reminder=?", (now,), "all")
    if not rows: return
    for row in rows:
        try:
            await ctx.bot.send_message(
                chat_id=row["user_id"],
                text=(
                    f"🦉 *Salom, {row['name']}!*\n\n"
                    "Bugun ham polyakcha o'rganish vaqti! 📚\n"
                    "Har kun 1 ta dars — 1 oyda erkin muloqot! 🔥\n\n"
                    "👇 Boshlash uchun bosing:"
                ),
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("📚 Darsni boshlash", callback_data="lessons")]
                ])
            )
        except Exception as e:
            logger.warning(f"Eslatma yuborishda xatolik {row['user_id']}: {e}")

# ═══════════════════════════════════════════
# BUYRUQLAR
# ═══════════════════════════════════════════
async def cmd_darslar(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    ensure_user(uid, update.effective_user.first_name)
    await update.message.reply_text(
        "📚 *Darslar — Darajani tanlang:*",
        parse_mode="Markdown",
        reply_markup=kb_lessons(uid)
    )

async def cmd_progress(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid  = update.effective_user.id
    ensure_user(uid, update.effective_user.first_name)
    u    = get_user(uid) or {}
    done = done_lessons(uid)
    is_prem = payments.is_premium(uid)
    await update.message.reply_text(
        f"📊 *Progressim*\n\n"
        f"💎 Holat: *{'Premium ✅' if is_prem else 'Bepul 🆓'}*\n"
        f"⭐ XP: *{u.get('xp',0)}*\n"
        f"🔥 Streak: *{u.get('streak',0)} kun*\n"
        f"❤️ Yuraklar: *{u.get('hearts',5)}/5*\n"
        f"📚 Tugatilgan darslar: *{len(done)}/{len(LESSON_ORDER)}*",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📊 Batafsil progress", callback_data="progress")]
        ])
    )

async def cmd_lugat(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *Lug'at — Darajani tanlang:*",
        parse_mode="Markdown",
        reply_markup=kb_vocab_menu()
    )

async def cmd_premium(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await payments.show_premium(update, ctx)

async def cmd_id(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    await update.message.reply_text(
        f"🆔 *Sizning Telegram ID raqamingiz:* `{uid}`",
        parse_mode="Markdown"
    )

async def cmd_admin(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    # Agar admin bo'lsa yoki ADMIN_IDS bo'sh bo'lsa (barcha egalar)
    if ADMIN_IDS and uid not in ADMIN_IDS and 0 not in ADMIN_IDS:
        await update.message.reply_text(
            f"⛔️ *Sizda admin huquqi yo'q.*\n\n"
            f"🆔 Sizning Telegram ID: `{uid}`\n"
            f"Admin bo'lish uchun ushbu ID raqamni `ADMIN_IDS` ro'yxatiga qo'shish kerak.",
            parse_mode="Markdown"
        )
        return

    users_cnt = db("SELECT COUNT(*) as cnt FROM users", (), "one")
    stats = payments.get_payment_stats()
    
    text = (
        "👑 *PolUzAcademy Admin Paneli*\n\n"
        f"👥 Jami foydalanuvchilar: *{users_cnt['cnt'] if users_cnt else 0} ta*\n"
        f"💎 Faol Premium obunachilar: *{stats['active_users']} ta*\n"
        f"💳 Jami to'lovlar soni: *{stats['total_payments_count']} ta*\n"
        f"💰 Jami tushum: *{stats['total_revenue_pln']:.2f} PLN*\n\n"
        "⚡️ *Foydalanuvchiga Premium berish:*\n"
        "`/grant <user_id> <kunlar_soni>`\n"
        "Masalan: `/grant 123456789 30`"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def cmd_grant(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if ADMIN_IDS and uid not in ADMIN_IDS and 0 not in ADMIN_IDS:
        return
    
    args = ctx.args
    if len(args) < 2:
        await update.message.reply_text("Format: `/grant <user_id> <kunlar>`", parse_mode="Markdown")
        return
    
    try:
        target_uid = int(args[0])
        days = int(args[1])
        exp = payments.activate_premium(target_uid, "admin_grant", f"admin_{uid}", 0, days=days)
        await update.message.reply_text(
            f"✅ User `{target_uid}` ga *{days} kunlik* Premium muvaffaqiyatli berildi!\nTugash sanasi: *{exp.strftime('%d.%m.%Y')}*",
            parse_mode="Markdown"
        )
    except Exception as e:
        await update.message.reply_text(f"Xatolik: {e}")

async def handle_text(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    # Promo kod tekshirish
    handled = await payments.check_promo_code(update, ctx)
    if handled:
        return

    await update.message.reply_text(
        "🦉 Botdan foydalanish uchun /start bosing yoki quyidagi tugmalardan birini tanlang.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
        ])
    )

# ═══════════════════════════════════════════
# RENDER.COM UCHUN HEALTH CHECK SERVER
# ═══════════════════════════════════════════
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"PolUzAcademy Bot is running 24/7!")

    def log_message(self, format, *args):
        return  # Ortiqcha loglarni chiqarmaslik

def start_health_server():
    port_str = os.environ.get("PORT")
    if port_str and port_str.isdigit():
        port = int(port_str)
        server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
        t = threading.Thread(target=server.serve_forever, daemon=True)
        t.start()
        print(f"✅ Render.com Health Check server {port}-portda ishga tushdi!")

# ═══════════════════════════════════════════
# ASOSIY ISHGA TUSHIRISH (MAIN)
# ═══════════════════════════════════════════
def main():
    init_db()
    start_health_server()
    print("🦉 PolUzAcademy Bot ishga tushmoqda...")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start",    cmd_start))
    app.add_handler(CommandHandler("darslar",  cmd_darslar))
    app.add_handler(CommandHandler("progress", cmd_progress))
    app.add_handler(CommandHandler("lugat",    cmd_lugat))
    app.add_handler(CommandHandler("premium",  cmd_premium))
    app.add_handler(CommandHandler("admin",    cmd_admin))
    app.add_handler(CommandHandler("grant",    cmd_grant))
    app.add_handler(CommandHandler("id",       cmd_id))
    app.add_handler(CommandHandler("myid",     cmd_id))
    app.add_handler(CommandHandler("help",     payments.show_premium)) # or help
    app.add_handler(CallbackQueryHandler(on_cb))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    app.job_queue.run_repeating(daily_reminder, interval=60, first=10)

    async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        logger.error("Botda kutilmagan xatolik yuz berdi:", exc_info=context.error)

    app.add_error_handler(on_error)

    async def post_init(application):
        await application.bot.set_my_commands([
            BotCommand("start",    "🦉 Bosh menyu"),
            BotCommand("darslar",  "📚 Darslar"),
            BotCommand("progress", "📊 Progressim"),
            BotCommand("lugat",    "📖 Lug'at"),
            BotCommand("premium",  "💎 Premium Obuna"),
            BotCommand("admin",    "👑 Admin Paneli"),
        ])
    app.post_init = post_init

    print("✅ Bot ishga tushdi! Ctrl+C — to'xtatish")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
