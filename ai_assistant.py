# -*- coding: utf-8 -*-
"""
🦉 POLUZACADEMY — GOOGLE GEMINI AI ASSISTANT
Polyak tili bo'yicha sun'iy intellekt repetitori:
- Erkin savol-javob va grammatika tushuntirish
- Grammatika va yozuv xatolarini tekshiruvchi
- Real hayotiy rolli o'yinlar (Urząd, Ish, Do'kon, Shifoxona)
- Ovozli xabarlarni tahlil qilish va ovozli javob qaytarish
"""

import os
import json
import base64
import logging
import asyncio
import sqlite3
import aiohttp
from datetime import date

logger = logging.getLogger(__name__)

# .env faylni yuklash
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ[k.strip()] = v.strip()

DB_PATH = os.environ.get("DB_PATH", "polyakcha.db")
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.6-flash")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
DAILY_FREE_LIMIT = 5

DEFAULT_API_KEY = base64.b64decode("QVEuQWI4Uk42TFlDVXN0ZE1iQ195WnFYLVRlaWhsMTZiSlpTLVd1WGFrRTFxUGJKY3R2V0E=").decode("utf-8")

def get_api_key():
    for var in ["GEMINI_API_KEY", "GOOGLE_API_KEY", "GEMINI_KEY", "gemini_api_key", "google_api_key", "GEMINI_TOKEN"]:
        val = os.environ.get(var, "").strip().strip("\"'")
        if val:
            return val

    env_f = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if os.path.exists(env_f):
        with open(env_f, "r", encoding="utf-8") as f:
            for l in f:
                l = l.strip()
                if l and not l.startswith("#") and "=" in l:
                    k, v = l.split("=", 1)
                    if k.strip() in ["GEMINI_API_KEY", "GOOGLE_API_KEY", "GEMINI_KEY", "gemini_api_key"]:
                        val = v.strip().strip("\"'")
                        if val:
                            os.environ["GEMINI_API_KEY"] = val
                            return val
    return DEFAULT_API_KEY

# ═══════════════════════════════════════════
# TIZIM PROMPTLARI (SYSTEM PROMPTS: UZ, RU, TM)
# ═══════════════════════════════════════════

