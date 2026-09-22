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

import asyncio
from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup,
    ReplyKeyboardMarkup, KeyboardButton, BotCommand
)
from telegram.constants import ChatAction
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
import dictionary_service
import poland_guide
import ai_assistant
import i18n

# ═══════════════════════════════════════════
# SOZLAMALAR
# ═══════════════════════════════════════════
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8749989883:AAGX0RiQ32ExbIayYbevhxxBkDIxL-QEN0k")
DB_PATH   = "polyakcha.db"
# Doimiy asosiy adminlar (har qanday holatda admin huquqiga ega)
MASTER_ADMINS = [1628696149, 8022251674]
import re
_env_admins = [int(x) for x in re.findall(r'\d+', os.environ.get("ADMIN_IDS", ""))]
ADMIN_IDS = list(dict.fromkeys(MASTER_ADMINS + _env_admins))

def is_admin(user_id: int) -> bool:
    """Foydalanuvchi admin ekanligini tekshiradi."""
    return (user_id in ADMIN_IDS) or (user_id in MASTER_ADMINS)

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
    dictionary_service.init_dict_db()
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
            created_at TEXT,
            referrer_id INTEGER,
            invited_count INTEGER DEFAULT 0,
            last_heart_regen TEXT
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
    # Avtomatik migratsiya
    cur = con.cursor()
    user_cols = [c[1] for c in cur.execute("PRAGMA table_info(users)").fetchall()]
    if "created_at" not in user_cols:
        cur.execute("ALTER TABLE users ADD COLUMN created_at TEXT")
    if "referrer_id" not in user_cols:
        cur.execute("ALTER TABLE users ADD COLUMN referrer_id INTEGER")
    if "invited_count" not in user_cols:
        cur.execute("ALTER TABLE users ADD COLUMN invited_count INTEGER DEFAULT 0")
    if "last_heart_regen" not in user_cols:
        cur.execute("ALTER TABLE users ADD COLUMN last_heart_regen TEXT")
    if "ai_requests_today" not in user_cols:
        cur.execute("ALTER TABLE users ADD COLUMN ai_requests_today INTEGER DEFAULT 0")
    if "last_ai_date" not in user_cols:
        cur.execute("ALTER TABLE users ADD COLUMN last_ai_date TEXT")
    if "lang" not in user_cols:
        cur.execute("ALTER TABLE users ADD COLUMN lang TEXT DEFAULT 'uz'")
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

