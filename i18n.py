# -*- coding: utf-8 -*-
"""
🦉 POLUZACADEMY — XALQARO TILLAR (i18n) MODULI
O'zbek, Rus va Turkman tillarida interfeys, xabarnomalar va klaviaturalar.
"""

import os
import sqlite3
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

DB_PATH = os.environ.get("DB_PATH", "polyakcha.db")

LANGUAGES = {
    "uz": "🇺🇿 O'zbek tili",
    "ru": "🇷🇺 Русский язык",
    "tm": "🇹🇲 Türkmen dili",
}

# ═══════════════════════════════════════════
# BAZA BILAN BOG'LANISH VA TILNI OLISH
# ═══════════════════════════════════════════

def _ensure_column():
    try:
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cols = [c[1] for c in cur.execute("PRAGMA table_info(users)").fetchall()]
        if cols and "lang" not in cols:
            cur.execute("ALTER TABLE users ADD COLUMN lang TEXT DEFAULT 'uz'")
            con.commit()
        con.close()
    except Exception:
        pass

_ensure_column()

def get_user_lang(user_id: int) -> str:
    """Foydalanuvchining tanlagan tilini qaytaradi ('uz', 'ru' yoki 'tm')."""
    try:
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        row = cur.execute("SELECT lang FROM users WHERE user_id=?", (user_id,)).fetchone()
        con.close()
        if row and row[0] in LANGUAGES:
            return row[0]
    except Exception:
        pass
    return "uz"

def set_user_lang(user_id: int, lang: str) -> bool:
    """Foydalanuvchi tilini bazaga saqlaydi (mavjud bo'lmasa yaratadi)."""
    if lang not in LANGUAGES:
        lang = "uz"
    try:
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute("UPDATE users SET lang=? WHERE user_id=?", (lang, user_id))
        if cur.rowcount == 0:
            cur.execute("INSERT OR IGNORE INTO users (user_id, lang) VALUES (?, ?)", (user_id, lang))
            cur.execute("UPDATE users SET lang=? WHERE user_id=?", (lang, user_id))
        con.commit()
        con.close()
        return True
    except Exception:
        return False

# ═══════════════════════════════════════════
# MATNLAR VA TARJIMALAR LUG'ATI
# ═══════════════════════════════════════════