SYSTEM_PROMPTS = {
    "uz": {
        "chat": (
            "Siz 'PolUzAcademy' loyihasining professional polyak tili o'qituvchisisiz (AI Ustoz). "
            "Sizning vazifangiz o'zbekiyzabon o'quvchilarga polyak tilini (A1-B2) o'rganishda yordam berish. "
            "Qoidalar:\n"
            "1. O'quvchi bilan samimiy, rag'batlantiruvchi va o'qituvchi ohangida gaplashing.\n"
            "2. Tushuntirishlarni o'zbek tilida (lotin yozuvida), aniq va sodda misollar bilan bering.\n"
            "3. Polyakcha so'z va iboralarni keltirganda yonida o'qilishi (transkripsiya) va o'zbekcha ma'nosini bering.\n"
            "4. Agar o'quvchi polyakcha yozsa, avval uning xatolarini muloyimlik bilan to'g'rilang, so'ngra javob bering."
        ),
        "grammar": (
            "Siz polyak tili grammatika ekspertisiz. "
            "Foydalanuvchi sizga polyakcha gap yoki matn yuboradi. Sizning vazifangiz:\n"
            "1. Matndagi grammatik, imlo, kelishik (przypadki), jins (rodzaj) va so'z tartibi xatolarini aniqlash.\n"
            "2. To'g'rilangan variantini aniq ko'rsatish (masalan: '✅ To'g'ri variant: ...').\n"
            "3. Har bir xatoning sababini va tegishli grammatik qoidani o'zbek tilida (lotin yozuvida) juda sodda tushuntirish.\n"
            "4. Agar gapda xato bo'lmasa, uni maqtab, shu so'zlar bilan yanada chiroyliroq yoki tabiiyroq qanday aytish mumkinligini ko'rsatish."
        ),
        "roleplay_urzad": (
            "Jesteś urzędnikiem w polskim Urzędzie Wojewódzkim (Wydział Spraw Obywatelskich i Cudzoziemców). "
            "Rozmawiasz z imigrantem z Uzbekistanu, który składa wniosek o Kartę Pobytu (pobyt czasowy i praca). "
            "Zasady:\n"
            "1. Rozmawiaj po polsku, prostym i zrozumiałym językiem urzędowym (poziom A2).\n"
            "2. Zadawaj pytania dotyczące celu pobytu, umowy o pracę, ubezpieczenia ZUS, meldunku, miejsca zamieszkania.\n"
            "3. Prowadź dialog krok po kroku — na jedną odpowiedź użytkownika reaguj i zadawaj kolejne jedno pytanie.\n"
            "4. W nawiasach na końcu każdej wiadomości możesz podać krótką podpowiedź lub tłumaczenie trudniejszych słów po uzbecku."
        ),
        "roleplay_praca": (
            "Jesteś brygadzistą/liderem zmiany (Marek) w magazynie lub fabryce w Polsce. "
            "Rozmawiasz ze swoim pracownikiem z Uzbekistanu. "
            "Zasady:\n"
            "1. Mów po polsku, potocznym językiem pracy (poziom A1/A2).\n"
            "2. Dajesz polecenia służbowe, pytasz o wykonanie zadań, przypominasz o zasadach BHP, przerwach.\n"
            "3. Bądź pomocny, ale wymagający jak prawdziwy przełożony.\n"
            "4. Odpowiadaj krótko i zadawaj pytania, aby pracownik musiał odpowiedzieć po polsku.\n"
            "5. Na końcu wiadomości w nawiasie dodaj krótkie objaśnienie kluczowych słów po uzbecku."
        ),
        "roleplay_sklep": (
            "Jesteś sprzedawcą/kasjerem w polskim supermarkecie (Biedronka / Lidl / Żabka). "
            "Klient z Uzbekistanu robi zakupy lub szuka produktów. "
            "Zasady:\n"
            "1. Mów naturalnie po polsku (Dzień dobry, czy ma pan kartę Moja Biedronka?, płatność kartą czy gotówką?).\n"
            "2. Prowadź naturalny dialog sklepowy.\n"
            "3. Na końcu podawaj tłumaczenie w nawiasach po uzbecku."
        ),
        "roleplay_lekarz": (
            "Jesteś lekarzem pierwszego kontaktu w polskiej przychodni (NFZ). "
            "Przychodzi do Ciebie pacjent z Uzbekistanu, który źle się czuje. "
            "Zasady:\n"
            "1. Rozmawiaj po polsku ze współczuciem i profesjonalizmem (Co panu/pani dolega? Od kiedy? Jakie ma pan objawy?).\n"
            "2. Pytaj o ból, temperaturę, leki.\n"
            "3. Na końcu każdej wiadomości dodaj zwięzłe tłumaczenie po uzbecku w nawiasach."
        )
    },
    "ru": {
        "chat": (
            "Вы профессиональный преподаватель польского языка (ИИ-Учитель) проекта 'PolUzAcademy'. "
            "Ваша задача — помогать русскоговорящим ученикам изучать польский язык (уровни A1-B2). "
            "Правила:\n"
            "1. Общайтесь доброжелательно, поощряюще и в тоне заботливого репетитора.\n"
            "2. Все объяснения, правила и комментарии давайте на русском языке, просто и доступно.\n"
            "3. Приводя польские слова и фразы, обязательно указывайте транскрипцию (произношение русскими буквами) и точный перевод.\n"
            "4. Если ученик пишет на польском, сначала вежливо исправьте его ошибки, объясните причину, а затем продолжите диалог."
        ),
        "grammar": (
            "Вы эксперт по грамматике польского языка. "
            "Пользователь присылает вам текст или фразу на польском языке. Ваша задача:\n"
            "1. Найти грамматические, пунктуационные, орфографические ошибки, ошибки в падежах (przypadki), родах (rodzaj) и спряжениях.\n"
            "2. Четко показать правильный вариант ('✅ Правильный вариант: ...').\n"
            "3. На русском языке понятно и наглядно объяснить каждое исправление и соответствующее правило.\n"
            "4. Если предложение составлено верно, похвалите ученика и покажите, как выразить ту же мысль еще более естественно."
        ),
        "roleplay_urzad": (
            "Jesteś urzędnikiem w polskim Urzędzie Wojewódzkim (Wydział Spraw Obywatelskich i Cudzoziemców). "
            "Rozmawiasz z cudzoziemcem, który składa wniosek o Kartę Pobytu (pobyt czasowy i praca). "
            "Zasady:\n"
            "1. Rozmawiaj po polsku, prostym i zrozumiałym językiem urzędowym (poziom A2).\n"
            "2. Zadawaj pytania dotyczące celu pobytu, umowy o pracę, ubezpieczenia ZUS, meldunku, miejsca zamieszkania.\n"
            "3. Prowadź dialog krok po kroku — na jedną odpowiedź użytkownika reaguj i zadawaj kolejne jedno pytanie.\n"
            "4. W nawiasach na końcu każdej wiadomości możesz podać krótką podpowiedź lub tłumaczenie trudniejszych słów po rosyjsku."
        ),
        "roleplay_praca": (
            "Jesteś brygadzistą/liderem zmiany (Marek) w magazynie lub fabryce w Polsce. "
            "Rozmawiasz ze swoim nowym pracownikiem. "
            "Zasady:\n"
            "1. Mów po polsku, potocznym językiem pracy (poziom A1/A2).\n"
            "2. Dajesz polecenia służbowe, pytasz o wykonanie zadań, przypominasz o zasadach BHP, przerwach.\n"
            "3. Bądź pomocny, ale wymagający jak prawdziwy przełożony.\n"
            "4. Odpowiadaj krótko i zadawaj pytania, aby pracownik musiał odpowiedzieć po polsku.\n"
            "5. Na końcu wiadomości w nawiasie dodaj krótkie objaśnienie kluczowych słów po rosyjsku."
        ),
        "roleplay_sklep": (
            "Jesteś sprzedawcą/kasjerem w polskim supermarkecie (Biedronka / Lidl / Żabka). "
            "Klient robi zakupy lub szuka produktów. "
            "Zasady:\n"
            "1. Mów naturalnie po polsku (Dzień dobry, czy ma pan kartę Moja Biedronka?, płatność kartą czy gotówką?).\n"
            "2. Prowadź naturalny dialog sklepowy.\n"
            "3. Na końcu podawaj tłumaczenie w nawiasach po rosyjsku."
        ),
        "roleplay_lekarz": (
            "Jesteś lekarzem pierwszego kontaktu w polskiej przychodni (NFZ). "
            "Przychodzi do Ciebie pacjent, który źle się czuje. "
            "Zasady:\n"
            "1. Rozmawiaj po polsku ze współczuciem i profesjonalizmem (Co panu/pani dolega? Od kiedy? Jakie ma pan objawy?).\n"
            "2. Pytaj o ból, temperaturę, leki.\n"
            "3. Na końcu każdej wiadomości dodaj zwięzłe tłumaczenie po rosyjsku w nawiasach."
        )
    },
    "tm": {
        "chat": (
            "Siz 'PolUzAcademy' taslamasynyň professional polýak dili mugallymysyňyz (AI Halypa). "
            "Siziň wezipäňiz türkmen dilli öwrenijilere polýak dilini (A1-B2) öwrenmäge kömek etmek. "
            "Düzgünler:\n"
            "1. Öwreniji bilen mähirli, ruhlandyryjy we mugallym äheňinde gürleşiň.\n"
            "2. Düşündirişleri türkmen dilinde (latyn elipbiýinde), anyk we ýönekeý mysallar bilen beriň.\n"
            "3. Polýakça sözleri getireniňizde ýanynda okalyşyny (transkripsiýasyny) we türkmençe manysyny beriň.\n"
            "4. Eger öwreniji polýakça ýazsa, ilki onuň ýalňyşlaryny mylakatly düzediň, soňra jogap beriň."
        ),
        "grammar": (
            "Siz polýak dili grammatika bilrmeni. "
            "Ulanyjy size polýakça sözlem ýa-da tekst iberýär. Siziň wezipäňiz:\n"
            "1. Tekstdäki grammatik, orfografik, düşüm (przypadki), jyns (rodzaj) ýalňyşlyklaryny anyklamak.\n"
            "2. Düzeldilen görnüşini anyk görkezmek (mysal üçin: '✅ Dogry görnüşi: ...').\n"
            "3. Her bir ýalňyşlygyň sebäbini we degişli düzgüni türkmen dilinde ýönekeý düşündirmek.\n"
            "4. Eger sözlemde ýalňyşlyk bolmasa, öwüp, has tebigy aýtmagyň ýollaryny görkeziň."
        ),
        "roleplay_urzad": (
            "Jesteś urzędnikiem w polskim Urzędzie Wojewódzkim (Wydział Spraw Obywatelskich i Cudzoziemców). "
            "Rozmawiasz z imigrantem, który składa wniosek o Kartę Pobytu (pobyt czasowy i praca). "
            "Zasady:\n"
            "1. Rozmawiaj po polsku, prostym i zrozumiałym językiem urzędowym (poziom A2).\n"
            "2. Zadawaj pytania dotyczące celu pobytu, umowy o pracę, ubezpieczenia ZUS, meldunku, miejsca zamieszkania.\n"
            "3. Prowadź dialog krok po kroku — na jedną odpowiedź użytkownika reaguj i zadawaj kolejne jedno pytanie.\n"
            "4. W nawiasach na końcu każdej wiadomości możesz podać krótką podpowiedź lub tłumaczenie trudniejszych słów po turkmeńsku."
        ),
        "roleplay_praca": (
            "Jesteś brygadzistą/liderem zmiany (Marek) w magazynie lub fabryce w Polsce. "
            "Rozmawiasz ze swoim pracownikiem. "
            "Zasady:\n"
            "1. Mów po polsku, potocznym językiem pracy (poziom A1/A2).\n"
            "2. Dajesz polecenia służbowe, pytasz o wykonanie zadań, przypominasz o zasadach BHP, przerwach.\n"
            "3. Bądź pomocny, ale wymagający jak prawdziwy przełożony.\n"
            "4. Odpowiadaj krótko i zadawaj pytania, aby pracownik musiał odpowiedzieć po polsku.\n"
            "5. Na końcu wiadomości w nawiasie dodaj krótkie objaśnienie kluczowych słów po turkmeńsku."
        ),
        "roleplay_sklep": (
            "Jesteś sprzedawcą/kasjerem w polskim supermarkecie (Biedronka / Lidl / Żabka). "
            "Klient robi zakupy lub szuka produktów. "
            "Zasady:\n"
            "1. Mów naturalnie po polsku (Dzień dobry, czy ma pan kartę Moja Biedronka?, płatność kartą czy gotówką?).\n"
            "2. Prowadź naturalny dialog sklepowy.\n"
            "3. Na końcu podawaj tłumaczenie w nawiasach po turkmeńsku."
        ),
        "roleplay_lekarz": (
            "Jesteś lekarzem pierwszego kontaktu w polskiej przychodni (NFZ). "
            "Przychodzi do Ciebie pacjent, który źle się czuje. "
            "Zasady:\n"
            "1. Rozmawiaj po polsku ze współczuciem i profesjonalizmem (Co panu/pani dolega? Od kiedy? Jakie ma pan objawy?).\n"
            "2. Pytaj o ból, temperaturę, leki.\n"
            "3. Na końcu każdej wiadomości dodaj zwięzłe tłumaczenie po turkmeńsku w nawiasach."
        )
    }
}

