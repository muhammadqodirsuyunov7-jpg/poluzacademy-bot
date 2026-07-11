#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
 POLYAKCHA BOT
Telegram orqali polyak tilini o'rganish — Duolingo uslubida
Muallif: Sizning Platformangiz
"""
import logging
import sqlite3
from datetime import datetime, date, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    ContextTypes, MessageHandler, filters
)
# ═══════════════════════════════════════════
#  SOZLAMALAR
# ═══════════════════════════════════════════
BOT_TOKEN = "8749989883:AAGX0RiQ32ExbIayYbevhxxBkDIxL-QEN0k"
DB_PATH   = "polyakcha.db"
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)
# ═══════════════════════════════════════════
#  DARSLAR MA'LUMOTLARI
# ═══════════════════════════════════════════
CURRICULUM = {
    "a1_1": {
        "title": "A1.1 — Boshlang'ich Muloqot",
        "emoji": " ",
        "lessons": {
            "l1": {
                "title": "Salomlashish",
                "emoji": " ",
                "vocab": [
                    {"pl": "Dzień dobry",     "ph": "djen DOB-ri",       "uz": "Xayrli kun (rasmiy)"},
                    {"pl": "Dobry wieczór",   "ph": "DOB-ri vye-CHUR",   "uz": "Xayrli kech"},
                    {"pl": "Dobranoc",        "ph": "dob-RA-nots",       "uz": "Xayrli tun"},
                    {"pl": "Cześć",           "ph": "cheshch",           "uz": "Salom (do'stona)"},
                    {"pl": "Do widzenia",     "ph": "do vi-DZE-nya",     "uz": "Xayr (rasmiy)"},
                    {"pl": "Na razie",        "ph": "na RA-zye",         "uz": "Hozircha xayr"},
                    {"pl": "Dziękuję",        "ph": "djen-KU-ye",        "uz": "Rahmat"},
                    {"pl": "Bardzo dziękuję", "ph": "BAR-dzo djen-KU-ye","uz": "Katta rahmat"},
                    {"pl": "Proszę",          "ph": "PRO-she",           "uz": "Marhamat / Iltimos"},
                    {"pl": "Przepraszam",     "ph": "pshe-PRA-sham",     "uz": "Kechirasiz"},
                    {"pl": "Tak",             "ph": "tak",               "uz": "Ha"},
                    {"pl": "Nie",             "ph": "nye",               "uz": "Yo'q"},
                    {"pl": "Dobrze",          "ph": "DOB-zhe",           "uz": "Yaxshi / Mayli"},
                    {"pl": "Miło mi",         "ph": "MI-vo mi",          "uz": "Tanishganimdan xursandman"},
                    {"pl": "Pan / Pani",      "ph": "pan / PA-ni",       "uz": "Janob / Xonim"},
                ],
                "exercises": [
                    {"q": " *'Dzień dobry'* nima degani?",
                     "opts": ["Xayrli tun","Xayrli kun","Salom","Xayr"],          "ans": 1},
                    {"q": "*'Rahmat'* polyakchada qanday?",
                     "opts": ["Proszę","Przepraszam","Dziękuję","Tak"],             "ans": 2},
                    {"q": "*'Do widzenia'* nima degani?",
                     "opts": ["Salom","Rahmat","Xayr (rasmiy)","Kechirasiz"],      "ans": 2},
                    {"q": "*'Kechirasiz'* polyakchada?",
                     "opts": ["Proszę","Przepraszam","Dziękuję","Dobranoc"],        "ans": 1},
                    {"q": "*'Na razie'* nima degani?",
                     "opts": ["Xayrli kun","Hozircha xayr","Rahmat","Ha"],         "ans": 1},
                    {"q": "*'Tak'* nima degani?",
                     "opts": ["Yo'q","Ha","Kechirasiz","Rahmat"],                   "ans": 1},
                    {"q": "*'Dobranoc'* nima degani?",
                     "opts": ["Xayrli kun","Xayrli kech","Xayrli tun","Salom"],    "ans": 2},
                    {"q": "*'Proszę'* nima degani?",
                     "opts": ["Rahmat","Kechirasiz","Marhamat","Ha"],               "ans": 2},
                    {"q": "*'Yaxshi / Mayli'* polyakchada?",
                     "opts": ["Tak","Nie","Dobrze","Proszę"],                       "ans": 2},
                    {"q": "*'Dobry wieczór'* nima degani?",
                     "opts": ["Xayrli tun","Xayrli kech","Xayrli kun","Salom"],    "ans": 1},
                ],
            },
            "l2": {
                "title": "Sonlar 1–20",
                "emoji": " ",
                "vocab": [
                    {"pl": "Jeden",        "ph": "YE-den",        "uz": "Bir (1)"},
                    {"pl": "Dwa",          "ph": "dva",            "uz": "Ikki (2)"},
                    {"pl": "Trzy",         "ph": "tshi",           "uz": "Uch (3)"},
                    {"pl": "Cztery",       "ph": "CHTE-ri",        "uz": "To'rt (4)"},
                    {"pl": "Pięć",         "ph": "pyench",         "uz": "Besh (5)"},
                    {"pl": "Sześć",        "ph": "sheshch",        "uz": "Olti (6)"},
                    {"pl": "Siedem",       "ph": "SHYE-dem",       "uz": "Yetti (7)"},
                    {"pl": "Osiem",        "ph": "O-shem",         "uz": "Sakkiz (8)"},
                    {"pl": "Dziewięć",     "ph": "DJE-vyench",     "uz": "To'qqiz (9)"},
                    {"pl": "Dziesięć",     "ph": "DJE-shench",     "uz": "O'n (10)"},
                    {"pl": "Jedenaście",   "ph": "ye-de-NASH-che", "uz": "O'n bir (11)"},
                    {"pl": "Dwanaście",    "ph": "dva-NASH-che",   "uz": "O'n ikki (12)"},
                    {"pl": "Dwadzieścia",  "ph": "dva-DJESH-cha",  "uz": "Yigirma (20)"},
                    {"pl": "Sto",          "ph": "sto",            "uz": "Yuz (100)"},
                    {"pl": "Tysiąc",       "ph": "TY-shonts",      "uz": "Ming (1000)"},
                ],
                "exercises": [
                    {"q": " *'Pięć'* necha?",
                     "opts": ["To'rt","Besh","Olti","Yetti"],     "ans": 1},
                    {"q": "*7* soni polyakchada?",
                     "opts": ["Sześć","Siedem","Osiem","Dziewięć"],"ans": 1},
                    {"q": "*'Dziesięć'* necha?",
                     "opts": ["8","9","10","11"],                  "ans": 2},
                    {"q": "*'Trzy'* necha?",
                     "opts": ["Bir","Ikki","Uch","To'rt"],         "ans": 2},
                    {"q": "*4* soni polyakchada?",
                     "opts": ["Trzy","Cztery","Pięć","Sześć"],     "ans": 1},
                    {"q": "*'Osiem'* necha?",
                     "opts": ["6","7","8","9"],                    "ans": 2},
                    {"q": "*1* soni polyakchada?",
                     "opts": ["Jeden","Dwa","Trzy","Cztery"],      "ans": 0},
                    {"q": "*'Dwadzieścia'* necha?",
                     "opts": ["12","15","20","21"],                "ans": 2},
                    {"q": "*'Sto'* necha?",
                     "opts": ["10","100","1000","20"],             "ans": 1},
                    {"q": "*100* soni polyakchada?",
                     "opts": ["Tysiąc","Sto","Dziesięć","Zero"],   "ans": 1},
                ],
            },
            "l3": {
                "title": "Tanishuv",
                "emoji": " ",
                "vocab": [
                    {"pl": "Jak masz na imię?",   "ph": "yak mash na I-mye",      "uz": "Ismingiz nima?"},
                    {"pl": "Mam na imię...",       "ph": "mam na I-mye",           "uz": "Mening ismim..."},
                    {"pl": "Jak masz na nazwisko?","ph": "yak mash na na-ZVIS-ko", "uz": "Familiyangiz?"},
                    {"pl": "Ile masz lat?",        "ph": "ILE mash lat",           "uz": "Yoshingiz necha?"},
                    {"pl": "Mam ... lat",          "ph": "mam ... lat",            "uz": "Men ... yoshdaman"},
                    {"pl": "Skąd jesteś?",         "ph": "skond YES-tesh",         "uz": "Qayerdansiz?"},
                    {"pl": "Jestem z...",           "ph": "YES-tem z",              "uz": "Men ...danman"},
                    {"pl": "Gdzie mieszkasz?",     "ph": "gDJE MYESH-kash",        "uz": "Qayerda yashaysiz?"},
                    {"pl": "Miło mi!",             "ph": "MI-vo mi",               "uz": "Tanishganimdan xursandman!"},
                    {"pl": "Uczę się polskiego",   "ph": "U-che she pol-SKI-go",   "uz": "Polyakcha o'rganayapman"},
                    {"pl": "Rozumiem",             "ph": "ro-ZU-myem",             "uz": "Tushundim"},
                    {"pl": "Nie rozumiem",         "ph": "nye ro-ZU-myem",         "uz": "Tushunmadim"},
                    {"pl": "Staram się",           "ph": "STA-ram she",            "uz": "Harakat qilaman"},
                    {"pl": "Mówię po polsku",      "ph": "MU-vye po POL-sku",      "uz": "Polyakcha bilaman"},
                    {"pl": "Trochę",               "ph": "TRO-he",                 "uz": "Biroz"},
                ],
                "exercises": [
                    {"q": " *'Jak masz na imię?'* nima so'ramoqda?",
                     "opts": ["Yoshingiz?","Ismingiz?","Qayerdansiz?","Kasbingiz?"],    "ans": 1},
                    {"q": "*'Ile masz lat?'* nima so'ramoqda?",
                     "opts": ["Ismingiz?","Qayerdansiz?","Yoshingiz?","Telefon?"],      "ans": 2},
                    {"q": "*'Skąd jesteś?'* nima degani?",
                     "opts": ["Qayerda yashaysiz?","Qayerdansiz?","Qayerga?","Qachon?"],"ans": 1},
                    {"q": "*'Tushundim'* polyakchada?",
                     "opts": ["Nie rozumiem","Rozumiem","Uczę się","Miło mi"],           "ans": 1},
                    {"q": "*'Miło mi!'* nima degani?",
                     "opts": ["Rahmat!","Ko'rishguncha!","Tanishganimdan xursandman!","Salom!"],"ans": 2},
                    {"q": "*'Polyakcha o'rganayapman'* polyakchada?",
                     "opts": ["Mówię po polsku","Uczę się polskiego","Rozumiem","Nie mówię"],"ans": 1},
                    {"q": "*'Gdzie mieszkasz?'* nima so'ramoqda?",
                     "opts": ["Qayerdansiz?","Yoshingiz?","Qayerda yashaysiz?","Ismingiz?"],"ans": 2},
                    {"q": "*'Harakat qilaman'* polyakchada?",
                     "opts": ["Rozumiem","Staram się","Trochę","Miło mi"],               "ans": 1},
                    {"q": "*'Mam na imię...'* nima degani?",
                     "opts": ["Mening yoshim...","Mening ismim...","Mening kasibm...","Mening uyim..."],"ans": 1},
                    {"q": "*'Biroz'* polyakchada?",
                     "opts": ["Bardzo","Trochę","Dobrze","Tak"],                          "ans": 1},
                ],
            },
            "l4": {
                "title": "Oila",
                "emoji": " ",
                "vocab": [
                    {"pl": "Rodzina",    "ph": "ro-DZI-na",   "uz": "Oila"},
                    {"pl": "Mama",       "ph": "MA-ma",        "uz": "Ona"},
                    {"pl": "Tata",       "ph": "TA-ta",        "uz": "Ota"},
                    {"pl": "Brat",       "ph": "brat",         "uz": "Aka / Uka"},
                    {"pl": "Siostra",    "ph": "SHOSH-tra",    "uz": "Opa / Singil"},
                    {"pl": "Mąż",        "ph": "monsh",        "uz": "Er"},
                    {"pl": "Żona",       "ph": "ZHO-na",       "uz": "Xotin"},
                    {"pl": "Syn",        "ph": "syn",          "uz": "O'g'il"},
                    {"pl": "Córka",      "ph": "TSUR-ka",      "uz": "Qiz (farzand)"},
                    {"pl": "Dzieci",     "ph": "DJE-chi",      "uz": "Bolalar"},
                    {"pl": "Dziadek",    "ph": "DJYA-dek",     "uz": "Buva"},
                    {"pl": "Babcia",     "ph": "BAB-cha",      "uz": "Buvi"},
                    {"pl": "Wujek",      "ph": "VU-yek",       "uz": "Amaki / Tog'a"},
                    {"pl": "Ciocia",     "ph": "CHO-cha",      "uz": "Xola / Amma"},
                    {"pl": "Mam brata",  "ph": "mam BRA-ta",   "uz": "Akam/ukam bor"},
                ],
                "exercises": [
                    {"q": " *'Żona'* nima degani?",
                     "opts": ["Ona","Qiz","Xotin","Singil"],          "ans": 2},
                    {"q": " *'Brat'* nima degani?",
                     "opts": ["Ota","Aka/Uka","O'g'il","Er"],          "ans": 1},
                    {"q": " *'Córka'* nima degani?",
                     "opts": ["Ona","Qiz (farzand)","Singil","Buvi"],  "ans": 1},
                    {"q": "*'Oila'* polyakchada?",
                     "opts": ["Rodzice","Rodzeństwo","Rodzina","Dom"],  "ans": 2},
                    {"q": " *'Syn'* nima degani?",
                     "opts": ["Qiz","O'g'il","Aka","Ota"],             "ans": 1},
                    {"q": "*'Bolalar'* polyakchada?",
                     "opts": ["Dzieci","Córka","Syn","Rodzina"],        "ans": 0},
                    {"q": " *'Babcia'* nima degani?",
                     "opts": ["Buva","Xola","Buvi","Amma"],             "ans": 2},
                    {"q": " *'Dziadek'* nima degani?",
                     "opts": ["Amaki","Buva","Ota","Buvi"],             "ans": 1},
                    {"q": "*'Xotin'* polyakchada?",
                     "opts": ["Mąż","Żona","Mama","Siostra"],          "ans": 1},
                    {"q": " *'Ciocia'* nima degani?",
                     "opts": ["Buvi","Singil","Xola/Amma","Ona"],       "ans": 2},
                ],
            },
            "l5": {
                "title": "Kasblar",
                "emoji": " ",
                "vocab": [
                    {"pl": "Pracownik",    "ph": "pra-TSOV-nik",    "uz": "Ishchi"},
                    {"pl": "Kierowca",     "ph": "kye-ROV-tsa",     "uz": "Haydovchi"},
                    {"pl": "Lekarz",       "ph": "LE-kazh",         "uz": "Shifokor"},
                    {"pl": "Pielęgniarka", "ph": "pye-leng-NYAR-ka","uz": "Hamshira"},
                    {"pl": "Nauczyciel",   "ph": "na-u-CHI-chel",   "uz": "O'qituvchi"},
                    {"pl": "Kucharz",      "ph": "KU-hazh",         "uz": "Oshpaz"},
                    {"pl": "Spawacz",      "ph": "SPA-vach",        "uz": "Payvandchi"},
                    {"pl": "Mechanik",     "ph": "me-HA-nik",       "uz": "Mexanik"},
                    {"pl": "Elektryk",     "ph": "e-LEK-trik",      "uz": "Elektrik"},
                    {"pl": "Budowlaniec",  "ph": "bu-dov-LA-nyets", "uz": "Qurilishchi"},
                    {"pl": "Sprzedawca",   "ph": "pshe-DAV-tsa",    "uz": "Sotuvchi"},
                    {"pl": "Hydraulik",    "ph": "hid-RAV-lik",     "uz": "Santexnik"},
                    {"pl": "Student",      "ph": "STU-dent",        "uz": "Talaba"},
                    {"pl": "Inżynier",     "ph": "in-ZHY-ner",      "uz": "Muhandis"},
                    {"pl": "Ochroniarz",   "ph": "oh-RO-nyazh",     "uz": "Qo'riqchi"},
                ],
                "exercises": [
                    {"q": "*'Lekarz'* nima kasb?",
                     "opts": ["Oshpaz","Shifokor","O'qituvchi","Mexanik"],      "ans": 1},
                    {"q": " *'Spawacz'* nima kasb?",
                     "opts": ["Elektrik","Santexnik","Payvandchi","Haydovchi"], "ans": 2},
                    {"q": "*'Haydovchi'* polyakchada?",
                     "opts": ["Pracownik","Kierowca","Mechanik","Elektryk"],    "ans": 1},
                    {"q": "*'Nauczyciel'* nima kasb?",
                     "opts": ["Shifokor","Oshpaz","O'qituvchi","Sotuvchi"],     "ans": 2},
                    {"q": "*'Mexanik'* polyakchada?",
                     "opts": ["Elektryk","Mechanik","Spawacz","Hydraulik"],     "ans": 1},
                    {"q": "*'Kucharz'* nima kasb?",
                     "opts": ["Qurilishchi","Haydovchi","Oshpaz","Ishchi"],     "ans": 2},
                    {"q": "*'Elektryk'* nima kasb?",
                     "opts": ["Santexnik","Mexanik","Elektrik","Payvandchi"],   "ans": 2},
                    {"q": "*'Talaba'* polyakchada?",
                     "opts": ["Pracownik","Inżynier","Student","Nauczyciel"],   "ans": 2},
                    {"q": "*'Hydraulik'* nima kasb?",
                     "opts": ["Elektrik","Santexnik","Qurilishchi","Oshpaz"],   "ans": 1},
                    {"q": "*'Qo'riqchi'* polyakchada?",
                     "opts": ["Kasjer","Ochroniarz","Budowlaniec","Sprzedawca"],"ans": 1},
                ],
            },
            "l6": {
                "title": "Ishda Muloqot",
                "emoji": " ",
                "vocab": [
                    {"pl": "Praca",               "ph": "PRA-tsa",              "uz": "Ish"},
                    {"pl": "Szef",                "ph": "shef",                 "uz": "Boshliq"},
                    {"pl": "Zmiana",              "ph": "ZMYA-na",              "uz": "Smena"},
                    {"pl": "Przerwa",             "ph": "PZHER-va",             "uz": "Tanaffus"},
                    {"pl": "Wynagrodzenie",       "ph": "vy-na-gro-DZE-nye",   "uz": "Ish haqi"},
                    {"pl": "Umowa o pracę",       "ph": "u-MO-va o PRA-tse",   "uz": "Ish shartnomasi"},
                    {"pl": "Fabryka",             "ph": "FAB-ry-ka",            "uz": "Fabrika"},
                    {"pl": "Magazyn",             "ph": "ma-GA-zyn",            "uz": "Ombor"},
                    {"pl": "Urlop",               "ph": "UR-lop",               "uz": "Ta'til"},
                    {"pl": "Nadgodziny",          "ph": "nad-go-DZI-ni",        "uz": "Qo'shimcha soatlar"},
                    {"pl": "Pracuję w fabryce",   "ph": "pra-TSU-ye v FAB-ri-tse","uz": "Fabrikada ishlayman"},
                    {"pl": "Kiedy jest przerwa?", "ph": "KYE-di yest PZHER-va","uz": "Tanaffus qachon?"},
                    {"pl": "Ile zarabiam?",       "ph": "ILE za-RAB-yam",       "uz": "Qancha topaman?"},
                    {"pl": "Mam pytanie",         "ph": "mam py-TA-nye",        "uz": "Savolim bor"},
                    {"pl": "Nie rozumiem",        "ph": "nye ro-ZU-myem",       "uz": "Tushunmayapman"},
                ],
                "exercises": [
                    {"q": "*'Zmiana'* nima degani?",
                     "opts": ["Ta'til","Smena","Tanaffus","Ish haqi"],          "ans": 1},
                    {"q": "*'Szef'* nima degani?",
                     "opts": ["Ishchi","Hamkasb","Boshliq","Kasb"],             "ans": 2},
                    {"q": "*'Tanaffus'* polyakchada?",
                     "opts": ["Urlop","Zmiana","Przerwa","Praca"],              "ans": 2},
                    {"q": " *'Wynagrodzenie'* nima degani?",
                     "opts": ["Shartnoma","Ish haqi","Smena","Ta'til"],         "ans": 1},
                    {"q": "*'Ta'til'* polyakchada?",
                     "opts": ["Przerwa","Zmiana","Urlop","Praca"],              "ans": 2},
                    {"q": "*'Umowa o pracę'* nima degani?",
                     "opts": ["Ish","Fabrika","Ish shartnomasi","Ombor"],       "ans": 2},
                    {"q": "*'Nadgodziny'* nima degani?",
                     "opts": ["Qo'shimcha soatlar","Ta'til","Maosh","Ish joyи"],"ans": 0},
                    {"q": "*'Savolim bor'* polyakchada?",
                     "opts": ["Mam urlop","Mam pytanie","Mam pracę","Mam umowę"],"ans": 1},
                    {"q": "*'Magazyn'* nima degani?",
                     "opts": ["Fabrika","Ofis","Ombor","Do'kon"],               "ans": 2},
                    {"q": "*'Fabrikada ishlayman'* polyakchada?",
                     "opts": ["Pracuję w biurze","Pracuję w fabryce","Pracuję w sklepie","Pracuj"],"ans": 1},
                ],
            },
        },
    },
}
LESSON_ORDER = [
    ("a1_1","l1"),("a1_1","l2"),("a1_1","l3"),
    ("a1_1","l4"),("a1_1","l5"),("a1_1","l6"),
]
# ═══════════════════════════════════════════
#  MA'LUMOTLAR BAZASI
# ═══════════════════════════════════════════
def init_db():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            user_id     INTEGER PRIMARY KEY,
            name        TEXT,
            xp          INTEGER DEFAULT 0,
            hearts      INTEGER DEFAULT 5,
            streak      INTEGER DEFAULT 0,
            last_date   TEXT,
            reminder    TEXT
        );
        CREATE TABLE IF NOT EXISTS progress (
            user_id   INTEGER,
            lesson_id TEXT,
            done      INTEGER DEFAULT 0,
            score     INTEGER DEFAULT 0,
            PRIMARY KEY (user_id, lesson_id)
        );
        CREATE TABLE IF NOT EXISTS sessions (
            user_id    INTEGER PRIMARY KEY,
            lesson_id  TEXT,
            ex_idx     INTEGER DEFAULT 0,
            lives      INTEGER DEFAULT 3,
            correct    INTEGER DEFAULT 0,
            wrong      INTEGER DEFAULT 0,
            xp_earned  INTEGER DEFAULT 0
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
    if fetch == "one":  result = cur.fetchone()
    elif fetch == "all": result = cur.fetchall()
    con.commit()
    con.close()
    return result
def get_user(uid):
    row = db("SELECT * FROM users WHERE user_id=?", (uid,), "one")
    return dict(row) if row else None
def ensure_user(uid, name):
    db("INSERT OR IGNORE INTO users (user_id, name) VALUES (?,?)", (uid, name))
def upd_user(uid, **kw):
    sets = ", ".join(f"{k}=?" for k in kw)
    db(f"UPDATE users SET {sets} WHERE user_id=?", (*kw.values(), uid))
def completed_lessons(uid):
    rows = db("SELECT lesson_id FROM progress WHERE user_id=? AND done=1", (uid,), "all")
    return [r["lesson_id"] for r in rows] if rows else []
def mark_done(uid, lid, score):
    db("""INSERT INTO progress(user_id,lesson_id,done,score) VALUES(?,?,1,?)
          ON CONFLICT(user_id,lesson_id) DO UPDATE SET done=1, score=MAX(score,?)""",
       (uid, lid, score, score))
def get_session(uid):
    row = db("SELECT * FROM sessions WHERE user_id=?", (uid,), "one")
    return dict(row) if row else None
def new_session(uid, lid):
    db("""INSERT INTO sessions(user_id,lesson_id,ex_idx,lives,correct,wrong,xp_earned)
          VALUES(?,?,0,3,0,0,0)
          ON CONFLICT(user_id) DO UPDATE SET
          lesson_id=?, ex_idx=0, lives=3, correct=0, wrong=0, xp_earned=0""",
       (uid, lid, lid))
def upd_session(uid, **kw):
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
#  KLAVIATURALAR
# ═══════════════════════════════════════════
def kb_main():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(" Darslar",    callback_data="lessons"),
         InlineKeyboardButton(" Lug'at",     callback_data="vocab_menu")],
        [InlineKeyboardButton(" Progressim", callback_data="progress"),
         InlineKeyboardButton(" Eslatma",    callback_data="reminder_menu")],
        [InlineKeyboardButton(" Yordam",      callback_data="help")],
    ])
def kb_lessons(done_list):
    rows = []
    for mid, lid in LESSON_ORDER:
        les = CURRICULUM[mid]["lessons"][lid]
        key = f"{mid}:{lid}"
        icon = " " if key in done_list else ""
        rows.append([InlineKeyboardButton(
            f"{icon}{les['emoji']} {les['title']}",
            callback_data=f"lesson:{mid}:{lid}"
        )])
    rows.append([InlineKeyboardButton(" Bosh menyu", callback_data="main")])
    return InlineKeyboardMarkup(rows)
def kb_lesson_detail(mid, lid, done_list):
    key = f"{mid}:{lid}"
    rows = [
        [InlineKeyboardButton(" Lug'at ko'rish", callback_data=f"vocab:{mid}:{lid}"),
         InlineKeyboardButton(" Boshlash",        callback_data=f"go:{mid}:{lid}")],
    ]
    if key in done_list:
        rows.append([InlineKeyboardButton(" Qayta ishlash", callback_data=f"go:{mid}:{lid}")])
    rows.append([InlineKeyboardButton(" Darslar", callback_data="lessons")])
    return InlineKeyboardMarkup(rows)
def kb_exercise(opts, ex_idx):
    letters = ["A","B","C","D"]
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(f"{letters[i]}  {opt}",
                              callback_data=f"ans:{ex_idx}:{i}")]
        for i, opt in enumerate(opts)
    ])
def kb_after_lesson(mid, lid):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(" Keyingi dars", callback_data="lessons")],
        [InlineKeyboardButton(" Qayta",         callback_data=f"go:{mid}:{lid}")],
        [InlineKeyboardButton(" Bosh menyu",    callback_data="main")],
    ])
# ═══════════════════════════════════════════
#  YORDAMCHI FUNKSIYALAR
# ═══════════════════════════════════════════
def hearts_bar(lives):
    return " " * lives + " " * (3 - lives)
def progress_bar(done, total):
    pct = int(done / total * 100) if total else 0
    filled = pct // 10
    bar = "▓" * filled + "░" * (10 - filled)
    return f"`[{bar}]` {pct}%"
def lesson_data(mid, lid):
    return CURRICULUM[mid]["lessons"][lid]
# ═══════════════════════════════════════════
#  HANDLER — /start
# ═══════════════════════════════════════════
async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    ensure_user(u.id, u.first_name)
    text = (
        f" *Salom, {u.first_name}! Polyakcha Botiga xush kelibsiz!*\n\n"
        "Bu bot orqali siz *polyak tilini* — xuddi Duolingo kabi —\n"
        "o'yin, darslar va testlar orqali o'rganasiz!\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "*Kurs haqida:*\n"
        "• *A1.1* — Boshlang'ich muloqot *(6 dars — mavjud)*\n"
        "• *A1.2* — Kundalik hayot *(tez kunda)*\n"
        "• *A2.1* — Mustaqil muloqot *(tez kunda)*\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "*Kursni tugatgach siz:*\n"
        "*O'zingizni polyakcha tanishtira olasiz\n"
        "*Do'konda, idorada, ishda gaplasha olasiz\n"
        "*Sana, yosh, narx ayta olasiz\n"
        "*Oila va kasb haqida gapirasiz\n"
   
 
 
 "*A1-A2* darajasida muloqot qila olasiz\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "*O'yin tizimi:*\n"
        "*XP* — har to'g'ri javob uchun 10 ball\n"
        "*Yurak* — har darsda 3 ta, xato = 1 kamayadi\n"
        "*Streak* — ketma-ket o'rganish kunlari\n"
        "*Eslatma* — har kuni sizni o'rganishga chaqiradi\n\n"
        "*Quyidagi tugmani bosing va boshlang!*"
 
 
 
 
 
    )
    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=kb_main())
# ═══════════════════════════════════════════
#  HANDLER — CALLBACK QUERY
# ═══════════════════════════════════════════
async def on_callback(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q   = update.callback_query
    uid = q.from_user.id
    d   = q.data
    await q.answer()
    # - Bosh menyu -

    if d == "main":
        u = get_user(uid) or {}
        text = (
            f"*Polyakcha Bot*\n\n"
 
            f"Streak: *{u.get('streak',0)} kun*   "
            f"XP: *{u.get('xp',0)}*   "
            f"*{u.get('hearts',5)}/5*\n\n"
 
 
 
            "Nima qilamiz?"
        )
    # - Darslar royxati -
        await q.edit_message_text(text, parse_mode="Markdown", reply_markup=kb_main())

    elif d == "lessons":
        done = completed_lessons(uid)
        await q.edit_message_text(
            " *Darslar — A1.1 Boshlang'ich Muloqot*\n\n"
            "- tugatilgan  |   - boshlash",
 
            parse_mode="Markdown",
            reply_markup=kb_lessons(done)
        )
    # - Dars detali -

    elif d.startswith("lesson:"):
        _, mid, lid = d.split(":")
        les  = lesson_data(mid, lid)
        done = completed_lessons(uid)
        key  = f"{mid}:{lid}"
        status = " *Tugatilgan!*" if key in done else " Hali tugatilmagan"
        text = (
            f"{les['emoji']} *{les['title']}*\n\n"
            f"So'zlar: *{len(les['vocab'])} ta*\n"
 
            f"Mashqlar: *{len(les['exercises'])} ta*\n"
            f"Mukofot: *+{len(les['exercises'])*10} XP*\n\n"
 
 
            f"{status}\n\n"
            "Avval lug'atni ko'ring, keyin boshlang!"
 
        )
        await q.edit_message_text(text, parse_mode="Markdown",
                                  reply_markup=kb_lesson_detail(mid, lid, done))
    # - Lug'at bo'limi (menyu) -

    elif d == "vocab_menu":
        rows = []
        for mid, lid in LESSON_ORDER:
            les = lesson_data(mid, lid)
            rows.append([InlineKeyboardButton(
                f"{les['emoji']} {les['title']}",
                callback_data=f"vocab:{mid}:{lid}"
            )])
        rows.append([InlineKeyboardButton(" Bosh menyu", callback_data="main")])
        await q.edit_message_text(
            "*Lug'at — Darsni tanlang:*",
 
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(rows)
        )
    # - Lugat (alohida dars) -

    elif d.startswith("vocab:"):
        _, mid, lid = d.split(":")
        les  = lesson_data(mid, lid)
        text = f" *{les['emoji']} {les['title']} — Lug'at*\n\n"
        for i, w in enumerate(les["vocab"], 1):
            text += (f"*{i}.*  `{w['pl']}`\n"
                     f"     _{w['ph']}_\n"
                     f"     {w['uz']}\n\n")
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton(" Darsni boshlash", callback_data=f"go:{mid}:{lid}")],
            [InlineKeyboardButton(" Orqaga",          callback_data=f"lesson:{mid}:{lid}")]
        ])
        await q.edit_message_text(text, parse_mode="Markdown", reply_markup=kb)
    # - Darsni boshlash -

    elif d.startswith("go:"):
        _, mid, lid = d.split(":")
        new_session(uid, f"{mid}:{lid}")
        refresh_streak(uid)
        await show_exercise(q, uid, mid, lid, 0, 3)
    # - Javob -

    elif d.startswith("ans:"):
        _, ex_idx_s, choice_s = d.split(":")
        ex_idx = int(ex_idx_s)
        choice = int(choice_s)
        ses = get_session(uid)
        if not ses:
            await q.edit_message_text(" Sessiya topilmadi. /start bosing.")
            return
        mid, lid = ses["lesson_id"].split(":")
        les       = lesson_data(mid, lid)
        exercises = les["exercises"]
        ex        = exercises[ex_idx]
        correct   = ex["ans"]
        is_ok     = (choice == correct)
        lives     = ses["lives"]
        corr_cnt  = ses["correct"]
        wrong_cnt = ses["wrong"]
        xp_earned = ses["xp_earned"]
        if is_ok:
            corr_cnt += 1
            xp_earned += 10
 
            result = "*To'g'ri!* +10 "
        else:
            lives    -= 1
            wrong_cnt += 1
            result = f" *Xato!*  To'g'ri javob: *{ex['opts'][correct]}*"
        next_idx = ex_idx + 1
        upd_session(uid, ex_idx=next_idx, lives=lives,
                    correct=corr_cnt, wrong=wrong_cnt, xp_earned=xp_earned)
        # Natijani ko'rsat
        opts_display = "\n".join(
            f"{' ' if i==correct else (' ' if i==choice and not is_ok else ' ')}  {opt}"
            for i, opt in enumerate(ex["opts"])
        )
        result_text = (
            f"{hearts_bar(lives)}\n"
            f"{progress_bar(ex_idx+1, len(exercises))}\n\n"
            f"{ex['q']}\n\n"
            f"{opts_display}\n\n"
            f"{result}"
        )
        # Yuraklar tugadi
        if lives <= 0:
            u = get_user(uid)
            new_h = max(0, (u.get("hearts") or 5) - 1)
            upd_user(uid, hearts=new_h)
            final = (
                f"{result_text}\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━\n"
                f"*Yuraklar tugadi!*\n\n"
 
                f"To'g'ri: {corr_cnt}   Xato: {wrong_cnt}\n"
                f"Ball: +{xp_earned}\n"
                f"Qoldi: {new_h}/5\n\n"
 
 
 
                "Qayta urinib ko'ring!"
            )
            await q.edit_message_text(final, parse_mode="Markdown",
                                      reply_markup=kb_after_lesson(mid, lid))
            return
        # Dars tugadi
        if next_idx >= len(exercises):
            u = get_user(uid)
            new_xp = (u.get("xp") or 0) + xp_earned
            upd_user(uid, xp=new_xp)
            mark_done(uid, f"{mid}:{lid}", corr_cnt)
            stars = (" " if lives == 3 else
                     " "  if lives == 2 else " ")
            final = (
                f"{result_text}\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━\n"
                f"*Dars tugadi!*\n\n"
 
                f"{stars}\n\n"
                f"To'g'ri: *{corr_cnt}*    Xato: *{wrong_cnt}*\n"
 
                f"Jami XP: *+{xp_earned}*\n"
                f"Streak: *{u.get('streak',1)} kun*\n\n"
 
 
                f"Davom eting! "
            )
            await q.edit_message_text(final, parse_mode="Markdown",
                                      reply_markup=kb_after_lesson(mid, lid))
            return
        # Keyingi savol
        await q.edit_message_text(
            f"{result_text}\n\n Keyingi savol...",
            parse_mode="Markdown"
        )
        await show_exercise(q, uid, mid, lid, next_idx, lives)
    # - Progress -

    elif d == "progress":
        u     = get_user(uid) or {}
        done  = completed_lessons(uid)
        total = len(LESSON_ORDER)
        n_done = len(done)
        text = (
            f"*{q.from_user.first_name} — Progressim*\n\n"
            f"Streak: *{u.get('streak',0)} kun*\n"
            f"Jami XP: *{u.get('xp',0)}*\n"
            f" Yuraklar: *{u.get('hearts',5)}/5*\n\n"
            f"*Darslar:*\n"
 
 
 

 
            f"{progress_bar(n_done, total)}\n"
            f"Tugatilgan: *{n_done}/{total}*\n\n"
        )
        for mid, lid in LESSON_ORDER:
            les = lesson_data(mid, lid)
            key = f"{mid}:{lid}"
            ico = " " if key in done else " "
            text += f"{ico} {les['emoji']} {les['title']}\n"
        await q.edit_message_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(" Darslar",  callback_data="lessons")],
                [InlineKeyboardButton(" Bosh menyu", callback_data="main")]
            ]))
    # - Eslatma menyu -

    elif d == "reminder_menu":
        u = get_user(uid) or {}
        cur_r = u.get("reminder") or "—"
        times = ["07:00","09:00","12:00","18:00","20:00","22:00"]
        rows  = []
        row   = []
        for t in times:
            row.append(InlineKeyboardButton(
                f"{'' if cur_r==t else ''}{t}",
 
                callback_data=f"setr:{t}"
            ))
            if len(row) == 3:
                rows.append(row); row = []
        if row: rows.append(row)
        rows.append([InlineKeyboardButton(" O'chirish", callback_data="delr")])
        rows.append([InlineKeyboardButton(" Bosh menyu", callback_data="main")])
        text = (
            f"*Kunlik Eslatma*\n\n"
 
            f"Hozirgi vaqt: *{cur_r}*\n\n"
            "Har kuni qaysi vaqtda eslataylik?"
        )
        await q.edit_message_text(text, parse_mode="Markdown",
                                  reply_markup=InlineKeyboardMarkup(rows))
    elif d.startswith("setr:"):
        t = d[5:]
        upd_user(uid, reminder=t)
        await q.edit_message_text(
            f"*Eslatma o'rnatildi!*\n\nHar kuni soat *{t}* da xabar keladi. ",
 
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(" Bosh menyu", callback_data="main")]
            ])
        )
    elif d == "delr":
        upd_user(uid, reminder=None)
        await q.edit_message_text(" Eslatma o'chirildi.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(" Bosh menyu", callback_data="main")]
     
            ]))
    #- Yordam -
    elif d == "help":
        text = (
            " *Yordam — Polyakcha Bot*\n\n"
            "*Qanday ishlaydi?*\n"
 
            "*Darslar* → darsni tanlang\n"
            "* Lug'at* → yangi so'zlarni o'rganing\n"
            "* Boshlash* → mashqlarni bajaring\n"
            "*To'g'ri javob* =  +10 XP\n"
            "*Xato javob* =   kamayadi\n"
            "*3 ta xato* =  dars tugaydi\n\n"
 
 
 
 
 
 
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "*Tizim:*\n"
 
            "Yuraklar — 3 ta har darsda\n"
            "XP — to'g'ri javob uchun\n"
            "Streak — ketma-ket kunlar\n"
            "Eslatma — kunlik bildirishnoma\n\n"
 
 
 
 
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "*Bog'lanish:*\n"
 
            "Muammo bo'lsa: @sizning_username\n\n"
            "*Buyruqlar:*\n"
            "/start — Bosh menyu\n"
            "/darslar — Darslar\n"
            "/progress — Progressim\n"
        )
        await q.edit_message_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(" Bosh menyu", callback_data="main")]
            ]))
# ═══════════════════════════════════════════
#  EXERCISE KO'RSATISH
# ═══════════════════════════════════════════
async def show_exercise(q, uid, mid, lid, ex_idx, lives):
    les       = lesson_data(mid, lid)
    exercises = les["exercises"]
    ex        = exercises[ex_idx]
    total     = len(exercises)
    text = (
        f"{hearts_bar(lives)}\n"
        f"{progress_bar(ex_idx, total)}\n\n"
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
async def daily_reminder_job(ctx: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().strftime("%H:%M")
    rows = db("SELECT user_id, name FROM users WHERE reminder=?", (now,), "all")
    if not rows: return
    for row in rows:
        try:
            await ctx.bot.send_message(
                chat_id=row["user_id"],
                text=(
                    f" *Salom, {row['name']}!*\n\n"
                    "Bugun ham polyakcha o'rganish vaqti keldi! \n\n"
                    "Har kun bir dars — oyiga A1 darajasi! \n\n"
                    "Boshlash uchun quyida bosing:"
 
                ),
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(" Darsni boshlash", callback_data="lessons")]
                ])
            )
        except Exception as e:
            logger.warning(f"Eslatma xatosi {row['user_id']}: {e}")
# ═══════════════════════════════════════════
#  QO'SHIMCHA BUYRUQLAR
# ═══════════════════════════════════════════
async def cmd_darslar(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid  = update.effective_user.id
    done = completed_lessons(uid)
    await update.message.reply_text(
        "*Darslar*", parse_mode="Markdown",
 
        reply_markup=kb_lessons(done)
    )
async def cmd_progress(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid  = update.effective_user.id
    u    = get_user(uid) or {}
    done = completed_lessons(uid)
    await update.message.reply_text(
        f" *Progressim*\n\n"
        f" XP: *{u.get('xp',0)}*\n"
        f" Streak: *{u.get('streak',0)} kun*\n"
        f" Yuraklar: *{u.get('hearts',5)}/5*\n"
        f" Darslar: *{len(done)}/{len(LESSON_ORDER)}*",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(" Batafsil", callback_data="progress")]
        ])
    )
async def cmd_help(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "*Yordam:*\n"
 
        "/start — Bosh menyu\n"
        "/darslar — Darslar\n"
        "/progress — Progressim",
        parse_mode="Markdown"
    )
# Noma'lum xabar
async def unknown_msg(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Botdan foydalanish uchun /start bosing!",
 
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(" Bosh menyu", callback_data="main")]
        ])
    )
# ═══════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════
def main():
    init_db()
    print(" Polyakcha Bot ishga tushmoqda...")
    app = Application.builder().token(BOT_TOKEN).build()
    # Handlers
    app.add_handler(CommandHandler("start",    cmd_start))
    app.add_handler(CommandHandler("darslar",  cmd_darslar))
    app.add_handler(CommandHandler("progress", cmd_progress))
    app.add_handler(CommandHandler("help",     cmd_help))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_msg))
    # Kunlik eslatma — har daqiqа tekshirish
    #app.job_queue.run_repeating(daily_reminder_job, interval=60, first=5)
    async def post_init(application):
        await application.bot.set_my_commands([
            BotCommand("start",    " Bosh menyu"),
            BotCommand("darslar",  " Darslar ro'yxati"),
            BotCommand("progress", " Mening progressim"),
            BotCommand("help",     " Yordam"),
        ])
    app.post_init = post_init
    print(" Bot ishga tushdi! Ctrl+C — to'xtatish")
    app.run_polling(allowed_updates=Update.ALL_TYPES)
if __name__ == "__main__":
    main()