STRINGS = {
    # ── Til tanlash ─────────────────────────
    "choose_language": {
        "uz": "🌐 *Iltimos, o'zingizga qulay tilni tanlang:*\n\n🇷🇺 *Пожалуйста, выберите язык обучения:*\n\n🇹🇲 *Haýyş edýäris, okuw dilini saýlaň:*",
        "ru": "🌐 *Пожалуйста, выберите удобный для вас язык:*",
        "tm": "🌐 *Haýyş edýäris, özüňize amatly dili saýlaň:*",
    },
    "lang_changed": {
        "uz": "✅ *O'zbek tili tanlandi!*",
        "ru": "✅ *Выбран русский язык!*",
        "tm": "✅ *Türkmen dili saýlandy!*",
    },

    # ── Bosh sahifa va salomlashuv ──────────
    "welcome_header": {
        "uz": (
            "🦉 *Assalomu alaykum, {name}! PolUzAcademy'ga xush kelibsiz!*\n\n"
            "Bu bot orqali siz **polyak tilini** 0 dan erkin muloqot darajasigacha "
            "qulay, tez va qiziqarli o'rganishingiz mumkin.\n\n"
            "🎮 *Imkoniyatlar:*\n"
            "• 📚 40+ bosqichma-bosqich darslar (A1-A2)\n"
            "• 🔊 Microsoft AI tabiiy audio talaffuzi\n"
            "• 🤖 Google Gemini AI repetitori (matnli va ovozli)\n"
            "• 🇵🇱 Polshadagi real hayotiy muloqotlar (Urząd, Ish, Do'kon)\n"
            "• 💎 Duolingo uslubidagi o'yin, streak va ballar tizimi\n\n"
            "{status_badge}\n\n"
            "Boshlash uchun quyidagi bo'limlardan birini tanlang:"
        ),
        "ru": (
            "🦉 *Здравствуйте, {name}! Добро пожаловать в PolUzAcademy!*\n\n"
            "С помощью этого бота вы сможете выучить **польский язык** с нуля до уровня свободного общения "
            "легко, быстро и интерактивно.\n\n"
            "🎮 *Возможности:*\n"
            "• 📚 40+ пошаговых уроков (A1-A2)\n"
            "• 🔊 Естественное произношение Microsoft AI\n"
            "• 🤖 ИИ-репетитор Google Gemini (текст и голос)\n"
            "• 🇵🇱 Реальные жизненные диалоги в Польше (Ужонд, Работа, Магазин)\n"
            "• 💎 Система рейтинга, ударного режима (streak) и очков в стиле Duolingo\n\n"
            "{status_badge}\n\n"
            "Для начала выберите нужный раздел ниже:"
        ),
        "tm": (
            "🦉 *Salam, {name}! PolUzAcademy botyna hoş geldiňiz!*\n\n"
            "Bu bot arkaly siz **polýak dilini** noldan erkin gürleşmek derejesine çenli "
            "aňsat, çalt we gyzykly öwrenip bilersiňiz.\n\n"
            "🎮 *Mümkinçilikler:*\n"
            "• 📚 40+ yzygiderli sapaklar (A1-A2)\n"
            "• 🔊 Microsoft AI tebigy sesli aýdylyşy\n"
            "• 🤖 Google Gemini AI halypasy (tekst we sesli)\n"
            "• 🇵🇱 Polşadaky durmuş gürrüňdeşlikleri (Urząd, Iş, Dükan)\n"
            "• 💎 Duolingo stilinde reýting, streak we ball ulgamy\n\n"
            "{status_badge}\n\n"
            "Başlamak üçin aşakdaky bölümlerden birini saýlaň:"
        ),
    },

    # ── Pastki klaviatura tugmalari ─────────
    "btn_ai": {
        "uz": "🤖 AI Ustoz",
        "ru": "🤖 AI Учитель",
        "tm": "🤖 AI Halypa",
    },
    "btn_continue": {
        "uz": "▶️ Davom ettirish",
        "ru": "▶️ Продолжить",
        "tm": "▶️ Dowam etmek",
    },
    "btn_lessons": {
        "uz": "📚 Darslar",
        "ru": "📚 Уроки",
        "tm": "📚 Sapaklar",
    },
    "btn_dict": {
        "uz": "📖 Lug'at & Qidiruv",
        "ru": "📖 Словарь & Поиск",
        "tm": "📖 Sözlük & Gözleg",
    },
    "btn_guide": {
        "uz": "🇵🇱 Polsha hayoti",
        "ru": "🇵🇱 Жизнь в Польше",
        "tm": "🇵🇱 Polşada durmuş",
    },
    "btn_rating": {
        "uz": "🏆 Reyting",
        "ru": "🏆 Рейтинг",
        "tm": "🏆 Reýting",
    },
    "btn_premium": {
        "uz": "💎 Premium",
        "ru": "💎 Премиум",
        "tm": "💎 Premium",
    },
    "btn_profile": {
        "uz": "👤 Profilim",
        "ru": "👤 Мой профиль",
        "tm": "👤 Profilim",
    },
    "btn_invite": {
        "uz": "👥 Do'stlarni taklif qilish",
        "ru": "👥 Пригласить друзей",
        "tm": "👥 Dostlary çagyrmak",
    },

    # ── Inline Menyu Tugmalari ──────────────
    "in_ai_gemini": {
        "uz": "🤖 AI Ustoz (Google Gemini)",
        "ru": "🤖 AI Учитель (Google Gemini)",
        "tm": "🤖 AI Halypa (Google Gemini)",
    },
    "in_continue": {
        "uz": "▶️ Qolgan joyidan davom ettirish",
        "ru": "▶️ Продолжить с места остановки",
        "tm": "▶️ Galan ýerinden dowam etmek",
    },
    "in_lessons": {
        "uz": "📚 Darslar",
        "ru": "📚 Уроки",
        "tm": "📚 Sapaklar",
    },
    "in_restart": {
        "uz": "🔄 Boshidan boshlash",
        "ru": "🔄 Начать заново",
        "tm": "🔄 Başyndan başlamak",
    },
    "in_dict": {
        "uz": "📖 Lug'at & Qidiruv",
        "ru": "📖 Словарь & Поиск",
        "tm": "📖 Sözlük & Gözleg",
    },
    "in_progress": {
        "uz": "📊 Progressim",
        "ru": "📊 Мой прогресс",
        "tm": "📊 Meniň ösüşim",
    },
    "in_rating": {
        "uz": "🏆 Peshqadamlar Reytingi",
        "ru": "🏆 Таблица лидеров",
        "tm": "🏆 Öňdebaryjylar reýtingi",
    },
    "in_guide": {
        "uz": "🇵🇱 Polsha hayoti",
        "ru": "🇵🇱 Жизнь в Польше",
        "tm": "🇵🇱 Polşada durmuş",
    },
    "in_invite": {
        "uz": "👥 Do'stlarni taklif qilish",
        "ru": "👥 Пригласить друзей",
        "tm": "👥 Dostlary çagyrmak",
    },
    "in_prem": {
        "uz": "💎 Premium Obuna",
        "ru": "💎 Премиум Подписка",
        "tm": "💎 Premium Ýazylma",
    },
    "in_prem_active": {
        "uz": "💎 Premium (Faol ✅)",
        "ru": "💎 Премиум (Активен ✅)",
        "tm": "💎 Premium (Işjeň ✅)",
    },
    "in_reminder": {
        "uz": "⏰ Eslatma",
        "ru": "⏰ Напоминания",
        "tm": "⏰ Ýatlatma",
    },
    "in_about": {
        "uz": "ℹ️ Kurs haqida",
        "ru": "ℹ️ О курсе",
        "tm": "ℹ️ Kurs barada",
    },
    "in_help": {
        "uz": "❓ Yordam",
        "ru": "❓ Помощь",
        "tm": "❓ Kömek",
    },
    "in_change_lang": {
        "uz": "🌐 Tilni o'zgartirish",
        "ru": "🌐 Сменить язык",
        "tm": "🌐 Dili üýtgetmek",
    },
    "in_main": {
        "uz": "🏠 Bosh menyu",
        "ru": "🏠 Главное меню",
        "tm": "🏠 Baş menýu",
    },
    "in_back": {
        "uz": "◀️ Orqaga",
        "ru": "◀️ Назад",
        "tm": "◀️ Yza",
    },

    # ── AI Menyu Matnlari ───────────────────
    "ai_title": {
        "uz": (
            "🤖 *PolUzAcademy — AI Ustoz (Google Gemini)*\n\n"
            "Sun'iy intellekt repetitori bilan polyak tilini 10 barobar tezroq va qulay o'rganing!\n\n"
            "📊 Sizning bugungi limitingiz: {quota_txt}\n\n"
            "Quyidagi imkoniyatlardan birini tanlang:\n"
            "• 💬 *Erkin suhbat:* Grammatika, yangi so'zlar yoki tarjima bo'yicha savol bering.\n"
            "• ✍️ *Grammatika tekshiruvi:* Polyakcha yozgan matnlaringizdagi xatolarni aniqlab, qoidasini tushuntiradi.\n"
            "• 🎭 *Rolli o'yinlar:* Urząd, Ish, Do'kon va Shifoxonadagi real polyakcha muloqot mashqi.\n"
            "• 🎙 *Ovozli muloqot:* Istalgan rejimda ovozli xabar (audio) yuborsangiz, AI uni tushunib javob beradi!"
        ),
        "ru": (
            "🤖 *PolUzAcademy — ИИ-Учитель (Google Gemini)*\n\n"
            "Изучайте польский язык в 10 раз быстрее с персональным ИИ-репетитором!\n\n"
            "📊 Ваш лимит на сегодня: {quota_txt}\n\n"
            "Выберите нужный режим:\n"
            "• 💬 *Свободный диалог:* Задавайте любые вопросы по грамматике, словам и переводу.\n"
            "• ✍️ *Проверка грамматики:* Отправьте польский текст — ИИ найдет ошибки и подробно объяснит правила.\n"
            "• 🎭 *Ролевые игры:* Реальные диалоги в Ужонде (ВНЖ/Karta Pobytu), на работе, в магазине и у врача.\n"
            "• 🎙 *Голосовое общение:* Отправляйте голосовые сообщения, ИИ понимает речь и отвечает голосом!"
        ),
        "tm": (
            "🤖 *PolUzAcademy — AI Halypa (Google Gemini)*\n\n"
            "Şahsy emeli aň halypasy bilen polýak dilini 10 esse çalt we aňsat öwreniň!\n\n"
            "📊 Şu günki çägiňiz: {quota_txt}\n\n"
            "Aşakdaky bölümlerden birini saýlaň:\n"
            "• 💬 *Erkin gürrüňdeşlik:* Grammatika, täze sözler ýa-da terjime boýunça sorag beriň.\n"
            "• ✍️ *Grammatika barlagy:* Ýazan polýakça sözlemleriňizdäki ýalňyşlyklary derňäp, düşündirer.\n"
            "• 🎭 *Rollu oýunlar:* Urząd, Iş, Dükan we Lukman ýaly ýerlerde hakyky gürrüňdeşlik.\n"
            "• 🎙 *Sesli aragatnaşyk:* Sesli habar iberiň, AI diňläp jogap berer!"
        ),
    },

    "ai_btn_chat": {
        "uz": "💬 Erkin suhbat (AI Ustoz)",
        "ru": "💬 Свободный диалог (ИИ)",
        "tm": "💬 Erkin gürrüňdeşlik (AI)",
    },
    "ai_btn_grammar": {
        "uz": "✍️ Grammatika & Matn tekshiruvi",
        "ru": "✍️ Проверка грамматики и текста",
        "tm": "✍️ Grammatika we tekst barlagy",
    },
    "ai_btn_roleplay": {
        "uz": "🎭 Situatsion rolli o'yinlar",
        "ru": "🎭 Ситуационные ролевые игры",
        "tm": "🎭 Ýagdaýly rollu oýunlar",
    },
    "ai_btn_clear": {
        "uz": "🔄 Suhbatni tozalash",
        "ru": "🔄 Очистить контекст",
        "tm": "🔄 Gürrüňdeşligi arassalamak",
    },
    "ai_btn_exit": {
        "uz": "🚪 AI rejimidan chiqish",
        "ru": "🚪 Выйти из режима ИИ",
        "tm": "🚪 AI tertibinden çykmak",
    },
    "ai_exited": {
        "uz": "🚪 *AI Ustoz rejimidan chiqildi.* Bosh menyudasiz.",
        "ru": "🚪 *Вы вышли из режима ИИ.* Вы в главном меню.",
        "tm": "🚪 *AI Halypa tertibinden çykyldy.* Baş menýudasyňyz.",
    },
    "ai_cleared": {
        "uz": "🔄 Suhbat tarixi tozalandi. Yangi savolingizni yuborishingiz mumkin.",
        "ru": "🔄 История диалога очищена. Можете задать новый вопрос.",
        "tm": "🔄 Gürrüňdeşlik taryhy arassalandy. Täze sorag berip bilersiňiz.",
    },
    "ai_quota_exceeded": {
        "uz": (
            "⚠️ *Kunlik bepul AI so'rovlaringiz (5 ta) tugadi!*\n\n"
            "💎 *Premium obuna* orqali siz sun'iy intellekt repetitoridan **mutlaqo cheksiz** foydalanishingiz mumkin.\n"
            "Yoki yangi so'rovlar uchun ertangi kunni kuting."
        ),
        "ru": (
            "⚠️ *Ваш дневной лимит бесплатных запросов (5) исчерпан!*\n\n"
            "💎 С подпиской *Premium* вы сможете общаться с ИИ-репетитором **без каких-либо ограничений**.\n"
            "Либо подождите до завтра для обновления лимита."
        ),
        "tm": (
            "⚠️ *Şu günki mugt AI soraglaryňyz (5 sany) gutardy!*\n\n"
            "💎 *Premium ýazylma* bilen emeli aň halypasyndan **çäksiz** peýdalanyp bilersiňiz.\n"
            "Ýa-da ertire çenli garaşyň."
        ),
    },

    # ── Bosh menyu sarlavhasi ────────────────
    "main_menu_card": {
        "uz": (
            "🦉 *PolUzAcademy — Bosh Menyu*\n\n"
            "👤 *{name}* ({status_txt})\n\n"
            "🔥 Streak: *{streak} kun*\n"
            "⭐ XP: *{xp}*\n"
            "❤️ Yuraklar: *{hearts}*\n\n"
            "📗 A1.1: *{a1_1}/10* dars\n"
            "📘 A1.2: *{a1_2}/10* dars\n"
            "📙 A2.1: *{a2_1}/10* dars\n"
            "📕 A2.2: *{a2_2}/10* dars\n\n"
            "Nima qilamiz?"
        ),
        "ru": (
            "🦉 *PolUzAcademy — Главное Меню*\n\n"
            "👤 *{name}* ({status_txt})\n\n"
            "🔥 Ударный режим (Streak): *{streak} дн.*\n"
            "⭐ Очки (XP): *{xp}*\n"
            "❤️ Жизни: *{hearts}*\n\n"
            "📗 A1.1: *{a1_1}/10* уроков\n"
            "📘 A1.2: *{a1_2}/10* уроков\n"
            "📙 A2.1: *{a2_1}/10* уроков\n"
            "📕 A2.2: *{a2_2}/10* уроков\n\n"
            "Что будем изучать?"
        ),
        "tm": (
            "🦉 *PolUzAcademy — Baş Menýu*\n\n"
            "👤 *{name}* ({status_txt})\n\n"
            "🔥 Streak: *{streak} gün*\n"
            "⭐ XP: *{xp}*\n"
            "❤️ Ýürekler: *{hearts}*\n\n"
            "📗 A1.1: *{a1_1}/10* sapak\n"
            "📘 A1.2: *{a1_2}/10* sapak\n"
            "📙 A2.1: *{a2_1}/10* sapak\n"
            "📕 A2.2: *{a2_2}/10* sapak\n\n"
            "Näme öwrenýäris?"
        ),
    }
}