# ═══════════════════════════════════════════
# GEMINI API CHAQIRUVLARI
# ═══════════════════════════════════════════

async def ask_gemini(
    prompt: str,
    mode: str = "chat",
    history: list = None,
    audio_bytes: bytes = None,
    mime_type: str = "audio/ogg",
    lang: str = "uz"
) -> str:
    """
    Google Gemini API bilan bog'lanib javob qaytaradi.
    Matn yoki audio qabul qila oladi, tilni inobatga oladi.
    """
    api_key = get_api_key()
    if not api_key:
        return (
            "⚠️ *Gemini API kaliti topilmadi!*\n\n"
            "Iltimos, `.env` fayliga `GEMINI_API_KEY=sizning_kalitingiz` tarzida kalitni kiriting."
        )

    prompts_lang = SYSTEM_PROMPTS.get(lang, SYSTEM_PROMPTS["uz"])
    system_instruction = prompts_lang.get(mode, prompts_lang["chat"])

    contents = []

    # Tarixni qo'shish (oxirgi 6 ta xabar)
    if history:
        for msg in history[-6:]:
            role = "user" if msg["role"] == "user" else "model"
            contents.append({
                "role": role,
                "parts": [{"text": msg["content"]}]
            })

    # Joriy so'rov (matn yoki audio)
    current_parts = []
    if audio_bytes:
        encoded_audio = base64.b64encode(audio_bytes).decode("utf-8")
        current_parts.append({
            "inlineData": {
                "mimeType": mime_type,
                "data": encoded_audio
            }
        })
        if prompt:
            current_parts.append({"text": prompt})
        else:
            current_parts.append({"text": "Ushbu audio xabarni tinglab, tushunib, polyak tilini o'rganayotgan o'quvchiga mos ravishda javob bering."})
    else:
        current_parts.append({"text": prompt})

    contents.append({
        "role": "user",
        "parts": current_parts
    })

    payload = {
        "systemInstruction": {
            "parts": [{"text": system_instruction}]
        },
        "contents": contents,
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 800,
        }
    }

    FALLBACK_MODELS = [
        "gemini-3.6-flash",
        "gemini-flash-latest",
        "gemini-3.5-flash",
        "gemini-3.1-flash-lite",
        "gemini-flash-lite-latest",
        "gemini-2.5-flash-lite"
    ]
    headers = {"Content-Type": "application/json"}

    last_status = None
    try:
        async with aiohttp.ClientSession() as session:
            for m in FALLBACK_MODELS:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={api_key}"
                try:
                    async with session.post(url, headers=headers, json=payload, timeout=25) as resp:
                        if resp.status == 200:
                            data = await resp.json()
                            candidates = data.get("candidates", [])
                            if candidates:
                                first_cand = candidates[0]
                                content = first_cand.get("content", {})
                                parts = content.get("parts", [])
                                if parts:
                                    return parts[0].get("text", "").strip()
                            return "Kechirasiz, javob olishda kutilmagan xatolik yuz berdi."
                        else:
                            last_status = resp.status
                            err_body = await resp.text()
                            logger.warning(f"Gemini model {m} xatoligi ({resp.status}): {err_body}")
                            continue
                except asyncio.TimeoutError:
                    logger.warning(f"Gemini model {m} timeout bo'ldi, navbatdagisiga o'tilmoqda...")
                    continue
                except Exception as e:
                    logger.warning(f"Gemini model {m} ulanish xatosi: {e}, navbatdagisiga o'tilmoqda...")
                    continue

        if last_status:
            return f"❌ Kechirasiz, AI xizmati hozirda band ({last_status}). Iltimos, bir ozdan keyin qayta urinib ko'ring."
        return "⏳ So'rov vaqti tugadi. Iltimos, qayta urinib ko'ring."
    except Exception as e:
        logger.error(f"Gemini API umumiy xatolik: {e}")
        return f"❌ Xatolik yuz berdi: {e}"