def check_heart_regen(u: dict) -> dict:
    """Bepul foydalanuvchining yuraklarini har 2 soatda +1 tadan tiklaydi (maksimal 5 gacha)."""
    if not u or payments.is_premium(u.get("user_id")):
        return u
    hearts = u.get("hearts", 5)
    if hearts is None:
        hearts = 5
    if hearts >= 5:
        return u

    last_regen_str = u.get("last_heart_regen")
    now = datetime.now()
    if not last_regen_str:
        now_iso = now.isoformat()
        upd_user(u["user_id"], last_heart_regen=now_iso)
        u["last_heart_regen"] = now_iso
        return u

    try:
        last_regen = datetime.fromisoformat(last_regen_str)
        diff_hours = (now - last_regen).total_seconds() / 3600.0
        if diff_hours >= 2.0:
            hearts_to_add = int(diff_hours // 2)
            new_hearts = min(5, hearts + hearts_to_add)
            new_last_regen = last_regen + timedelta(hours=hearts_to_add * 2)
            upd_user(u["user_id"], hearts=new_hearts, last_heart_regen=new_last_regen.isoformat())
            u["hearts"] = new_hearts
            u["last_heart_regen"] = new_last_regen.isoformat()
    except Exception as e:
        logger.warning(f"Yurak tiklashda xatolik: {e}")

    return u

def heart_status_text(u: dict) -> str:
    """Yuraklar holati va tiklanish vaqtini matn ko'rinishida beradi."""
    if not u:
        return "❤️❤️❤️❤️❤️ (5/5)"
    if payments.is_premium(u.get("user_id")):
        return "❤️ Cheksiz (💎 Premium)"
    h = u.get("hearts", 5)
    if h is None:
        h = 5
    if h >= 5:
        return f"{'❤️'*5} (5/5 To'liq)"
    last_str = u.get("last_heart_regen")
    time_left_txt = ""
    if last_str:
        try:
            last = datetime.fromisoformat(last_str)
            next_regen = last + timedelta(hours=2)
            rem_sec = max(0, int((next_regen - datetime.now()).total_seconds()))
            rem_min = rem_sec // 60
            time_left_txt = f" (Keyingisi: ~{rem_min} daqiqada)"
        except Exception:
            pass
    return f"{'❤️'*h}{'🖤'*(5-h)} ({h}/5){time_left_txt}"

def get_leaderboard(current_uid: int):
    """Top 10 o'quvchilar va joriy foydalanuvchining reytingdagi o'rnini qaytaradi."""
    rows = db("SELECT user_id, name, xp, streak FROM users ORDER BY xp DESC LIMIT 10", fetch="all")
    user_row = db("SELECT COUNT(*) + 1 as rank FROM users WHERE xp > (SELECT COALESCE(xp, 0) FROM users WHERE user_id=?)", (current_uid,), fetch="one")
    user_rank = user_row["rank"] if user_row else 1
    return rows, user_rank

def get_user(uid):
    row = db("SELECT * FROM users WHERE user_id=?", (uid,), "one")
    if not row:
        return None
    u = dict(row)
    return check_heart_regen(u)

def ensure_user(uid, name):
    now = datetime.now().isoformat()
    db("INSERT OR IGNORE INTO users (user_id, name, created_at, last_heart_regen, lang) VALUES (?, ?, ?, ?, 'uz')", (uid, name, now, now))

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

def get_continue_lesson(uid):
    """Foydalanuvchi to'xtagan (hali tugatilmagan birinchi) darsni topadi."""
    done = done_lessons(uid)
    for lid in LESSON_ORDER:
        if lid not in done:
            return lid
    return LESSON_ORDER[-1]

# ═══════════════════════════════════════════
# KLAVIATURALAR (i18n orqali ko'p tilli)
# ═══════════════════════════════════════════
def kb_reply_main(lang: str = "uz"):
    return i18n.kb_reply_main(lang)

def kb_main(uid: int = None, lang: str = None):
    if lang is None:
        lang = i18n.get_user_lang(uid) if uid else "uz"
    is_prem = payments.is_premium(uid) if uid else False
    return i18n.kb_main(uid, is_premium=is_prem, lang=lang)

def kb_ai_menu(uid: int = None, lang: str = None):
    if lang is None:
        lang = i18n.get_user_lang(uid) if uid else "uz"
    is_prem = payments.is_premium(uid) if uid else False
    used, remaining = ai_assistant.get_ai_quota_info(uid, is_prem) if uid else (0, 5)
    return i18n.kb_ai_menu(uid, is_premium=is_prem, remaining=remaining, lang=lang)

def kb_ai_roleplay_menu(lang: str = "uz"):
    return i18n.kb_ai_roleplay_menu(lang)

def kb_ai_active(mode: str = "chat", lang: str = "uz"):
    return i18n.kb_ai_active(mode, lang)


def kb_lessons(uid):
    done = done_lessons(uid)
    is_prem = payments.is_premium(uid)
    rows = [
        [InlineKeyboardButton("▶️ Qolgan joyidan davom ettirish", callback_data="continue_lesson")],
        [InlineKeyboardButton("🔄 Darslarni boshidan boshlash", callback_data="restart_lessons")],
    ]
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
        les_num = LESSON_ORDER.index(lid) + 1 if lid in LESSON_ORDER else (i + 1)
        rows.append([InlineKeyboardButton(
            f"{icon}{les.get('emoji','📘')} {les_num}. {les.get('title',lid)}{free_badge}",
            callback_data=f"lesson:{lid}"
        )])
    rows.append([InlineKeyboardButton("◀️ Darslarga", callback_data="lessons")])
    return InlineKeyboardMarkup(rows)

def kb_lesson_detail(lid, uid):
    done = done_lessons(uid)
    rows = [
        [InlineKeyboardButton("🔊 Lug'atni eshitish", callback_data=f"audio_vocab:{lid}"),
         InlineKeyboardButton("📖 Lug'at", callback_data=f"vocab:{lid}")],
        [InlineKeyboardButton("🗂 Flashcard orqali yodlash", callback_data=f"flashcards:{lid}:0")],
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
        [InlineKeyboardButton("▶️ Keyingi dars",   callback_data="continue_lesson")],
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
    args = ctx.args

    # Do'stni taklif qilish havolasi (/start ref_123456)
    if args and len(args) > 0 and args[0].startswith("ref_"):
        try:
            inv_id = int(args[0].replace("ref_", ""))
            existing = db("SELECT * FROM users WHERE user_id=?", (u.id,), "one")
            if not existing and inv_id != u.id:
                await payments.process_referral_reward(inv_id, u.id, u.first_name, ctx.bot)
        except Exception as e:
            logger.warning(f"Referal xatoligi: {e}")

    ensure_user(u.id, u.first_name)

    # To'lovdan qaytgandagi linklarni tekshirish (/start success_oylik_12345 yoki simpay_oylik)
    if args and len(args) > 0:
        arg = args[0]
        if arg.startswith("success_") or arg.startswith("simpay_"):
            parts = arg.split("_")
            plan = parts[1] if len(parts) > 1 else "oylik"
            exp = payments.activate_premium(u.id, plan, f"stripe_{arg}", payments.NARXLAR.get(plan, {}).get("narx", 2499))
            lang = i18n.get_user_lang(u.id)
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

    # Start bosilganda 3 ta tilni tanlash tugmasi chiqadi
    text = (
        f"🦉 *Assalomu alaykum, {u.first_name}! / Здравствуйте! / Salam!*\n\n"
        "PolUzAcademy — polyak tilini professional o'rganish botiga xush kelibsiz!\n"
        "Добро пожаловать в бот изучения польского языка!\n"
        "Polýak dilini öwrenmek üçin bota hoş geldiňiz!\n\n"
        "🌐 *Iltimos, o'zingizga qulay tilni tanlang:*\n"
        "🇷🇺 *Пожалуйста, выберите язык обучения:*\n"
        "🇹🇲 *Haýyş edýäris, okuw dilini saýlaň:*"
    )
    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=i18n.kb_lang_select()
    )

async def cmd_lang(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    ensure_user(uid, update.effective_user.first_name)
    lang = i18n.get_user_lang(uid)
    await update.message.reply_text(
        i18n.t("choose_language", lang),
        parse_mode="Markdown",
        reply_markup=i18n.kb_lang_select(include_back=False)
    )

async def cmd_ai(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    ensure_user(uid, update.effective_user.first_name)
    lang = i18n.get_user_lang(uid)
    is_prem = payments.is_premium(uid)
    used, remaining = ai_assistant.get_ai_quota_info(uid, is_prem)

    if is_prem:
        quota_txt = "💎 *Premium (Cheksiz)*" if lang == "uz" else ("💎 *Премиум (Безлимитно)*" if lang == "ru" else "💎 *Premium (Çäksiz)*")
    else:
        quota_txt = f"⚡️ *{remaining}/5 ta bepul so'rov qoldi*" if lang == "uz" else (f"⚡️ *Осталось: {remaining}/5 бесплатных запросов*" if lang == "ru" else f"⚡️ *{remaining}/5 mugt sorag galdy*")

    text = i18n.t("ai_title", lang, quota_txt=quota_txt)
    reply_kb = i18n.kb_ai_menu(uid, is_prem, remaining, lang)

    if update.callback_query:
        await update.callback_query.edit_message_text(text, parse_mode="Markdown", reply_markup=reply_kb)
    else:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=reply_kb)

# ═══════════════════════════════════════════
# ASOSIY CALLBACK HANDLER
# ═══════════════════════════════════════════
async def on_cb(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q   = update.callback_query
    uid = q.from_user.id
    d   = q.data
    await q.answer()

    # ── To'lov bilan bog'liq callbacklar ────────────
    if d in ["premium_menu", "buy_oylik", "buy_3oylik", "buy_yillik", "premium_renew", "premium_info", "promo_code", "manual_pay_menu"] or d.startswith("mpay_"):
        await payments.payment_callback(update, ctx)
        return

    # ── Tilni o'zgartirish ─────────────────────────
    if d.startswith("set_lang:"):
        lang = d.split(":", 1)[1]
        i18n.set_user_lang(uid, lang)
        is_prem = payments.is_premium(uid)
        status_badge = "💎 *Premium*" if is_prem else ("🆓 *Dastlabki 5 ta dars bepul!*" if lang == "uz" else ("🆓 *Первые 5 уроков бесплатно!*" if lang == "ru" else "🆓 *Ilkinji 5 sapak mugt!*"))
        
        confirm_txt = i18n.t("lang_changed", lang)
        await q.message.reply_text(confirm_txt, parse_mode="Markdown", reply_markup=i18n.kb_reply_main(lang))
        
        welcome_txt = i18n.t("welcome_header", lang, name=q.from_user.first_name, status_badge=status_badge)
        await q.edit_message_text(welcome_txt, parse_mode="Markdown", reply_markup=i18n.kb_main(uid, is_prem, lang))
        return

    elif d == "change_lang":
        lang = i18n.get_user_lang(uid)
        txt = i18n.t("choose_language", lang)
        await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=i18n.kb_lang_select(include_back=True))
        return

    # ── AI Ustoz Callbacklari ──────────────────────
    elif d == "ai_menu":
        await cmd_ai(update, ctx)
        return

    elif d == "ai_roleplay_menu":
        lang = i18n.get_user_lang(uid)
        if lang == "ru":
            text = (
                "🎭 *Ситуационные Ролевые Игры (Реальные Диалоги)*\n\n"
                "Попробуйте себя в самых важных жизненных ситуациях в Польше! "
                "ИИ будет общаться с вами как настоящий собеседник-поляк.\n\n"
                "🎙 Вы можете писать текстом или отправлять *голосовые сообщения*!\n\n"
                "Какую ситуацию выберете?"
            )
        elif lang == "tm":
            text = (
                "🎭 *Ýagdaýly Rollu Oýunlar (Hakyky Durmuş Gürrüňdeşlikleri)*\n\n"
                "Polşadaky iň möhüm durmuş ýagdaýlarynda özüňizi synap görüň! "
                "AI siz bilen hakyky polýak ýaly gürleşer.\n\n"
                "🎙 Jogaplaryňyzy tekst ýa-da *sesli habar* arkaly iberip bilersiňiz!\n\n"
                "Haýsy ýagdaýy saýlaýarsyňyz?"
            )
        else:
            text = (
                "🎭 *Situatsion Rolli O'yinlar (Real Hayot Dialoglari)*\n\n"
                "Polshadagi eng muhim hayotiy vaziyatlarda o'zingizni sinab ko'ring! "
                "AI siz bilan haqiqiy polyak suhbatdoshi kabi muloqot qiladi.\n\n"
                "🎙 Javoblaringizni matn yoki *ovozli xabar* orqali yuborishingiz mumkin!\n\n"
                "Qaysi vaziyatni tanlaysiz?"
            )
        await q.edit_message_text(text, parse_mode="Markdown", reply_markup=i18n.kb_ai_roleplay_menu(lang))
        return

    elif d.startswith("ai_mode:"):
        mode = d.split(":", 1)[1]
        ctx.user_data["ai_mode"] = mode
        ctx.user_data["ai_history"] = []
        lang = i18n.get_user_lang(uid)

        if mode == "chat":
            if lang == "ru":
                text = (
                    "💬 *ИИ-Учитель — Режим вопрос-ответ активирован!*\n\n"
                    "Задавайте любые вопросы по польскому языку, грамматике, словам или переводам, "
                    "пишите текстом или отправляйте *голосовые сообщения*.\n\n"
                    "_(Для выхода нажмите кнопку ниже или напишите /exit)_"
                )
            elif lang == "tm":
                text = (
                    "💬 *AI Halypa — Sorag-jogap tertibi işjeňleşdirildi!*\n\n"
                    "Polýak dili, grammatika düzgünleri, sözler ýa-da terjimeler barada "
                    "islendik soragyňyzy ýazyň ýa-da *sesli habar* iberiň.\n\n"
                    "_(Tertipden çykmak üçin aşakdaky düwmä basyň ýa-da /exit ýazyň)_"
                )
            else:
                text = (
                    "💬 *AI Ustoz — Savol-javob rejimi faollashdi!*\n\n"
                    "Polyak tili, grammatika qoidalari, so'zlar yoki tarjimalar haqida "
                    "istalgan savolingizni yozing yoki *ovozli xabar* yuboring.\n\n"
                    "💡 *Maslahat:* Masalan, `Być fe'lining tuslanishini tushuntirib ber`, "
                    "yoki `Urządga borganda nima deyish kerak?` deb so'rang.\n\n"
                    "_(Rejimdan chiqish uchun quyidagi tugmani bosing yoki /exit deb yozing)_"
                )
        elif mode == "grammar":
            if lang == "ru":
                text = (
                    "✍️ *Проверка грамматики и текста активирована!*\n\n"
                    "Отправьте предложение или текст на польском языке, который хотите проверить.\n\n"
                    "ИИ найдет ошибки, покажет правильный вариант и доступно объяснит правила на русском языке.\n\n"
                    "_(Для выхода нажмите кнопку ниже или напишите /exit)_"
                )
            elif lang == "tm":
                text = (
                    "✍️ *Grammatika we tekst barlagy işjeňleşdirildi!*\n\n"
                    "Barlatmak isleýän polýakça sözlemiňizi ýa-da tekstiňizi iberiň.\n\n"
                    "AI Halypa ýalňyşlaryňyzy tapyp, dogry görnüşini görkezer we düzgünini türkmen dilinde düşündirer.\n\n"
                    "_(Tertipden çykmak üçin aşakdaky düwmä basyň ýa-da /exit ýazyň)_"
                )
            else:
                text = (
                    "✍️ *Grammatika va Matn Tekshiruvi faollashdi!*\n\n"
                    "O'zingiz tuzgan yoki tekshirmoqchi bo'lgan polyakcha gap yoki matnni yuboring.\n\n"
                    "AI Ustoz xatolaringizni aniqlab, to'g'ri variantini ko'rsatadi va qoidasini "
                    "o'zbek tilida batafsil tushuntirib beradi.\n\n"
                    "_(Rejimdan chiqish uchun quyidagi tugmani bosing yoki /exit deb yozing)_"
                )
        else:
            text = "🤖 *AI Ustoz rejimi faol.*"
        await q.message.reply_text(text, parse_mode="Markdown", reply_markup=i18n.kb_ai_active(mode, lang))
        return

    elif d.startswith("ai_roleplay:"):
        rp_type = d.split(":", 1)[1]
        ctx.user_data["ai_mode"] = rp_type
        ctx.user_data["ai_history"] = []
        lang = i18n.get_user_lang(uid)

        intro_text = ""
        polish_starter = ""

        if rp_type == "roleplay_urzad":
            hint = "_(Xayrli kun! Sizga qanday yordam bera olaman? Karta pobytu arizasini topshirishga keldingizmi?)_" if lang == "uz" else ("_(Добрый день! Чем могу помочь? Вы пришли подать заявление на карту побыту?)_" if lang == "ru" else "_(Salam! Size nähili kömek edip bilerin? Karta pobytu tabşyrmaga geldiňizmi?)_")
            call_action = "🎙 Javobingizni matn yoki *ovozli xabar* qilib yuboring!" if lang == "uz" else ("🎙 Отправьте ответ текстом или *голосовым сообщением*!" if lang == "ru" else "🎙 Jogabyňyzy tekst ýa-da *sesli habar* bilen iberiň!")
            intro_text = f"🏛 *Urząd Wojewódzki (Karta Pobytu)*\n\n👨‍💼 *Urzędnik:* „Dzień dobry! W czym mogę Panu/Pani pomóc? Czy przyszedł Pan złożyć wniosek o kartę pobytu?”\n{hint}\n\n{call_action}"
            polish_starter = "Dzień dobry! W czym mogę Panu pomóc? Czy przyszedł Pan złożyć wniosek o kartę pobytu?"
        elif rp_type == "roleplay_praca":
            hint = "_(Salom! Kelganing yaxshi bo'ldi. Bugungi ish qanday ketyapti?)_" if lang == "uz" else ("_(Привет! Рад, что ты пришел. Как идут дела на твоем рабочем месте?)_" if lang == "ru" else "_(Salam! Geleniň gowy boldy. Şu günki iş nähili gidýär?)_")
            call_action = "🎙 Javobingizni matn yoki *ovozli xabar* qilib yuboring!" if lang == "uz" else ("🎙 Отправьте ответ текстом или *голосовым сообщением*!" if lang == "ru" else "🎙 Jogabyňyzy tekst ýa-da *sesli habar* bilen iberiň!")
            intro_text = f"💼 *Praca / Magazyn (Kierownik Marek)*\n\n👷‍♂️ *Kierownik (Marek):* „Cześć! Dobrze, że jesteś. Jak idzie dzisiejsza praca na Twoim stanowisku?”\n{hint}\n\n{call_action}"
            polish_starter = "Cześć! Dobrze, że jesteś. Jak idzie dzisiejsza praca na Twoim stanowisku?"
        elif rp_type == "roleplay_sklep":
            hint = "_(Xayrli kun! Moja Biedronka kartangiz bormi?)_" if lang == "uz" else ("_(Добрый день! У вас есть карта Moja Biedronka?)_" if lang == "ru" else "_(Salam! Moja Biedronka kartyňyz barmy?)_")
            call_action = "🎙 Javobingizni matn yoki *ovozli xabar* qilib yuboring!" if lang == "uz" else ("🎙 Отправьте ответ текстом или *голосовым сообщением*!" if lang == "ru" else "🎙 Jogabyňyzy tekst ýa-da *sesli habar* bilen iberiň!")
            intro_text = f"🛒 *Supermarket (Biedronka)*\n\n👩‍💼 *Kasjer:* „Dzień dobry! Czy ma Pan naszą kartę Moja Biedronka?”\n{hint}\n\n{call_action}"
            polish_starter = "Dzień dobry! Czy ma Pan naszą kartę Moja Biedronka?"
        elif rp_type == "roleplay_lekarz":
            hint = "_(Xayrli kun, o'tiring. Nima bezovta qilyapti? Qanday alomatlar bor?)_" if lang == "uz" else ("_(Добрый день, присаживайтесь. Что вас беспокоит? Какие симптомы?)_" if lang == "ru" else "_(Salam, geçiň, otyryň. Nämäňiz agyrýar? Nähili alamatlar bar?)_")
            call_action = "🎙 Javobingizni matn yoki *ovozli xabar* qilib yuboring!" if lang == "uz" else ("🎙 Отправьте ответ текстом или *голосовым сообщением*!" if lang == "ru" else "🎙 Jogabyňyzy tekst ýa-da *sesli habar* bilen iberiň!")
            intro_text = f"🏥 *Przychodnia NFZ (Lekarz)*\n\n👨‍⚕️ *Lekarz:* „Dzień dobry, proszę usiąść. Co Panu dolega? Jakie ma Pan objawy?”\n{hint}\n\n{call_action}"
            polish_starter = "Dzień dobry, proszę usiąść. Co Panu dolega? Jakie ma Pan objawy?"

        ctx.user_data["ai_history"].append({"role": "model", "content": polish_starter})

        await q.message.reply_text(intro_text, parse_mode="Markdown", reply_markup=i18n.kb_ai_active(rp_type, lang))
        if polish_starter:
            try:
                audio_file = await tts.generate_speech(polish_starter)
                if audio_file and os.path.exists(audio_file):
                    with open(audio_file, "rb") as vf:
                        await q.message.reply_voice(vf)
            except Exception as e:
                logger.error(f"Roleplay starter audio error: {e}")
        return

    elif d == "ai_clear_history":
        ctx.user_data["ai_history"] = []
        lang = i18n.get_user_lang(uid)
        await q.message.reply_text(i18n.t("ai_cleared", lang), reply_markup=i18n.kb_ai_active(ctx.user_data.get("ai_mode", "chat"), lang))
        return

    elif d == "ai_exit":
        ctx.user_data.pop("ai_mode", None)
        ctx.user_data.pop("ai_history", None)
        lang = i18n.get_user_lang(uid)
        is_prem = payments.is_premium(uid)
        await q.message.reply_text(i18n.t("ai_exited", lang), parse_mode="Markdown", reply_markup=i18n.kb_reply_main(lang))
        await q.message.reply_text(i18n.t("in_main", lang), reply_markup=i18n.kb_main(uid, is_prem, lang))
        return

    # ── Bosh menyu ──────────────────────────────────
    if d == "main":
        u = get_user(uid) or {}
        lvl_p = level_progress(uid)
        is_prem = payments.is_premium(uid)
        lang = i18n.get_user_lang(uid)
        if lang == "ru":
            status_txt = "💎 Премиум Подписчик ✅" if is_prem else "🆓 Бесплатная версия"
        elif lang == "tm":
            status_txt = "💎 Premium Ýazylyjy ✅" if is_prem else "🆓 Mugt wersiýa"
        else:
            status_txt = "💎 Premium Obunachi ✅" if is_prem else "🆓 Bepul versiya"

        h_txt = heart_status_text(u)
        text = i18n.t(
            "main_menu_card",
            lang,
            name=q.from_user.first_name,
            status_txt=status_txt,
            streak=u.get('streak', 0),
            xp=u.get('xp', 0),
            hearts=h_txt,
            a1_1=lvl_p.get('A1.1', 0),
            a1_2=lvl_p.get('A1.2', 0),
            a2_1=lvl_p.get('A2.1', 0),
            a2_2=lvl_p.get('A2.2', 0)
        )
        await q.edit_message_text(text, parse_mode="Markdown", reply_markup=i18n.kb_main(uid, is_prem, lang))

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

    # ── Qolgan joyidan davom ettirish ───────────────
    elif d == "continue_lesson":
        lid = get_continue_lesson(uid)
        les = lesson(lid)
        les_num = LESSON_ORDER.index(lid) + 1 if lid in LESSON_ORDER else 1
        done = done_lessons(uid)

        if len(done) == len(LESSON_ORDER):
            await q.edit_message_text(
                "🎉 *Tabriklaymiz! Siz barcha 40 ta darsni muvaffaqiyatli tugatgansiz!*\n\n"
                "Bilimlaringizni mustahkamlash uchun darslarni boshidan qayta boshlashingiz "
                "yoki istalgan darsni takrorlashingiz mumkin.",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔄 Darslarni boshidan boshlash", callback_data="restart_lessons")],
                    [InlineKeyboardButton("📚 Darslar ro'yxati", callback_data="lessons")],
                    [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
                ])
            )
            return

        ok, reason = can_access_lesson(uid, lid)
        if reason == "premium_required":
            await q.edit_message_text(
                f"🔒 *Navbatdagi dars:* *{les_num}. {les.get('title', lid)}*\n\n"
                "Ushbu dars faqat **Premium** obunachilar uchun ochiq!\n\n"
                "Darslarni to'xtovsiz davom ettirish va barcha 40+ darslarni ochish uchun "
                "Premium obunani faollashtiring.",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("💎 Premium obunani olish", callback_data="premium_menu")],
                    [InlineKeyboardButton("📚 Darslar ro'yxati", callback_data="lessons")]
                ])
            )
            return

        status = "✅ *Tugatilgan!*" if lid in done else "🔓 *Navbatdagi dars (Qolgan joyingiz)*"
        text = (
            f"▶️ *Darsni davom ettirish*\n\n"
            f"{les.get('emoji','📘')} *{les_num}. {les.get('title',lid)}*\n"
            f"📗 Daraja: *{les.get('level','A1')}*\n\n"
            f"📚 So'zlar: *{len(les.get('vocab',[]))} ta* (Ovozli)\n"
            f"🧪 Testlar: *{len(les.get('exercises',[]))} ta*\n"
            f"⭐ Mukofot: *+{len(les.get('exercises',[]))*10} XP*\n\n"
            f"{status}\n\n"
            "📖 Darsni boshlash uchun quyidagi tugmani bosing:"
        )
        await q.edit_message_text(text, parse_mode="Markdown", reply_markup=kb_lesson_detail(lid, uid))

    # ── Darslarni boshidan boshlash ─────────────────
    elif d == "restart_lessons":
        first_lid = LESSON_ORDER[0]
        les = lesson(first_lid)
        done_count = len(done_lessons(uid))
        text = (
            "🔄 *Darslarni boshidan boshlash*\n\n"
            f"Hozirgacha o'zlashtirilgan darslar: *{done_count}/{len(LESSON_ORDER)} ta*.\n\n"
            f"Kursni 1-darsdan (*{les.get('emoji','👋')} 1. {les.get('title')}*) qayta boshlash uchun quyidagilardan birini tanlang:\n\n"
            "• **1-darsga o'tish** — to'plangan XP va natijalaringiz saqlanadi, shunchaki 1-dars ochiladi.\n"
            "• **Progressni tozalab 0 dan boshlash** — barcha o'tilgan darslar qulflanadi va kurs to'liq yangidan boshlanadi."
        )
        await q.edit_message_text(
            text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"▶️ 1-darsga o'tish ({les.get('title')})", callback_data=f"lesson:{first_lid}")],
                [InlineKeyboardButton("🗑 Progressni tozalash va 0 dan boshlash", callback_data="confirm_reset_progress")],
                [InlineKeyboardButton("◀️ Bekor qilish", callback_data="lessons")],
            ])
        )

    # ── Progressni tozalash tasdig'i ────────────────
    elif d == "confirm_reset_progress":
        db("DELETE FROM progress WHERE user_id=?", (uid,))
        db("DELETE FROM sessions WHERE user_id=?", (uid,))
        first_lid = LESSON_ORDER[0]
        les = lesson(first_lid)
        text = (
            "✅ *Progress muvaffaqiyatli tozalandi!*\n\n"
            f"Kurs to'liq yangidan boshlandi. Endi 1-dars (*1. {les.get('title')}*) dan o'rganishni boshlashingiz mumkin! 🚀"
        )
        await q.edit_message_text(
            text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"▶️ 1. {les.get('title')} darsini boshlash", callback_data=f"lesson:{first_lid}")],
                [InlineKeyboardButton("📚 Darslar ro'yxati", callback_data="lessons")],
                [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
            ])
        )

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
            les_num = LESSON_ORDER.index(lid) + 1 if lid in LESSON_ORDER else ""
            num_prefix = f"{les_num}. " if les_num else ""
            text = (
                f"🔒 *{num_prefix}{les.get('title', lid)} — Ushbu dars faqat Premium obunachilar uchun!*\n\n"
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
            prev_num = idx
            await q.edit_message_text(
                f"🔒 *Bu dars hali qulfli!*\n\n"
                f"Avval bu darsni tugatib keling:\n"
                f"*{prev.get('emoji','')} {prev_num}. {prev.get('title','')}* 📚",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(
                        f"▶️ {prev.get('emoji','')} {prev_num}. {prev.get('title','')}",
                        callback_data=f"lesson:{LESSON_ORDER[idx-1]}"
                    )],
                    [InlineKeyboardButton("◀️ Orqaga", callback_data="lessons")]
                ])
            )
            return

        les_num = LESSON_ORDER.index(lid) + 1 if lid in LESSON_ORDER else ""
        num_prefix = f"{les_num}. " if les_num else ""
        done = done_lessons(uid)
        status = "✅ *Tugatilgan!*" if lid in done else "🔓 Boshlashga tayyor"
        text = (
            f"{les.get('emoji','📘')} *{num_prefix}{les.get('title',lid)}*\n"
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
            les_num = LESSON_ORDER.index(lid) + 1 if lid in LESSON_ORDER else ""
            num_prefix = f"{les_num}. " if les_num else ""
            rows.append([InlineKeyboardButton(
                f"{les.get('emoji','')} {num_prefix}{les.get('title',lid)}",
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
            try:
                dictionary_service.record_mistake(
                    uid, lid, ex['q'], ex['opts'], correct, ex['opts'][choice]
                )
            except Exception as e:
                logger.warning(f"Xatoni yozishda muammo: {e}")

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
            upd_user(uid, hearts=new_h, last_heart_regen=datetime.now().isoformat())
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
        h_txt = heart_status_text(u)
        _, user_rank = get_leaderboard(uid)
        mistakes_cnt = dictionary_service.get_user_mistakes_count(uid)

        text = (
            f"📊 *Mening Progressim*\n\n"
            f"👤 O'quvchi: *{q.from_user.first_name}*\n"
            f"💎 Holat: *{'Premium ✅' if is_prem else 'Bepul 🆓'}*\n"
            f"⭐ Jami XP: *{u.get('xp',0)} ball* (Reyting: *#{user_rank}*)\n"
            f"🔥 Streak: *{u.get('streak',0)} kun ketma-ket*\n"
            f"❤️ Yuraklar: *{h_txt}*\n"
            f"👥 Taklif qilgan do'stlar: *{u.get('invited_count', 0)} ta*\n"
            f"⚠️ Hal qilinmagan xatolar: *{mistakes_cnt} ta*\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"📚 *Darajalar bo'yicha progress:*\n"
            f"📗 A1.1: {pbar(lvl_p.get('A1.1',0),10)} {lvl_p.get('A1.1',0)}/10\n"
            f"📘 A1.2: {pbar(lvl_p.get('A1.2',0),10)} {lvl_p.get('A1.2',0)}/10\n"
            f"📙 A2.1: {pbar(lvl_p.get('A2.1',0),10)} {lvl_p.get('A2.1',0)}/10\n"
            f"📕 A2.2: {pbar(lvl_p.get('A2.2',0),10)} {lvl_p.get('A2.2',0)}/10\n\n"
            f"🎯 Jami tugatilgan darslar: *{len(done)}/{len(LESSON_ORDER)}*"
        )
        prog_buttons = []
        if mistakes_cnt > 0:
            prog_buttons.append([InlineKeyboardButton(f"🔁 Xatolar ustida ishlash ({mistakes_cnt} ta)", callback_data="review_mistakes:0")])
        prog_buttons.append([
            InlineKeyboardButton("🏆 Reyting", callback_data="leaderboard"),
            InlineKeyboardButton("👥 Taklif qilish", callback_data="referral_info")
        ])
        prog_buttons.append([InlineKeyboardButton("📚 Darslarga o'tish", callback_data="lessons")])
        prog_buttons.append([InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")])

        await q.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(prog_buttons))

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
            "• To'lovlar **BLIK**, **Karta** yoki **Uzcard/Humo** orqali qabul qilinadi\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📞 *Qo'llab-quvvatlash va Aloqa:*\n"
            "Bot bo'yicha savol yoki takliflaringiz bo'lsa, adminga yozing."
        )
        await q.edit_message_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💎 Premium obuna", callback_data="premium_menu")],
                [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
            ]))

    # ── Peshqadamlar Reytingi (Leaderboard) ────────
    elif d == "leaderboard":
        rows, user_rank = get_leaderboard(uid)
        u = get_user(uid) or {}
        medals = ["🥇","🥈","🥉","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
        txt = "🏆 *PolUzAcademy Peshqadamlar Reytingi (TOP-10)*\n\n"
        for idx, r in enumerate(rows):
            medal = medals[idx] if idx < len(medals) else f"{idx+1}."
            name = r["name"] or f"O'quvchi {r['user_id']}"
            txt += f"{medal} *{name}* — `{r['xp']}` XP (🔥 {r['streak']} kun)\n"
        txt += (
            f"\n━━━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 Sizning o'rningiz: *#{user_rank}* (`{u.get('xp',0)}` XP)\n\n"
            "Har kuni darslarni bajaring va peshqadamlar safiga qo'shiling! 🚀"
        )
        await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("▶️ Darslarni davom ettirish", callback_data="continue_lesson")],
            [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
        ]))

    # ── Do'stlarni taklif qilish (Referral) ────────
    elif d == "referral_info":
        bot_me = await ctx.bot.get_me()
        bot_user = bot_me.username or "PolUzAcademyBot"
        ref_link = f"https://t.me/{bot_user}?start=ref_{uid}"
        u = get_user(uid) or {}
        cnt = u.get("invited_count") or 0
        txt = (
            "👥 *Do'stlarni taklif qiling va Bepul Premium yutib oling!*\n\n"
            f"Sizning shaxsiy taklif havolangiz:\n`{ref_link}`\n\n"
            f"📊 Siz taklif qilgan do'stlar soni: *{cnt} ta*\n\n"
            "🎁 *Mukofotlar:*\n"
            "• Har bir qo'shilgan do'st uchun: *+50 XP* ball ⭐\n"
            "• 3 ta do'st: *7 kunlik bepul Premium* 💎\n"
            "• 10 ta do'st: *30 kunlik bepul Premium* 👑\n\n"
            "Ushbu havolani nusxalab, do'stlaringizga yoki guruhlarga yuboring!"
        )
        import urllib.parse
        share_caption = urllib.parse.quote("Polyak tilini PolUzAcademy boti bilan 0 dan bepul o'rganing! 🦉🇵🇱")
        share_url = f"https://t.me/share/url?url={ref_link}&text={share_caption}"
        await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📲 Do'stlarga ulashish (Telegram)", url=share_url)],
            [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
        ]))

    # ── Polsha hayoti qo'llanmasi ─────────────────
    elif d == "poland_guide":
        txt = (
            "🇵🇱 *Polsha hayoti va Muloqot qo'llanmasi*\n\n"
            "Polshada yashayotgan va ishlayotgan vatandoshlarimiz uchun eng zarur amaliy qo'llanma:\n"
            "• 🏛 **Urząd va Karta Pobytu** — arizalar, meldunek, PESEL\n"
            "• 💼 **Ish joyi** — sklad, zavod, kuryer, qurilish iboralari\n"
            "• 🚑 **SOS & Elchixona** — tez yordam, dorixona, favqulodda vaziyatlar\n"
            "• 🚌 **Transport va Do'kon** — chiptalar, shahar muloqoti\n\n"
            "O'rganmoqchi bo'lgan bo'limingizni tanlang:"
        )
        await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=poland_guide.kb_guide_main())

    elif d.startswith("guide:"):
        sec_id = d.split(":")[1]
        sec = poland_guide.GUIDE_SECTIONS.get(sec_id)
        if sec:
            txt = f"*{sec['title']}*\n_{sec['desc']}_\n\n━━━━━━━━━━━━━━━━━━━━━━\n📚 *Asosiy so'z va iboralar:*\n\n"
            for pl, ph, uz in sec["terms"]:
                txt += f"• 🇵🇱 `{pl}`\n    🔊 _{ph}_\n    🇺🇿 {uz}\n\n"
            if sec.get("dialog"):
                txt += f"━━━━━━━━━━━━━━━━━━━━━━\n{sec['dialog']}\n\n"
            if sec.get("embassy_info"):
                txt += f"━━━━━━━━━━━━━━━━━━━━━━\n{sec['embassy_info']}\n"
            await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=poland_guide.kb_guide_section(sec_id))

    elif d.startswith("guide_audio:"):
        sec_id = d.split(":")[1]
        sec = poland_guide.GUIDE_SECTIONS.get(sec_id)
        if sec:
            await q.answer("🔊 Audio tayyorlanmoqda...")
            words = [p[0] for p in sec["terms"][:12]]
            clean_diag = ". ".join(words)
            audio_path = await tts.generate_speech(clean_diag)
            if audio_path and os.path.exists(audio_path):
                with open(audio_path, "rb") as af:
                    await ctx.bot.send_voice(
                        chat_id=uid,
                        voice=af,
                        caption=f"🦉 *{sec['title']}* — Lug'at talaffuzi (Polyakcha)",
                        parse_mode="Markdown"
                    )
            else:
                await q.answer("Ovoz hosil qilishda xatolik!", show_alert=True)

    # ── Flashcards (Lug'at kartochkalari) ──────────
    elif d.startswith("flashcards:"):
        _, lid, idx_s = d.split(":")
        idx = int(idx_s)
        les = lesson(lid)
        vocab = les.get("vocab", [])
        if not vocab:
            await q.answer("Lug'at topilmadi!", show_alert=True)
            return

        if idx >= len(vocab):
            learned_cnt = dictionary_service.get_lesson_flashcards_progress(uid, lid)
            txt = (
                f"🎉 *Ajoyib natija!*\n\n"
                f"Siz *{les.get('title', lid)}* darsidagi barcha {len(vocab)} ta so'z kartochkalarini ko'rib chiqdingiz!\n"
                f"✅ O'zlashtirilgan so'zlar: *{learned_cnt}/{len(vocab)} ta*\n\n"
                "Endi dars testlarini topshirishingiz yoki boshidan takrorlashingiz mumkin."
            )
            await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("▶️ Darsni boshlash", callback_data=f"go:{lid}")],
                [InlineKeyboardButton("🔁 Kartochkalarni qayta o'qish", callback_data=f"flashcards:{lid}:0")],
                [InlineKeyboardButton("◀️ Darsga qaytish", callback_data=f"lesson:{lid}")]
            ]))
            return

        w = vocab[idx]
        txt = (
            f"🗂 *Lug'at Kartochkasi ({idx+1}/{len(vocab)})*\n"
            f"Dars: *{les.get('title', lid)}*\n\n"
            f"🇵🇱 So'z: *{w['pl']}*\n"
            f"🔊 Talaffuz: _{w['ph']}_\n\n"
            "Tarjimasini bilasizmi? Bilish uchun quyidagi tugmani bosing:"
        )
        await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("👁 Tarjimasini ko'rish", callback_data=f"fc_reveal:{lid}:{idx}")],
            [InlineKeyboardButton("⏭ O'tkazib yuborish", callback_data=f"flashcards:{lid}:{idx+1}")],
            [InlineKeyboardButton("◀️ Darsga qaytish", callback_data=f"lesson:{lid}")]
        ]))

    elif d.startswith("fc_reveal:"):
        _, lid, idx_s = d.split(":")
        idx = int(idx_s)
        les = lesson(lid)
        vocab = les.get("vocab", [])
        if idx >= len(vocab):
            return
        w = vocab[idx]
        txt = (
            f"🗂 *Lug'at Kartochkasi ({idx+1}/{len(vocab)})*\n"
            f"Dars: *{les.get('title', lid)}*\n\n"
            f"🇵🇱 Polyakcha: *{w['pl']}*\n"
            f"🔊 O'qilishi: _{w['ph']}_\n"
            f"🇺🇿 Tarjimasi: *{w['uz']}*\n\n"
            "Ushbu so'zni eslab qoldingizmi?"
        )
        await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🔊 Talaffuzni eshitish", callback_data=f"tts_word:{w['pl']}")],
            [InlineKeyboardButton("✅ Yodladim", callback_data=f"fc_learn:{lid}:{idx}:1"),
             InlineKeyboardButton("🔄 Qaytarish", callback_data=f"fc_learn:{lid}:{idx}:0")],
            [InlineKeyboardButton("➡️ Keyingi so'z", callback_data=f"flashcards:{lid}:{idx+1}")],
            [InlineKeyboardButton("◀️ Darsga qaytish", callback_data=f"lesson:{lid}")]
        ]))

    elif d.startswith("fc_learn:"):
        _, lid, idx_s, val_s = d.split(":")
        idx = int(idx_s)
        learned = (val_s == "1")
        les = lesson(lid)
        vocab = les.get("vocab", [])
        if idx < len(vocab):
            dictionary_service.mark_card_learned(uid, lid, vocab[idx]["pl"], learned)
        next_idx = idx + 1
        q.data = f"flashcards:{lid}:{next_idx}"
        await on_cb(update, ctx)
        return

    # ── Xatolar ustida ishlash (Review Mistakes) ──
    elif d.startswith("review_mistakes:"):
        mistakes = dictionary_service.get_user_mistakes(uid, limit=10)
        if not mistakes:
            await q.edit_message_text(
                "🎉 *Tabriklaymiz! Sizda hal qilinmagan xatolar yo'q!*\n\n"
                "Barcha dars testlarini a'lo darajada o'zlashtirgansiz.",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("📚 Darslarga o'tish", callback_data="lessons")],
                    [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
                ])
            )
            return

        m = mistakes[0]
        opts = m["opts"]
        mid = m["id"]
        txt = (
            f"🔁 *Xatolar ustida ishlash ({len(mistakes)} ta qoldi)*\n\n"
            f"{m['question']}\n\n"
            f"⚠️ Oldingi xato javobingiz: _{m.get('wrong_choice','Noma`lum')}_\n\n"
            "To'g'ri javobni tanlang:"
        )
        letters = ["🅐","🅑","🅒","🅓"]
        rows = [
            [InlineKeyboardButton(f"{letters[i]}  {opt}", callback_data=f"ans_mistake:{mid}:{i}")]
            for i, opt in enumerate(opts)
        ]
        rows.append([InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")])
        await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(rows))

    elif d.startswith("ans_mistake:"):
        _, mid_s, ch_s = d.split(":")
        mid = int(mid_s)
        choice = int(ch_s)
        con = sqlite3.connect(DB_PATH)
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        m = cur.execute("SELECT * FROM mistakes WHERE id=?", (mid,)).fetchone()
        con.close()
        if not m:
            await q.answer("Savol topilmadi!", show_alert=True)
            return

        import json
        opts = json.loads(m["opts_json"])
        correct_idx = m["correct_idx"]
        is_ok = (choice == correct_idx)

        if is_ok:
            dictionary_service.resolve_mistake(uid, m["question"])
            u = get_user(uid) or {}
            upd_user(uid, xp=(u.get("xp",0) + 5))
            txt = (
                "✅ *Ajoyib! Xatoni to'g'riladingiz!* (+5 ⭐)\n\n"
                f"{m['question']}\n\n"
                f"To'g'ri javob: *{opts[correct_idx]}*"
            )
            btn = [InlineKeyboardButton("➡️ Keyingi xato", callback_data="review_mistakes:0")]
        else:
            txt = (
                "❌ *Afsuski, yana noto'g'ri bo'ldi.*\n\n"
                f"{m['question']}\n\n"
                f"To'g'ri javob: *{opts[correct_idx]}*\n"
                "Qaytadan urinib ko'ring!"
            )
            btn = [InlineKeyboardButton("🔁 Qaytadan urinish", callback_data="review_mistakes:0")]

        await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([
            btn,
            [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
        ]))

    # ── TTS so'z talaffuzi ─────────────────────────
    elif d.startswith("tts_word:"):
        word = d[9:]
        await q.answer("🔊 Talaffuz tayyorlanmoqda...")
        audio_path = await tts.generate_speech(word)
        if audio_path and os.path.exists(audio_path):
            with open(audio_path, "rb") as af:
                await ctx.bot.send_voice(
                    chat_id=uid,
                    voice=af,
                    caption=f"🇵🇱 *{word}* — Polyakcha talaffuz",
                    parse_mode="Markdown"
                )

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
                    [InlineKeyboardButton("▶️ Qolgan joyidan davom ettirish", callback_data="continue_lesson")],
                    [InlineKeyboardButton("📚 Darslar ro'yxati", callback_data="lessons")]
                ])
            )
        except Exception as e:
            logger.warning(f"Eslatma yuborishda xatolik {row['user_id']}: {e}")