def t(key: str, lang: str = "uz", **kwargs) -> str:
    """Berilgan til bo'yicha tarjima matnini formatlab qaytaradi."""
    item = STRINGS.get(key, {})
    txt = item.get(lang) or item.get("uz") or key
    if kwargs:
        try:
            return txt.format(**kwargs)
        except Exception:
            return txt
    return txt

# ═══════════════════════════════════════════
# KLAVIATURALAR GENERATORI
# ═══════════════════════════════════════════

def kb_lang_select(include_back: bool = False) -> InlineKeyboardMarkup:
    """3 ta tilni tanlash tugmalari."""
    rows = [
        [InlineKeyboardButton("🇺🇿 O'zbek tili", callback_data="set_lang:uz")],
        [InlineKeyboardButton("🇷🇺 Русский язык", callback_data="set_lang:ru")],
        [InlineKeyboardButton("🇹🇲 Türkmen dili", callback_data="set_lang:tm")],
    ]
    if include_back:
        rows.append([InlineKeyboardButton("◀️ Orqaga / Назад / Yza", callback_data="main")])
    return InlineKeyboardMarkup(rows)

def kb_reply_main(lang: str = "uz") -> ReplyKeyboardMarkup:
    """Ekranning pastki doimiy klaviaturasi (tilga mos)."""
    return ReplyKeyboardMarkup([
        [KeyboardButton(t("btn_ai", lang)), KeyboardButton(t("btn_continue", lang))],
        [KeyboardButton(t("btn_lessons", lang)), KeyboardButton(t("btn_dict", lang))],
        [KeyboardButton(t("btn_guide", lang)), KeyboardButton(t("btn_rating", lang))],
        [KeyboardButton(t("btn_premium", lang)), KeyboardButton(t("btn_profile", lang))],
        [KeyboardButton(t("btn_invite", lang))],
    ], resize_keyboard=True)