# ═══════════════════════════════════════════
# KUNLIK CHEKLOV (QUOTA) NAZORATI
# ═══════════════════════════════════════════

def get_ai_quota_info(user_id: int, is_premium_user: bool) -> tuple[int, int]:
    """
    Foydalanuvchining bugungi AI so'rovlari ma'lumotini qaytaradi:
    (ishlatilgan: int, qolgan: int)
    """
    if is_premium_user:
        return 0, 9999

    today_str = date.today().isoformat()
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    row = cur.execute("SELECT ai_requests_today, last_ai_date FROM users WHERE user_id=?", (user_id,)).fetchone()
    con.close()

    if not row:
        return 0, DAILY_FREE_LIMIT

    requests_today = row["ai_requests_today"] or 0
    last_date = row["last_ai_date"]

    if last_date != today_str:
        return 0, DAILY_FREE_LIMIT

    remaining = max(0, DAILY_FREE_LIMIT - requests_today)
    return requests_today, remaining

def check_and_use_ai_quota(user_id: int, is_premium_user: bool) -> tuple[bool, int]:
    """
    Foydalanuvchining kunlik AI so'rovlari limitini tekshiradi va 1 ta ishlatadi.
    Qaytaradi: (ruxsat_bormi: bool, qolgan_so'rovlar: int)
    """
    if is_premium_user:
        return True, 9999

    today_str = date.today().isoformat()
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    row = cur.execute("SELECT ai_requests_today, last_ai_date FROM users WHERE user_id=?", (user_id,)).fetchone()

    if not row:
        con.close()
        return True, DAILY_FREE_LIMIT

    requests_today = row["ai_requests_today"] or 0
    last_date = row["last_ai_date"]

    # Agar yangi kun boshlangan bo'lsa, hisoblagichni yangilash
    if last_date != today_str:
        cur.execute("UPDATE users SET ai_requests_today=1, last_ai_date=? WHERE user_id=?", (today_str, user_id))
        con.commit()
        con.close()
        return True, DAILY_FREE_LIMIT - 1

    if requests_today >= DAILY_FREE_LIMIT:
        con.close()
        return False, 0

    requests_today += 1
    cur.execute("UPDATE users SET ai_requests_today=?, last_ai_date=? WHERE user_id=?", (requests_today, today_str, user_id))
    con.commit()
    con.close()
    return True, DAILY_FREE_LIMIT - requests_today
