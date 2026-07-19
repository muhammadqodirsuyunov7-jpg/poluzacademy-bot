#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🦉 POLYAKCHA BOT
Telegram orqali polyak tilini o'rganish
Professional daraja — Duolingo uslubida
"""

import logging
import sqlite3
import os
from datetime import date, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    ContextTypes, MessageHandler, filters
)
from lessons_a1 import A1_LESSONS
from lessons_a2 import A2_LESSONS
# ═══════════════════════════════════════════
#  SOZLAMALAR
# ═══════════════════════════════════════════
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8749989883:AAGX0RiQ32ExbIayYbevhxxBkDIxL-QEN0k")
DB_PATH   = "polyakcha.db"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ═══════════════════════════════════════════
#  DARSLAR TARTIBI
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
    "A2.1": [f"a2_l{str(i).zfill(2)}" for i in range(1, 21)],
}

# ═══════════════════════════════════════════
#  MA'LUMOTLAR BAZASI
# ═══════════════════════════════════════════
def init_db():
    con = sqlite3.connect(DB_PATH)
    con.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            user_id   INTEGER PRIMARY KEY,
            name      TEXT,
            xp        INTEGER DEFAULT 0,
            hearts    INTEGER DEFAULT 5,
            streak    INTEGER DEFAULT 0,
            last_date TEXT,
            reminder  TEXT
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
    con.commit()
    con.close()

def db(query, args=(), fetch=None):
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(query, args)
    result = None
    if   fetch == "one": result = cur.fetchone()
    elif fetch == "all": result = cur.fetchall()
    con.commit()
    con.close()
    return result

def get_user(uid):
    row = db("SELECT * FROM users WHERE user_id=?", (uid,), "one")
    return dict(row) if row else None

def ensure_user(uid, name):
    db("INSERT OR IGNORE INTO users (user_id,name) VALUES (?,?)", (uid, name))

def upd_user(uid, **kw):
    sets = ", ".join(f"{k}=?" for k in kw)
    db(f"UPDATE users SET {sets} WHERE user_id=?", (*kw.values(), uid))

def done_lessons(uid):
    rows = db("SELECT lesson_id FROM progress WHERE user_id=? AND done=1", (uid,), "all")
    return [r["lesson_id"] for r in rows] if rows else []

def mark_done(uid, lid, score):
    db("""INSERT INTO progress(user_id,lesson_id,done,score) VALUES(?,?,1,?)
          ON CONFLICT(user_id,lesson_id) DO UPDATE SET done=1,score=MAX(score,?)""",
       (uid, lid, score, score))

def get_ses(uid):
    row = db("SELECT * FROM sessions WHERE user_id=?", (uid,), "one")
    return dict(row) if row else None

def new_ses(uid, lid):
    db("""INSERT INTO sessions(user_id,lesson_id,ex_idx,lives,correct,wrong,xp_earned)
          VALUES(?,?,0,3,0,0,0)
          ON CONFLICT(user_id) DO UPDATE SET
          lesson_id=?,ex_idx=0,lives=3,correct=0,wrong=0,xp_earned=0""",
       (uid, lid, lid))

def upd_ses(uid, **kw):
    sets = ", ".join(f"{k}=?" for k in kw)
    db(f"UPDATE sessions SET {sets} WHERE user_id=?", (*kw.values(), uid))

def refresh_streak(uid):
    u = get_user(uid)
    if not u: return
    today = date.today().isoformat()
    if u["last_date"] == today: return
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    streak = (u["streak"] + 1) if u["last_date"] == yesterday else 1
    upd_user(uid, streak=streak, last_date=today)

# ═══════════════════════════════════════════
#  YORDAMCHI FUNKSIYALAR
# ═══════════════════════════════════════════
def hbar(lives):
    return "❤️" * lives + "🖤" * (3 - lives)

def pbar(done, total):
    pct = int(done / total * 100) if total else 0
    filled = pct // 10
    return f"`[{'▓'*filled}{'░'*(10-filled)}]` {pct}%"

def stars(lives):
    return "⭐⭐⭐" if lives==3 else "⭐⭐" if lives==2 else "⭐"

def lesson(lid):
    return ALL_LESSONS.get(lid, {})

def level_progress(uid):
    done = done_lessons(uid)
    result = {}
    for lvl, ids in LEVELS.items():
        result[lvl] = sum(1 for i in ids if i in done)
    return result

# ═══════════════════════════════════════════
#  KLAVIATURALAR
# ═══════════════════════════════════════════
def kb_main():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📚 Darslar",    callback_data="lessons"),
         InlineKeyboardButton("📖 Lug'at",     callback_data="vocab_menu")],
        [InlineKeyboardButton("📊 Progressim", callback_data="progress"),
         InlineKeyboardButton("⏰ Eslatma",    callback_data="reminder_menu")],
        [InlineKeyboardButton("ℹ️ Kurs haqida", callback_data="about"),
         InlineKeyboardButton("❓ Yordam",      callback_data="help")],
    ])

def kb_lessons(uid):
    done = done_lessons(uid)
    rows = []
    for lvl, ids in LEVELS.items():
        n_done = sum(1 for i in ids if i in done)
        rows.append([InlineKeyboardButton(
            f"📗 {lvl} — {n_done}/{len(ids)} ✅",
            callback_data=f"level:{lvl}"
        )])
    rows.append([InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")])
    return InlineKeyboardMarkup(rows)

def kb_level(lvl, uid):
    done = done_lessons(uid)
    ids  = LEVELS[lvl]
    rows = []
    for lid in ids:
        les  = lesson(lid)
        icon = "✅ " if lid in done else ""
        rows.append([InlineKeyboardButton(
            f"{icon}{les.get('emoji','📘')} {les.get('title',lid)}",
            callback_data=f"lesson:{lid}"
        )])
    rows.append([InlineKeyboardButton("◀️ Darslarga", callback_data="lessons")])
    return InlineKeyboardMarkup(rows)

def kb_lesson_detail(lid, uid):
    done = done_lessons(uid)
    rows = [
        [InlineKeyboardButton("📖 Lug'at",       callback_data=f"vocab:{lid}"),
         InlineKeyboardButton("📝 Grammatika",    callback_data=f"grammar:{lid}")],
        [InlineKeyboardButton("💬 Dialog",        callback_data=f"dialog:{lid}")],
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
    lvl = lesson(lid).get("level", "A1.1")
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
#  /START
# ═══════════════════════════════════════════
async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    ensure_user(u.id, u.first_name)

    text = (
        f"🦉 *Assalomu alaykum, {u.first_name}!*\n"
        f"*Polyakcha Botiga xush kelibsiz!*\n\n"
        "Bu bot orqali siz *polyak tilini* professional darajada "
        "o'yin va darslar orqali o'rganasiz!\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "📚 *Kurs tarkibi:*\n"
        "🟢 *A1.1* — Boshlang'ich muloqot *(10 dars)*\n"
        "🔵 *A1.2* — Kundalik hayot *(10 dars)*\n"
        "🟡 *A2.1* — Mustaqil muloqot *(tez kunda)*\n"
        "🔴 *A2.2* — Professional muloqot *(tez kunda)*\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🎯 *Kursni tugatgach siz:*\n"
        "✅ O'zingizni polyakcha tanishtira olasiz\n"
        "✅ Ishda, idorada, do'konda gaplasha olasiz\n"
        "✅ Hujjatlar bilan ish qila olasiz\n"
        "✅ Polshada mustaqil hayot kechirasiz\n"
        "✅ *A1–A2* darajasida erkin muloqot\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🎮 *O'yin tizimi:*\n"
        "⭐ *XP* — har to'g'ri javob uchun +10 ball\n"
        "❤️ *Yurak* — har darsda 3 ta (xato = kamayadi)\n"
        "🔥 *Streak* — ketma-ket o'rganish kunlari\n"
        "📊 *Progress* — qaysi darsni tugatgani\n\n"
        "⬇️ *Quyidagi tugmani bosing va boshlang!*"
    )
    await update.message.reply_text(
        text, parse_mode="Markdown", reply_markup=kb_main()
    )

# ═══════════════════════════════════════════
#  ASOSIY CALLBACK HANDLER
# ═══════════════════════════════════════════
async def on_cb(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q   = update.callback_query
    uid = q.from_user.id
    d   = q.data
    await q.answer()

    # ── Bosh menyu ──────────────────────────────────
    if d == "main":
        u = get_user(uid) or {}
        lvl_p = level_progress(uid)
        text = (
            f"🦉 *Polyakcha Bot — Bosh Menyu*\n\n"
            f"👤 *{q.from_user.first_name}*\n\n"
            f"🔥 Streak: *{u.get('streak',0)} kun*\n"
            f"⭐ XP: *{u.get('xp',0)}*\n"
            f"❤️ Yuraklar: *{u.get('hearts',5)}/5*\n\n"
            f"📗 A1.1: *{lvl_p.get('A1.1',0)}/10* dars\n"
            f"📘 A1.2: *{lvl_p.get('A1.2',0)}/10* dars\n\n"
            "Nima qilamiz?"
        )
        await q.edit_message_text(text, parse_mode="Markdown", reply_markup=kb_main())

    # ── Kurs haqida ─────────────────────────────────
    elif d == "about":
        text = (
            "ℹ️ *Kurs haqida*\n\n"
            "Bu kurs *Polshada yashovchi o'zbek tilida*\n"
            "*so'zlashuvchilar* uchun maxsus tuzilgan.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📗 *A1.1 — Boshlang'ich muloqot* (10 dars)\n"
            "• Salomlashish va alifbo\n"
            "• Tanishuv va oila\n"
            "• Kasblar va ish muloqoti\n"
            "• Ranglar, vaqt, sonlar\n\n"
            "📘 *A1.2 — Kundalik hayot* (10 dars)\n"
            "• Ovqat va do'kon\n"
            "• Transport va yo'l\n"
            "• Bank va pul\n"
            "• Hujjatlar va idora\n"
            "• Kasallik va shifokor\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎓 *Har bir darsda:*\n"
            "📖 15 ta yangi so'z + talaffuz\n"
            "📝 Grammatika tushuntirish\n"
            "💬 Haqiqiy dialog\n"
            "🧪 10 ta test savoli\n"
            "⭐ XP ball + yuraklar tizimi"
        )
        await q.edit_message_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📚 Darslarni boshlash", callback_data="lessons")],
                [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
            ]))

    # ── Darslar (daraja tanlash) ─────────────────────
    elif d == "lessons":
        done = done_lessons(uid)
        text = (
            "📚 *Darslar*\n\n"
            "Darajani tanlang:"
        )
        await q.edit_message_text(text, parse_mode="Markdown",
                                  reply_markup=kb_lessons(uid))

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
        await q.edit_message_text(text, parse_mode="Markdown",
                                  reply_markup=kb_level(lvl, uid))

    # ── Alohida dars detali ─────────────────────────
    elif d.startswith("lesson:"):
        lid  = d[7:]
        les  = lesson(lid)
        done = done_lessons(uid)
        status = "✅ *Tugatilgan!*" if lid in done else "🔓 Boshlashga tayyor"
        text = (
            f"{les.get('emoji','📘')} *{les.get('title',lid)}*\n"
            f"📗 Daraja: *{les.get('level','A1')}*\n\n"
            f"📚 So'zlar: *{len(les.get('vocab',[]))} ta*\n"
            f"🧪 Testlar: *{len(les.get('exercises',[]))} ta*\n"
            f"⭐ Mukofot: *+{len(les.get('exercises',[]))*10} XP*\n\n"
            f"{status}\n\n"
            "📖 Avval lug'at va grammatikani ko'ring,\n"
            "keyin darsni boshlang!"
        )
        await q.edit_message_text(text, parse_mode="Markdown",
                                  reply_markup=kb_lesson_detail(lid, uid))

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
        await q.edit_message_text(text, parse_mode="Markdown",
                                  reply_markup=kb_level(lvl, uid))

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
                [InlineKeyboardButton("📝 Grammatika", callback_data=f"grammar:{lid}")],
                [InlineKeyboardButton("▶️ Darsni boshlash", callback_data=f"go:{lid}")],
                [InlineKeyboardButton("◀️ Orqaga", callback_data=f"lesson:{lid}")]
            ]))

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
        new_ses(uid, lid)
        refresh_streak(uid)
        await show_ex(q, uid, lid, 0, 3)

    # ── Javob ───────────────────────────────────────
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

        if is_ok:
            corr_cnt += 1
            xp_earn  += 10
            result = "✅ *To'g'ri!* +10 ⭐"
        else:
            lives    -= 1
            wrng_cnt += 1
            result = f"❌ *Xato!*  To'g'ri: *{ex['opts'][correct]}*"

        next_idx = ex_idx + 1
        upd_ses(uid, ex_idx=next_idx, lives=lives,
                correct=corr_cnt, wrong=wrng_cnt, xp_earned=xp_earn)

        # Natijani ko'rsat
        opts_txt = "\n".join(
            f"{'✅' if i==correct else ('❌' if i==choice and not is_ok else '◾')}  {opt}"
            for i, opt in enumerate(ex["opts"])
        )
        res_txt = (
            f"{hbar(lives)}\n"
            f"{pbar(ex_idx+1, len(exs))}\n\n"
            f"{ex['q']}\n\n"
            f"{opts_txt}\n\n"
            f"{result}"
        )

        # Yuraklar tugadi
        if lives <= 0:
            u     = get_user(uid)
            new_h = max(0, (u.get("hearts") or 5) - 1)
            upd_user(uid, hearts=new_h)
            final = (
                f"{res_txt}\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"💔 *Yuraklar tugadi!*\n\n"
                f"✅ To'g'ri: *{corr_cnt}*\n"
                f"❌ Xato: *{wrng_cnt}*\n"
                f"⭐ Ball: *+{xp_earn}*\n\n"
                f"❤️ Qolgan yurak: *{new_h}/5*\n\n"
                "Qayta urinib ko'ring! 💪"
            )
            await q.edit_message_text(final, parse_mode="Markdown",
                                      reply_markup=kb_after_lesson(lid))
            return

        # Dars tugadi
        if next_idx >= len(exs):
            u      = get_user(uid)
            new_xp = (u.get("xp") or 0) + xp_earn
            upd_user(uid, xp=new_xp)
            mark_done(uid, lid, corr_cnt)

            accuracy = int(corr_cnt / len(exs) * 100)
            final = (
                f"{res_txt}\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"🎉 *Dars muvaffaqiyatli tugadi!*\n\n"
                f"{stars(lives)}\n\n"
                f"✅ To'g'ri: *{corr_cnt}/{len(exs)}*\n"
                f"❌ Xato: *{wrng_cnt}*\n"
                f"🎯 Aniqlik: *{accuracy}%*\n"
                f"⭐ Jami XP: *+{xp_earn}*\n"
                f"🔥 Streak: *{u.get('streak',1)} kun*\n\n"
                f"Davom eting! 💪🦉"
            )
            await q.edit_message_text(final, parse_mode="Markdown",
                                      reply_markup=kb_after_lesson(lid))
            return

        # Keyingi savol
        await q.edit_message_text(
            f"{res_txt}\n\n⏳ *Keyingi savol...*",
            parse_mode="Markdown"
        )
        await show_ex(q, uid, lid, next_idx, lives)

    # ── Progress ────────────────────────────────────
    elif d == "progress":
        u    = get_user(uid) or {}
        done = done_lessons(uid)
        total = len(LESSON_ORDER)
        n_done = len(done)
        lvl_p = level_progress(uid)

        text = (
            f"📊 *{q.from_user.first_name} — Progressim*\n\n"
            f"🔥 Streak: *{u.get('streak',0)} kun*\n"
            f"⭐ Jami XP: *{u.get('xp',0)}*\n"
            f"❤️ Yuraklar: *{u.get('hearts',5)}/5*\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"📚 *Darslar:*\n"
            f"{pbar(n_done, total)}\n"
            f"Tugatilgan: *{n_done}/{total}*\n\n"
        )
        for lvl, ids in LEVELS.items():
            n = sum(1 for i in ids if i in done)
            text += f"📗 *{lvl}:* {n}/{len(ids)}\n"
            for lid in ids:
                les = lesson(lid)
                ico = "✅" if lid in done else "⬜"
                text += f"  {ico} {les.get('emoji','')} {les.get('title',lid)}\n"
            text += "\n"

        await q.edit_message_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📚 Darslar",   callback_data="lessons")],
                [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
            ]))

    # ── Eslatma menyu ───────────────────────────────
    elif d == "reminder_menu":
        u     = get_user(uid) or {}
        cur_r = u.get("reminder") or "—"
        times = ["07:00","09:00","12:00","18:00","20:00","22:00"]
        rows  = []
        row   = []
        for t in times:
            label = f"✅ {t}" if cur_r == t else t
            row.append(InlineKeyboardButton(label, callback_data=f"setr:{t}"))
            if len(row) == 3:
                rows.append(row); row = []
        if row: rows.append(row)
        rows.append([InlineKeyboardButton("❌ O'chirish", callback_data="delr")])
        rows.append([InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")])
        await q.edit_message_text(
            f"⏰ *Kunlik Eslatma*\n\nHozirgi vaqt: *{cur_r}*\n\n"
            "Har kuni qaysi vaqtda eslataylik?",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(rows)
        )

    elif d.startswith("setr:"):
        t = d[5:]
        upd_user(uid, reminder=t)
        await q.edit_message_text(
            f"✅ *Eslatma o'rnatildi!*\n\n"
            f"Har kuni soat *{t}* da eslatma keladi. 🦉\n\n"
            "Polyakcha o'rganishni unutmang!",
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
            "❓ *Yordam — Polyakcha Bot*\n\n"
            "🎮 *Qanday ishlaydi?*\n"
            "1️⃣ *Darslar* → darajani tanlang\n"
            "2️⃣ Darsni tanlang\n"
            "3️⃣ *Lug'at* → so'zlarni o'rganing\n"
            "4️⃣ *Grammatika* → qoidalarni o'rganing\n"
            "5️⃣ *Dialog* → amaliy misol\n"
            "6️⃣ *Darsni boshlash* → testlarni bajaring\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📊 *Ball tizimi:*\n"
            "✅ To'g'ri javob = *+10 XP ⭐*\n"
            "❌ Xato = *❤️ kamayadi*\n"
            "💔 3 xato = dars tugaydi\n"
            "🔥 Streak = ketma-ket kunlar\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📞 *Muammo yoki taklif?*\n"
            "Bot muallifi bilan bog'laning!\n\n"
            "*/start* — Bosh menyu\n"
            "*/darslar* — Darslar\n"
            "*/progress* — Progressim\n"
            "*/lugat* — Lug'at"
        )
        await q.edit_message_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
            ]))

# ═══════════════════════════════════════════
#  MASHQ KO'RSATISH
# ═══════════════════════════════════════════
async def show_ex(q, uid, lid, ex_idx, lives):
    les = lesson(lid)
    exs = les.get("exercises", [])
    ex  = exs[ex_idx]
    total = len(exs)

    text = (
        f"{hbar(lives)}\n"
        f"{pbar(ex_idx, total)}\n\n"
        f"*Savol {ex_idx+1}/{total}*\n\n"
        f"{ex['q']}"
    )
    await q.edit_message_text(
        text, parse_mode="Markdown",
        reply_markup=kb_exercise(ex["opts"], ex_idx)
    )

# ═══════════════════════════════════════════
#  KUNLIK ESLATMA
# ═══════════════════════════════════════════
async def daily_reminder(ctx: ContextTypes.DEFAULT_TYPE):
    from datetime import datetime
    now  = datetime.now().strftime("%H:%M")
    rows = db("SELECT user_id, name FROM users WHERE reminder=?", (now,), "all")
    if not rows: return
    for row in rows:
        try:
            await ctx.bot.send_message(
                chat_id=row["user_id"],
                text=(
                    f"🦉 *Salom, {row['name']}!*\n\n"
                    "Bugun ham polyakcha o'rganish vaqti! 📚\n\n"
                    "Har kun bir dars — 1 oyda A1 darajasi! 🔥\n\n"
                    "👇 Boshlash uchun bosing:"
                ),
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("📚 Darsni boshlash", callback_data="lessons")]
                ])
            )
        except Exception as e:
            logger.warning(f"Eslatma xatosi {row['user_id']}: {e}")

# ═══════════════════════════════════════════
#  QO'SHIMCHA BUYRUQLAR
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
    await update.message.reply_text(
        f"📊 *Progressim*\n\n"
        f"⭐ XP: *{u.get('xp',0)}*\n"
        f"🔥 Streak: *{u.get('streak',0)} kun*\n"
        f"❤️ Yuraklar: *{u.get('hearts',5)}/5*\n"
        f"📚 Darslar: *{len(done)}/{len(LESSON_ORDER)}*",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📊 Batafsil", callback_data="progress")]
        ])
    )

async def cmd_lugat(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *Lug'at — Darajani tanlang:*",
        parse_mode="Markdown",
        reply_markup=kb_vocab_menu()
    )

async def cmd_help(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🦉 *Buyruqlar:*\n\n"
        "/start — Bosh menyu\n"
        "/darslar — Darslar ro'yxati\n"
        "/progress — Mening progressim\n"
        "/lugat — Lug'at\n"
        "/help — Yordam",
        parse_mode="Markdown"
    )

async def unknown(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🦉 Botdan foydalanish uchun /start bosing!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
        ])
    )

# ═══════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════
def main():
    init_db()
    print("🦉 Polyakcha Bot ishga tushmoqda...")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start",    cmd_start))
    app.add_handler(CommandHandler("darslar",  cmd_darslar))
    app.add_handler(CommandHandler("progress", cmd_progress))
    app.add_handler(CommandHandler("lugat",    cmd_lugat))
    app.add_handler(CommandHandler("help",     cmd_help))
    app.add_handler(CallbackQueryHandler(on_cb))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))

    app.job_queue.run_repeating(daily_reminder, interval=60, first=10)

    async def post_init(application):
        await application.bot.set_my_commands([
            BotCommand("start",    "🦉 Bosh menyu"),
            BotCommand("darslar",  "📚 Darslar"),
            BotCommand("progress", "📊 Progressim"),
            BotCommand("lugat",    "📖 Lug'at"),
            BotCommand("help",     "❓ Yordam"),
        ])
    app.post_init = post_init

    print("✅ Bot ishga tushdi! Ctrl+C — to'xtatish")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