def kb_main(uid: int = None, is_premium: bool = False, lang: str = "uz") -> InlineKeyboardMarkup:
    """Asosiy interaktiv bosh menyu klaviaturasi."""
    prem_label = t("in_prem_active", lang) if is_premium else t("in_prem", lang)

    return InlineKeyboardMarkup([
        [InlineKeyboardButton(t("in_ai_gemini", lang), callback_data="ai_menu")],
        [InlineKeyboardButton(t("in_continue", lang), callback_data="continue_lesson")],
        [InlineKeyboardButton(t("in_lessons", lang), callback_data="lessons"),
         InlineKeyboardButton(t("in_restart", lang), callback_data="restart_lessons")],
        [InlineKeyboardButton(t("in_dict", lang), callback_data="vocab_menu"),
         InlineKeyboardButton(t("in_progress", lang), callback_data="progress")],
        [InlineKeyboardButton(t("in_rating", lang), callback_data="leaderboard"),
         InlineKeyboardButton(t("in_guide", lang), callback_data="poland_guide")],
        [InlineKeyboardButton(t("in_invite", lang), callback_data="referral_info"),
         InlineKeyboardButton(prem_label, callback_data="premium_menu")],
        [InlineKeyboardButton(t("in_change_lang", lang), callback_data="change_lang"),
         InlineKeyboardButton(t("in_reminder", lang), callback_data="reminder_menu")],
        [InlineKeyboardButton(t("in_about", lang), callback_data="about"),
         InlineKeyboardButton(t("in_help", lang), callback_data="help")],
    ])