# ═══════════════════════════════════════════
# BUYRUQLAR
# ═══════════════════════════════════════════
async def cmd_davom(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    ensure_user(uid, update.effective_user.first_name)
    lid = get_continue_lesson(uid)
    les = lesson(lid)
    les_num = LESSON_ORDER.index(lid) + 1 if lid in LESSON_ORDER else 1
    done = done_lessons(uid)

    if len(done) == len(LESSON_ORDER):
        await update.message.reply_text(
            "🎉 *Tabriklaymiz! Siz barcha 40 ta darsni muvaffaqiyatli tugatgansiz!*\n\n"
            "Darslarni boshidan qayta boshlashingiz yoki istalgan darsni takrorlashingiz mumkin.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 Darslarni boshidan boshlash", callback_data="restart_lessons")],
                [InlineKeyboardButton("📚 Darslar ro'yxati", callback_data="lessons")]
            ])
        )
        return

    ok, reason = can_access_lesson(uid, lid)
    if reason == "premium_required":
        await update.message.reply_text(
            f"🔒 *Navbatdagi dars:* *{les_num}. {les.get('title', lid)}*\n\n"
            "Ushbu dars faqat **Premium** obunachilar uchun ochiq!\n\n"
            "Darslarni to'xtovsiz davom ettirish va barcha 40+ darslarni ochish uchun "
            "Premium obunani faollashtiring.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💎 Premium obunani olish", callback_data="premium_menu")],
                [InlineKeyboardButton("📚 Barcha darslar", callback_data="lessons")]
            ])
        )
        return

    status = "✅ *Tugatilgan!*" if lid in done else "🔓 *Navbatdagi dars (Qolgan joyingiz)*"
    text = (
        f"▶️ *Qolgan joyingizdan davom eting!*\n\n"
        f"{les.get('emoji','📘')} *{les_num}. {les.get('title',lid)}*\n"
        f"📗 Daraja: *{les.get('level','A1')}*\n\n"
        f"📚 So'zlar: *{len(les.get('vocab',[]))} ta* (Ovozli)\n"
        f"🧪 Testlar: *{len(les.get('exercises',[]))} ta*\n"
        f"⭐ Mukofot: *+{len(les.get('exercises',[]))*10} XP*\n\n"
        f"{status}\n\n"
        "Quyidagi tugmalardan birini tanlang:"
    )
    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=kb_lesson_detail(lid, uid))

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
    if not is_admin(uid):
        await update.message.reply_text(
            f"⛔️ *Sizda admin huquqi yo'q.*\n\n"
            f"🆔 Sizning Telegram ID: `{uid}`\n"
            f"Admin bo'lish uchun ushbu ID raqamni `ADMIN_IDS` ro'yxatiga qo'shish kerak.",
            parse_mode="Markdown"
        )
        return

    users_cnt = db("SELECT COUNT(*) as cnt FROM users", (), "one")
    stats = payments.get_payment_stats()
    
    pending_m = db("SELECT COUNT(*) as cnt FROM manual_payments WHERE status='pending'", (), "one")
    pending_cnt = pending_m["cnt"] if pending_m else 0

    text = (
        "👑 *PolUzAcademy Admin Paneli*\n\n"
        f"👥 Jami foydalanuvchilar: *{users_cnt['cnt'] if users_cnt else 0} ta*\n"
        f"💎 Faol Premium obunachilar: *{stats['active_users']} ta*\n"
        f"💳 Jami to'lovlar soni: *{stats['total_payments_count']} ta*\n"
        f"💰 Jami tushum: *{stats['total_revenue_pln']:.2f} PLN*\n"
        f"⏳ Kutilayotgan cheklar: *{pending_cnt} ta*\n\n"
        "⚡️ *Admin buyruqlari:*\n"
        "• `/grant <user_id> <kunlar>` — Premium berish\n"
        "• `/broadcast <matn>` — Barcha foydalanuvchilarga xabar tarqatish\n"
        "• `/reply <user_id> <matn>` — O'quvchiga bot nomidan javob berish\n"
        "• `/backup` — Ma'lumotlar bazasini yuklab olish"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def cmd_grant(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if not is_admin(uid):
        await update.message.reply_text("⛔️ Bu buyruq faqat adminlar uchun.")
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

async def cmd_broadcast(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if not is_admin(uid):
        return
    if not ctx.args:
        await update.message.reply_text("Format: `/broadcast <xabar matni>`\n\nBarcha foydalanuvchilarga xabar yuborish.", parse_mode="Markdown")
        return

    broadcast_text = " ".join(ctx.args)
    users = db("SELECT user_id FROM users", fetch="all")
    if not users:
        await update.message.reply_text("Foydalanuvchilar topilmadi.")
        return

    sent = 0
    failed = 0
    status_msg = await update.message.reply_text(f"📢 Xabar tarqatilmoqda (Jami: {len(users)})...")

    for u in users:
        try:
            await ctx.bot.send_message(
                chat_id=u["user_id"],
                text=broadcast_text,
                parse_mode="Markdown"
            )
            sent += 1
        except Exception:
            failed += 1
        await asyncio.sleep(0.04)

    await status_msg.edit_text(
        f"✅ *Xabar tarqatish yakunlandi!*\n\n"
        f"📨 Yuborildi: *{sent} ta*\n"
        f"❌ Yetib bormadi (bloklagan): *{failed} ta*",
        parse_mode="Markdown"
    )

async def cmd_backup(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if not is_admin(uid):
        return
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "rb") as doc:
            await update.message.reply_document(
                document=doc,
                filename=f"polyakcha_backup_{datetime.now().strftime('%Y%m%d_%H%M')}.db",
                caption="💾 *PolUzAcademy ma'lumotlar bazasi zaxira nusxasi*",
                parse_mode="Markdown"
            )
    else:
        await update.message.reply_text("Baza fayli topilmadi.")

async def cmd_reply(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if not is_admin(uid):
        return
    if len(ctx.args) < 2:
        await update.message.reply_text("Format: `/reply <user_id> <xabar>`", parse_mode="Markdown")
        return
    try:
        target_uid = int(ctx.args[0])
        reply_txt = " ".join(ctx.args[1:])
        await ctx.bot.send_message(
            chat_id=target_uid,
            text=f"💬 *PolUzAcademy Adminidan javob:*\n\n{reply_txt}",
            parse_mode="Markdown"
        )
        await update.message.reply_text(f"✅ Xabar `{target_uid}` ga muvaffaqiyatli yetkazildi.")
    except Exception as e:
        await update.message.reply_text(f"Xatolik: {e}")

async def cmd_reyting(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    ensure_user(uid, update.effective_user.first_name)
    rows, user_rank = get_leaderboard(uid)
    u = get_user(uid) or {}
    medals = ["🥇","🥈","🥉","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
    txt = "🏆 *PolUzAcademy Peshqadamlar Reytingi (TOP-10)*\n\n"
    for idx, r in enumerate(rows):
        medal = medals[idx] if idx < len(medals) else f"{idx+1}."
        name = r["name"] or f"O'quvchi {r['user_id']}"
        txt += f"{medal} *{name}* — `{r['xp']}` XP (🔥 {r['streak']} kun)\n"
    txt += (
        f"\n━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 Sizning o'rningiz: *#{user_rank}* (`{u.get('xp',0)}` XP)\n\n"
        "Har kuni darslarni bajaring va peshqadamlar safiga qo'shiling! 🚀"
    )
    await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("▶️ Darslarni davom ettirish", callback_data="continue_lesson")],
        [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
    ]))

async def cmd_guide(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    txt = (
        "🇵🇱 *Polsha hayoti va Muloqot qo'llanmasi*\n\n"
        "Polshada yashayotgan va ishlayotgan vatandoshlarimiz uchun eng zarur amaliy qo'llanma:\n"
        "• 🏛 **Urząd va Karta Pobytu** — arizalar, meldunek, PESEL\n"
        "• 💼 **Ish joyi** — sklad, zavod, kuryer, qurilish iboralari\n"
        "• 🚑 **SOS & Elchixona** — tez yordam, dorixona, favqulodda vaziyatlar\n"
        "• 🚌 **Transport va Do'kon** — chiptalar, shahar muloqoti\n\n"
        "O'rganmoqchi bo'lgan bo'limingizni tanlang:"
    )
    await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=poland_guide.kb_guide_main())

async def show_referral_msg(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    ensure_user(uid, update.effective_user.first_name)
    bot_me = await ctx.bot.get_me()
    bot_user = bot_me.username or "PolUzAcademyBot"
    ref_link = f"https://t.me/{bot_user}?start=ref_{uid}"
    u = get_user(uid) or {}
    cnt = u.get("invited_count") or 0
    txt = (
        "👥 *Do'stlarni taklif qiling va Bepul Premium yutib oling!*\n\n"
        f"Sizning shaxsiy taklif havolangiz:\n`{ref_link}`\n\n"
        f"📊 Siz taklif qilgan do'stlar soni: *{cnt} ta*\n\n"
        "🎁 *Mukofotlar:*\n"
        "• Har bir do'st uchun: *+50 XP* ball ⭐\n"
        "• 3 ta do'st: *7 kunlik bepul Premium* 💎\n"
        "• 10 ta do'st: *30 kunlik bepul Premium* 👑\n\n"
        "Ushbu havolani nusxalab, do'stlaringizga yoki guruhlarga yuboring!"
    )
    import urllib.parse
    share_caption = urllib.parse.quote("Polyak tilini PolUzAcademy boti bilan 0 dan bepul o'rganing! 🦉🇵🇱")
    share_url = f"https://t.me/share/url?url={ref_link}&text={share_caption}"
    await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("📲 Do'stlarga ulashish (Telegram)", url=share_url)],
        [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
    ]))

async def handle_photo(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    """Foydalanuvchi yuborgan rasmni (masalan, to'lov cheki) qabul qilish."""
    handled = await payments.handle_receipt_photo(update, ctx, ADMIN_IDS)
    if not handled:
        await update.message.reply_text(
            "📸 Rasm qabul qilindi. Agar bu to'lov cheki bo'lsa, avval '💎 Premium' bo'limidan 'Uzcard/Humo yoki Chek orqali' tugmasini bosing.",
            reply_markup=kb_main(update.effective_user.id)
        )

async def handle_text(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    msg_text = update.message.text.strip()
    uid = update.effective_user.id
    ensure_user(uid, update.effective_user.first_name)
    user_lang = i18n.get_user_lang(uid)
    is_prem = payments.is_premium(uid)

    # 1. AI Ustoz menyusini ochish
    ai_triggers = [
        "🤖 AI Ustoz", "🤖 AI Учитель", "🤖 AI Halypa",
        "/ai", "AI Ustoz", "ai", "ai ustoz", "ai halypa", "ai учитель"
    ]
    if msg_text in ai_triggers:
        await cmd_ai(update, ctx)
        return

    # 2. Agar foydalanuvchi hozir AI rejimida bo'lsa
    ai_mode = ctx.user_data.get("ai_mode")
    if ai_mode:
        # Rejimdan chiqish buyruqlari
        exit_phrases = [
            "/exit", "chiqish", "exit", "orqaga", "stop", "tugatish",
            "выход", "назад", "стоп",
            "çykyş", "yzyna"
        ]
        if msg_text.lower() in exit_phrases:
            ctx.user_data.pop("ai_mode", None)
            ctx.user_data.pop("ai_history", None)
            await update.message.reply_text(
                i18n.t("ai_exited", user_lang),
                parse_mode="Markdown",
                reply_markup=i18n.kb_reply_main(user_lang)
            )
            await update.message.reply_text(
                "🦉" if user_lang != "uz" else "Nima qilamiz?",
                reply_markup=i18n.kb_main(uid, is_prem, user_lang)
            )
            return

        # Agar pastki menyu tugmalari bosilsa, AI rejimini yopib menyuga o'tish
        nav_buttons = [
            "▶️ Davom ettirish", "▶️ Продолжить", "▶️ Dowam etmek",
            "📚 Darslar", "📚 Уроки", "📚 Sapaklar",
            "📖 Lug'at & Qidiruv", "📖 Словарь & Поиск", "📖 Sözlük & Gözleg",
            "🏆 Reyting", "🏆 Рейтинг", "🏆 Reýting",
            "🇵🇱 Polsha hayoti", "🇵🇱 Жизнь в Польше", "🇵🇱 Polşada durmuş",
            "👤 Profilim", "👤 Мой профиль",
            "💎 Premium", "💎 Премиум",
            "👥 Do'stlarni taklif qilish", "👥 Пригласить друзей", "👥 Dostlary çagyrmak", "👥 Taklif qilish"
        ]
        if msg_text in nav_buttons:
            ctx.user_data.pop("ai_mode", None)
            ctx.user_data.pop("ai_history", None)
            # Pastdagi tugmalar handleriga o'tadi
        else:
            # AI savol-javobini bajarish
            allowed, remaining = ai_assistant.check_and_use_ai_quota(uid, is_prem)
            if not allowed:
                prem_btn_txt = i18n.t("btn_premium", user_lang)
                exit_btn_txt = i18n.t("ai_btn_exit", user_lang)
                await update.message.reply_text(
                    i18n.t("ai_quota_exceeded", user_lang),
                    parse_mode="Markdown",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(prem_btn_txt, callback_data="premium_menu")],
                        [InlineKeyboardButton(exit_btn_txt, callback_data="ai_exit")]
                    ])
                )
                return

            await ctx.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
            history = ctx.user_data.get("ai_history", [])
            reply_text = await ai_assistant.ask_gemini(msg_text, mode=ai_mode, history=history, lang=user_lang)

            history.append({"role": "user", "content": msg_text})
            history.append({"role": "model", "content": reply_text})
            ctx.user_data["ai_history"] = history[-8:]

            if is_prem:
                quota_note = "💎 " + ("Cheksiz" if user_lang == "uz" else ("Безлимитно" if user_lang == "ru" else "Çäksiz"))
            else:
                quota_note = f"⚡️ Bugun qoldi: {remaining} ta" if user_lang == "uz" else (f"⚡️ Осталось: {remaining}" if user_lang == "ru" else f"⚡️ Şu gün galdy: {remaining}")
            footer = f"\n\n_({quota_note})_"

            try:
                await update.message.reply_text(
                    reply_text + footer,
                    parse_mode="Markdown",
                    reply_markup=i18n.kb_ai_active(ai_mode, user_lang)
                )
            except Exception:
                await update.message.reply_text(
                    reply_text + f"\n\n({quota_note})",
                    reply_markup=i18n.kb_ai_active(ai_mode, user_lang)
                )

            # Rolli o'yinda javobning polyakcha qismini ovozli jo'natish
            if ai_mode.startswith("roleplay_"):
                polish_only = re.sub(r"\(.*?\)", "", reply_text).strip()
                polish_only = re.sub(r"[*_`#~]", "", polish_only).strip()
                if polish_only and len(polish_only) < 300:
                    try:
                        voice_file = await tts.generate_speech(polish_only)
                        if voice_file and os.path.exists(voice_file):
                            with open(voice_file, "rb") as vf:
                                await update.message.reply_voice(vf)
                    except Exception as e:
                        logger.error(f"TTS voice reply error: {e}")
            return

    # 3. Pastki klaviatura tugmalarini qayta ishlash (O'zbek, Rus, Turkman)
    if msg_text in ["▶️ Davom ettirish", "▶️ Продолжить", "▶️ Dowam etmek"]:
        await cmd_davom(update, ctx)
        return
    elif msg_text in ["📚 Darslar", "📚 Уроки", "📚 Sapaklar"]:
        await cmd_darslar(update, ctx)
        return
    elif msg_text in ["📖 Lug'at & Qidiruv", "📖 Словарь & Поиск", "📖 Sözlük & Gözleg"]:
        await cmd_lugat(update, ctx)
        return
    elif msg_text in ["🏆 Reyting", "🏆 Рейтинг", "🏆 Reýting"]:
        await cmd_reyting(update, ctx)
        return
    elif msg_text in ["🇵🇱 Polsha hayoti", "🇵🇱 Жизнь в Польше", "🇵🇱 Polşada durmuş"]:
        await cmd_guide(update, ctx)
        return
    elif msg_text in ["👤 Profilim", "👤 Мой профиль"]:
        await cmd_progress(update, ctx)
        return
    elif msg_text in ["💎 Premium", "💎 Премиум"]:
        await payments.show_premium(update, ctx)
        return
    elif msg_text in ["👥 Do'stlarni taklif qilish", "👥 Пригласить друзей", "👥 Dostlary çagyrmak", "👥 Taklif qilish"]:
        await show_referral_msg(update, ctx)
        return

    # 4. Promo kod tekshirish
    handled = await payments.check_promo_code(update, ctx)
    if handled:
        return

    # 5. Lug'atdan tezkor qidiruv (Pocket search)
    results = dictionary_service.search_vocab(msg_text, limit=5)
    if results:
        res_text = f"🔍 *Lug'atdan topildi:* *'{msg_text}'*\n\n"
        buttons = []
        for i, item in enumerate(results, 1):
            res_text += (
                f"*{i}.* 🇵🇱 `{item['pl']}`\n"
                f"    🔊 _{item['ph']}_\n"
                f"    🇺🇿 {item['uz']}\n"
                f"    📚 _{item['lesson_title']}_\n\n"
            )
            if i <= 3:
                buttons.append([InlineKeyboardButton(f"🔊 '{item['pl']}' talaffuzi", callback_data=f"tts_word:{item['pl']}")])

        buttons.append([InlineKeyboardButton(i18n.t("in_main", user_lang), callback_data="main")])
        await update.message.reply_text(
            res_text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        return

    # 6. Agar so'z topilmasa
    if user_lang == "ru":
        no_match_text = (
            f"🤔 Слово *'{msg_text}'* не найдено в словаре уроков.\n\n"
            "💡 *Совет:* Для поиска введите слово на польском (например: `dzień`, `praca`, `urząd`).\n"
            "Или задайте вопрос в разделе **🤖 AI Учитель**!\n\n"
            "Выберите один из разделов ниже:"
        )
    elif user_lang == "tm":
        no_match_text = (
            f"🤔 *'{msg_text}'* sözi sapaklar sözlüginden tapylmady.\n\n"
            "💡 *Maslahat:* Gözlemek üçin sözi polýakça ýazyň (meselem: `dzień`, `praca`, `urząd`).\n"
            "Ýa-da soragyňyz bar bolsa, **🤖 AI Halypa** bölümine ýüz tutuň!\n\n"
            "Aşakdaky bölümlerden birini saýlaň:"
        )
    else:
        no_match_text = (
            f"🤔 *'{msg_text}'* so'zi darslar lug'atidan topilmadi.\n\n"
            "💡 *Maslahat:* Qidirish uchun so'zni polyakcha yoki o'zbekcha yozing (masalan: `salom`, `dzień`, `ish`, `urząd`).\n"
            "Yoki savolingiz bo'lsa, **🤖 AI Ustoz** bo'limiga murojaat qiling!\n\n"
            "Quyidagi tugmalardan birini tanlang:"
        )
    await update.message.reply_text(
        no_match_text,
        parse_mode="Markdown",
        reply_markup=i18n.kb_main(uid, is_prem, user_lang)
    )

async def handle_voice(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    """
    Foydalanuvchining ovozli xabarini qabul qilib,
    Google Gemini multimodal modeli orqali tahlil qiladi va javob beradi.
    """
    uid = update.effective_user.id
    ensure_user(uid, update.effective_user.first_name)
    voice = update.message.voice
    if not voice:
        return

    user_lang = i18n.get_user_lang(uid)
    ai_mode = ctx.user_data.get("ai_mode", "chat")
    is_prem = payments.is_premium(uid)

    allowed, remaining = ai_assistant.check_and_use_ai_quota(uid, is_prem)
    if not allowed:
        prem_btn_txt = i18n.t("btn_premium", user_lang)
        exit_btn_txt = i18n.t("ai_btn_exit", user_lang)
        await update.message.reply_text(
            i18n.t("ai_quota_exceeded", user_lang),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(prem_btn_txt, callback_data="premium_menu")],
                [InlineKeyboardButton(exit_btn_txt, callback_data="ai_exit")]
            ])
        )
        return

    listening_txt = (
        "🎧 _Голос обрабатывается и анализируется..._" if user_lang == "ru"
        else ("🎧 _Sesiňiz diňlenilýär we derňelýär..._" if user_lang == "tm"
        else "🎧 _Ovozingiz tinglanmoqda va tahlil qilinmoqda..._")
    )
    status_msg = await update.message.reply_text(listening_txt, parse_mode="Markdown")
    await ctx.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.RECORD_VOICE)

    try:
        voice_file = await ctx.bot.get_file(voice.file_id)
        audio_byte_array = await voice_file.download_as_bytearray()
        audio_bytes = bytes(audio_byte_array)

        history = ctx.user_data.get("ai_history", [])

        audio_prompts = {
            "uz": "Ushbu yuborilgan audio xabarni tinglab, to'liq tushunib, polyak tilini o'rganuvchiga mos ravishda o'zbek tilida tushuntirish berib javob bering.",
            "ru": "Прослушай это аудиосообщение, пойми его и ответь изучающему польский язык с пояснениями на русском языке.",
            "tm": "Bu iberilen sesli habary diňläp, polýak dilini öwrenijä laýyk edip türkmen dilinde düşündiriş bilen jogap beriň."
        }
        audio_prompt = audio_prompts.get(user_lang, audio_prompts["uz"])

        reply_text = await ai_assistant.ask_gemini(
            prompt=audio_prompt,
            mode=ai_mode,
            history=history,
            audio_bytes=audio_bytes,
            mime_type="audio/ogg",
            lang=user_lang
        )

        history.append({"role": "user", "content": "[Ovozli xabar]"})
        history.append({"role": "model", "content": reply_text})
        ctx.user_data["ai_history"] = history[-8:]

        if is_prem:
            quota_note = "💎 " + ("Cheksiz" if user_lang == "uz" else ("Безлимитно" if user_lang == "ru" else "Çäksiz"))
        else:
            quota_note = f"⚡️ Bugun qoldi: {remaining} ta" if user_lang == "uz" else (f"⚡️ Осталось: {remaining}" if user_lang == "ru" else f"⚡️ Şu gün galdy: {remaining}")
        footer = f"\n\n_({quota_note})_"

        try:
            await status_msg.edit_text(reply_text + footer, parse_mode="Markdown", reply_markup=i18n.kb_ai_active(ai_mode, user_lang))
        except Exception:
            await status_msg.edit_text(reply_text + f"\n\n({quota_note})", reply_markup=i18n.kb_ai_active(ai_mode, user_lang))

        # Agar rol o'yini bo'lsa, qahramon javobini ovozli yuborish
        if ai_mode.startswith("roleplay_"):
            polish_speech_part = re.sub(r"\(.*?\)", "", reply_text).strip()
            polish_speech_part = re.sub(r"[*_`#~]", "", polish_speech_part).strip()
            if polish_speech_part and len(polish_speech_part) < 250:
                try:
                    resp_audio = await tts.generate_speech(polish_speech_part)
                    if resp_audio and os.path.exists(resp_audio):
                        with open(resp_audio, "rb") as vf:
                            await update.message.reply_voice(vf)
                except Exception as e:
                    logger.error(f"Voice reply TTS generation error: {e}")

    except Exception as e:
        logger.error(f"Ovozli xabarni qayta ishlashda xatolik: {e}")
        err_txt = "❌ Ошибка при обработке голоса" if user_lang == "ru" else ("❌ Sesi gaýtadan işlemekde ýalňyşlyk" if user_lang == "tm" else "❌ Ovozni qayta ishlashda xatolik yuz berdi")
        await status_msg.edit_text(f"{err_txt}: {e}")

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

    app.add_handler(CommandHandler("start",     cmd_start))
    app.add_handler(CommandHandler("lang",      cmd_lang))
    app.add_handler(CommandHandler("til",       cmd_lang))
    app.add_handler(CommandHandler("davom",     cmd_davom))
    app.add_handler(CommandHandler("darslar",   cmd_darslar))
    app.add_handler(CommandHandler("progress",  cmd_progress))
    app.add_handler(CommandHandler("lugat",     cmd_lugat))
    app.add_handler(CommandHandler("reyting",   cmd_reyting))
    app.add_handler(CommandHandler("guide",     cmd_guide))
    app.add_handler(CommandHandler("premium",   cmd_premium))
    app.add_handler(CommandHandler("ai",        cmd_ai))
    app.add_handler(CommandHandler("admin",     cmd_admin))
    app.add_handler(CommandHandler("grant",     cmd_grant))
    app.add_handler(CommandHandler("broadcast", cmd_broadcast))
    app.add_handler(CommandHandler("backup",    cmd_backup))
    app.add_handler(CommandHandler("reply",     cmd_reply))
    app.add_handler(CommandHandler("id",        cmd_id))
    app.add_handler(CommandHandler("myid",      cmd_id))
    app.add_handler(CommandHandler("help",      payments.show_premium))
    app.add_handler(CallbackQueryHandler(on_cb))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    app.job_queue.run_repeating(daily_reminder, interval=60, first=10)

    async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        logger.error("Botda kutilmagan xatolik yuz berdi:", exc_info=context.error)

    app.add_error_handler(on_error)

    async def post_init(application):
        await application.bot.set_my_commands([
            BotCommand("start",    "🦉 Bosh menyu / Главное меню / Baş menýu"),
            BotCommand("lang",     "🌐 Til / Язык / Dil"),
            BotCommand("ai",       "🤖 AI Ustoz (Gemini)"),
            BotCommand("davom",    "▶️ Darsni davom ettirish"),
            BotCommand("darslar",  "📚 Darslar"),
            BotCommand("progress", "📊 Progressim"),
            BotCommand("lugat",    "📖 Lug'at & Qidiruv"),
            BotCommand("reyting",  "🏆 Peshqadamlar Reytingi"),
            BotCommand("guide",    "🇵🇱 Polsha Hayoti Qo'llanmasi"),
            BotCommand("premium",  "💎 Premium Obuna"),
            BotCommand("admin",    "👑 Admin Paneli"),
        ])
    app.post_init = post_init

    print("✅ Bot ishga tushdi! Ctrl+C — to'xtatish")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
