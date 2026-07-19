# -*- coding: utf-8 -*-
"""
🦉 POLYAKCHA BOT — A1 DARSLARI
40 ta dars: A1.1 (20 dars) + A1.2 (20 dars)
"""

A1_LESSONS = {

    # ════════════════════════════════════
    # A1.1 — BOSHLANG'ICH (20 dars)
    # ════════════════════════════════════

    "a1_l01": {
        "title": "Salomlashish",
        "emoji": "👋",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika:*\n\n"
            "Polyakchada *rasmiy* va *norasmiy* muloqot farq qiladi:\n\n"
            "• *Rasmiy* (katta yoshlilar, begonalar):\n"
            "  → *Dzień dobry!* (Xayrli kun)\n"
            "  → *Do widzenia!* (Xayr)\n\n"
            "• *Norasmiy* (do'stlar, tengdoshlar):\n"
            "  → *Cześć!* (Salom/Xayr)\n"
            "  → *Hej!* (Hey)\n\n"
            "⚠️ *Muhim:* Begona katta kishiga *Ty* (sen) deyish qo'pollik!"
        ),
        "vocab": [
            {"pl": "Dzień dobry",      "ph": "djen DOB-ri",        "uz": "Xayrli kun (rasmiy)"},
            {"pl": "Dobry wieczór",    "ph": "DOB-ri vye-CHUR",    "uz": "Xayrli kech"},
            {"pl": "Dobranoc",         "ph": "dob-RA-nots",        "uz": "Xayrli tun"},
            {"pl": "Cześć",            "ph": "cheshch",            "uz": "Salom / Ko'rishguncha"},
            {"pl": "Hej",              "ph": "hey",                "uz": "Hey (norasmiy)"},
            {"pl": "Do widzenia",      "ph": "do vi-DZE-nya",      "uz": "Xayr (rasmiy)"},
            {"pl": "Do zobaczenia",    "ph": "do zo-ba-CHE-nya",   "uz": "Ko'rishguncha"},
            {"pl": "Na razie",         "ph": "na RA-zye",          "uz": "Hozircha xayr"},
            {"pl": "Dziękuję",         "ph": "djen-KU-ye",         "uz": "Rahmat"},
            {"pl": "Bardzo dziękuję",  "ph": "BAR-dzo djen-KU-ye", "uz": "Katta rahmat"},
            {"pl": "Proszę",           "ph": "PRO-she",            "uz": "Marhamat / Iltimos"},
            {"pl": "Przepraszam",      "ph": "pshe-PRA-sham",      "uz": "Kechirasiz"},
            {"pl": "Tak",              "ph": "tak",                "uz": "Ha"},
            {"pl": "Nie",              "ph": "nye",                "uz": "Yo'q"},
            {"pl": "Dobrze",           "ph": "DOB-zhe",            "uz": "Yaxshi / Mayli"},
        ],
        "dialog": (
            "💬 *Dialog: Do'konda*\n\n"
            "🧑 Mijoz: *Dzień dobry!*\n"
            "🏪 Satuvchi: *Dzień dobry! Słucham?*\n"
            "🧑 Mijoz: *Dziękuję. Do widzenia!*\n"
            "🏪 Satuvchi: *Do widzenia! Miłego dnia!*\n\n"
            "📝 *Tarjima:*\n"
            "🧑 Xayrli kun!\n"
            "🏪 Xayrli kun! Eshitaman?\n"
            "🧑 Rahmat. Xayr!\n"
            "🏪 Xayr! Yaxshi kun!"
        ),
        "exercises": [
            {"q": "🇵🇱 *'Dzień dobry'* nima degani?",
             "opts": ["Xayrli tun", "Xayrli kun", "Salom", "Xayr"], "ans": 1},
            {"q": "🇺🇿 *'Rahmat'* polyakchada?",
             "opts": ["Proszę", "Przepraszam", "Dziękuję", "Tak"], "ans": 2},
            {"q": "🇵🇱 *'Do widzenia'* nima degani?",
             "opts": ["Salom", "Rahmat", "Xayr (rasmiy)", "Kechirasiz"], "ans": 2},
            {"q": "🇺🇿 *'Kechirasiz'* polyakchada?",
             "opts": ["Proszę", "Przepraszam", "Dziękuję", "Dobranoc"], "ans": 1},
            {"q": "🇵🇱 *'Na razie'* nima degani?",
             "opts": ["Xayrli kun", "Hozircha xayr", "Rahmat", "Ha"], "ans": 1},
            {"q": "🇵🇱 *'Tak'* nima degani?",
             "opts": ["Yo'q", "Ha", "Kechirasiz", "Rahmat"], "ans": 1},
            {"q": "🇵🇱 *'Dobranoc'* nima degani?",
             "opts": ["Xayrli kun", "Xayrli kech", "Xayrli tun", "Salom"], "ans": 2},
            {"q": "🇵🇱 *'Proszę'* nima degani?",
             "opts": ["Rahmat", "Kechirasiz", "Marhamat", "Ha"], "ans": 2},
            {"q": "🇺🇿 *'Yaxshi / Mayli'* polyakchada?",
             "opts": ["Tak", "Nie", "Dobrze", "Proszę"], "ans": 2},
            {"q": "🇵🇱 *'Dobry wieczór'* nima degani?",
             "opts": ["Xayrli tun", "Xayrli kech", "Xayrli kun", "Salom"], "ans": 1},
        ],
    },

    "a1_l02": {
        "title": "Alifbo va Talaffuz",
        "emoji": "🔤",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika:*\n\n"
            "Polyak alifbosi — *32 harf*\n\n"
            "*Maxsus harflar:*\n"
            "• *Ą ą* → 'on' (burun orqali)\n"
            "• *Ę ę* → 'en' (burun orqali)\n"
            "• *Ł ł* → inglizcha 'w'\n"
            "• *Ó ó* → 'u'\n"
            "• *Ź ź* → 'zh' (yumshoq)\n"
            "• *Ż ż* → 'zh' (qattiq)\n\n"
            "*Kombinatsiyalar:*\n"
            "• *sz* → 'sh'\n"
            "• *cz* → 'ch'\n"
            "• *rz* → 'zh'\n"
            "• *dz* → 'dz'\n\n"
            "⚠️ *Urg'u:* Doim oxirdan *2-bo'g'inda*"
        ),
        "vocab": [
            {"pl": "Polska",        "ph": "POL-ska",         "uz": "Polsha"},
            {"pl": "Warszawa",      "ph": "var-SHA-va",      "uz": "Varshava (poytaxt)"},
            {"pl": "Kraków",        "ph": "KRA-kuf",         "uz": "Krakov (shahar)"},
            {"pl": "Wrocław",       "ph": "VROTS-wav",       "uz": "Vroslav (shahar)"},
            {"pl": "Łódź",          "ph": "vudj",            "uz": "Lodz (shahar)"},
            {"pl": "szczery",       "ph": "SHCHE-ri",        "uz": "samimiy"},
            {"pl": "grzyb",         "ph": "gzhyb",           "uz": "qo'ziqorin"},
            {"pl": "dżem",          "ph": "dzhem",           "uz": "murabbo"},
            {"pl": "pięć",          "ph": "pyench",          "uz": "besh"},
            {"pl": "święto",        "ph": "SHVYEN-to",       "uz": "bayram"},
            {"pl": "środa",         "ph": "SHRO-da",         "uz": "chorshanba"},
            {"pl": "dźwięk",        "ph": "djvyenk",         "uz": "tovush"},
            {"pl": "rzeka",         "ph": "ZHE-ka",          "uz": "daryo"},
            {"pl": "ćwiczenie",     "ph": "chvi-CHE-nye",    "uz": "mashq"},
            {"pl": "źródło",        "ph": "ZHRUD-vo",        "uz": "manba"},
        ],
        "dialog": (
            "💬 *Dialog: Imlo*\n\n"
            "👩‍🏫 O'qituvchi: *Jak się pisze Pana imię?*\n"
            "🧑 Aziz: *A-Z-I-Z.*\n"
            "👩‍🏫 *A nazwisko?*\n"
            "🧑 *K-A-R-I-M-O-V. Karimov.*\n\n"
            "📝 *Tarjima:*\n"
            "👩‍🏫 Ismingiz qanday yoziladi?\n"
            "🧑 A-Z-I-Z.\n"
            "👩‍🏫 Familiyangiz-chi?\n"
            "🧑 K-A-R-I-M-O-V. Karimov."
        ),
        "exercises": [
            {"q": "Polyak alifbosida nechta harf bor?",
             "opts": ["26", "30", "32", "35"], "ans": 2},
            {"q": "🔤 *'Ł'* harfi qanday o'qiladi?",
             "opts": ["l", "v/u (w)", "sh", "zh"], "ans": 1},
            {"q": "🔤 *'sz'* kombinatsiyasi?",
             "opts": ["sz", "ts", "sh", "ch"], "ans": 2},
            {"q": "🔤 *'cz'* kombinatsiyasi?",
             "opts": ["ts", "ch", "sh", "dz"], "ans": 1},
            {"q": "🔤 Urg'u qaysi bo'g'inda?",
             "opts": ["Birinchi", "Oxirgi", "Oxirdan ikkinchi", "Har doim turli"], "ans": 2},
            {"q": "🔤 *'Ą'* harfi qanday o'qiladi?",
             "opts": ["a", "o", "on (burun)", "an"], "ans": 2},
            {"q": "🔤 *'W'* harfi polyakchada?",
             "opts": ["w", "v", "u", "b"], "ans": 1},
            {"q": "🔤 *'rz'* kombinatsiyasi?",
             "opts": ["r-z", "zh", "sh", "ts"], "ans": 1},
            {"q": "🔤 *'Ó'* harfi qanday o'qiladi?",
             "opts": ["o", "u", "oy", "uo"], "ans": 1},
            {"q": "🔤 *'J'* harfi polyakchada?",
             "opts": ["dj", "zh", "y", "j"], "ans": 2},
        ],
    },

    "a1_l03": {
        "title": "Sonlar 1–20",
        "emoji": "🔢",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika:*\n\n"
            "*'1' va '2' soni jins bilan o'zgaradi:*\n\n"
            "• Erkak: *jeden* / *dwa*\n"
            "• Ayol: *jedna* / *dwie*\n"
            "• Neytral: *jedno* / *dwa*\n\n"
            "*Narx so'rash:*\n"
            "❓ *Ile kosztuje?* — Qancha turadi?\n"
            "💰 *To kosztuje 5 złotych* — Bu 5 zloty turadi\n\n"
            "*Yosh aytish:*\n"
            "❓ *Ile masz lat?* — Yoshingiz necha?\n"
            "✅ *Mam 28 lat* — 28 yoshdaman"
        ),
        "vocab": [
            {"pl": "jeden / jedna",   "ph": "YE-den / YED-na",      "uz": "Bir (1)"},
            {"pl": "dwa / dwie",      "ph": "dva / dvye",            "uz": "Ikki (2)"},
            {"pl": "trzy",            "ph": "tshi",                  "uz": "Uch (3)"},
            {"pl": "cztery",          "ph": "CHTE-ri",               "uz": "To'rt (4)"},
            {"pl": "pięć",            "ph": "pyench",                "uz": "Besh (5)"},
            {"pl": "sześć",           "ph": "sheshch",               "uz": "Olti (6)"},
            {"pl": "siedem",          "ph": "SHYE-dem",              "uz": "Yetti (7)"},
            {"pl": "osiem",           "ph": "O-shem",                "uz": "Sakkiz (8)"},
            {"pl": "dziewięć",        "ph": "DJE-vyench",            "uz": "To'qqiz (9)"},
            {"pl": "dziesięć",        "ph": "DJE-shench",            "uz": "O'n (10)"},
            {"pl": "jedenaście",      "ph": "ye-de-NASH-che",        "uz": "O'n bir (11)"},
            {"pl": "dwanaście",       "ph": "dva-NASH-che",          "uz": "O'n ikki (12)"},
            {"pl": "dwadzieścia",     "ph": "dva-DJESH-cha",         "uz": "Yigirma (20)"},
            {"pl": "ile kosztuje?",   "ph": "ILE kosh-TU-ye",        "uz": "Qancha turadi?"},
            {"pl": "złoty",           "ph": "ZVO-ti",                "uz": "Zloty (pul)"},
        ],
        "dialog": (
            "💬 *Dialog: Do'konda*\n\n"
            "🧑 *Przepraszam, ile kosztuje chleb?*\n"
            "🏪 *Cztery złote pięćdziesiąt.*\n"
            "🧑 *Poproszę dwa.*\n"
            "🏪 *Proszę. Dziewięć złotych.*\n\n"
            "📝 *Tarjima:*\n"
            "🧑 Kechirasiz, non qancha?\n"
            "🏪 To'rt zloty ellik.\n"
            "🧑 Ikkita bering.\n"
            "🏪 Mana. To'qqiz zloty."
        ),
        "exercises": [
            {"q": "🔢 *'Pięć'* necha?",
             "opts": ["To'rt", "Besh", "Olti", "Yetti"], "ans": 1},
            {"q": "🔢 *7* soni polyakchada?",
             "opts": ["Sześć", "Siedem", "Osiem", "Dziewięć"], "ans": 1},
            {"q": "🔢 *'Dziesięć'* necha?",
             "opts": ["8", "9", "10", "11"], "ans": 2},
            {"q": "🔢 *4* soni polyakchada?",
             "opts": ["Trzy", "Cztery", "Pięć", "Sześć"], "ans": 1},
            {"q": "🔢 *'Osiem'* necha?",
             "opts": ["6", "7", "8", "9"], "ans": 2},
            {"q": "🔢 *1* soni polyakchada (erkak)?",
             "opts": ["Jeden", "Jedna", "Jedno", "Dwa"], "ans": 0},
            {"q": "🔢 *'Dwadzieścia'* necha?",
             "opts": ["12", "15", "20", "21"], "ans": 2},
            {"q": "❓ *'Ile kosztuje?'* nima degani?",
             "opts": ["Qancha kishi?", "Qancha turadi?", "Qancha vaqt?", "Yoshingiz?"], "ans": 1},
            {"q": "🔢 *'Trzy'* necha?",
             "opts": ["Bir", "Ikki", "Uch", "To'rt"], "ans": 2},
            {"q": "🔢 *'Jedenaście'* necha?",
             "opts": ["10", "11", "12", "13"], "ans": 1},
        ],
    },

    "a1_l04": {
        "title": "Tanishuv",
        "emoji": "🤝",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika: 'Jestem' — Men ...man*\n\n"
            "*Być (bo'lmoq) fe'li:*\n"
            "• ja → *jestem* (men)\n"
            "• ty → *jesteś* (sen)\n"
            "• on/ona → *jest* (u)\n"
            "• my → *jesteśmy* (biz)\n"
            "• oni → *są* (ular)\n\n"
            "*Ishlatilishi:*\n"
            "→ *Jestem Aziz.* — Men Azizman.\n"
            "→ *Jestem z Uzbekistanu.* — O'zbekistondan.\n"
            "→ *Jestem zmęczony.* — Charchadim. (erk.)\n"
            "→ *Nie jestem z Polski.* — Polshadan emas."
        ),
        "vocab": [
            {"pl": "Jak masz na imię?",    "ph": "yak mash na I-mye",       "uz": "Ismingiz nima?"},
            {"pl": "Mam na imię...",        "ph": "mam na I-mye",            "uz": "Mening ismim..."},
            {"pl": "Jak masz na nazwisko?", "ph": "yak mash na na-ZVIS-ko",  "uz": "Familiyangiz?"},
            {"pl": "Ile masz lat?",         "ph": "ILE mash lat",            "uz": "Yoshingiz necha?"},
            {"pl": "Mam ... lat",           "ph": "mam ... lat",             "uz": "Men ... yoshdaman"},
            {"pl": "Skąd jesteś?",          "ph": "skond YES-tesh",          "uz": "Qayerdansiz?"},
            {"pl": "Jestem z...",            "ph": "YES-tem z",               "uz": "Men ...danman"},
            {"pl": "Gdzie mieszkasz?",      "ph": "gDJE MYESH-kash",         "uz": "Qayerda yashaysiz?"},
            {"pl": "Miło mi!",              "ph": "MI-vo mi",                "uz": "Tanishganimdan xursandman!"},
            {"pl": "Uczę się polskiego",    "ph": "U-che she pol-SKI-go",    "uz": "Polyakcha o'rganayapman"},
            {"pl": "Rozumiem",              "ph": "ro-ZU-myem",              "uz": "Tushundim"},
            {"pl": "Nie rozumiem",          "ph": "nye ro-ZU-myem",          "uz": "Tushunmadim"},
            {"pl": "Staram się",            "ph": "STA-ram she",             "uz": "Harakat qilaman"},
            {"pl": "Mówię po polsku",       "ph": "MU-vye po POL-sku",       "uz": "Polyakcha bilaman"},
            {"pl": "Trochę",                "ph": "TRO-he",                  "uz": "Biroz"},
        ],
        "dialog": (
            "💬 *Dialog: Birinchi tanishish*\n\n"
            "👨 *Dzień dobry! Jestem Marek.*\n"
            "🧑 *Dzień dobry! Miło mi. Jestem Aziz.*\n"
            "👨 *Skąd Pan pochodzi?*\n"
            "🧑 *Jestem z Uzbekistanu, z Taszkentu.*\n"
            "👨 *Świetnie mówi Pan po polsku!*\n"
            "🧑 *Dziękuję, staram się.*\n\n"
            "📝 *Tarjima:*\n"
            "👨 Xayrli kun! Men Marek.\n"
            "🧑 Xayrli kun! Tanishganimdan xursandman. Aziz.\n"
            "👨 Qayerdansiniz?\n"
            "🧑 O'zbekistondan, Toshkentdan.\n"
            "👨 Polyakchani zo'r gapиrasiz!\n"
            "🧑 Rahmat, harakat qilaman."
        ),
        "exercises": [
            {"q": "🤝 *'Jak masz na imię?'* nima so'ramoqda?",
             "opts": ["Yoshingiz?", "Ismingiz?", "Qayerdansiz?", "Kasbingiz?"], "ans": 1},
            {"q": "🤝 *'Ile masz lat?'* nima so'ramoqda?",
             "opts": ["Ismingiz?", "Qayerdansiz?", "Yoshingiz?", "Telefon?"], "ans": 2},
            {"q": "🤝 *'Skąd jesteś?'* nima degani?",
             "opts": ["Qayerda yashaysiz?", "Qayerdansiz?", "Qayerga?", "Qachon?"], "ans": 1},
            {"q": "🇺🇿 *'Tushundim'* polyakchada?",
             "opts": ["Nie rozumiem", "Rozumiem", "Uczę się", "Miło mi"], "ans": 1},
            {"q": "🤝 *'Miło mi!'* nima degani?",
             "opts": ["Rahmat!", "Ko'rishguncha!", "Tanishganimdan xursandman!", "Salom!"], "ans": 2},
            {"q": "🇺🇿 *'Polyakcha o'rganayapman'* polyakchada?",
             "opts": ["Mówię po polsku", "Uczę się polskiego", "Rozumiem", "Nie mówię"], "ans": 1},
            {"q": "🤝 *'Gdzie mieszkasz?'* nima so'ramoqda?",
             "opts": ["Qayerdansiz?", "Yoshingiz?", "Qayerda yashaysiz?", "Ismingiz?"], "ans": 2},
            {"q": "🇺🇿 *'Harakat qilaman'* polyakchada?",
             "opts": ["Rozumiem", "Staram się", "Trochę", "Miło mi"], "ans": 1},
            {"q": "🤝 *'Mam na imię...'* nima degani?",
             "opts": ["Mening yoshim...", "Mening ismim...", "Mening kasbim...", "Mening uyim..."], "ans": 1},
            {"q": "🇺🇿 *'Biroz'* polyakchada?",
             "opts": ["Bardzo", "Trochę", "Dobrze", "Tak"], "ans": 1},
        ],
    },

    "a1_l05": {
        "title": "Oila",
        "emoji": "👨‍👩‍👧",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika: 'Mieć' — Ega bo'lmoq*\n\n"
            "• ja → *mam* (menda bor)\n"
            "• ty → *masz*\n"
            "• on/ona → *ma*\n"
            "• my → *mamy*\n"
            "• oni → *mają*\n\n"
            "*Inkor:* nie + fe'l\n"
            "→ *Mam brata.* — Akam bor.\n"
            "→ *Nie mam brata.* — Akam yo'q.\n\n"
            "*Tegishlilik:*\n"
            "• mój (mening - erkak)\n"
            "• moja (mening - ayol)\n"
            "• moje (mening - neytral)"
        ),
        "vocab": [
            {"pl": "rodzina",       "ph": "ro-DJI-na",    "uz": "oila"},
            {"pl": "mama / matka",  "ph": "MA-ma",         "uz": "ona"},
            {"pl": "tata / ojciec", "ph": "TA-ta",         "uz": "ota"},
            {"pl": "brat",          "ph": "brat",          "uz": "aka / uka"},
            {"pl": "siostra",       "ph": "SHOSH-tra",     "uz": "opa / singil"},
            {"pl": "mąż",           "ph": "monsh",         "uz": "er"},
            {"pl": "żona",          "ph": "ZHO-na",        "uz": "xotin"},
            {"pl": "syn",           "ph": "syn",           "uz": "o'g'il"},
            {"pl": "córka",         "ph": "TSUR-ka",       "uz": "qiz (farzand)"},
            {"pl": "dzieci",        "ph": "DJE-chi",       "uz": "bolalar"},
            {"pl": "dziadek",       "ph": "DJYA-dek",      "uz": "buva"},
            {"pl": "babcia",        "ph": "BAB-cha",       "uz": "buvi"},
            {"pl": "wujek",         "ph": "VU-yek",        "uz": "amaki / tog'a"},
            {"pl": "ciocia",        "ph": "CHO-cha",       "uz": "xola / amma"},
            {"pl": "rodzeństwo",    "ph": "ro-DJENSHТ-vo", "uz": "aka-ukalar (umumiy)"},
        ],
        "dialog": (
            "💬 *Dialog: Oila haqida*\n\n"
            "👩 *Masz rodzinę w Polsce?*\n"
            "🧑 *Nie, moja rodzina jest w Uzbekistanie.*\n"
            "   *Mam żonę i dwoje dzieci.*\n"
            "👩 *Ile mają lat twoje dzieci?*\n"
            "🧑 *Syn ma pięć lat, a córka trzy.*\n"
            "👩 *Tęsknisz za nimi?*\n"
            "🧑 *Bardzo. Dzwonię do nich codziennie.*\n\n"
            "📝 *Tarjima:*\n"
            "👩 Polshada oilangiz bormi?\n"
            "🧑 Yo'q, oilam O'zbekistonda. Xotinim va ikki bolam bor.\n"
            "👩 Bolalaringiz necha yoshda?\n"
            "🧑 O'g'lim besh, qizim uch yoshda.\n"
            "👩 Ularga sog'inasizmi?\n"
            "🧑 Juda. Har kuni qo'ng'iroq qilaman."
        ),
        "exercises": [
            {"q": "👨‍👩 *'Żona'* nima degani?",
             "opts": ["Ona", "Qiz", "Xotin", "Singil"], "ans": 2},
            {"q": "👨‍👩 *'Brat'* nima degani?",
             "opts": ["Ota", "Aka/Uka", "O'g'il", "Er"], "ans": 1},
            {"q": "👨‍👩 *'Córka'* nima degani?",
             "opts": ["Ona", "Qiz (farzand)", "Singil", "Buvi"], "ans": 1},
            {"q": "🇺🇿 *'Oila'* polyakchada?",
             "opts": ["Rodzice", "Rodzeństwo", "Rodzina", "Dom"], "ans": 2},
            {"q": "👨‍👩 *'Syn'* nima degani?",
             "opts": ["Qiz", "O'g'il", "Aka", "Ota"], "ans": 1},
            {"q": "🇺🇿 *'Bolalar'* polyakchada?",
             "opts": ["Dzieci", "Córka", "Syn", "Rodzina"], "ans": 0},
            {"q": "👨‍👩 *'Babcia'* nima degani?",
             "opts": ["Buva", "Xola", "Buvi", "Amma"], "ans": 2},
            {"q": "👨‍👩 *'Dziadek'* nima degani?",
             "opts": ["Amaki", "Buva", "Ota", "Buvi"], "ans": 1},
            {"q": "🇺🇿 *'Xotin'* polyakchada?",
             "opts": ["Mąż", "Żona", "Mama", "Siostra"], "ans": 1},
            {"q": "👨‍👩 *'Ciocia'* nima degani?",
             "opts": ["Buvi", "Singil", "Xola/Amma", "Ona"], "ans": 2},
        ],
    },

    "a1_l06": {
        "title": "Kasblar",
        "emoji": "💼",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika: Kasb aytish*\n\n"
            "Kasb aytishda *Instrumental* kelishigi:\n"
            "*Jestem + kasb (Instrumental)*\n\n"
            "• Erkak: *pracownik → pracownikiem*\n"
            "• Ayol: *pracownica → pracownicą*\n\n"
            "*Misollar:*\n"
            "→ *Jestem pracownikiem.* — Men ishchiman. (erk.)\n"
            "→ *Jestem pracownicą.* — Men ishchiman. (ay.)\n"
            "→ *On jest lekarzem.* — U shifokor.\n\n"
            "❓ *Czym się zajmujesz?*\n"
            "→ Kasbingiz nima?"
        ),
        "vocab": [
            {"pl": "pracownik",    "ph": "pra-TSOV-nik",     "uz": "ishchi"},
            {"pl": "kierowca",     "ph": "kye-ROV-tsa",      "uz": "haydovchi"},
            {"pl": "lekarz",       "ph": "LE-kazh",          "uz": "shifokor"},
            {"pl": "pielęgniarka", "ph": "pye-leng-NYAR-ka", "uz": "hamshira"},
            {"pl": "nauczyciel",   "ph": "na-u-CHI-chel",    "uz": "o'qituvchi"},
            {"pl": "kucharz",      "ph": "KU-hazh",          "uz": "oshpaz"},
            {"pl": "spawacz",      "ph": "SPA-vach",         "uz": "payvandchi"},
            {"pl": "mechanik",     "ph": "me-HA-nik",        "uz": "mexanik"},
            {"pl": "elektryk",     "ph": "e-LEK-trik",       "uz": "elektrik"},
            {"pl": "budowlaniec",  "ph": "bu-dov-LA-nyets",  "uz": "qurilishchi"},
            {"pl": "sprzedawca",   "ph": "pshe-DAV-tsa",     "uz": "sotuvchi"},
            {"pl": "hydraulik",    "ph": "hid-RAV-lik",      "uz": "santexnik"},
            {"pl": "inżynier",     "ph": "in-ZHY-ner",       "uz": "muhandis"},
            {"pl": "ochroniarz",   "ph": "oh-RO-nyazh",      "uz": "qo'riqchi"},
            {"pl": "kierownik",    "ph": "kye-ROV-nik",      "uz": "menejer / rahbar"},
        ],
        "dialog": (
            "💬 *Dialog: Ishga qabul*\n\n"
            "👔 *Czym się zajmujesz?*\n"
            "🧑 *Jestem spawaczem. Mam 10 lat doświadczenia.*\n"
            "👔 *Gdzie Pan pracował wcześniej?*\n"
            "🧑 *W Uzbekistanie, w fabryce metalu.*\n"
            "👔 *Kiedy może Pan zacząć?*\n"
            "🧑 *Od przyszłego tygodnia.*\n\n"
            "📝 *Tarjima:*\n"
            "👔 Kasbingiz nima?\n"
            "🧑 Men payvandchiman. 10 yillik tajribam bor.\n"
            "👔 Avval qaerda ishlagan edingiz?\n"
            "🧑 O'zbekistonda, metall fabrikasida.\n"
            "👔 Qachon boshlay olasiz?\n"
            "🧑 Kelasi haftadan."
        ),
        "exercises": [
            {"q": "💼 *'Lekarz'* nima kasb?",
             "opts": ["Oshpaz", "Shifokor", "O'qituvchi", "Mexanik"], "ans": 1},
            {"q": "💼 *'Spawacz'* nima kasb?",
             "opts": ["Elektrik", "Santexnik", "Payvandchi", "Haydovchi"], "ans": 2},
            {"q": "🇺🇿 *'Haydovchi'* polyakchada?",
             "opts": ["Pracownik", "Kierowca", "Mechanik", "Elektryk"], "ans": 1},
            {"q": "💼 *'Nauczyciel'* nima kasb?",
             "opts": ["Shifokor", "Oshpaz", "O'qituvchi", "Sotuvchi"], "ans": 2},
            {"q": "🇺🇿 *'Mexanik'* polyakchada?",
             "opts": ["Elektryk", "Mechanik", "Spawacz", "Hydraulik"], "ans": 1},
            {"q": "💼 *'Kucharz'* nima kasb?",
             "opts": ["Qurilishchi", "Haydovchi", "Oshpaz", "Ishchi"], "ans": 2},
            {"q": "💼 *'Elektryk'* nima kasb?",
             "opts": ["Santexnik", "Mexanik", "Elektrik", "Payvandchi"], "ans": 2},
            {"q": "🇺🇿 *'Muhandis'* polyakchada?",
             "opts": ["Pracownik", "Inżynier", "Student", "Nauczyciel"], "ans": 1},
            {"q": "💼 *'Hydraulik'* nima kasb?",
             "opts": ["Elektrik", "Santexnik", "Qurilishchi", "Oshpaz"], "ans": 1},
            {"q": "❓ *'Czym się zajmujesz?'* nima so'ramoqda?",
             "opts": ["Qayerdansiz?", "Yoshingiz?", "Kasbingiz nima?", "Ismingiz?"], "ans": 2},
        ],
    },

    "a1_l07": {
        "title": "Ishda Muloqot",
        "emoji": "🏭",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika: Locative — Qayerda?*\n\n"
            "*'w' + Lokativ* = ...da\n\n"
            "• dom → *w domu* (uyda)\n"
            "• praca → *w pracy* (ishda)\n"
            "• fabryka → *w fabryce* (fabrikada)\n"
            "• sklep → *w sklepie* (do'konda)\n\n"
            "*Misol:*\n"
            "→ *Pracuję w fabryce.* — Fabrikada ishlayman.\n"
            "→ *Jestem w domu.* — Uyda(man).\n\n"
            "⚠️ *'na'* ham ishlatiladi:\n"
            "→ *na budowie* (qurilishda)\n"
            "→ *na zmianie* (smеnada)"
        ),
        "vocab": [
            {"pl": "praca",               "ph": "PRA-tsa",              "uz": "ish"},
            {"pl": "szef",                "ph": "shef",                 "uz": "boshliq"},
            {"pl": "zmiana",              "ph": "ZMYA-na",              "uz": "smena"},
            {"pl": "przerwa",             "ph": "PZHER-va",             "uz": "tanaffus"},
            {"pl": "wynagrodzenie",       "ph": "vy-na-gro-DZE-nye",   "uz": "ish haqi"},
            {"pl": "umowa o pracę",       "ph": "u-MO-va o PRA-tse",   "uz": "ish shartnomasi"},
            {"pl": "fabryka",             "ph": "FAB-ry-ka",            "uz": "fabrika"},
            {"pl": "magazyn",             "ph": "ma-GA-zyn",            "uz": "ombor"},
            {"pl": "urlop",               "ph": "UR-lop",               "uz": "ta'til"},
            {"pl": "nadgodziny",          "ph": "nad-go-DZI-ni",        "uz": "qo'shimcha soatlar"},
            {"pl": "pracuję w...",        "ph": "pra-TSU-ye v",         "uz": "...da ishlayman"},
            {"pl": "kiedy jest przerwa?", "ph": "KYE-di yest PZHER-va","uz": "tanaffus qachon?"},
            {"pl": "mam pytanie",         "ph": "mam py-TA-nye",        "uz": "savolim bor"},
            {"pl": "zepsuty",             "ph": "zep-SU-ti",            "uz": "buzilgan"},
            {"pl": "pomoc",               "ph": "PO-mots",              "uz": "yordam"},
        ],
        "dialog": (
            "💬 *Dialog: Birinchi kun*\n\n"
            "👷 *Dzień dobry. Pan jest nowym pracownikiem?*\n"
            "🧑 *Tak, jestem Aziz. Pierwszy dzień w pracy.*\n"
            "👷 *Zmiana zaczyna się o szóstej.*\n"
            "   *Przerwa jest o dziesiątej, trzydzieści minut.*\n"
            "🧑 *Rozumiem. A kiedy jest wypłata?*\n"
            "👷 *Piętnastego każdego miesiąca.*\n\n"
            "📝 *Tarjima:*\n"
            "👷 Xayrli kun. Siz yangi ishchimisiz?\n"
            "🧑 Ha, men Aziz. Birinchi kun.\n"
            "👷 Smena soat oltida boshlanadi. Tanaffus o'nda, 30 daqiqa.\n"
            "🧑 Tushundim. Maosh qachon?\n"
            "👷 Har oyning 15-sida."
        ),
        "exercises": [
            {"q": "🏭 *'Zmiana'* nima degani?",
             "opts": ["Ta'til", "Smena", "Tanaffus", "Ish haqi"], "ans": 1},
            {"q": "🏭 *'Szef'* nima degani?",
             "opts": ["Ishchi", "Hamkasb", "Boshliq", "Kasb"], "ans": 2},
            {"q": "🇺🇿 *'Tanaffus'* polyakchada?",
             "opts": ["Urlop", "Zmiana", "Przerwa", "Praca"], "ans": 2},
            {"q": "🏭 *'Wynagrodzenie'* nima degani?",
             "opts": ["Shartnoma", "Ish haqi", "Smena", "Ta'til"], "ans": 1},
            {"q": "🇺🇿 *'Ta'til'* polyakchada?",
             "opts": ["Przerwa", "Zmiana", "Urlop", "Praca"], "ans": 2},
            {"q": "🏭 *'Umowa o pracę'* nima degani?",
             "opts": ["Ish", "Fabrika", "Ish shartnomasi", "Ombor"], "ans": 2},
            {"q": "🏭 *'Nadgodziny'* nima degani?",
             "opts": ["Qo'shimcha soatlar", "Ta'til", "Maosh", "Ish joyi"], "ans": 0},
            {"q": "🇺🇿 *'Savolim bor'* polyakchada?",
             "opts": ["Mam urlop", "Mam pytanie", "Mam pracę", "Mam umowę"], "ans": 1},
            {"q": "🏭 *'Zepsuty'* nima degani?",
             "opts": ["Yangi", "Buzilgan", "Yaxshi", "Katta"], "ans": 1},
            {"q": "🇺🇿 *'Fabrikada ishlayman'* polyakchada?",
             "opts": ["Pracuję w biurze", "Pracuję w fabryce", "Pracuję w sklepie", "Pracuję w domu"], "ans": 1},
        ],
    },

    "a1_l08": {
        "title": "Ranglar va Sifatlar",
        "emoji": "🎨",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika: Sifatlar*\n\n"
            "Sifatlar *otning jinsi bilan kelishadi:*\n\n"
            "• Erkak: *duży* (katta)\n"
            "• Ayol: *duża* (katta)\n"
            "• Neytral: *duże* (katta)\n\n"
            "*Asosiy sifatlar:*\n"
            "• *duży/a/e* — katta\n"
            "• *mały/a/e* — kichik\n"
            "• *dobry/a/e* — yaxshi\n"
            "• *zły/a/e* — yomon\n"
            "• *nowy/a/e* — yangi\n"
            "• *stary/a/e* — eski\n"
            "• *piękny/a/e* — go'zal"
        ),
        "vocab": [
            {"pl": "czerwony",      "ph": "che-RVO-ni",      "uz": "qizil"},
            {"pl": "niebieski",     "ph": "nye-BYES-ki",     "uz": "ko'k"},
            {"pl": "zielony",       "ph": "zye-LO-ni",       "uz": "yashil"},
            {"pl": "żółty",         "ph": "ZHUL-ti",         "uz": "sariq"},
            {"pl": "biały",         "ph": "BYA-vi",          "uz": "oq"},
            {"pl": "czarny",        "ph": "CHAR-ni",         "uz": "qora"},
            {"pl": "szary",         "ph": "SHA-ri",          "uz": "kulrang"},
            {"pl": "brązowy",       "ph": "bron-ZO-vi",      "uz": "jigarrang"},
            {"pl": "różowy",        "ph": "ru-ZHO-vi",       "uz": "pushti"},
            {"pl": "pomarańczowy",  "ph": "po-ma-RANCH-o-vi","uz": "to'q sariq"},
            {"pl": "duży",          "ph": "DU-zhi",          "uz": "katta"},
            {"pl": "mały",          "ph": "MA-vi",           "uz": "kichik"},
            {"pl": "dobry",         "ph": "DOB-ri",          "uz": "yaxshi"},
            {"pl": "piękny",        "ph": "PYEN-kni",        "uz": "go'zal"},
            {"pl": "nowy",          "ph": "NO-vi",           "uz": "yangi"},
        ],
        "dialog": (
            "💬 *Dialog: Kiyim do'konida*\n\n"
            "🛍️ *Słucham?*\n"
            "🧑 *Poproszę tę niebieską koszulę.*\n"
            "🛍️ *Jaki rozmiar?*\n"
            "🧑 *Rozmiar L, proszę.*\n"
            "🛍️ *Proszę bardzo.*\n"
            "🧑 *Ile kosztuje?*\n"
            "🛍️ *Pięćdziesiąt złotych.*\n\n"
            "📝 *Tarjima:*\n"
            "🛍️ Eshitaman?\n"
            "🧑 Ko'k ko'ylakni bering.\n"
            "🛍️ Qaysi o'lcham?\n"
            "🧑 L o'lcham, iltimos.\n"
            "🛍️ Marhamat.\n"
            "🧑 Qancha turadi?\n"
            "🛍️ Ellik zloty."
        ),
        "exercises": [
            {"q": "🎨 *'Czerwony'* nima degani?",
             "opts": ["Ko'k", "Qizil", "Yashil", "Sariq"], "ans": 1},
            {"q": "🎨 *'Niebieski'* nima degani?",
             "opts": ["Ko'k", "Qizil", "Yashil", "Sariq"], "ans": 0},
            {"q": "🇺🇿 *'Yashil'* polyakchada?",
             "opts": ["Żółty", "Zielony", "Szary", "Różowy"], "ans": 1},
            {"q": "🎨 *'Biały'* nima degani?",
             "opts": ["Qora", "Oq", "Kulrang", "Pushti"], "ans": 1},
            {"q": "🇺🇿 *'Qora'* polyakchada?",
             "opts": ["Biały", "Szary", "Czarny", "Brązowy"], "ans": 2},
            {"q": "🎨 *'Duży'* nima degani?",
             "opts": ["Kichik", "Yaxshi", "Katta", "Yangi"], "ans": 2},
            {"q": "🎨 *'Piękny'* nima degani?",
             "opts": ["Yomon", "Kichik", "Eski", "Go'zal"], "ans": 3},
            {"q": "🇺🇿 *'Sariq'* polyakchada?",
             "opts": ["Różowy", "Żółty", "Szary", "Zielony"], "ans": 1},
            {"q": "🎨 *'Nowy'* nima degani?",
             "opts": ["Eski", "Yangi", "Katta", "Kichik"], "ans": 1},
            {"q": "🇺🇿 *'Jigarrang'* polyakchada?",
             "opts": ["Różowy", "Szary", "Brązowy", "Pomarańczowy"], "ans": 2},
        ],
    },

    "a1_l09": {
        "title": "Hafta Kunlari va Oylar",
        "emoji": "📅",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika: Vaqt iboralari*\n\n"
            "*Qachon?* — Kiedy?\n\n"
            "• *w poniedziałek* — dushanbada\n"
            "• *we wtorek* — sesshanbada\n"
            "• *w środę* — chorshanbada\n"
            "• *w czwartek* — payshanbada\n"
            "• *w piątek* — jumada\n"
            "• *w sobotę* — shanbada\n"
            "• *w niedzielę* — yakshanbada\n\n"
            "⚠️ *Muhim:* Polyakchada hafta *dushanbadan* boshlanadi!\n\n"
            "📅 *Oy:*\n"
            "• *w styczniu* — yanvarda\n"
            "• *w maju* — mayda"
        ),
        "vocab": [
            {"pl": "poniedziałek", "ph": "po-nye-DJYA-lek",  "uz": "dushanba"},
            {"pl": "wtorek",       "ph": "VTO-rek",           "uz": "seshanba"},
            {"pl": "środa",        "ph": "SHRO-da",           "uz": "chorshanba"},
            {"pl": "czwartek",     "ph": "CHVAR-tek",         "uz": "payshanba"},
            {"pl": "piątek",       "ph": "PYON-tek",          "uz": "juma"},
            {"pl": "sobota",       "ph": "so-BO-ta",          "uz": "shanba"},
            {"pl": "niedziela",    "ph": "nye-DJYE-la",       "uz": "yakshanba"},
            {"pl": "styczeń",      "ph": "STI-chen",          "uz": "yanvar"},
            {"pl": "luty",         "ph": "LU-ti",             "uz": "fevral"},
            {"pl": "marzec",       "ph": "MA-zhets",          "uz": "mart"},
            {"pl": "kwiecień",     "ph": "KVYE-chen",         "uz": "aprel"},
            {"pl": "maj",          "ph": "may",               "uz": "may"},
            {"pl": "czerwiec",     "ph": "CHER-vyets",        "uz": "iyun"},
            {"pl": "weekend",      "ph": "WI-kend",           "uz": "dam olish kunlari"},
            {"pl": "święto",       "ph": "SHVYEN-to",         "uz": "bayram kuni"},
        ],
        "dialog": (
            "💬 *Dialog: Ish jadvali*\n\n"
            "👔 *Kiedy Pan pracuje?*\n"
            "🧑 *Pracuję od poniedziałku do piątku.*\n"
            "👔 *A w sobotę?*\n"
            "🧑 *Czasem pracuję też w sobotę.*\n"
            "👔 *Kiedy ma Pan urlop?*\n"
            "🧑 *W lipcu, przez dwa tygodnie.*\n\n"
            "📝 *Tarjima:*\n"
            "👔 Qachon ishlaysiz?\n"
            "🧑 Dushanbadan jumagacha ishlayman.\n"
            "👔 Shanbada-chi?\n"
            "🧑 Ba'zan shanbada ham ishlayman.\n"
            "👔 Ta'tilingiz qachon?\n"
            "🧑 Iyulda, ikki hafta."
        ),
        "exercises": [
            {"q": "📅 *'Poniedziałek'* nima degani?",
             "opts": ["Seshanba", "Dushanba", "Chorshanba", "Payshanba"], "ans": 1},
            {"q": "📅 *'Piątek'* nima degani?",
             "opts": ["Shanba", "Yakshanba", "Juma", "Payshanba"], "ans": 2},
            {"q": "🇺🇿 *'Chorshanba'* polyakchada?",
             "opts": ["Wtorek", "Środa", "Czwartek", "Piątek"], "ans": 1},
            {"q": "📅 *'Sobota'* nima degani?",
             "opts": ["Juma", "Shanba", "Yakshanba", "Dushanba"], "ans": 1},
            {"q": "📅 *'Styczeń'* qaysi oy?",
             "opts": ["Fevral", "Mart", "Yanvar", "Aprel"], "ans": 2},
            {"q": "🇺🇿 *'Iyun'* polyakchada?",
             "opts": ["Maj", "Czerwiec", "Lipiec", "Sierpień"], "ans": 1},
            {"q": "📅 *'Niedziela'* nima degani?",
             "opts": ["Shanba", "Juma", "Yakshanba", "Dushanba"], "ans": 2},
            {"q": "📅 *'Marzec'* qaysi oy?",
             "opts": ["Yanvar", "Fevral", "Mart", "Aprel"], "ans": 2},
            {"q": "🇺🇿 *'Payshanba'* polyakchada?",
             "opts": ["Środa", "Czwartek", "Piątek", "Sobota"], "ans": 1},
            {"q": "📅 *'Weekend'* nima degani?",
             "opts": ["Bayram kuni", "Ish kuni", "Dam olish kunlari", "Ta'til"], "ans": 2},
        ],
    },

    "a1_l10": {
        "title": "Soat va Vaqt",
        "emoji": "🕐",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika: Soat aytish*\n\n"
            "❓ *Która godzina?* — Soat necha?\n\n"
            "*Soatlar:*\n"
            "• 1:00 → *pierwsza*\n"
            "• 2:00 → *druga*\n"
            "• 8:00 → *ósma*\n"
            "• 12:00 → *dwunasta*\n\n"
            "*Qo'shimchalar:*\n"
            "• 8:15 → *ósma piętnaście*\n"
            "• 8:30 → *wpół do dziewiątej* (to'qqizga yarim)\n"
            "• 8:45 → *kwadrans do dziewiątej* (to'qqizga chorak)\n\n"
            "• *rano* — ertalab\n"
            "• *wieczorem* — kechqurun\n"
            "• *w nocy* — kechasi"
        ),
        "vocab": [
            {"pl": "Która godzina?",  "ph": "KTU-ra go-DZI-na",    "uz": "Soat necha?"},
            {"pl": "Jest godzina...", "ph": "yest go-DZI-na",       "uz": "Soat ..."},
            {"pl": "rano",            "ph": "RA-no",                "uz": "ertalab"},
            {"pl": "południe",        "ph": "po-VUD-nye",           "uz": "tush"},
            {"pl": "popołudnie",      "ph": "po-po-VUD-nye",        "uz": "tushdan keyin"},
            {"pl": "wieczór",         "ph": "VYE-chur",             "uz": "kechqurun"},
            {"pl": "noc",             "ph": "nots",                 "uz": "tun"},
            {"pl": "dziś / dzisiaj",  "ph": "djish / DJI-shay",    "uz": "bugun"},
            {"pl": "jutro",           "ph": "YUT-ro",               "uz": "ertaga"},
            {"pl": "wczoraj",         "ph": "VCHO-ray",             "uz": "kecha"},
            {"pl": "teraz",           "ph": "TE-raz",               "uz": "hozir"},
            {"pl": "za chwilę",       "ph": "za KHVI-le",           "uz": "bir ozdan keyin"},
            {"pl": "punktualnie",     "ph": "punk-tu-AL-nye",       "uz": "aniq vaqtida"},
            {"pl": "za późno",        "ph": "za PUZH-no",           "uz": "kech"},
            {"pl": "za wcześnie",     "ph": "za VCHESH-nye",        "uz": "erta"},
        ],
        "dialog": (
            "💬 *Dialog: Smena vaqti*\n\n"
            "🧑 *Która godzina zaczyna się zmiana?*\n"
            "👷 *Zmiana zaczyna się o ósmej rano.*\n"
            "🧑 *A kiedy kończy się?*\n"
            "👷 *O szesnastej. Przerwa jest o dwunastej.*\n"
            "🧑 *Która jest teraz godzina?*\n"
            "👷 *Siedem pięćdziesiąt pięć.*\n"
            "🧑 *To prawie ósma! Idę!*\n\n"
            "📝 *Tarjima:*\n"
            "🧑 Smena soat nechada boshlanadi?\n"
            "👷 Smena ertalab soat sakkizda.\n"
            "🧑 Qachon tugaydi?\n"
            "👷 O'n oltida. Tanaffus o'n ikkida.\n"
            "🧑 Hozir soat necha?\n"
            "👷 Yetti ellik besh.\n"
            "🧑 Deyarli sakkiz! Ketdim!"
        ),
        "exercises": [
            {"q": "🕐 *'Która godzina?'* nima degani?",
             "opts": ["Qachon?", "Soat necha?", "Qancha vaqt?", "Hozir?"], "ans": 1},
            {"q": "🕐 *'Rano'* nima degani?",
             "opts": ["Kechqurun", "Ertalab", "Tush", "Kecha"], "ans": 1},
            {"q": "🇺🇿 *'Kechqurun'* polyakchada?",
             "opts": ["Rano", "Południe", "Wieczór", "Noc"], "ans": 2},
            {"q": "🕐 *'Dziś'* nima degani?",
             "opts": ["Kecha", "Ertaga", "Bugun", "Hozir"], "ans": 2},
            {"q": "🕐 *'Jutro'* nima degani?",
             "opts": ["Bugun", "Ertaga", "Kecha", "Hozir"], "ans": 1},
            {"q": "🇺🇿 *'Kecha'* polyakchada?",
             "opts": ["Jutro", "Dziś", "Wczoraj", "Teraz"], "ans": 2},
            {"q": "🕐 *'Teraz'* nima degani?",
             "opts": ["Hozir", "Keyin", "Avval", "Doim"], "ans": 0},
            {"q": "🕐 *'Południe'* nima degani?",
             "opts": ["Ertalab", "Tush", "Kechqurun", "Kecha"], "ans": 1},
            {"q": "🕐 *'Za późno'* nima degani?",
             "opts": ["Erta", "Vaqtida", "Kech", "Tez"], "ans": 2},
            {"q": "🇺🇿 *'Hozir'* polyakchada?",
             "opts": ["Jutro", "Teraz", "Wczoraj", "Zawsze"], "ans": 1},
        ],
    },

    "a1_l11": {
        "title": "Ovqat va Ichimliklar",
        "emoji": "🍽️",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika: 'Poproszę' — Buyurtma*\n\n"
            "*Poproszę + narsa* = '...ni bering'\n\n"
            "→ *Poproszę chleb.* — Non bering.\n"
            "→ *Poproszę dwie kawy.* — Ikki qahva.\n"
            "→ *Poproszę rachunek.* — Hisob bering.\n\n"
            "*Restoranda iboralar:*\n"
            "• *Smacznego!* — Yaxshi ishtaha!\n"
            "• *Na zdrowie!* — Sog'ligingizga!\n"
            "• *Co Pan/Pani zamawia?* — Nima buyurtma?\n"
            "• *Do picia?* — Ichimlik?\n\n"
            "⚠️ *Lubię + ovqat* = yaxshi ko'raman\n"
            "→ *Lubię kawę.* — Qahvani yaxshi ko'raman."
        ),
        "vocab": [
            {"pl": "chleb",         "ph": "hleb",            "uz": "non"},
            {"pl": "mleko",         "ph": "MLE-ko",          "uz": "sut"},
            {"pl": "jajko",         "ph": "YAY-ko",          "uz": "tuxum"},
            {"pl": "mięso",         "ph": "MYE-nso",         "uz": "go'sht"},
            {"pl": "kurczak",       "ph": "KUR-chak",        "uz": "tovuq"},
            {"pl": "ryba",          "ph": "RY-ba",           "uz": "baliq"},
            {"pl": "ziemniak",      "ph": "ZHEM-nyak",       "uz": "kartoshka"},
            {"pl": "zupa",          "ph": "ZU-pa",           "uz": "sho'rva"},
            {"pl": "herbata",       "ph": "her-BA-ta",       "uz": "choy"},
            {"pl": "kawa",          "ph": "KA-va",           "uz": "qahva"},
            {"pl": "woda",          "ph": "VO-da",           "uz": "suv"},
            {"pl": "sok",           "ph": "sok",             "uz": "sharbat"},
            {"pl": "piwo",          "ph": "PYI-vo",          "uz": "pivo"},
            {"pl": "rachunek",      "ph": "ra-HU-nek",       "uz": "hisob"},
            {"pl": "kelner",        "ph": "KEL-ner",         "uz": "ofitsiant"},
        ],
        "dialog": (
            "💬 *Dialog: Restoranda*\n\n"
            "🍽️ *Co Pan zamawia?*\n"
            "🧑 *Poproszę rosół i schabowego.*\n"
            "🍽️ *Do picia?*\n"
            "🧑 *Poproszę wodę mineralną.*\n"
            "🍽️ *Proszę bardzo. Smacznego!*\n"
            "🧑 *Dziękuję. Poproszę rachunek.*\n"
            "🍽️ *Sto złotych proszę.*\n\n"
            "📝 *Tarjima:*\n"
            "🍽️ Nima buyurtma qilasiz?\n"
            "🧑 Sho'rva va kotlet bering.\n"
            "🍽️ Ichimlik?\n"
            "🧑 Mineral suv bering.\n"
            "🍽️ Marhamat. Yaxshi ishtaha!\n"
            "🧑 Rahmat. Hisob bering.\n"
            "🍽️ Yuz zloty."
        ),
        "exercises": [
            {"q": "🍽️ *'Chleb'* nima degani?",
             "opts": ["Sut", "Non", "Tuxum", "Go'sht"], "ans": 1},
            {"q": "🍽️ *'Woda'* nima degani?",
             "opts": ["Choy", "Suv", "Sut", "Sharbat"], "ans": 1},
            {"q": "🇺🇿 *'Choy'* polyakchada?",
             "opts": ["Kawa", "Woda", "Herbata", "Sok"], "ans": 2},
            {"q": "🍽️ *'Mięso'* nima degani?",
             "opts": ["Baliq", "Tuxum", "Go'sht", "Non"], "ans": 2},
            {"q": "🍽️ *'Rachunek'* nima degani?",
             "opts": ["Menyu", "Hisob", "Narx", "Chipta"], "ans": 1},
            {"q": "🇺🇿 *'Sho'rva'* polyakchada?",
             "opts": ["Zupa", "Rosół", "Ryba", "Kurczak"], "ans": 0},
            {"q": "🍽️ *'Smacznego!'* nima degani?",
             "opts": ["Sog'ligingizga!", "Rahmat!", "Yaxshi ishtaha!", "Marhamat!"], "ans": 2},
            {"q": "🇺🇿 *'Baliq'* polyakchada?",
             "opts": ["Kurczak", "Ryba", "Mięso", "Jajko"], "ans": 1},
            {"q": "🍽️ *'Kelner'* nima degani?",
             "opts": ["Oshpaz", "Ofitsiant", "Kassir", "Rahbar"], "ans": 1},
            {"q": "🇺🇿 *'Kartoshka'* polyakchada?",
             "opts": ["Pomidor", "Cebula", "Ziemniak", "Marchewka"], "ans": 2},
        ],
    },

    "a1_l12": {
        "title": "Transport",
        "emoji": "🚌",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika: Transport bilan borish*\n\n"
            "*Iść* = piyoda borish\n"
            "*Jechać* = transport bilan borish\n\n"
            "→ *Idę do sklepu.* — Do'konga piyoda boraman.\n"
            "→ *Jadę autobusem.* — Avtobus bilan boraman.\n\n"
            "*Transport + Instrumental:*\n"
            "• *autobusem* — avtobus bilan\n"
            "• *tramwajem* — tramvay bilan\n"
            "• *taksówką* — taksi bilan\n"
            "• *pociągiem* — poyezd bilan\n\n"
            "*Do (ga):*\n"
            "→ *Jadę do Warszawy.* — Varshavaga boraman.\n"
            "→ *Idę do pracy.* — Ishga boraman."
        ),
        "vocab": [
            {"pl": "autobus",       "ph": "av-TO-bus",       "uz": "avtobus"},
            {"pl": "tramwaj",       "ph": "TRAM-vay",        "uz": "tramvay"},
            {"pl": "metro",         "ph": "ME-tro",          "uz": "metro"},
            {"pl": "pociąg",        "ph": "PO-chong",        "uz": "poyezd"},
            {"pl": "taksówka",      "ph": "tak-SUV-ka",      "uz": "taksi"},
            {"pl": "samochód",      "ph": "sa-MO-hud",       "uz": "mashina"},
            {"pl": "rower",         "ph": "RO-ver",          "uz": "velosiped"},
            {"pl": "samolot",       "ph": "sa-MO-lot",       "uz": "samolyot"},
            {"pl": "bilet",         "ph": "BI-let",          "uz": "chipta"},
            {"pl": "przystanek",    "ph": "pshis-TA-nek",    "uz": "bekat"},
            {"pl": "dworzec",       "ph": "DVO-zhets",       "uz": "vokzal"},
            {"pl": "lotnisko",      "ph": "lot-NIS-ko",      "uz": "aeroport"},
            {"pl": "rozkład jazdy", "ph": "ROZ-kvad YAZ-di", "uz": "jadval"},
            {"pl": "opóźnienie",    "ph": "o-puzh-NYE-nye",  "uz": "kechikish"},
            {"pl": "peron",         "ph": "PE-ron",          "uz": "peron"},
        ],
        "dialog": (
            "💬 *Dialog: Kassada chipta olish*\n\n"
            "🧑 *Poproszę bilet do Krakowa.*\n"
            "🎫 *W jedną stronę czy powrotny?*\n"
            "🧑 *Powrotny, proszę.*\n"
            "🎫 *Na kiedy?*\n"
            "🧑 *Na jutro rano.*\n"
            "🎫 *Jest pociąg o 6:42. To będzie 80 złotych.*\n"
            "🧑 *Dobrze, poproszę.*\n\n"
            "📝 *Tarjima:*\n"
            "🧑 Krakovga chipta bering.\n"
            "🎫 Bir tomonga yoki qaytish bilan?\n"
            "🧑 Qaytish bilan.\n"
            "🎫 Qachonga?\n"
            "🧑 Ertaga ertalab.\n"
            "🎫 6:42 da poyezd bor. 80 zloty.\n"
            "🧑 Mayli, bering."
        ),
        "exercises": [
            {"q": "🚌 *'Autobus'* nima degani?",
             "opts": ["Tramvay", "Avtobus", "Metro", "Taksi"], "ans": 1},
            {"q": "🚌 *'Bilet'* nima degani?",
             "opts": ["Chipta", "Jadval", "Bekat", "Peron"], "ans": 0},
            {"q": "🇺🇿 *'Taksi'* polyakchada?",
             "opts": ["Tramwaj", "Autobus", "Taksówka", "Metro"], "ans": 2},
            {"q": "🚌 *'Dworzec'* nima degani?",
             "opts": ["Aeroport", "Vokzal", "Metro", "Do'kon"], "ans": 1},
            {"q": "🚌 *'Lotnisko'* nima degani?",
             "opts": ["Vokzal", "Aeroport", "Bekat", "Shahar"], "ans": 1},
            {"q": "🇺🇿 *'Poyezd'* polyakchada?",
             "opts": ["Tramwaj", "Autobus", "Pociąg", "Samolot"], "ans": 2},
            {"q": "🚌 *'Opóźnienie'* nima degani?",
             "opts": ["Jadval", "Kechikish", "Chipta", "Bekat"], "ans": 1},
            {"q": "🇺🇿 *'Samolyot'* polyakchada?",
             "opts": ["Samochód", "Samolot", "Statek", "Rower"], "ans": 1},
            {"q": "🚌 *'Przystanek'* nima degani?",
             "opts": ["Vokzal", "Peron", "Bekat", "Aeroport"], "ans": 2},
            {"q": "🇺🇿 *'Velosiped'* polyakchada?",
             "opts": ["Samochód", "Motocykl", "Rower", "Taksówka"], "ans": 2},
        ],
    },

    "a1_l13": {
        "title": "Yo'l So'rash",
        "emoji": "🗺️",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika: Yo'nalish so'zlari*\n\n"
            "*Qaerda? — Gdzie?*\n"
            "• *prosto* — to'g'ri\n"
            "• *w lewo* — chapga\n"
            "• *w prawo* — o'ngga\n"
            "• *przy skrzyżowaniu* — chorrahada\n"
            "• *na rogu* — burchakda\n"
            "• *naprzeciwko* — qarshisida\n"
            "• *obok* — yonida\n"
            "• *przed* — oldida\n"
            "• *za* — orqasida\n\n"
            "*Yo'l so'rash:*\n"
            "❓ *Przepraszam, gdzie jest...?*\n"
            "→ Kechirasiz, ... qayerda?"
        ),
        "vocab": [
            {"pl": "prosto",           "ph": "PROS-to",           "uz": "to'g'ri"},
            {"pl": "w lewo",           "ph": "v LE-vo",           "uz": "chapga"},
            {"pl": "w prawo",          "ph": "v PRA-vo",          "uz": "o'ngga"},
            {"pl": "przy skrzyżowaniu","ph": "pshi skshi-ZHO-va-nyu","uz": "chorrahada"},
            {"pl": "na rogu",          "ph": "na RO-gu",          "uz": "burchakda"},
            {"pl": "naprzeciwko",      "ph": "na-pshe-CHIV-ko",   "uz": "qarshisida"},
            {"pl": "obok",             "ph": "O-bok",             "uz": "yonida"},
            {"pl": "niedaleko",        "ph": "nye-da-LE-ko",      "uz": "yaqin"},
            {"pl": "daleko",           "ph": "da-LE-ko",          "uz": "uzoq"},
            {"pl": "ulica",            "ph": "U-li-tsa",          "uz": "ko'cha"},
            {"pl": "skrzyżowanie",     "ph": "skshi-ZHO-va-nye",  "uz": "chorraxa"},
            {"pl": "most",             "ph": "most",              "uz": "ko'prik"},
            {"pl": "park",             "ph": "park",              "uz": "park"},
            {"pl": "apteka",           "ph": "ap-TE-ka",          "uz": "dorixona"},
            {"pl": "szpital",          "ph": "SHPI-tal",          "uz": "kasalxona"},
        ],
        "dialog": (
            "💬 *Dialog: Ko'chada yo'l so'rash*\n\n"
            "🧑 *Przepraszam, gdzie jest apteka?*\n"
            "👴 *Apteka jest niedaleko. Proszę iść prosto,*\n"
            "   *potem w lewo przy skrzyżowaniu.*\n"
            "🧑 *Daleko stąd?*\n"
            "👴 *Nie, jakieś pięć minut piechotą.*\n"
            "🧑 *Dziękuję bardzo!*\n"
            "👴 *Nie ma za co.*\n\n"
            "📝 *Tarjima:*\n"
            "🧑 Kechirasiz, dorixona qayerda?\n"
            "👴 Dorixona yaqin. To'g'ri boring, keyin chorrahada chapga.\n"
            "🧑 Bu yerdan uzoqmi?\n"
            "👴 Yo'q, taxminan 5 daqiqa piyoda.\n"
            "🧑 Katta rahmat!\n"
            "👴 Arzimaydi."
        ),
        "exercises": [
            {"q": "🗺️ *'Prosto'* nima degani?",
             "opts": ["Chapga", "O'ngga", "To'g'ri", "Orqaga"], "ans": 2},
            {"q": "🗺️ *'W lewo'* nima degani?",
             "opts": ["Chapga", "O'ngga", "To'g'ri", "Yonida"], "ans": 0},
            {"q": "🇺🇿 *'O'ngga'* polyakchada?",
             "opts": ["W lewo", "W prawo", "Prosto", "Za"], "ans": 1},
            {"q": "🗺️ *'Niedaleko'* nima degani?",
             "opts": ["Uzoq", "Yaqin", "Qarshisida", "Yonida"], "ans": 1},
            {"q": "🗺️ *'Obok'* nima degani?",
             "opts": ["Oldida", "Orqasida", "Yonida", "Ustida"], "ans": 2},
            {"q": "🇺🇿 *'Chorraxa'* polyakchada?",
             "opts": ["Ulica", "Skrzyżowanie", "Most", "Park"], "ans": 1},
            {"q": "🗺️ *'Apteka'* nima degani?",
             "opts": ["Kasalxona", "Dorixona", "Maktab", "Bank"], "ans": 1},
            {"q": "🗺️ *'Naprzeciwko'* nima degani?",
             "opts": ["Yonida", "Qarshisida", "Oldida", "Orqasida"], "ans": 1},
            {"q": "🗺️ *'Szpital'* nima degani?",
             "opts": ["Maktab", "Bank", "Kasalxona", "Do'kon"], "ans": 2},
            {"q": "🇺🇿 *'Ko'prik'* polyakchada?",
             "opts": ["Park", "Ulica", "Most", "Skrzyżowanie"], "ans": 2},
        ],
    },

    "a1_l14": {
        "title": "Do'konda Xarid",
        "emoji": "🛒",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika: Do'konda muloqot*\n\n"
            "*Savol:* Ile kosztuje? (Qancha?)\n"
            "*Javob:* To kosztuje... złotych\n\n"
            "*To'lash:*\n"
            "• *Płacę kartą.* — Karta bilan to'layman.\n"
            "• *Płacę gotówką.* — Naqd to'layman.\n\n"
            "*Foydali iboralar:*\n"
            "• *Poproszę to.* — Shuni bering.\n"
            "• *Nie wezmę.* — Olmayman.\n"
            "• *Za drogie.* — Juda qimmat.\n"
            "• *Czy jest zniżka?* — Chegirma bormi?\n"
            "• *Paragon proszę.* — Chek bering.\n"
            "• *Reszta* — Qaytim"
        ),
        "vocab": [
            {"pl": "sklep",          "ph": "sklep",           "uz": "do'kon"},
            {"pl": "supermarket",    "ph": "su-per-MAR-ket",  "uz": "supermarket"},
            {"pl": "kasa",           "ph": "KA-sa",           "uz": "kassa"},
            {"pl": "cena",           "ph": "TSE-na",          "uz": "narx"},
            {"pl": "zniżka",         "ph": "ZNISH-ka",        "uz": "chegirma"},
            {"pl": "drogi",          "ph": "DRO-gi",          "uz": "qimmat"},
            {"pl": "tani",           "ph": "TA-ni",           "uz": "arzon"},
            {"pl": "gotówka",        "ph": "go-TUV-ka",       "uz": "naqd pul"},
            {"pl": "karta",          "ph": "KAR-ta",          "uz": "karta"},
            {"pl": "reszta",         "ph": "RESH-ta",         "uz": "qaytim"},
            {"pl": "paragon",        "ph": "pa-RA-gon",       "uz": "chek"},
            {"pl": "torba",          "ph": "TOR-ba",          "uz": "sumka"},
            {"pl": "kilogram",       "ph": "ki-lo-GRAM",      "uz": "kilogram"},
            {"pl": "sztuka",         "ph": "SHTU-ka",         "uz": "dona"},
            {"pl": "kasjer",         "ph": "KAS-yer",         "uz": "kassir"},
        ],
        "dialog": (
            "💬 *Dialog: Bozorda*\n\n"
            "🧑 *Przepraszam, ile kosztują te jabłka?*\n"
            "🍎 *Cztery złote za kilogram.*\n"
            "🧑 *Poproszę dwa kilogramy.*\n"
            "🍎 *Osiem złotych. Płaci Pan kartą?*\n"
            "🧑 *Nie, gotówką. Proszę dziesięć złotych.*\n"
            "🍎 *Reszta dwa złote. Dziękuję!*\n\n"
            "📝 *Tarjima:*\n"
            "🧑 Kechirasiz, bu olmalar qancha?\n"
            "🍎 Kilosi to'rt zloty.\n"
            "🧑 Ikki kilo bering.\n"
            "🍎 Sakkiz zloty. Karta bilanmi?\n"
            "🧑 Yo'q, naqd. Mana o'n zloty.\n"
            "🍎 Qaytim ikki zloty. Rahmat!"
        ),
        "exercises": [
            {"q": "🛒 *'Sklep'* nima degani?",
             "opts": ["Bozor", "Do'kon", "Supermarket", "Kassa"], "ans": 1},
            {"q": "🛒 *'Cena'* nima degani?",
             "opts": ["Chegirma", "Narx", "Qaytim", "Chek"], "ans": 1},
            {"q": "🇺🇿 *'Qimmat'* polyakchada?",
             "opts": ["Tani", "Drogi", "Duży", "Mały"], "ans": 1},
            {"q": "🛒 *'Reszta'* nima degani?",
             "opts": ["Narx", "Qaytim", "Chek", "Sumka"], "ans": 1},
            {"q": "🇺🇿 *'Chegirma'* polyakchada?",
             "opts": ["Cena", "Zniżka", "Rabat", "Tani"], "ans": 1},
            {"q": "🛒 *'Gotówka'* nima degani?",
             "opts": ["Karta", "Naqd pul", "Chipta", "Chek"], "ans": 1},
            {"q": "🛒 *'Paragon'* nima degani?",
             "opts": ["Qaytim", "Narx", "Chek", "Sumka"], "ans": 2},
            {"q": "🇺🇿 *'Arzon'* polyakchada?",
             "opts": ["Drogi", "Tani", "Duży", "Mały"], "ans": 1},
            {"q": "🛒 *'Kasjer'* nima degani?",
             "opts": ["Sotuvchi", "Kassir", "Oshpaz", "Haydovchi"], "ans": 1},
            {"q": "🇺🇿 *'Kilo'* polyakchada?",
             "opts": ["Sztuka", "Kilogram", "Litr", "Gram"], "ans": 1},
        ],
    },

    "a1_l15": {
        "title": "Ob-havo",
        "emoji": "☀️",
        "level": "A1.1",
        "grammar": (
            "🇵🇱 *Grammatika: Ob-havo gaplari*\n\n"
            "*Jest + ob-havo:*\n"
            "→ *Jest zimno.* — Sovuq.\n"
            "→ *Jest ciepło.* — Iliq.\n"
            "→ *Jest gorąco.* — Issiq.\n\n"
            "*Pada:*\n"
            "→ *Pada deszcz.* — Yomg'ir yog'yapti.\n"
            "→ *Pada śnieg.* — Qor yog'yapti.\n\n"
            "*Harorat:*\n"
            "→ *Jest plus pięć stopni.* — +5 daraja.\n"
            "→ *Jest minus dziesięć.* — -10 daraja.\n\n"
            "❓ *Jaka jest pogoda?* — Ob-havo qanday?"
        ),
        "vocab": [
            {"pl": "pogoda",         "ph": "po-GO-da",        "uz": "ob-havo"},
            {"pl": "słońce",         "ph": "SVON-tse",        "uz": "quyosh"},
            {"pl": "deszcz",         "ph": "deshch",          "uz": "yomg'ir"},
            {"pl": "śnieg",          "ph": "shnyeg",          "uz": "qor"},
            {"pl": "wiatr",          "ph": "vyatr",           "uz": "shamol"},
            {"pl": "chmury",         "ph": "HMUS-ry",         "uz": "bulutlar"},
            {"pl": "mgła",           "ph": "mgva",            "uz": "tuman"},
            {"pl": "ciepło",         "ph": "CHE-pvo",         "uz": "iliq"},
            {"pl": "gorąco",         "ph": "go-RON-tso",      "uz": "issiq"},
            {"pl": "zimno",          "ph": "ZIM-no",          "uz": "sovuq"},
            {"pl": "mróz",           "ph": "mruz",            "uz": "ayoz"},
            {"pl": "temperatura",    "ph": "tem-pe-ra-TU-ra", "uz": "harorat"},
            {"pl": "stopień",        "ph": "STO-pyen",        "uz": "daraja"},
            {"pl": "pada deszcz",    "ph": "PA-da deshch",    "uz": "yomg'ir yog'yapti"},
            {"pl": "słonecznie",     "ph": "svo-NECH-nye",    "uz": "quyoshli"},
        ],
        "dialog": (
            "💬 *Dialog: Ob-havo haqida*\n\n"
            "👩 *Jaka dzisiaj jest pogoda?*\n"
            "🧑 *Pada deszcz i jest zimno. Tylko osiem stopni.*\n"
            "👩 *W Polsce jesienią jest często tak.*\n"
            "🧑 *W Uzbekistanie jest cieplej.*\n"
            "👩 *Tak, wiem. Ale lato w Polsce jest piękne!*\n\n"
            "📝 *Tarjima:*\n"
            "👩 Bugun ob-havo qanday?\n"
            "🧑 Yomg'ir yog'yapti va sovuq. Atigi 8 daraja.\n"
            "👩 Polshada kuzda ko'pincha shunday.\n"
            "🧑 O'zbekistonda iliqroq.\n"
            "👩 Ha, bilaman. Lekin Polshaning yozi go'zal!"
        ),
        "exercises": [
            {"q": "☀️ *'Pogoda'* nima degani?",
             "opts": ["Harorat", "Ob-havo", "Quyosh", "Shamol"], "ans": 1},
            {"q": "☀️ *'Deszcz'* nima degani?",
             "opts": ["Qor", "Yomg'ir", "Shamol", "Tuman"], "ans": 1},
            {"q": "🇺🇿 *'Qor'* polyakchada?",
             "opts": ["Deszcz", "Śnieg", "Wiatr", "Mgła"], "ans": 1},
            {"q": "☀️ *'Zimno'* nima degani?",
             "opts": ["Issiq", "Iliq", "Sovuq", "Quruq"], "ans": 2},
            {"q": "🇺🇿 *'Issiq'* polyakchada?",
             "opts": ["Zimno", "Ciepło", "Gorąco", "Mróz"], "ans": 2},
            {"q": "☀️ *'Słońce'* nima degani?",
             "opts": ["Bulut", "Quyosh", "Yomg'ir", "Shamol"], "ans": 1},
            {"q": "🇺🇿 *'Tuman'* polyakchada?",
             "opts": ["Śnieg", "Chmury", "Mgła", "Wiatr"], "ans": 2},
            {"q": "☀️ *'Mróz'* nima degani?",
             "opts": ["Sovuq", "Ayoz", "Yomg'ir", "Qor"], "ans": 1},
            {"q": "❓ *'Jaka jest pogoda?'* nima degani?",
             "opts": ["Ob-havo qanday?", "Harorat necha?", "Qor yog'yadimi?", "Bugun qanday kun?"], "ans": 0},
            {"q": "☀️ *'Pada deszcz'* nima degani?",
             "opts": ["Qor yog'yapti", "Yomg'ir yog'yapti", "Shamol esyapti", "Quyosh chiqdi"], "ans": 1},
        ],
    },

    "a1_l16": {
        "title": "Bank va Pul",
        "emoji": "🏦",
        "level": "A1.2",
        "grammar": (
            "🇵🇱 *Grammatika: Bankda muloqot*\n\n"
            "*Chcę + infinitiv* = ...moqchiman\n\n"
            "→ *Chcę otworzyć konto.* — Hisob ochmoqchiman.\n"
            "→ *Chcę wypłacić pieniądze.* — Pul olmoqchiman.\n"
            "→ *Chcę zrobić przelew.* — O'tkazma qilmoqchiman.\n\n"
            "*Muhim so'zlar:*\n"
            "• *PESEL* — shaxsiy raqam (Polsha)\n"
            "• *NIP* — soliq raqami\n"
            "• *konto bankowe* — bank hisobi\n"
            "• *karta debetowa* — debet karta"
        ),
        "vocab": [
            {"pl": "bank",              "ph": "bank",              "uz": "bank"},
            {"pl": "konto bankowe",     "ph": "KON-to ban-KO-ve",  "uz": "bank hisobi"},
            {"pl": "karta bankowa",     "ph": "KAR-ta ban-KO-va",  "uz": "bank kartasi"},
            {"pl": "przelew",           "ph": "PSHE-lev",          "uz": "pul o'tkazma"},
            {"pl": "wypłata",           "ph": "vy-PVA-ta",         "uz": "pul olish"},
            {"pl": "wpłata",            "ph": "VPVA-ta",           "uz": "pul qo'yish"},
            {"pl": "bankomat",          "ph": "ban-KO-mat",        "uz": "bankomat"},
            {"pl": "waluta",            "ph": "va-LU-ta",          "uz": "valyuta"},
            {"pl": "kurs",              "ph": "kurs",              "uz": "kurs"},
            {"pl": "prowizja",          "ph": "pro-VIZ-ya",        "uz": "komissiya"},
            {"pl": "PESEL",             "ph": "PE-sel",            "uz": "shaxsiy raqam"},
            {"pl": "dowód osobisty",    "ph": "DO-vud o-so-BIS-ti","uz": "shaxsiga ID"},
            {"pl": "otworzyć konto",    "ph": "ot-VO-zhich KON-to","uz": "hisob ochish"},
            {"pl": "Zgubiłem kartę",    "ph": "zgu-BI-vem KAR-te", "uz": "Kartamni yo'qotdim"},
            {"pl": "zablokować kartę",  "ph": "za-blo-KO-vach",   "uz": "kartani bloklash"},
        ],
        "dialog": (
            "💬 *Dialog: Bankda*\n\n"
            "🧑 *Dzień dobry. Chcę otworzyć konto bankowe.*\n"
            "🏦 *Proszę o paszport i kartę pobytu.*\n"
            "🧑 *Proszę, mam oba dokumenty.*\n"
            "🏦 *Jaki numer PESEL Pan ma?*\n"
            "🧑 *Jeszcze nie mam numeru PESEL.*\n"
            "🏦 *Rozumiem. Wypełni Pan ten formularz?*\n"
            "🧑 *Kiedy będzie gotowa karta?*\n"
            "🏦 *Za siedem dni roboczych.*\n\n"
            "📝 *Tarjima:*\n"
            "🧑 Xayrli kun. Bank hisobi ochmoqchiman.\n"
            "🏦 Pasport va yashash kartasini bering.\n"
            "🧑 Mana, ikkalasi ham bor.\n"
            "🏦 PESEL raqamingiz?\n"
            "🧑 Hali PESEL raqamim yo'q.\n"
            "🏦 Tushundim. Bu blankni to'ldirасiz?\n"
            "🧑 Karta qachon tayyor?\n"
            "🏦 7 ish kunida."
        ),
        "exercises": [
            {"q": "🏦 *'Przelew'* nima degani?",
             "opts": ["Pul olish", "Pul o'tkazma", "Pul qo'yish", "Karta"], "ans": 1},
            {"q": "🏦 *'Bankomat'* nima degani?",
             "opts": ["Bank", "Bankomat", "Kassa", "Hisob"], "ans": 1},
            {"q": "🇺🇿 *'Valyuta'* polyakchada?",
             "opts": ["Kurs", "Waluta", "Prowizja", "Przelew"], "ans": 1},
            {"q": "🏦 *'Wypłata'* nima degani?",
             "opts": ["Pul qo'yish", "Pul olish", "O'tkazma", "Hisob"], "ans": 1},
            {"q": "🏦 *'PESEL'* nima degani?",
             "opts": ["Soliq raqami", "Shaxsiy raqam", "Bank raqami", "Karta raqami"], "ans": 1},
            {"q": "🇺🇿 *'Bank hisobi'* polyakchada?",
             "opts": ["Karta bankowa", "Konto bankowe", "Przelew", "Bankomat"], "ans": 1},
            {"q": "🏦 *'Waluta'* nima degani?",
             "opts": ["Narx", "Valyuta", "Kurs", "Komissiya"], "ans": 1},
            {"q": "🏦 *'Prowizja'* nima degani?",
             "opts": ["Chegirma", "Soliq", "Komissiya", "Qaytim"], "ans": 2},
            {"q": "🇺🇿 *'Kartamni yo'qotdim'* polyakchada?",
             "opts": ["Mam nową kartę", "Zgubiłem kartę", "Chcę kartę", "Mam kartę"], "ans": 1},
            {"q": "🏦 *'Wpłata'* nima degani?",
             "opts": ["Pul olish", "Pul o'tkazma", "Pul qo'yish", "Komissiya"], "ans": 2},
        ],
    },

    "a1_l17": {
        "title": "Hujjatlar va Idora",
        "emoji": "📄",
        "level": "A1.2",
        "grammar": (
            "🇵🇱 *Grammatika: Idorada muloqot*\n\n"
            "*Muhim fe'llar:*\n"
            "• *złożyć wniosek* — ariza berish\n"
            "• *przedłużyć* — uzaytirish\n"
            "• *zameldować się* — ro'yxatdan o'tish\n"
            "• *potrzebować* — kerak bo'lish\n\n"
            "*Zarur iboralar:*\n"
            "→ *Potrzebuję pomocy.* — Yordamga muhtojman.\n"
            "→ *Jakie dokumenty są potrzebne?*\n"
            "   — Qanday hujjatlar kerak?\n"
            "→ *Kiedy będzie gotowe?* — Qachon tayyor?"
        ),
        "vocab": [
            {"pl": "paszport",           "ph": "PAS-port",            "uz": "pasport"},
            {"pl": "wiza",               "ph": "VI-za",               "uz": "viza"},
            {"pl": "karta pobytu",       "ph": "KAR-ta po-BY-tu",     "uz": "yashash kartasi"},
            {"pl": "zezwolenie na pracę","ph": "zez-vo-LE-nye na PRA-tse","uz": "ish ruxsati"},
            {"pl": "umowa o pracę",      "ph": "u-MO-va o PRA-tse",   "uz": "ish shartnomasi"},
            {"pl": "zaświadczenie",      "ph": "za-shvyad-CHE-nye",   "uz": "ma'lumotnoma"},
            {"pl": "wniosek",            "ph": "VNYO-sek",            "uz": "ariza"},
            {"pl": "formularz",          "ph": "for-MU-lazh",         "uz": "blank / forma"},
            {"pl": "podpis",             "ph": "POD-pis",             "uz": "imzo"},
            {"pl": "pieczątka",          "ph": "pye-CHONT-ka",        "uz": "muhr"},
            {"pl": "urząd",              "ph": "U-zhond",             "uz": "idora"},
            {"pl": "kolejka",            "ph": "ko-LEY-ka",           "uz": "navbat"},
            {"pl": "termin",             "ph": "TER-min",             "uz": "uchrashув vaqti"},
            {"pl": "meldunek",           "ph": "mel-DU-nek",          "uz": "ro'yxatdan o'tish"},
            {"pl": "tłumacz",            "ph": "TVU-mach",            "uz": "tarjimon"},
        ],
        "dialog": (
            "💬 *Dialog: Chet elliklar idorasida*\n\n"
            "🧑 *Dzień dobry. Chcę złożyć wniosek o kartę pobytu.*\n"
            "🏢 *Czy ma Pan wszystkie dokumenty?*\n"
            "🧑 *Mam paszport, umowę o pracę i zdjęcia.*\n"
            "🏢 *Potrzebujemy jeszcze zaświadczenia o zameldowaniu.*\n"
            "🧑 *Gdzie mogę to dostać?*\n"
            "🏢 *W urzędzie gminy. Ile czeka się na kartę?*\n"
            "🧑 *Około trzech miesięcy.*\n\n"
            "📝 *Tarjima:*\n"
            "🧑 Xayrli kun. Yashash kartasiga ariza bermoqchiman.\n"
            "🏢 Barcha hujjatlar bormi?\n"
            "🧑 Pasport, ish shartnomasi va fotosuratlar bor.\n"
            "🏢 Ro'yxatdan o'tish ma'lumotnomasiz ham kerak.\n"
            "🧑 Uni qayerdan olsam bo'ladi?\n"
            "🏢 Mahalla idorasida. Karta taxminan 3 oyda tayyor."
        ),
        "exercises": [
            {"q": "📄 *'Paszport'* nima degani?",
             "opts": ["Viza", "Pasport", "Hujjat", "Ariza"], "ans": 1},
            {"q": "📄 *'Karta pobytu'* nima degani?",
             "opts": ["Ish kartasi", "Yashash kartasi", "Bank kartasi", "ID karta"], "ans": 1},
            {"q": "🇺🇿 *'Ariza'* polyakchada?",
             "opts": ["Dokument", "Wniosek", "Paszport", "Adres"], "ans": 1},
            {"q": "📄 *'Podpis'* nima degani?",
             "opts": ["Muhr", "Imzo", "Blank", "Raqam"], "ans": 1},
            {"q": "📄 *'Kolejka'* nima degani?",
             "opts": ["Vaqt", "Navbat", "Ariza", "Idora"], "ans": 1},
            {"q": "🇺🇿 *'Tarjimon'* polyakchada?",
             "opts": ["Prawnik", "Tłumacz", "Lekarz", "Urzędnik"], "ans": 1},
            {"q": "📄 *'Termin'* nima degani?",
             "opts": ["Muddat", "Uchrashув vaqti", "Navbat", "Ariza"], "ans": 1},
            {"q": "📄 *'Zaświadczenie'* nima degani?",
             "opts": ["Ariza", "Shartnoma", "Ma'lumotnoma", "Pasport"], "ans": 2},
            {"q": "🇺🇿 *'Muhr'* polyakchada?",
             "opts": ["Podpis", "Pieczątka", "Formularz", "Wniosek"], "ans": 1},
            {"q": "📄 *'Meldunek'* nima degani?",
             "opts": ["Viza", "Pasport", "Ro'yxatdan o'tish", "Ariza"], "ans": 2},
        ],
    },

    "a1_l18": {
        "title": "Kasallik va Shifokor",
        "emoji": "🏥",
        "level": "A1.2",
        "grammar": (
            "🇵🇱 *Grammatika: Og'riq aytish*\n\n"
            "*Boli mnie + a'zo* = ...og'riyapti\n\n"
            "→ *Boli mnie głowa.* — Boshim og'riyapti.\n"
            "→ *Boli mnie brzuch.* — Qorinim og'riyapti.\n"
            "→ *Boli mnie ząb.* — Tishim og'riyapti.\n"
            "→ *Boli mnie gardło.* — Tomoqim og'riyapti.\n\n"
            "*Muhim iboralar:*\n"
            "• *Mam gorączkę.* — Haroratim bor.\n"
            "• *Jestem chory/a.* — Kasal(man).\n"
            "• *Od kiedy?* — Qachondan beri?\n"
            "• *Od wczoraj.* — Kechadan beri."
        ),
        "vocab": [
            {"pl": "lekarz",          "ph": "LE-kazh",          "uz": "shifokor"},
            {"pl": "apteka",          "ph": "ap-TE-ka",         "uz": "dorixona"},
            {"pl": "ból",             "ph": "bul",              "uz": "og'riq"},
            {"pl": "ból głowy",       "ph": "bul GVO-vy",       "uz": "bosh og'riq"},
            {"pl": "gorączka",        "ph": "go-RONCH-ka",      "uz": "harorat (isitma)"},
            {"pl": "kaszel",          "ph": "KA-shel",          "uz": "yo'tal"},
            {"pl": "katar",           "ph": "KA-tar",           "uz": "tumov"},
            {"pl": "wysypka",         "ph": "vy-SYP-ka",        "uz": "toshma"},
            {"pl": "recepta",         "ph": "re-TSEP-ta",       "uz": "retsept"},
            {"pl": "lek / lekarstwo", "ph": "lek",              "uz": "dori"},
            {"pl": "tabletka",        "ph": "tab-LET-ka",       "uz": "tabletka"},
            {"pl": "alergia",         "ph": "a-LER-gya",        "uz": "allergiya"},
            {"pl": "chory/a",         "ph": "HO-ri/a",          "uz": "kasal"},
            {"pl": "zdrowy/a",        "ph": "ZDRO-vi/a",        "uz": "sog'lom"},
            {"pl": "szpital",         "ph": "SHPI-tal",         "uz": "kasalxona"},
        ],
        "dialog": (
            "💬 *Dialog: Shifokorда*\n\n"
            "👨‍⚕️ *Co Pana boli?*\n"
            "🧑 *Boli mnie głowa i mam gorączkę. Od wczoraj.*\n"
            "👨‍⚕️ *Ile ma Pan gorączki?*\n"
            "🧑 *Trzydzieści osiem i pół.*\n"
            "👨‍⚕️ *Czy ma Pan kaszel lub katar?*\n"
            "🧑 *Tak, mam lekki kaszel.*\n"
            "👨‍⚕️ *To wygląda na grypę. Wypisuję receptę.*\n"
            "🧑 *Ile dni powinienem zostać w domu?*\n"
            "👨‍⚕️ *Trzy do pięciu dni. I dużo pić.*\n\n"
            "📝 *Tarjima:*\n"
            "👨‍⚕️ Nering og'riyapti?\n"
            "🧑 Boshim og'riyapti va haroratim bor. Kechadan.\n"
            "👨‍⚕️ Haroratingiz necha?\n"
            "🧑 38.5.\n"
            "👨‍⚕️ Yo'talmi yoki tumovmi?\n"
            "🧑 Ha, biroz yo'talim bor.\n"
            "👨‍⚕️ Gripp ko'rinadi. Retsept yozaman.\n"
            "🧑 Necha kun uyda qolaman?\n"
            "👨‍⚕️  3-5 kun. Ko'p suyuqlik iching."
        ),
        "exercises": [
            {"q": "🏥 *'Lekarz'* nima degani?",
             "opts": ["Hamshira", "Shifokor", "Apteka", "Kasalxona"], "ans": 1},
            {"q": "🏥 *'Gorączka'* nima degani?",
             "opts": ["Yo'tal", "Harorat (isitma)", "Tumov", "Og'riq"], "ans": 1},
            {"q": "🇺🇿 *'Yo'tal'* polyakchada?",
             "opts": ["Katar", "Kaszel", "Ból", "Wysypka"], "ans": 1},
            {"q": "🏥 *'Recepta'* nima degani?",
             "opts": ["Dori", "Retsept", "Tabletka", "Kasalxona"], "ans": 1},
            {"q": "🏥 *'Chory'* nima degani?",
             "opts": ["Sog'lom", "Kasal", "Charchagan", "Kuchli"], "ans": 1},
            {"q": "🇺🇿 *'Dorixona'* polyakchada?",
             "opts": ["Szpital", "Apteka", "Klinika", "Lekarz"], "ans": 1},
            {"q": "🏥 *'Ból głowy'* nima degani?",
             "opts": ["Tomoq og'riq", "Bosh og'riq", "Qorin og'riq", "Tish og'riq"], "ans": 1},
            {"q": "🇺🇿 *'Allergiya'* polyakchada?",
             "opts": ["Kaszel", "Wysypka", "Alergia", "Katar"], "ans": 2},
            {"q": "🏥 *'Zdrowy'* nima degani?",
             "opts": ["Kasal", "Sog'lom", "Charchagan", "Kuchsiz"], "ans": 1},
            {"q": "🏥 *'Tabletka'* nima degani?",
             "opts": ["Dori", "Ukol", "Tabletka", "Retsept"], "ans": 2},
        ],
    },

    "a1_l19": {
        "title": "Uy va Kvartira",
        "emoji": "🏠",
        "level": "A1.2",
        "grammar": (
            "🇵🇱 *Grammatika: Uy haqida gapirish*\n\n"
            "*Mieszkam w...* = ...da yashayman\n\n"
            "→ *Mieszkam w domu.* — Uyda yashayman.\n"
            "→ *Mieszkam w mieszkaniu.* — Kvartіrada yashayman.\n"
            "→ *Mieszkam na trzecim piętrze.* — 3-qavatda.\n\n"
            "*Kvartira xonalari:*\n"
            "• *sypialnia* — yotoqxona\n"
            "• *kuchnia* — oshxona\n"
            "• *łazienka* — hammom\n"
            "• *salon* — mehmonxona\n\n"
            "❓ *Ile pokoi?* — Nechta xona?"
        ),
        "vocab": [
            {"pl": "dom",          "ph": "dom",           "uz": "uy"},
            {"pl": "mieszkanie",   "ph": "myesh-KA-nye",  "uz": "kvartira"},
            {"pl": "pokój",        "ph": "PO-kuy",        "uz": "xona"},
            {"pl": "kuchnia",      "ph": "KUH-nya",       "uz": "oshxona"},
            {"pl": "łazienka",     "ph": "va-ZHEN-ka",    "uz": "hammom"},
            {"pl": "salon",        "ph": "SA-lon",        "uz": "mehmonxona"},
            {"pl": "sypialnia",    "ph": "sy-PYAL-nya",   "uz": "yotoqxona"},
            {"pl": "parter",       "ph": "PAR-ter",       "uz": "birinchi qavat"},
            {"pl": "piętro",       "ph": "PYE-tro",       "uz": "qavat"},
            {"pl": "winda",        "ph": "VIN-da",        "uz": "lift"},
            {"pl": "wynajem",      "ph": "vy-NA-yem",     "uz": "ijara"},
            {"pl": "właściciel",   "ph": "vvash-CHI-chel","uz": "uy egasi"},
            {"pl": "czynsz",       "ph": "chinsh",        "uz": "ijara to'lovi"},
            {"pl": "media",        "ph": "ME-dya",        "uz": "kommunal xarajatlar"},
            {"pl": "umeblowany",   "ph": "u-meb-LO-va-ni","uz": "mebelli"},
        ],
        "dialog": (
            "💬 *Dialog: Kvartira qidirish*\n\n"
            "🧑 *Dzień dobry. Widziałem ogłoszenie.*\n"
            "🏠 *Tak, zapraszam. Na trzecim piętrze.*\n"
            "🧑 *Ile pokoi?*\n"
            "🏠 *Dwa pokoje, kuchnia i łazienka.*\n"
            "🧑 *Ile kosztuje wynajem?*\n"
            "🏠 *Dwa tysiące złotych. Media są w cenie.*\n"
            "🧑 *Czy jest umeblowane?*\n"
            "🏠 *Tak, w pełni umeblowane.*\n\n"
            "📝 *Tarjima:*\n"
            "🧑 Xayrli kun. E'lonni ko'rdim.\n"
            "🏠 Ha, marhamat. 3-qavatda.\n"
            "🧑 Nechta xona?\n"
            "🏠 Ikki xona, oshxona va hammom.\n"
            "🧑 Ijara qancha?\n"
            "🏠 2000 zloty. Kommunal kiradi.\n"
            "🧑 Mebel bormi?\n"
            "🏠 Ha, to'liq mebelli."
        ),
        "exercises": [
            {"q": "🏠 *'Mieszkanie'* nima degani?",
             "opts": ["Uy", "Kvartira", "Xona", "Bino"], "ans": 1},
            {"q": "🏠 *'Kuchnia'* nima degani?",
             "opts": ["Hammom", "Oshxona", "Mehmonxona", "Yotoqxona"], "ans": 1},
            {"q": "🇺🇿 *'Hammom'* polyakchada?",
             "opts": ["Kuchnia", "Łazienka", "Salon", "Pokój"], "ans": 1},
            {"q": "🏠 *'Wynajem'* nima degani?",
             "opts": ["Narx", "Ijara", "To'lov", "Chegirma"], "ans": 1},
            {"q": "🏠 *'Piętro'* nima degani?",
             "opts": ["Lift", "Zinapoya", "Qavat", "Kirish"], "ans": 2},
            {"q": "🇺🇿 *'Mehmonxona'* polyakchada?",
             "opts": ["Sypialnia", "Kuchnia", "Salon", "Pokój"], "ans": 2},
            {"q": "🏠 *'Winda'* nima degani?",
             "opts": ["Zinapoya", "Lift", "Eshik", "Deraza"], "ans": 1},
            {"q": "🏠 *'Umeblowany'* nima degani?",
             "opts": ["Bo'sh", "Mebelli", "Katta", "Yangi"], "ans": 1},
            {"q": "🏠 *'Właściciel'* nima degani?",
             "opts": ["Ijara oluvchi", "Uy egasi", "Qo'shni", "Menejer"], "ans": 1},
            {"q": "🇺🇿 *'Kommunal xarajatlar'* polyakchada?",
             "opts": ["Czynsz", "Media", "Wynajem", "Kaucja"], "ans": 1},
        ],
    },

    "a1_l20": {
        "title": "Telefon va Internet",
        "emoji": "📱",
        "level": "A1.2",
        "grammar": (
            "🇵🇱 *Grammatika: Telefonda gapirish*\n\n"
            "*Telefon iboralari:*\n"
            "• *Halo?* — Alo?\n"
            "• *Słucham?* — Eshitaman?\n"
            "• *Czy mogę mówić z...?* — ...bilan gaplashsam?\n"
            "• *Proszę poczekać.* — Kuting.\n"
            "• *Oddzwonię.* — Qayta qo'ng'iroq qilaman.\n"
            "• *Numer jest zajęty.* — Raqam band.\n\n"
            "*Rasmiy email:*\n"
            "→ *Szanowny Panie* — Hurmatli janob\n"
            "→ *Z poważaniem* — Hurmat bilan"
        ),
        "vocab": [
            {"pl": "telefon",           "ph": "te-LE-fon",         "uz": "telefon"},
            {"pl": "zadzwonić",         "ph": "za-DZVO-nach",       "uz": "qo'ng'iroq qilmoq"},
            {"pl": "odebrać",           "ph": "o-DEB-rach",         "uz": "telefonni olmoq"},
            {"pl": "wiadomość",         "ph": "vya-DO-moshch",      "uz": "xabar"},
            {"pl": "SMS",               "ph": "es-em-es",           "uz": "SMS"},
            {"pl": "internet",          "ph": "IN-ter-net",         "uz": "internet"},
            {"pl": "Wi-Fi",             "ph": "vi-fi",              "uz": "Wi-Fi"},
            {"pl": "e-mail",            "ph": "i-meyl",             "uz": "elektron pochta"},
            {"pl": "aplikacja",         "ph": "ap-li-KATS-ya",      "uz": "ilova"},
            {"pl": "hasło",             "ph": "HAS-vo",             "uz": "parol"},
            {"pl": "numer telefonu",    "ph": "NU-mer te-LE-fo-nu", "uz": "telefon raqami"},
            {"pl": "zasięg",            "ph": "ZA-sheng",           "uz": "signal"},
            {"pl": "bateria",           "ph": "ba-TER-ya",          "uz": "batareya"},
            {"pl": "ładowarka",         "ph": "va-do-VAR-ka",       "uz": "zaryadlagich"},
            {"pl": "numer jest zajęty", "ph": "NU-mer yest za-YEN-ti","uz": "raqam band"},
        ],
        "dialog": (
            "💬 *Dialog: Telefon qo'ng'irog'i*\n\n"
            "🧑 *Halo? Dzień dobry. Mówi Aziz Karimov.*\n"
            "   *Czy mogę mówić z Panem Nowakiem?*\n"
            "📞 *Chwileczkę proszę.*\n"
            "   *Pan Nowak jest na spotkaniu.*\n"
            "   *Czy mogę przekazać wiadomość?*\n"
            "🧑 *Tak. Proszę powiedzieć, że zadzwoniłem*\n"
            "   *w sprawie jutrzejszego terminu.*\n"
            "📞 *Dobrze. Oddzwoni Pan Nowak.*\n\n"
            "📝 *Tarjima:*\n"
            "🧑 Alo? Xayrli kun. Bu Aziz Karimov.\n"
            "   Nowak janob bilan gaplashsam bo'ladimi?\n"
            "📞 Bir oz kuting.\n"
            "   Nowak janob yig'ilishda.\n"
            "   Xabar qoldirsam bo'ladimi?\n"
            "🧑 Ha. Qo'ng'iroq qilganimni aytib qo'ying,\n"
            "   ertangi uchrashув haqida.\n"
            "📞 Xop. Nowak janob qayta qo'ng'iroq qiladi."
        ),
        "exercises": [
            {"q": "📱 *'Zadzwonić'* nima degani?",
             "opts": ["Xabar yozmoq", "Qo'ng'iroq qilmoq", "Telefonni olmoq", "Uzilmoq"], "ans": 1},
            {"q": "📱 *'Wiadomość'* nima degani?",
             "opts": ["Qo'ng'iroq", "Xabar", "Signal", "Raqam"], "ans": 1},
            {"q": "🇺🇿 *'Parol'* polyakchada?",
             "opts": ["Numer", "Aplikacja", "Hasło", "Internet"], "ans": 2},
            {"q": "📱 *'Zasięg'* nima degani?",
             "opts": ["Batareya", "Signal", "Zaryadlagich", "Raqam"], "ans": 1},
            {"q": "📱 *'Bateria'* nima degani?",
             "opts": ["Zaryadlagich", "Batareya", "Signal", "Parol"], "ans": 1},
            {"q": "🇺🇿 *'Ilova'* polyakchada?",
             "opts": ["Internet", "Wi-Fi", "Aplikacja", "E-mail"], "ans": 2},
            {"q": "📱 *'Ładowarka'* nima degani?",
             "opts": ["Batareya", "Signal", "Zaryadlagich", "Telefon"], "ans": 2},
            {"q": "📱 *'Numer jest zajęty'* nima degani?",
             "opts": ["Raqam noto'g'ri", "Raqam band", "Signal yo'q", "Telefon o'chiq"], "ans": 1},
            {"q": "📱 *'Odebrać'* nima degani?",
             "opts": ["Qo'ng'iroq qilmoq", "Telefonni olmoq", "Xabar yozmoq", "O'chirmoq"], "ans": 1},
            {"q": "🇺🇿 *'Elektron pochta'* polyakchada?",
             "opts": ["SMS", "Wiadomość", "E-mail", "Aplikacja"], "ans": 2},
        ],
    },
}