def kb_ai_menu(uid: int = None, is_premium: bool = False, remaining: int = 5, lang: str = "uz") -> InlineKeyboardMarkup:
    """AI Ustoz menyusi klaviaturasi."""
    if is_premium:
        quota_btn_txt = "💎 Cheksiz (Premium)" if lang == "uz" else ("💎 Безлимитно (Премиум)" if lang == "ru" else "💎 Çäksiz (Premium)")
    else:
        quota_btn_txt = f"⚡️ {remaining}/5 ta qoldi" if lang == "uz" else (f"⚡️ Осталось: {remaining}/5" if lang == "ru" else f"⚡️ {remaining}/5 galdy")

    buttons = [
        [InlineKeyboardButton(t("ai_btn_chat", lang), callback_data="ai_mode:chat")],
        [InlineKeyboardButton(t("ai_btn_grammar", lang), callback_data="ai_mode:grammar")],
        [InlineKeyboardButton(t("ai_btn_roleplay", lang), callback_data="ai_roleplay_menu")],
        [InlineKeyboardButton(quota_btn_txt, callback_data="premium_menu" if not is_premium else "ai_menu")],
    ]
    if not is_premium:
        prem_btn_txt = "💎 Premium olish" if lang == "uz" else ("💎 Купить Премиум" if lang == "ru" else "💎 Premium satyn almak")
        buttons.append([InlineKeyboardButton(prem_btn_txt, callback_data="premium_menu")])
    buttons.append([InlineKeyboardButton(t("in_main", lang), callback_data="main")])
    return InlineKeyboardMarkup(buttons)

def kb_ai_roleplay_menu(lang: str = "uz") -> InlineKeyboardMarkup:
    """Rolli o'yinlar tanlash klaviaturasi."""
    if lang == "ru":
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("🏛 Ужонд (Подача на Карту Побыту)", callback_data="ai_roleplay:roleplay_urzad")],
            [InlineKeyboardButton("💼 На работе (С бригадиром / шефом)", callback_data="ai_roleplay:roleplay_praca")],
            [InlineKeyboardButton("🛒 В магазине (Кассир в Бедронке)", callback_data="ai_roleplay:roleplay_sklep")],
            [InlineKeyboardButton("🏥 В поликлинике (С врачом NFZ)", callback_data="ai_roleplay:roleplay_lekarz")],
            [InlineKeyboardButton("🔙 Назад в меню ИИ", callback_data="ai_menu")],
        ])
    elif lang == "tm":
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("🏛 Urząd (Karta Pobytu tabşyrmak)", callback_data="ai_roleplay:roleplay_urzad")],
            [InlineKeyboardButton("💼 Iş ýerinde (Başlyk / Kierownik bilen)", callback_data="ai_roleplay:roleplay_praca")],
            [InlineKeyboardButton("🛒 Dükanda (Biedronka kassiri)", callback_data="ai_roleplay:roleplay_sklep")],
            [InlineKeyboardButton("🏥 Lukmanhanada (NFZ lukmany)", callback_data="ai_roleplay:roleplay_lekarz")],
            [InlineKeyboardButton("🔙 AI menýusyna dolanmak", callback_data="ai_menu")],
        ])
    else:
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("🏛 Urząd (Karta Pobytu topshirish)", callback_data="ai_roleplay:roleplay_urzad")],
            [InlineKeyboardButton("💼 Ish joyida (Kierownik bilan)", callback_data="ai_roleplay:roleplay_praca")],
            [InlineKeyboardButton("🛒 Do'konda (Biedronka kassiri)", callback_data="ai_roleplay:roleplay_sklep")],
            [InlineKeyboardButton("🏥 Shifoxona (NFZ shifokori)", callback_data="ai_roleplay:roleplay_lekarz")],
            [InlineKeyboardButton("🔙 AI menyuga qaytish", callback_data="ai_menu")],
        ])

def kb_ai_active(mode: str = "chat", lang: str = "uz") -> InlineKeyboardMarkup:
    """Aktiv suhbat jarayonidagi boshqaruv tugmalari."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(t("ai_btn_clear", lang), callback_data="ai_clear_history"),
         InlineKeyboardButton(t("ai_btn_exit", lang), callback_data="ai_exit")]
    ])
