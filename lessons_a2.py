# -*- coding: utf-8 -*-
"""
🦉 POLYAKCHA BOT — A2 DARSLARI
20 ta dars: A2.1
"""

A2_LESSONS = {

    "a2_l01": {
        "title": "O'tgan Zamon",
        "emoji": "⏮️",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: O'tgan Zamon*\n\n"
            "*-ł / -ła / -ło / -li / -ły* qo'shimchalari:\n\n"
            "• ja (erk.) → *robiłem* — qildim\n"
            "• ja (ay.) → *robiłam* — qildim\n"
            "• on → *robił* — qildi\n"
            "• ona → *robiła* — qildi\n"
            "• my (erk.) → *robiliśmy*\n"
            "• oni → *robili*\n\n"
            "*Muhim fe'llar:*\n"
            "• być → *byłem/byłam* (bo'ldim)\n"
            "• mieć → *miałem/miałam* (edi)\n"
            "• iść → *szedłem/szłam* (bordim)\n"
            "• jeść → *jadłem/jadłam* (yedim)\n"
            "• kupić → *kupiłem/kupiłam* (sotib oldim)"
        ),
        "vocab": [
            {"pl": "wczoraj robiłem",    "ph": "VCHO-ray ro-BI-vem",    "uz": "kecha qildim"},
            {"pl": "byłem w pracy",      "ph": "BY-vem v PRA-tsi",       "uz": "ishda edim"},
            {"pl": "pojechałem",         "ph": "po-ye-HA-vem",           "uz": "bordim (transport)"},
            {"pl": "przyszedłem",        "ph": "pshi-SHED-vem",          "uz": "keldim (piyoda)"},
            {"pl": "zrobiłem",           "ph": "zro-BI-vem",             "uz": "qilib tugatdim"},
            {"pl": "kupiłem",            "ph": "ku-PI-vem",              "uz": "sotib oldim"},
            {"pl": "jadłem",             "ph": "YAD-vem",                "uz": "yedim"},
            {"pl": "piłem",              "ph": "PI-vem",                 "uz": "ichdim"},
            {"pl": "widziałem",          "ph": "vi-DJA-vem",             "uz": "ko'rdim"},
            {"pl": "rozmawiałem",        "ph": "roz-ma-VJA-vem",         "uz": "gaplashdim"},
            {"pl": "pracowałem",         "ph": "pra-tso-VA-vem",         "uz": "ishladim"},
            {"pl": "mieszkałem",         "ph": "myesh-KA-vem",           "uz": "yashardim"},
            {"pl": "uczyłem się",        "ph": "u-CHI-vem she",          "uz": "o'rgandim"},
            {"pl": "spałem",             "ph": "SPA-vem",                "uz": "uxladim"},
            {"pl": "wróciłem",           "ph": "vru-CHI-vem",            "uz": "qaytdim"},
        ],
        "dialog": (
            "💬 *Dialog: Kecha nima qildingiz?*\n\n"
            "👩 *Co robiłeś wczoraj wieczorem?*\n"
            "🧑 *Byłem zmęczony po pracy.*\n"
            "   *Jadłem kolację i oglądałem telewizję.*\n"
            "👩 *A w weekend co robiłeś?*\n"
            "🧑 *W sobotę pojechałem do centrum.*\n"
            "   *Kupiłem nowe buty i spotkałem kolegę.*\n"
            "👩 *Brzmi fajnie! Ja byłam w kinie.*\n\n"
            "📝 *Tarjima:*\n"
            "👩 Kecha kechqurun nima qilding?\n"
            "🧑 Ishdan keyin charchaganman. Kechki ovqat yedim va televizor ko'rdim.\n"
            "👩 Dam olish kunlari nima qilding?\n"
            "🧑 Shanba kuni markazga bordim. Yangi poyabzal sotib oldim va do'stim bilan uchrashdim.\n"
            "👩 Zo'r! Men kinoda edim."
        ),
        "exercises": [
            {"q": "⏮️ *'Byłem'* nima degani?",
             "opts": ["Bo'laman", "Bo'ldim (erk.)", "Bo'ladi", "Bo'ling"], "ans": 1},
            {"q": "⏮️ *'Jadłem'* nima degani?",
             "opts": ["Yeyapman", "Yeyman", "Yedim", "Yesin"], "ans": 2},
            {"q": "🇺🇿 *'Ishladim'* polyakchada? (erkak)",
             "opts": ["Pracuję", "Pracowałam", "Pracowałem", "Pracował"], "ans": 2},
            {"q": "⏮️ *'Kupiłem'* nima degani?",
             "opts": ["Sotib olaman", "Sotib oldim", "Sotib oladi", "Sotib olmoqchi"], "ans": 1},
            {"q": "⏮️ *'Widziałem'* nima degani?",
             "opts": ["Ko'raman", "Ko'rmoqchiman", "Ko'rdim", "Ko'rsatdim"], "ans": 2},
            {"q": "🇺🇿 *'Kecha bordim'* (transport, erkak) polyakchada?",
             "opts": ["Wczoraj szedłem", "Wczoraj pojechałem", "Wczoraj pójdę", "Wczoraj jadę"], "ans": 1},
            {"q": "⏮️ *'Spałem'* nima degani?",
             "opts": ["Uxlayman", "Uxlamoqchiman", "Uxladim", "Uxlayapman"], "ans": 2},
            {"q": "⏮️ *'Wróciłem'* nima degani?",
             "opts": ["Ketdim", "Qaytdim", "Keldim", "Bordim"], "ans": 1},
            {"q": "🇺🇿 *'Gaplashdim'* polyakchada?",
             "opts": ["Rozmawiałem", "Rozmawiam", "Będę rozmawiał", "Rozmawiaj"], "ans": 0},
            {"q": "⏮️ *'Uczyłem się'* nima degani?",
             "opts": ["O'rganaman", "O'rganmoqchiman", "O'rgandim", "O'rgatdim"], "ans": 2},
        ],
    },

    "a2_l02": {
        "title": "Kelasi Zamon",
        "emoji": "⏭️",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Kelasi Zamon*\n\n"
            "*1-usul: będę + infinitiv*\n\n"
            "• ja → *będę pracować* — ishlayman\n"
            "• ty → *będziesz pracować*\n"
            "• on/ona → *będzie pracować*\n"
            "• my → *będziemy pracować*\n"
            "• oni → *będą pracować*\n\n"
            "*2-usul: Perfektiv fe'l*\n"
            "→ *Zrobię to jutro.* — Buni ertaga qilaman.\n"
            "→ *Kupię chleb.* — Non sotib olaman.\n\n"
            "*Vaqt so'zlari:*\n"
            "• *jutro* — ertaga\n"
            "• *za tydzień* — bir haftadan keyin\n"
            "• *wkrótce* — tez orada\n"
            "• *w przyszłym roku* — kelasi yil"
        ),
        "vocab": [
            {"pl": "będę pracować",      "ph": "BEN-de pra-TSO-vach",    "uz": "ishlayman (kelajak)"},
            {"pl": "pojadę",             "ph": "po-YA-de",               "uz": "boraman (transport)"},
            {"pl": "pójdę",              "ph": "PUY-de",                 "uz": "boraman (piyoda)"},
            {"pl": "zrobię",             "ph": "ZRO-bye",                "uz": "qilaman (tugataman)"},
            {"pl": "kupię",              "ph": "KU-pye",                 "uz": "sotib olaman"},
            {"pl": "zadzwonię",          "ph": "za-DZvo-nye",            "uz": "qo'ng'iroq qilaman"},
            {"pl": "wrócę",              "ph": "VRU-tse",                "uz": "qaytaman"},
            {"pl": "spotkam się",        "ph": "SPOT-kam she",           "uz": "uchrasham"},
            {"pl": "nauczę się",         "ph": "na-U-che she",           "uz": "o'rganaman"},
            {"pl": "zacznę",             "ph": "ZACH-ne",                "uz": "boshlayman"},
            {"pl": "skończę",            "ph": "SKON-che",               "uz": "tugataman"},
            {"pl": "wyjadę",             "ph": "vy-YA-de",               "uz": "jo'nayman"},
            {"pl": "przyjadę",           "ph": "pshi-YA-de",             "uz": "kelaman (transport)"},
            {"pl": "zostanę",            "ph": "zos-TA-ne",              "uz": "qolaman"},
            {"pl": "planuję",            "ph": "pla-NU-ye",              "uz": "rejalashtiryapman"},
        ],
        "dialog": (
            "💬 *Dialog: Kelajak rejalari*\n\n"
            "👩 *Jakie masz plany na weekend?*\n"
            "🧑 *W sobotę będę pracować.*\n"
            "   *A w niedzielę pojadę do Krakowa.*\n"
            "👩 *Widziałeś już Wawel?*\n"
            "🧑 *Nie, jeszcze nie. Ale w tym roku na pewno.*\n"
            "   *A ty? Co będziesz robić?*\n"
            "👩 *Zostanę w domu i odpocznę.*\n"
            "   *W przyszłym tygodniu zacznę nowy kurs.*\n\n"
            "📝 *Tarjima:*\n"
            "👩 Dam olish kunlari rejang qanday?\n"
            "🧑 Shanba kuni ishlayman. Yakshanba kuni Krakovga boraman.\n"
            "👩 Vavelni ko'rganmisiz?\n"
            "🧑 Yo'q, hali emas. Lekin bu yil albatta. Siz-chi?\n"
            "👩 Uyda qolaman va dam olaman. Kelasi hafta yangi kurs boshlayman."
        ),
        "exercises": [
            {"q": "⏭️ *'Będę pracować'* nima degani?",
             "opts": ["Ishladim", "Ishlayman (kelajak)", "Ishlamoqchiman", "Ishlayapman"], "ans": 1},
            {"q": "⏭️ *'Pojadę'* nima degani?",
             "opts": ["Bordim", "Boraman (transport)", "Borayapman", "Bormoqchiman"], "ans": 1},
            {"q": "🇺🇿 *'Sotib olaman'* polyakchada?",
             "opts": ["Kupiłem", "Kupuję", "Kupię", "Będę kupować"], "ans": 2},
            {"q": "⏭️ *'Wrócę'* nima degani?",
             "opts": ["Qaytdim", "Qaytaman", "Qaytmoqchiman", "Qaytib kelgan"], "ans": 1},
            {"q": "⏭️ *'Zacznę'* nima degani?",
             "opts": ["Tugataman", "Davom etaman", "Boshlayman", "To'xtataman"], "ans": 2},
            {"q": "🇺🇿 *'Uchrasham'* polyakchada?",
             "opts": ["Spotkałem się", "Spotykam się", "Spotkam się", "Spotykaj się"], "ans": 2},
            {"q": "⏭️ *'Zostanę'* nima degani?",
             "opts": ["Ketaman", "Qolaman", "Boraman", "Kelaman"], "ans": 1},
            {"q": "⏭️ *'Zadzwonię'* nima degani?",
             "opts": ["Qo'ng'iroq qildim", "Qo'ng'iroq qilaman", "Qo'ng'iroq qilyapman", "Qo'ng'iroq qiling"], "ans": 1},
            {"q": "🇺🇿 *'O'rganaman'* polyakchada?",
             "opts": ["Uczyłem się", "Uczę się", "Nauczę się", "Ucz się"], "ans": 2},
            {"q": "⏭️ *'Skończę'* nima degani?",
             "opts": ["Boshlayman", "Davom etaman", "Tugataman", "To'xtataman"], "ans": 2},
        ],
    },

    "a2_l03": {
        "title": "Shart Gaplari",
        "emoji": "🔀",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Shart Gaplari*\n\n"
            "*Haqiqiy shart:*\n"
            "*Jeśli* + hozirgi zamon → kelasi zamon\n\n"
            "→ *Jeśli będę miał czas, pojadę.*\n"
            "   Vaqtim bo'lsa, boraman.\n\n"
            "→ *Jeśli nie rozumiesz, zapytaj.*\n"
            "   Tushunmasang, so'ra.\n\n"
            "*Xayoliy shart:*\n"
            "*Gdyby* + o'tgan zamon → *by* + o'tgan\n\n"
            "→ *Gdybym miał pieniądze, kupiłbym dom.*\n"
            "   Pulim bo'lganda, uy sotib olardim.\n\n"
            "*Boshqa bog'lovchilar:*\n"
            "• *chyba że* — faqat ... bo'lmasa\n"
            "• *pod warunkiem że* — shart bilan\n"
            "• *w przeciwnym razie* — aks holda"
        ),
        "vocab": [
            {"pl": "jeśli / jeżeli",     "ph": "YES-li / ye-ZHE-li",    "uz": "agar"},
            {"pl": "gdyby",              "ph": "GDY-by",                 "uz": "agar bo'lganda (xayoliy)"},
            {"pl": "wtedy",              "ph": "VTE-dy",                 "uz": "u vaqtda / keyin"},
            {"pl": "pod warunkiem",      "ph": "pod va-RUN-kem",         "uz": "shart bilan"},
            {"pl": "chyba że",           "ph": "HY-ba zhe",              "uz": "faqat ... bo'lmasa"},
            {"pl": "w przeciwnym razie", "ph": "v pshe-CHIV-nim RA-zye", "uz": "aks holda"},
            {"pl": "mimo że",            "ph": "MI-mo zhe",              "uz": "garchi ... bo'lsa ham"},
            {"pl": "ponieważ",           "ph": "po-NYE-vazh",            "uz": "chunki"},
            {"pl": "dlatego",            "ph": "dla-TE-go",              "uz": "shuning uchun"},
            {"pl": "jednak",             "ph": "YED-nak",                "uz": "lekin / biroq"},
            {"pl": "chociaż",            "ph": "HO-chazh",               "uz": "garchi"},
            {"pl": "żeby",               "ph": "ZHE-by",                 "uz": "... uchun (maqsad)"},
            {"pl": "zanim",              "ph": "ZA-nim",                 "uz": "... dan oldin"},
            {"pl": "kiedy",              "ph": "KYE-dy",                 "uz": "qachon"},
            {"pl": "dopóki",             "ph": "do-PU-ki",               "uz": "... gacha"},
        ],
        "dialog": (
            "💬 *Dialog: Shart va reja*\n\n"
            "👔 *Jeśli nie dostaniesz wizy, co zrobisz?*\n"
            "🧑 *Jeśli nie dostanę wizy, będę musiał wrócić.*\n"
            "   *Ale mam nadzieję, że wszystko będzie dobrze.*\n"
            "👔 *A gdybyś mógł zostać — co byś zrobił?*\n"
            "🧑 *Gdybym mógł zostać, nauczyłbym się lepiej*\n"
            "   *po polsku i znalazłbym lepszą pracę.*\n"
            "👔 *To dobry plan. Trzymam kciuki!*\n\n"
            "📝 *Tarjima:*\n"
            "👔 Agar viza olmasang, nima qilasiz?\n"
            "🧑 Viza olmasam, qaytishga majbur bo'laman. Lekin hammasi yaxshi bo'ladi deb umid qilaman.\n"
            "👔 Agar qola olsangiz — nima qilardingiz?\n"
            "🧑 Qola olsam, polyakchani yaxshiroq o'rgandim va yaxshiroq ish topardim.\n"
            "👔 Yaxshi reja. Omad tilayman!"
        ),
        "exercises": [
            {"q": "🔀 *'Jeśli'* nima degani?",
             "opts": ["Chunki", "Agar", "Lekin", "Shuning uchun"], "ans": 1},
            {"q": "🔀 *'Gdyby'* nima degani?",
             "opts": ["Agar (haqiqiy)", "Agar bo'lganda (xayoliy)", "Chunki", "Lekin"], "ans": 1},
            {"q": "🇺🇿 *'Chunki'* polyakchada?",
             "opts": ["Dlatego", "Jednak", "Ponieważ", "Chociaż"], "ans": 2},
            {"q": "🔀 *'Dlatego'* nima degani?",
             "opts": ["Chunki", "Shuning uchun", "Lekin", "Agar"], "ans": 1},
            {"q": "🔀 *'Chociaż'* nima degani?",
             "opts": ["Chunki", "Agar", "Garchi", "Shuning uchun"], "ans": 2},
            {"q": "🇺🇿 *'Shuning uchun'* polyakchada?",
             "opts": ["Ponieważ", "Dlatego", "Jednak", "Żeby"], "ans": 1},
            {"q": "🔀 *'Zanim'* nima degani?",
             "opts": ["Keyin", "Oldin", "Birga", "Hozir"], "ans": 1},
            {"q": "🔀 *'Żeby'* nima degani?",
             "opts": ["Chunki", "Agar", "...uchun (maqsad)", "Garchi"], "ans": 2},
            {"q": "🇺🇿 *'Lekin / biroq'* polyakchada?",
             "opts": ["Chociaż", "Jednak", "Ponieważ", "Dlatego"], "ans": 1},
            {"q": "🔀 *'Pod warunkiem'* nima degani?",
             "opts": ["Aks holda", "Shart bilan", "Chunki", "Agar"], "ans": 1},
        ],
    },

    "a2_l04": {
        "title": "Kelishiklar — Akkuzativ",
        "emoji": "📐",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Akkuzativ — Kimni? Nimani?*\n\n"
            "*To'g'ri to'ldiruvchi* — fe'l ob'ekti\n"
            "Fe'llar: widzieć, lubić, mieć, kupić...\n\n"
            "*Erkak (shaxs):*\n"
            "• pracownik → pracownik*a*\n"
            "• lekarz → lekarz*a*\n\n"
            "*Erkak (narsa):* o'zgarmaydi!\n"
            "• dom → dom\n"
            "• chleb → chleb\n\n"
            "*Ayol:*\n"
            "• praca → prac*ę*\n"
            "• kawa → kaw*ę*\n\n"
            "*Neytral:* o'zgarmaydi!\n"
            "• miasto → miasto\n\n"
            "*Misollar:*\n"
            "→ *Widzę pracownika.* — Ishchini ko'raman.\n"
            "→ *Lubię kawę.* — Qahvani yaxshi ko'raman.\n"
            "→ *Mam dom.* — Uyim bor."
        ),
        "vocab": [
            {"pl": "Widzę...",         "ph": "VI-dze",           "uz": "Ko'raman..."},
            {"pl": "Lubię...",         "ph": "LU-bye",           "uz": "Yaxshi ko'raman..."},
            {"pl": "Znam...",          "ph": "znam",             "uz": "Bilaman..."},
            {"pl": "Spotykam...",      "ph": "spo-TY-kam",       "uz": "Uchrashtiraman..."},
            {"pl": "Czytam...",        "ph": "CHY-tam",          "uz": "O'qiyman..."},
            {"pl": "Słyszę...",        "ph": "SVY-she",          "uz": "Eshitaman..."},
            {"pl": "Piszę...",         "ph": "PI-she",           "uz": "Yozaman..."},
            {"pl": "Szukam...",        "ph": "SHU-kam",          "uz": "Qidiraman..."},
            {"pl": "Odwiedzam...",     "ph": "od-VYE-dzam",      "uz": "Tashrif buyuraman..."},
            {"pl": "Zapraszam...",     "ph": "za-PRA-sham",      "uz": "Taklif qilaman..."},
            {"pl": "pracownika",       "ph": "pra-tsov-NI-ka",   "uz": "ishchini (Akk.)"},
            {"pl": "kawę",             "ph": "KA-ve",            "uz": "qahvani (Akk.)"},
            {"pl": "lekarza",          "ph": "le-KA-zha",        "uz": "shifokorni (Akk.)"},
            {"pl": "siostrę",          "ph": "SHOSH-tre",        "uz": "opani (Akk.)"},
            {"pl": "nową pracę",       "ph": "NO-vo PRA-tse",    "uz": "yangi ishni (Akk.)"},
        ],
        "dialog": (
            "💬 *Dialog: Akkuzativ amaliyot*\n\n"
            "👩 *Kogo znasz w Polsce?*\n"
            "🧑 *Znam kilku kolegów z pracy.*\n"
            "   *I znam jedną Polkę — Annę.*\n"
            "👩 *Co lubisz w Polsce?*\n"
            "🧑 *Lubię polską kuchnię i muzykę.*\n"
            "   *Lubię też spacery po parku.*\n"
            "👩 *A co lubisz jeść?*\n"
            "🧑 *Lubię żurek, bigos i pierogi.*\n\n"
            "📝 *Tarjima:*\n"
            "👩 Polshada kimni bilasiz?\n"
            "🧑 Ishdan bir necha hamkasbni bilaman. Va bir polyak ayolni — Annani.\n"
            "👩 Polshada nimani yaxshi ko'rasiz?\n"
            "🧑 Polyak taomi va musiqasini yaxshi ko'raman. Parkda sayr qilishni ham.\n"
            "👩 Nima yeyishni yaxshi ko'rasiz?\n"
            "🧑 Sho'rva, bigos va pierogini yaxshi ko'raman."
        ),
        "exercises": [
            {"q": "📐 *'Kawę'* qaysi kelishikda?",
             "opts": ["Nominativ", "Akkuzativ", "Genitiv", "Dativ"], "ans": 1},
            {"q": "📐 *'Lubię kawę'* — 'kawę' qaysi forma?",
             "opts": ["kawa", "kawy", "kawę", "kawie"], "ans": 2},
            {"q": "🇺🇿 *'Ishchini ko'raman'* polyakchada?",
             "opts": ["Widzę pracownik", "Widzę pracownika", "Widzę pracowniku", "Widzę pracownicy"], "ans": 1},
            {"q": "📐 Ayol otlar Akkuzativda qanday tugaydi?",
             "opts": ["-i", "-ę", "-a", "-e"], "ans": 1},
            {"q": "📐 *'Siostrę'* — bu qaysi ot?",
             "opts": ["Brat", "Mama", "Siostra", "Córka"], "ans": 2},
            {"q": "🇺🇿 *'Qahvani yaxshi ko'raman'* polyakchada?",
             "opts": ["Lubię kawa", "Lubię kawy", "Lubię kawę", "Lubię kawie"], "ans": 2},
            {"q": "📐 Erkak narsa Akkuzativda qanday o'zgaradi?",
             "opts": ["O'zgarmaydi", "-a qo'shiladi", "-ę qo'shiladi", "-i qo'shiladi"], "ans": 0},
            {"q": "📐 *'Lekarza'* — bu qaysi kelishik?",
             "opts": ["Nominativ", "Genitiv", "Akkuzativ", "Dativ"], "ans": 2},
            {"q": "🇺🇿 *'Ko'raman'* polyakchada?",
             "opts": ["Słyszę", "Widzę", "Znam", "Czytam"], "ans": 1},
            {"q": "📐 *'Nową pracę'* nima degani?",
             "opts": ["Yangi ish (Nom.)", "Yangi ishda", "Yangi ishni (Akk.)", "Yangi ishdan"], "ans": 2},
        ],
    },

    "a2_l05": {
        "title": "Kelishiklar — Genitiv",
        "emoji": "📎",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Genitiv — Kimning? Yo'qlik*\n\n"
            "*Qachon ishlatiladi:*\n"
            "1. Inkor: *Nie mam + Genitiv*\n"
            "2. Tegishlilik: ...ning\n"
            "3. Miqdor: dużo, mało, ile\n"
            "4. Prepositionlar: do, z, od, dla, bez\n\n"
            "*Shakllari:*\n"
            "• dom → dom*u* (uyning/uysiz)\n"
            "• szef → szef*a*\n"
            "• praca → prac*y*\n"
            "• kawa → kaw*y*\n"
            "• miasto → mias*ta*\n\n"
            "*Misollar:*\n"
            "→ *Nie mam pracy.* — Ishim yo'q.\n"
            "→ *Klucz szefa.* — Boshliqdniki kalit.\n"
            "→ *Dużo czasu.* — Ko'p vaqt.\n"
            "→ *Idę do domu.* — Uyga boraman."
        ),
        "vocab": [
            {"pl": "Nie mam...",      "ph": "nye mam",          "uz": "Menda ... yo'q"},
            {"pl": "Szukam...",       "ph": "SHU-kam",          "uz": "... qidiraman"},
            {"pl": "Do domu",         "ph": "do DO-mu",         "uz": "Uyga"},
            {"pl": "Z pracy",         "ph": "z PRA-tsi",        "uz": "Ishdan"},
            {"pl": "Bez pieniędzy",   "ph": "bes pye-NYEN-dzy", "uz": "Pulsiz"},
            {"pl": "Dla rodziny",     "ph": "dla ro-DJI-ni",    "uz": "Oila uchun"},
            {"pl": "Od szefa",        "ph": "od SHE-fa",        "uz": "Boshliqdan"},
            {"pl": "Dużo czasu",      "ph": "DU-zho CHA-su",    "uz": "Ko'p vaqt"},
            {"pl": "Mało pieniędzy",  "ph": "MA-vo pye-NYEN-dzy","uz": "Oz pul"},
            {"pl": "pracy",           "ph": "PRA-tsi",          "uz": "ishning (Gen.)"},
            {"pl": "domu",            "ph": "DO-mu",            "uz": "uyning (Gen.)"},
            {"pl": "kawy",            "ph": "KA-vi",            "uz": "qahvaning (Gen.)"},
            {"pl": "czasu",           "ph": "CHA-su",           "uz": "vaqtning (Gen.)"},
            {"pl": "pieniędzy",       "ph": "pye-NYEN-dzy",     "uz": "pulning (Gen.)"},
            {"pl": "Nie mam pojęcia", "ph": "nye mam po-YEN-cha","uz": "Bilmayman / Tushuncham yo'q"},
        ],
        "dialog": (
            "💬 *Dialog: Genitiv amaliyot*\n\n"
            "👩 *Skąd jesteś?*\n"
            "🧑 *Jestem z Uzbekistanu, z Taszkentu.*\n"
            "👩 *Czy masz rodzinę w Polsce?*\n"
            "🧑 *Nie mam rodziny tutaj.*\n"
            "   *Moja rodzina jest w Uzbekistanie.*\n"
            "👩 *Czy masz dużo czasu wolnego?*\n"
            "🧑 *Nie, nie mam dużo czasu.*\n"
            "   *Pracuję od rana do wieczora.*\n\n"
            "📝 *Tarjima:*\n"
            "👩 Qayerdansiz?\n"
            "🧑 O'zbekistondan, Toshkentdan.\n"
            "👩 Polshada oilangiz bormi?\n"
            "🧑 Bu yerda oilam yo'q. Oilam O'zbekistonda.\n"
            "👩 Ko'p bo'sh vaqtingiz bormi?\n"
            "🧑 Yo'q, vaqtim ko'p emas. Ertalabdan kechgacha ishlayman."
        ),
        "exercises": [
            {"q": "📎 *'Nie mam pracy'* — 'pracy' qaysi forma?",
             "opts": ["Nominativ", "Akkuzativ", "Genitiv", "Dativ"], "ans": 2},
            {"q": "📎 *'Do domu'* nima degani?",
             "opts": ["Uyda", "Uyga", "Uydan", "Uy uchun"], "ans": 1},
            {"q": "🇺🇿 *'Ishim yo'q'* polyakchada?",
             "opts": ["Nie mam praca", "Nie mam pracy", "Nie mam pracę", "Nie mam prace"], "ans": 1},
            {"q": "📎 *'Bez pieniędzy'* nima degani?",
             "opts": ["Pul bilan", "Pul uchun", "Pulsiz", "Puldan"], "ans": 2},
            {"q": "📎 *'Dużo czasu'* nima degani?",
             "opts": ["Oz vaqt", "Ko'p vaqt", "Vaqtsiz", "Vaqt uchun"], "ans": 1},
            {"q": "🇺🇿 *'Boshliqdan'* polyakchada?",
             "opts": ["Do szefa", "Od szefa", "Dla szefa", "Bez szefa"], "ans": 1},
            {"q": "📎 *'Dla rodziny'* nima degani?",
             "opts": ["Oiladan", "Oilada", "Oilaga", "Oila uchun"], "ans": 3},
            {"q": "📎 Erkak otlar Genitivda qanday tugaydi?",
             "opts": ["-a / -u", "-ę", "-i / -y", "-e"], "ans": 0},
            {"q": "🇺🇿 *'Bilmayman'* polyakchada?",
             "opts": ["Nie wiem", "Nie mam pojęcia", "Nie rozumiem", "Barchasi to'g'ri"], "ans": 1},
            {"q": "📎 *'Z pracy'* nima degani?",
             "opts": ["Ishga", "Ishda", "Ishdan", "Ish uchun"], "ans": 2},
        ],
    },

    "a2_l06": {
        "title": "Kelishiklar — Dativ va Instrumental",
        "emoji": "🔧",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Dativ va Instrumental*\n\n"
            "*DATIV — Kimga?*\n"
            "Fe'llar: dać, mówić, pomagać, kupować\n\n"
            "• szef → szefow*i*\n"
            "• mama → mam*ie*\n"
            "• dziecko → dzieck*u*\n\n"
            "→ *Dałem szefowi dokument.*\n"
            "   Boshliqqа hujjat berdim.\n\n"
            "*INSTRUMENTAL — Kim/Nima bilan?*\n"
            "Kasb + Vosita\n\n"
            "• pracownik → pracownik*iem*\n"
            "• kobieta → kobiet*ą*\n\n"
            "→ *Jestem pracownikiem.* — Ishchiman.\n"
            "→ *Jadę autobusem.* — Avtobus bilan.\n"
            "→ *Rozmawiam z szefem.* — Boshliq bilan."
        ),
        "vocab": [
            {"pl": "Daję...",           "ph": "DA-ye",             "uz": "Beraman..."},
            {"pl": "Mówię...",          "ph": "MU-vye",            "uz": "Gapriman..."},
            {"pl": "Pomagam...",        "ph": "po-MA-gam",         "uz": "Yordam beraman..."},
            {"pl": "Dziękuję...",       "ph": "djen-KU-ye",        "uz": "Rahmat aytaman..."},
            {"pl": "szefowi",           "ph": "she-FO-vi",         "uz": "boshliqqa (Dat.)"},
            {"pl": "mamie",             "ph": "MA-mye",            "uz": "onaga (Dat.)"},
            {"pl": "dziecku",           "ph": "DJETS-ku",          "uz": "bolaga (Dat.)"},
            {"pl": "koledze",           "ph": "ko-LE-dze",         "uz": "hamkasbga (Dat.)"},
            {"pl": "Jestem kierowcą",   "ph": "YES-tem kye-ROV-tson","uz": "Haydovchiman (Instr.)"},
            {"pl": "Jadę autobusem",    "ph": "YA-de av-to-BU-sem","uz": "Avtobus bilan boraman"},
            {"pl": "Płacę kartą",       "ph": "PVA-tse KAR-ton",   "uz": "Karta bilan to'layman"},
            {"pl": "z kolegą",          "ph": "z ko-LE-gon",       "uz": "hamkasb bilan (Instr.)"},
            {"pl": "z żoną",            "ph": "z ZHO-non",         "uz": "xotin bilan (Instr.)"},
            {"pl": "między nami",       "ph": "MYEN-dzy NA-mi",    "uz": "aramizda (Instr.)"},
            {"pl": "przed domem",       "ph": "pshed DO-mem",      "uz": "uy oldida (Instr.)"},
        ],
        "dialog": (
            "💬 *Dialog: Instrumental*\n\n"
            "👔 *Kim Pan jest z zawodu?*\n"
            "🧑 *Jestem spawaczem. Mam 10 lat doświadczenia.*\n"
            "👔 *Czym Pan przyjeżdża do pracy?*\n"
            "🧑 *Przyjeżdżam autobusem. Nie mam samochodu.*\n"
            "👔 *Z kim Pan mieszka?*\n"
            "🧑 *Mieszkam z kolegą z pracy.*\n"
            "   *Dzielimy mieszkanie.*\n\n"
            "📝 *Tarjima:*\n"
            "👔 Kasbingiz nima?\n"
            "🧑 Men payvandchiman. 10 yillik tajribam bor.\n"
            "👔 Ishga nima bilan kelasiz?\n"
            "🧑 Avtobus bilan kelaman. Mashinam yo'q.\n"
            "👔 Kim bilan yashaysiz?\n"
            "🧑 Ish hamkasb bilan yashaman. Kvartira bo'lishamiz."
        ),
        "exercises": [
            {"q": "🔧 *'Jestem spawaczem'* — bu qaysi kelishik?",
             "opts": ["Nominativ", "Akkuzativ", "Dativ", "Instrumental"], "ans": 3},
            {"q": "🔧 *'Szefowi'* qaysi kelishikda?",
             "opts": ["Nominativ", "Akkuzativ", "Dativ", "Instrumental"], "ans": 2},
            {"q": "🇺🇿 *'Avtobus bilan boraman'* polyakchada?",
             "opts": ["Jadę autobus", "Jadę autobusu", "Jadę autobusem", "Jadę autobusie"], "ans": 2},
            {"q": "🔧 *'Płacę kartą'* nima degani?",
             "opts": ["Karta bormi?", "Karta bilan to'layman", "Kartam yo'q", "Karta kerak"], "ans": 1},
            {"q": "🔧 *'Z żoną'* nima degani?",
             "opts": ["Xotinsiz", "Xotinga", "Xotin bilan", "Xotindan"], "ans": 2},
            {"q": "🇺🇿 *'Haydovchiman'* (ayol) polyakchada?",
             "opts": ["Jestem kierowca", "Jestem kierowcą", "Jestem kierowcy", "Jestem kierowce"], "ans": 1},
            {"q": "🔧 *'Mamie'* qaysi kelishikda?",
             "opts": ["Nominativ", "Akkuzativ", "Dativ", "Instrumental"], "ans": 2},
            {"q": "🔧 *'Między nami'* nima degani?",
             "opts": ["Biz uchun", "Bizdan", "Aramizda", "Bizga"], "ans": 2},
            {"q": "🇺🇿 *'Boshliqqa berdim'* polyakchada?",
             "opts": ["Dałem szefa", "Dałem szefowi", "Dałem szefem", "Dałem szefie"], "ans": 1},
            {"q": "🔧 *'Przed domem'* nima degani?",
             "opts": ["Uy orqasida", "Uy ichida", "Uy oldida", "Uy yonida"], "ans": 2},
        ],
    },

    "a2_l07": {
        "title": "Restoran va Mehmonxona",
        "emoji": "🍴",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Xushmuomalalik shakllari*\n\n"
            "*Buyurtma qilish:*\n"
            "• *Poproszę...* — ...bering (iltimos)\n"
            "• *Czy mogę prosić o...?* — ...so'rasam bo'ladimi?\n"
            "• *Chciałbym...* — ...olmoq edim (erk.)\n"
            "• *Chciałabym...* — ...olmoq edim (ay.)\n\n"
            "*Tavsiya so'rash:*\n"
            "• *Co Pan poleca?* — Nimani tavsiya qilasiz?\n"
            "• *Jaka jest specjalność?* — Maxsus taom nima?\n\n"
            "*Shikoyat:*\n"
            "• *Przepraszam, to nie jest...* — Bu... emas\n"
            "• *Zimne jest.* — Sovuq.\n"
            "• *Proszę o rachunek.* — Hisob bering."
        ),
        "vocab": [
            {"pl": "rezerwacja",        "ph": "re-zer-VATS-ya",    "uz": "bron"},
            {"pl": "stolik",            "ph": "STO-lik",           "uz": "stol (restoran)"},
            {"pl": "menu / karta dań",  "ph": "me-NU",             "uz": "menyu"},
            {"pl": "danie główne",      "ph": "DA-nye GVUV-ne",    "uz": "asosiy taom"},
            {"pl": "zupa dnia",         "ph": "ZU-pa dnya",        "uz": "kunlik sho'rva"},
            {"pl": "deser",             "ph": "DE-ser",            "uz": "desert"},
            {"pl": "napój",             "ph": "NA-puy",            "uz": "ichimlik"},
            {"pl": "napiwek",           "ph": "na-PI-vek",         "uz": "choy puli (tip)"},
            {"pl": "zamówienie",        "ph": "za-mu-VYE-nye",     "uz": "buyurtma"},
            {"pl": "Smacznego!",        "ph": "smach-NE-go",       "uz": "Yaxshi ishtaha!"},
            {"pl": "Na zdrowie!",       "ph": "na ZDRO-vye",       "uz": "Sog'ligingizga!"},
            {"pl": "Co Pan poleca?",    "ph": "tso pan po-LE-tsa", "uz": "Nimani tavsiya qilasiz?"},
            {"pl": "Proszę o rachunek", "ph": "PRO-she o ra-HU-nek","uz": "Hisob bering"},
            {"pl": "Czy mogę...?",      "ph": "chi MO-ge",         "uz": "...qilsam bo'ladimi?"},
            {"pl": "Chciałbym...",      "ph": "HCHAV-bim",         "uz": "...olmoq edim (erk.)"},
        ],
        "dialog": (
            "💬 *Dialog: Restoranda*\n\n"
            "🧑 *Dzień dobry. Mam rezerwację na nazwisko Karimov.*\n"
            "🍽️ *Proszę tędy. Oto menu.*\n"
            "🧑 *Co Pan poleca?*\n"
            "🍽️ *Polecam żurek i schabowego.*\n"
            "   *To są nasze specjalności.*\n"
            "🧑 *Poproszę żurek i schabowego z ziemniakami.*\n"
            "   *I wodę mineralną, proszę.*\n"
            "🍽️ *Już podaję. Smacznego!*\n"
            "🧑 *Dziękuję. Proszę o rachunek.*\n"
            "🍽️ *Sto dwadzieścia złotych.*\n\n"
            "📝 *Tarjima:*\n"
            "🧑 Xayrli kun. Karimov ismiga bron qilganman.\n"
            "🍽️ Bu tomonga. Mana menyu.\n"
            "🧑 Nimani tavsiya qilasiz?\n"
            "🍽️ Sho'rva va kotletni tavsiya qilaman. Bizning maxsus taomlar.\n"
            "🧑 Sho'rva, kartoshkali kotlet va mineral suv bering.\n"
            "🍽️ Hozir keltiraman. Yaxshi ishtaha!\n"
            "🧑 Rahmat. Hisob bering.\n"
            "🍽️ Yuz yigirma zloty."
        ),
        "exercises": [
            {"q": "🍴 *'Rezerwacja'* nima degani?",
             "opts": ["Buyurtma", "Bron", "Ro'yxat", "Chipta"], "ans": 1},
            {"q": "🍴 *'Danie główne'* nima degani?",
             "opts": ["Desert", "Asosiy taom", "Sho'rva", "Ichimlik"], "ans": 1},
            {"q": "🇺🇿 *'Yaxshi ishtaha!'* polyakchada?",
             "opts": ["Na zdrowie!", "Smacznego!", "Dziękuję!", "Proszę!"], "ans": 1},
            {"q": "🍴 *'Napiwek'* nima degani?",
             "opts": ["Ichimlik", "Hisob", "Choy puli (tip)", "Chegirma"], "ans": 2},
            {"q": "🍴 *'Co Pan poleca?'* nima degani?",
             "opts": ["Buyurtma bormi?", "Nimani tavsiya qilasiz?", "Hisob bormi?", "Menyu bormi?"], "ans": 1},
            {"q": "🇺🇿 *'Hisob bering'* polyakchada?",
             "opts": ["Proszę menu", "Proszę o rachunek", "Proszę stolik", "Proszę deser"], "ans": 1},
            {"q": "🍴 *'Chciałbym...'* nima degani?",
             "opts": ["...kerak", "...yaxshi ko'raman", "...olmoq edim (erk.)", "...boraman"], "ans": 2},
            {"q": "🍴 *'Zamówienie'* nima degani?",
             "opts": ["Bron", "Buyurtma", "Hisob", "Menyu"], "ans": 1},
            {"q": "🇺🇿 *'Sog'ligingizga!'* polyakchada?",
             "opts": ["Smacznego!", "Dziękuję!", "Na zdrowie!", "Proszę!"], "ans": 2},
            {"q": "🍴 *'Czy mogę...?'* nima degani?",
             "opts": ["...kerak", "...mumkin", "...qilsam bo'ladimi?", "...xohlayman"], "ans": 2},
        ],
    },

    "a2_l08": {
        "title": "Sport va Hobbi",
        "emoji": "⚽",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Hobbi va sport haqida gapirish*\n\n"
            "*Grać w + sport (Akkuzativ):*\n"
            "→ *Gram w piłkę nożną.* — Futbol o'ynayman.\n"
            "→ *Gram w karty.* — Karta o'ynayman.\n\n"
            "*Uprawiać + sport:*\n"
            "→ *Uprawiam sport.* — Sport bilan shug'ullanaman.\n"
            "→ *Uprawiam boks.* — Boks bilan.\n\n"
            "*Lubić + infinitiv:*\n"
            "→ *Lubię biegać.* — Yugurish yoqtiraman.\n"
            "→ *Lubię pływać.* — Suzish yoqtiraman.\n\n"
            "*Pasja:*\n"
            "→ *Moją pasją jest muzyka.*\n"
            "   Mening ehtirosim — musiqa."
        ),
        "vocab": [
            {"pl": "piłka nożna",       "ph": "PIL-ka NOZH-na",    "uz": "futbol"},
            {"pl": "siatkówka",         "ph": "shat-KUV-ka",       "uz": "voleybol"},
            {"pl": "koszykówka",        "ph": "ko-shi-KUV-ka",     "uz": "basketbol"},
            {"pl": "tenis",             "ph": "TE-nis",            "uz": "tennis"},
            {"pl": "pływanie",          "ph": "pvy-VA-nye",        "uz": "suzish"},
            {"pl": "bieganie",          "ph": "bye-GA-nye",        "uz": "yugurish"},
            {"pl": "siłownia",          "ph": "shi-VOV-nya",       "uz": "sport zali"},
            {"pl": "rower",             "ph": "RO-ver",            "uz": "velosiped"},
            {"pl": "muzyka",            "ph": "MU-zy-ka",          "uz": "musiqa"},
            {"pl": "czytanie",          "ph": "chi-TA-nye",        "uz": "kitob o'qish"},
            {"pl": "gotowanie",         "ph": "go-to-VA-nye",      "uz": "oshpazlik"},
            {"pl": "podróże",           "ph": "pod-RU-zhe",        "uz": "sayohat"},
            {"pl": "fotografia",        "ph": "fo-to-GRA-fya",     "uz": "fotografiya"},
            {"pl": "gram w...",         "ph": "gram v",            "uz": "...o'ynayman"},
            {"pl": "Mam wolny czas",    "ph": "mam VOL-ni chas",   "uz": "Bo'sh vaqtim bor"},
        ],
        "dialog": (
            "💬 *Dialog: Hobbi haqida*\n\n"
            "👩 *Co lubisz robić w wolnym czasie?*\n"
            "🧑 *Lubię grać w piłkę nożną i czytać.*\n"
            "   *W weekend często chodzę na siłownię.*\n"
            "👩 *Czy interesujesz się muzyką?*\n"
            "🧑 *Tak! Słucham różnej muzyki.*\n"
            "   *Lubię muzykę jazzową i rockową.*\n"
            "👩 *A jakie sporty uprawiasz zimą?*\n"
            "🧑 *Zimą chodzę na basen.*\n"
            "   *Lubię pływać.*\n\n"
            "📝 *Tarjima:*\n"
            "👩 Bo'sh vaqtingizda nima qilishni yaxshi ko'rasiz?\n"
            "🧑 Futbol o'ynash va kitob o'qishni yaxshi ko'raman. Dam olish kunlari ko'pincha sport zaliga boraman.\n"
            "👩 Musiqaga qiziqasizmi?\n"
            "🧑 Ha! Turli musiqani tinglyman. Jazz va rokni yaxshi ko'raman.\n"
            "👩 Qishda qanday sport bilan shug'ullanasiz?\n"
            "🧑 Qishda havzaga boraman. Suzishni yaxshi ko'raman."
        ),
        "exercises": [
            {"q": "⚽ *'Piłka nożna'* nima degani?",
             "opts": ["Voleybol", "Basketbol", "Futbol", "Tennis"], "ans": 2},
            {"q": "⚽ *'Pływanie'* nima degani?",
             "opts": ["Yugurish", "Suzish", "Velosiped", "Sakrash"], "ans": 1},
            {"q": "🇺🇿 *'Yugurish'* polyakchada?",
             "opts": ["Pływanie", "Bieganie", "Jazda", "Chodzenie"], "ans": 1},
            {"q": "⚽ *'Siłownia'* nima degani?",
             "opts": ["Stadion", "Havza", "Sport zali", "Park"], "ans": 2},
            {"q": "⚽ *'Gram w piłkę nożną'* nima degani?",
             "opts": ["Futbol ko'raman", "Futbol o'ynayman", "Futbol yaxshi ko'raman", "Futbolga boraman"], "ans": 1},
            {"q": "🇺🇿 *'Sayohat'* polyakchada?",
             "opts": ["Muzyka", "Czytanie", "Podróże", "Gotowanie"], "ans": 2},
            {"q": "⚽ *'Gotowanie'* nima degani?",
             "opts": ["Kitob o'qish", "Oshpazlik", "Fotografiya", "Rasm chizish"], "ans": 1},
            {"q": "⚽ *'Siatkówka'* nima degani?",
             "opts": ["Futbol", "Tennis", "Voleybol", "Basketbol"], "ans": 2},
            {"q": "🇺🇿 *'Bo'sh vaqtim bor'* polyakchada?",
             "opts": ["Nie mam czasu", "Mam dużo pracy", "Mam wolny czas", "Mam czas pracy"], "ans": 2},
            {"q": "⚽ *'Lubię pływać'* nima degani?",
             "opts": ["Suzganman", "Suzishni yaxshi ko'raman", "Suzayman", "Suzmoqchiman"], "ans": 1},
        ],
    },

    "a2_l09": {
        "title": "Sayohat",
        "emoji": "✈️",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Sayohat haqida gapirish*\n\n"
            "*Sayohat fe'llari:*\n"
            "• *podróżować* — sayohat qilmoq\n"
            "• *zwiedzać* — ko'rib chiqmoq\n"
            "• *rezerwować* — bron qilmoq\n"
            "• *pakować* — narsalarni joylash\n\n"
            "*Qaerda bo'lganini aytish:*\n"
            "→ *Byłem w Krakowie.* — Krakovda bo'ldim.\n"
            "→ *Pojechałem do Paryża.* — Parijga bordim.\n\n"
            "*Taassurot:*\n"
            "→ *Podobało mi się.* — Yoqdi.\n"
            "→ *Nie podobało mi się.* — Yoqmadi.\n"
            "→ *Było wspaniale!* — Zo'r bo'ldi!"
        ),
        "vocab": [
            {"pl": "podróż",            "ph": "POD-rush",          "uz": "sayohat"},
            {"pl": "wakacje",           "ph": "va-KATS-ye",        "uz": "ta'til (sayohat)"},
            {"pl": "hotel",             "ph": "ho-TEL",            "uz": "mehmonxona"},
            {"pl": "hostel",            "ph": "HOS-tel",           "uz": "xobgoh (hostel)"},
            {"pl": "walizka",           "ph": "va-LIS-ka",         "uz": "chemodan"},
            {"pl": "paszport",          "ph": "PAS-port",          "uz": "pasport"},
            {"pl": "mapa",              "ph": "MA-pa",             "uz": "xarita"},
            {"pl": "zwiedzanie",        "ph": "zvye-DZA-nye",      "uz": "ko'rib chiqish"},
            {"pl": "muzeum",            "ph": "mu-ZE-um",          "uz": "muzey"},
            {"pl": "zamek",             "ph": "ZA-mek",            "uz": "qal'a / zamok"},
            {"pl": "kościół",           "ph": "KOSH-chuw",         "uz": "cherkov"},
            {"pl": "plaża",             "ph": "PLA-zha",           "uz": "plyaj"},
            {"pl": "Podobało mi się",   "ph": "po-do-BA-vo mi she","uz": "Yoqdi"},
            {"pl": "Było wspaniale",    "ph": "BY-vo vspa-NYA-le", "uz": "Zo'r bo'ldi"},
            {"pl": "pamiątka",          "ph": "pa-MYON-tka",       "uz": "sovg'a (yodgorlik)"},
        ],
        "dialog": (
            "💬 *Dialog: Ta'tildan qaytish*\n\n"
            "👩 *Skąd wróciłeś? Byłeś na wakacjach?*\n"
            "🧑 *Tak! Byłem w Krakowie przez weekend.*\n"
            "👩 *I jak było?*\n"
            "🧑 *Było wspaniale! Zwiedziłem Wawel i Rynek Główny.*\n"
            "   *Jadłem żurek i pierogi. Było pyszne!*\n"
            "👩 *Gdzie nocowałeś?*\n"
            "🧑 *W hostelu w centrum. Bardzo tanio!*\n"
            "   *Polecam Kraków wszystkim.*\n\n"
            "📝 *Tarjima:*\n"
            "👩 Qaerdan qaytding? Ta'ilda bo'ldingmi?\n"
            "🧑 Ha! Dam olish kunlari Krakovda bo'ldim.\n"
            "👩 Qanday bo'ldi?\n"
            "🧑 Zo'r bo'ldi! Vavel va Bosh maydonni ko'rdim. Sho'rva va pierogi yedim. Juda mazali!\n"
            "👩 Qaerda qolding?\n"
            "🧑 Markazdagi xobgohda. Juda arzon! Krakovni hamma uchun tavsiya qilaman."
        ),
        "exercises": [
            {"q": "✈️ *'Wakacje'* nima degani?",
             "opts": ["Ish safari", "Ta'til (sayohat)", "Dam olish kuni", "Bayram"], "ans": 1},
            {"q": "✈️ *'Walizka'* nima degani?",
             "opts": ["Sumka", "Ryuksak", "Chemodan", "Quti"], "ans": 2},
            {"q": "🇺🇿 *'Muzey'* polyakchada?",
             "opts": ["Zamek", "Muzeum", "Kościół", "Rynek"], "ans": 1},
            {"q": "✈️ *'Podobało mi się'* nima degani?",
             "opts": ["Yoqmadi", "Zo'r bo'ldi", "Yoqdi", "Qiziq emas"], "ans": 2},
            {"q": "✈️ *'Zwiedzanie'* nima degani?",
             "opts": ["Sayohat", "Ko'rib chiqish", "Qolish", "Ketish"], "ans": 1},
            {"q": "🇺🇿 *'Qal'a / zamok'* polyakchada?",
             "opts": ["Muzeum", "Kościół", "Zamek", "Plaża"], "ans": 2},
            {"q": "✈️ *'Było wspaniale!'* nima degani?",
             "opts": ["Yomon bo'ldi!", "Zo'r bo'ldi!", "O'rtacha bo'ldi!", "Qiyin bo'ldi!"], "ans": 1},
            {"q": "✈️ *'Pamiątka'* nima degani?",
             "opts": ["Xarita", "Chipta", "Sovg'a (yodgorlik)", "Pasport"], "ans": 2},
            {"q": "🇺🇿 *'Plyaj'* polyakchada?",
             "opts": ["Park", "Zamek", "Plaża", "Góra"], "ans": 2},
            {"q": "✈️ *'Zwiedziłem Wawel'* nima degani?",
             "opts": ["Vavelga bormoqchiman", "Vavelni ko'rdim", "Vavelda yashayman", "Vavelni bilaman"], "ans": 1},
        ],
    },

    "a2_l10": {
        "title": "Mehnat Huquqi",
        "emoji": "⚖️",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Huquq va majburiyat*\n\n"
            "*Majburiyat:*\n"
            "• *musieć* — majbur bo'lmoq\n"
            "→ *Muszę przyjść.* — Kelishim shart.\n\n"
            "*Ruxsat:*\n"
            "• *móc* — qila olmoq / mumkin\n"
            "→ *Mogę wziąć urlop.* — Ta'til olsam bo'ladi.\n\n"
            "*Taqiq:*\n"
            "→ *Nie wolno...* — ...mumkin emas\n"
            "→ *Nie można...* — ...bo'lmaydi\n\n"
            "*Huquq:*\n"
            "→ *Mam prawo do...* — ...ga huquqim bor\n"
            "→ *Przysługuje mi...* — ...ga haqim bor"
        ),
        "vocab": [
            {"pl": "kodeks pracy",       "ph": "KO-deks PRA-tsi",     "uz": "mehnat qonuni"},
            {"pl": "urlop wypoczynkowy", "ph": "UR-lop vy-po-CHIN-ko-vi","uz": "dam olish ta'tili"},
            {"pl": "urlop chorobowy",    "ph": "UR-lop ho-ro-BO-vi",  "uz": "kasallik ta'tili"},
            {"pl": "zwolnienie lekarskie","ph": "zvol-NYE-nye le-KAR-skye","uz": "kasallik varag'i"},
            {"pl": "minimalna stawka",   "ph": "mi-ni-MAL-na STAV-ka","uz": "minimal ish haqi"},
            {"pl": "umowa o pracę",      "ph": "u-MO-va o PRA-tse",   "uz": "ish shartnomasi"},
            {"pl": "ZUS",                "ph": "zus",                  "uz": "ijtimoiy sug'urta"},
            {"pl": "NFZ",                "ph": "en-ef-zet",            "uz": "sog'liq sug'urtasi"},
            {"pl": "wypowiedzenie",      "ph": "vy-po-vye-DZE-nye",   "uz": "iste'fo / xatnoma"},
            {"pl": "Mam prawo do...",    "ph": "mam PRA-vo do",        "uz": "...ga huquqim bor"},
            {"pl": "Muszę...",           "ph": "MU-she",               "uz": "...majburman"},
            {"pl": "Nie wolno...",       "ph": "nye VOL-no",           "uz": "...mumkin emas"},
            {"pl": "ochrona pracy",      "ph": "oh-RO-na PRA-tsi",    "uz": "mehnatni muhofaza"},
            {"pl": "inspekcja pracy",    "ph": "ins-PEKTS-ya PRA-tsi","uz": "mehnat inspeksiyasi"},
            {"pl": "wypadek przy pracy", "ph": "vy-PA-dek pshi PRA-tsi","uz": "ish joyi baxtsiz hodisа"},
        ],
        "dialog": (
            "💬 *Dialog: Ish huquqi*\n\n"
            "🧑 *Przepraszam, ile dni urlopu mi przysługuje?*\n"
            "👔 *Przy umowie na czas nieokreślony —*\n"
            "   *dwadzieścia lub dwadzieścia sześć dni.*\n"
            "🧑 *Od czego to zależy?*\n"
            "👔 *Od stażu pracy. Jeśli pracujesz krócej niż 10 lat — 20 dni.*\n"
            "   *Jeśli dłużej — 26 dni.*\n"
            "🧑 *A co z nadgodzinami?*\n"
            "👔 *Za nadgodziny przysługuje dodatek lub wolny dzień.*\n\n"
            "📝 *Tarjima:*\n"
            "🧑 Kechirasiz, necha kun ta'til oling huquqim bor?\n"
            "👔 Muddatsiz shartnomada — yigirma yoki yigirma olti kun.\n"
            "🧑 Bu nimaga bog'liq?\n"
            "👔 Ish stajiga. 10 yildan kam bo'lsa — 20 kun. Ko'proq bo'lsa — 26 kun.\n"
            "🧑 Qo'shimcha soatlar haqida-chi?\n"
            "👔 Qo'shimcha soatlar uchun qo'shimcha to'lov yoki dam olish kuni beriladi."
        ),
        "exercises": [
            {"q": "⚖️ *'Kodeks pracy'* nima degani?",
             "opts": ["Ish shartnomasi", "Mehnat qonuni", "Ish jadvali", "Ish haqi"], "ans": 1},
            {"q": "⚖️ *'Urlop chorobowy'* nima degani?",
             "opts": ["Dam olish ta'tili", "Kasallik ta'tili", "Onlik ta'til", "Bola parvarish"], "ans": 1},
            {"q": "🇺🇿 *'Ijtimoiy sug'urta'* polyakchada?",
             "opts": ["NFZ", "ZUS", "PIT", "NIP"], "ans": 1},
            {"q": "⚖️ *'Mam prawo do...'* nima degani?",
             "opts": ["...majburman", "...ga huquqim bor", "...mumkin emas", "...xohlayman"], "ans": 1},
            {"q": "⚖️ *'Nie wolno'* nima degani?",
             "opts": ["Mumkin", "Shart", "Mumkin emas", "Kerak"], "ans": 2},
            {"q": "🇺🇿 *'Iste'fo'* polyakchada?",
             "opts": ["Umowa", "Wypowiedzenie", "Urlop", "Zwolnienie"], "ans": 1},
            {"q": "⚖️ *'Minimalna stawka'* nima degani?",
             "opts": ["Maksimal ish haqi", "Minimal ish haqi", "O'rtacha maosh", "Bonus"], "ans": 1},
            {"q": "⚖️ *'Muszę...'* nima degani?",
             "opts": ["...qila olaman", "...xohlayman", "...majburman", "...mumkin"], "ans": 2},
            {"q": "🇺🇿 *'Sog'liq sug'urtasi'* polyakchada?",
             "opts": ["ZUS", "NFZ", "PIT", "PESEL"], "ans": 1},
            {"q": "⚖️ *'Wypadek przy pracy'* nima degani?",
             "opts": ["Ish jadvali", "Ish haqi", "Ish joyi baxtsiz hodisa", "Ish ta'tili"], "ans": 2},
        ],
    },

    "a2_l11": {
        "title": "Soliq va Hujjatlar",
        "emoji": "🧾",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Rasmiy hujjat tili*\n\n"
            "*Rasmiy so'rash:*\n"
            "→ *Chciałbym złożyć...* — ...topshirmoqchiman\n"
            "→ *Proszę o...* — ...so'rayman\n"
            "→ *Potrzebuję...* — ...kerak\n\n"
            "*Zarur iboralar:*\n"
            "→ *Kiedy będzie gotowe?* — Qachon tayyor?\n"
            "→ *Ile to kosztuje?* — Qancha turadi?\n"
            "→ *Jakie dokumenty są potrzebne?*\n"
            "   — Qanday hujjatlar kerak?\n\n"
            "*Raqamlar:*\n"
            "• *PESEL* — shaxsiy raqam\n"
            "• *NIP* — soliq raqami\n"
            "• *REGON* — tashkilot raqami"
        ),
        "vocab": [
            {"pl": "podatek",           "ph": "po-DA-tek",         "uz": "soliq"},
            {"pl": "PIT",               "ph": "pit",               "uz": "daromad solig'i (PIT)"},
            {"pl": "rozliczenie",       "ph": "roz-li-CHE-nye",    "uz": "hisob-kitob"},
            {"pl": "deklaracja",        "ph": "dek-la-RATS-ya",    "uz": "deklaratsiya"},
            {"pl": "urząd skarbowy",    "ph": "U-zhond skar-BO-vi","uz": "soliq idorasi"},
            {"pl": "zwrot podatku",     "ph": "zvrot po-DAT-ku",   "uz": "soliq qaytarish"},
            {"pl": "NIP",               "ph": "nip",               "uz": "soliq raqami"},
            {"pl": "faktura",           "ph": "fak-TU-ra",         "uz": "faktura (hujjat)"},
            {"pl": "rachunek",          "ph": "ra-HU-nek",         "uz": "hisob / chek"},
            {"pl": "zaświadczenie",     "ph": "za-shvyad-CHE-nye", "uz": "ma'lumotnoma"},
            {"pl": "przelew bankowy",   "ph": "PSHE-lev ban-KO-vi","uz": "bank o'tkazmasi"},
            {"pl": "termin płatności",  "ph": "TER-min pwat-NOSH-chi","uz": "to'lov muddati"},
            {"pl": "składka",           "ph": "SKWAD-ka",          "uz": "badal / to'lov"},
            {"pl": "emerytura",         "ph": "e-me-ri-TU-ra",     "uz": "pensiya"},
            {"pl": "odliczenie",        "ph": "od-li-CHE-nye",     "uz": "chegirma (soliqda)"},
        ],
        "dialog": (
            "💬 *Dialog: Soliq idorasida*\n\n"
            "🧑 *Dzień dobry. Chcę złożyć deklarację PIT.*\n"
            "🏢 *Proszę podać numer PESEL i NIP.*\n"
            "🧑 *Proszę, oto moje dokumenty.*\n"
            "🏢 *Czy pracował Pan na umowie o pracę?*\n"
            "🧑 *Tak, przez cały rok.*\n"
            "🏢 *Dobrze. Może się Panu należeć zwrot podatku.*\n"
            "🧑 *Ile wynosi zwrot?*\n"
            "🏢 *To zależy od dochodu. Obliczymy razem.*\n\n"
            "📝 *Tarjima:*\n"
            "🧑 Xayrli kun. PIT deklaratsiyasini topshirmoqchiman.\n"
            "🏢 PESEL va NIP raqamingizni bering.\n"
            "🧑 Mana hujjatlarim.\n"
            "🏢 Ish shartномasi bilan ishladingizmi?\n"
            "🧑 Ha, butun yil.\n"
            "🏢 Yaxshi. Soliq qaytarish huquqingiz bo'lishi mumkin.\n"
            "🧑 Qaytarish qancha?\n"
            "🏢 Bu daromadga bog'liq. Birga hisoblaymiz."
        ),
        "exercises": [
            {"q": "🧾 *'Podatek'* nima degani?",
             "opts": ["Pensiya", "Soliq", "Sug'urta", "Maosh"], "ans": 1},
            {"q": "🧾 *'Zwrot podatku'* nima degani?",
             "opts": ["Soliq to'lash", "Soliq qaytarish", "Soliq hujjati", "Soliq idorasi"], "ans": 1},
            {"q": "🇺🇿 *'Soliq raqami'* polyakchada?",
             "opts": ["PESEL", "NIP", "REGON", "ZUS"], "ans": 1},
            {"q": "🧾 *'Faktura'* nima degani?",
             "opts": ["Chek", "Faktura (hujjat)", "Shartnoma", "Ariza"], "ans": 1},
            {"q": "🧾 *'Emerytura'* nima degani?",
             "opts": ["Ish haqi", "Sug'urta", "Pensiya", "Bonus"], "ans": 2},
            {"q": "🇺🇿 *'Daromad solig'i'* polyakchada?",
             "opts": ["ZUS", "NFZ", "PIT", "VAT"], "ans": 2},
            {"q": "🧾 *'Składka'* nima degani?",
             "opts": ["Chegirma", "Badal / to'lov", "Soliq", "Maosh"], "ans": 1},
            {"q": "🧾 *'Deklaracja'* nima degani?",
             "opts": ["Ariza", "Shartnoma", "Deklaratsiya", "Hujjat"], "ans": 2},
            {"q": "🇺🇿 *'Bank o'tkazmasi'* polyakchada?",
             "opts": ["Rachunek", "Przelew bankowy", "Faktura", "Paragon"], "ans": 1},
            {"q": "🧾 *'Urząd skarbowy'* nima degani?",
             "opts": ["Mehnat idorasi", "Soliq idorasi", "Bank", "Chet elliklar idorasi"], "ans": 1},
        ],
    },

    "a2_l12": {
        "title": "Bolalar va Maktab",
        "emoji": "🏫",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Maktab tizimi haqida*\n\n"
            "*Polsha ta'lim tizimi:*\n"
            "• *przedszkole* — bog'cha (3-6 yosh)\n"
            "• *szkoła podstawowa* — boshlang'ich (7-15)\n"
            "• *liceum* — litsey (15-18)\n"
            "• *technikum* — texnikum (15-19)\n"
            "• *studia* — oliy ta'lim\n\n"
            "*Maktabda:*\n"
            "→ *Moje dziecko chodzi do szkoły.*\n"
            "   Bolam maktabga boradi.\n\n"
            "→ *Jest w trzeciej klasie.*\n"
            "   Uchinchi sinfda."
        ),
        "vocab": [
            {"pl": "szkoła",            "ph": "SHKO-va",           "uz": "maktab"},
            {"pl": "przedszkole",       "ph": "pshed-SHKO-le",     "uz": "bog'cha"},
            {"pl": "uczeń",             "ph": "U-chen",            "uz": "o'quvchi"},
            {"pl": "nauczyciel",        "ph": "na-u-CHI-chel",     "uz": "o'qituvchi"},
            {"pl": "lekcja",            "ph": "LEKTS-ya",          "uz": "dars"},
            {"pl": "przerwa",           "ph": "PZHER-va",          "uz": "tanaffus"},
            {"pl": "ocena",             "ph": "o-TSE-na",          "uz": "baho"},
            {"pl": "świadectwo",        "ph": "shvya-DETS-tvo",    "uz": "guvohnoma"},
            {"pl": "egzamin",           "ph": "eg-ZA-min",         "uz": "imtihon"},
            {"pl": "zadanie domowe",    "ph": "za-DA-nye do-MO-ve","uz": "uy vazifasi"},
            {"pl": "plecak",            "ph": "PLE-tsak",          "uz": "ryuksak"},
            {"pl": "klasa",             "ph": "KLA-sa",            "uz": "sinf"},
            {"pl": "dyrektor",          "ph": "dy-REK-tor",        "uz": "direktor"},
            {"pl": "język obcy",        "ph": "YEN-zyk OB-tsi",    "uz": "chet tili"},
            {"pl": "matematyka",        "ph": "ma-te-MA-ty-ka",    "uz": "matematika"},
        ],
        "dialog": (
            "💬 *Dialog: Maktab haqida*\n\n"
            "👩 *Twoje dziecko chodzi do szkoły?*\n"
            "🧑 *Tak. Syn chodzi do szkoły podstawowej.*\n"
            "   *Jest w drugiej klasie.*\n"
            "👩 *Jak mu idzie?*\n"
            "🧑 *Dobrze. Ma dobre oceny z matematyki.*\n"
            "   *Ale język polski jest dla niego trudny.*\n"
            "👩 *To normalne. Z czasem się nauczy.*\n"
            "🧑 *Mam nadzieję. Szukam korepetytora.*\n\n"
            "📝 *Tarjima:*\n"
            "👩 Bolanagiz maktabga boradimi?\n"
            "🧑 Ha. O'g'lim boshlang'ich maktabda. Ikkinchi sinfda.\n"
            "👩 Qanday o'qiydi?\n"
            "🧑 Yaxshi. Matematikadan baholari yaxshi. Lekin polyak tili qiyin.\n"
            "👩 Bu normal. Vaqt o'tishi bilan o'rganadi.\n"
            "🧑 Umid qilaman. Repetitor qidiraman."
        ),
        "exercises": [
            {"q": "🏫 *'Przedszkole'* nima degani?",
             "opts": ["Maktab", "Bog'cha", "Litsey", "Universitet"], "ans": 1},
            {"q": "🏫 *'Ocena'* nima degani?",
             "opts": ["Imtihon", "Baho", "Dars", "Uy vazifasi"], "ans": 1},
            {"q": "🇺🇿 *'O'qituvchi'* polyakchada?",
             "opts": ["Uczeń", "Nauczyciel", "Dyrektor", "Rodzic"], "ans": 1},
            {"q": "🏫 *'Egzamin'* nima degani?",
             "opts": ["Baho", "Dars", "Imtihon", "Uy vazifasi"], "ans": 2},
            {"q": "🏫 *'Zadanie domowe'* nima degani?",
             "opts": ["Sinf ishi", "Uy vazifasi", "Imtihon", "Loyiha"], "ans": 1},
            {"q": "🇺🇿 *'Matematika'* polyakchada?",
             "opts": ["Biologia", "Matematyka", "Chemia", "Fizyka"], "ans": 1},
            {"q": "🏫 *'Język obcy'* nima degani?",
             "opts": ["Ona tili", "Chet tili", "Xorijiy mamlakat", "Tarjimon"], "ans": 1},
            {"q": "🏫 *'Świadectwo'* nima degani?",
             "opts": ["Imtihon", "Ariza", "Guvohnoma", "Diplom"], "ans": 2},
            {"q": "🇺🇿 *'Ryuksak'* polyakchada?",
             "opts": ["Torba", "Plecak", "Walizka", "Teczka"], "ans": 1},
            {"q": "🏫 *'Klasa'* nima degani?",
             "opts": ["Maktab", "O'qituvchi", "Sinf", "Dars"], "ans": 2},
        ],
    },

    "a2_l13": {
        "title": "Bayramlar va Urf-odatlar",
        "emoji": "🎉",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Tabrik iboralari*\n\n"
            "*Bayramlarda:*\n"
            "→ *Wesołych Świąt!* — Bayramingiz muborak!\n"
            "→ *Szczęśliwego Nowego Roku!* — Yangi yil muborak!\n"
            "→ *Wesołego Alleluja!* — Baxtli Pasxa!\n\n"
            "*Umumiy tabriklar:*\n"
            "→ *Wszystkiego najlepszego!* — Hammasida omad!\n"
            "→ *Sto lat!* — Yuz yil yashang! (tug'ilgan kun)\n"
            "→ *Powodzenia!* — Omad!\n"
            "→ *Gratulacje!* — Tabriklayman!\n\n"
            "*Mehmon odoblar:*\n"
            "→ *Zapraszam do domu!* — Uyga taklif qilaman!\n"
            "→ *Częstuj się!* — Oling, uyalmang!"
        ),
        "vocab": [
            {"pl": "Boże Narodzenie",   "ph": "BO-zhe na-ro-DZE-nye","uz": "Rojdestvo (25 dekabr)"},
            {"pl": "Sylwester",         "ph": "sil-VES-ter",         "uz": "Yangi yil kechasi (31 dek.)"},
            {"pl": "Wielkanoc",         "ph": "vyel-KA-nots",        "uz": "Pasxa"},
            {"pl": "Dzień Niepodległości","ph": "djen nye-pod-leg-VOSH-chi","uz": "Mustaqillik kuni (11 noy.)"},
            {"pl": "imieniny",          "ph": "i-mye-NI-ni",         "uz": "ism kuni (Polshada muhim!)"},
            {"pl": "urodziny",          "ph": "u-ro-DJI-ni",         "uz": "tug'ilgan kun"},
            {"pl": "życzenia",          "ph": "zhi-CHE-nya",         "uz": "tilaklар / tabriklar"},
            {"pl": "prezent",           "ph": "PRE-zent",            "uz": "sovg'a"},
            {"pl": "tort",              "ph": "tort",                "uz": "tort"},
            {"pl": "świeczka",          "ph": "SHVYECH-ka",          "uz": "shamcha (tortda)"},
            {"pl": "Sto lat!",          "ph": "sto lat",             "uz": "Yuz yil yashang!"},
            {"pl": "Wesołych Świąt!",   "ph": "ve-SO-vih shvyont",  "uz": "Bayramingiz muborak!"},
            {"pl": "Gratulacje!",       "ph": "gra-tu-LATS-ye",      "uz": "Tabriklayman!"},
            {"pl": "Powodzenia!",       "ph": "po-vo-DZE-nya",       "uz": "Omad!"},
            {"pl": "Częstuj się!",      "ph": "CHEN-stuy she",       "uz": "Oling, uyalmang!"},
        ],
        "dialog": (
            "💬 *Dialog: Tug'ilgan kun*\n\n"
            "🎂 *Wszystkiego najlepszego z okazji urodzin!*\n"
            "🧑 *Dziękuję bardzo!*\n"
            "🎂 *Sto lat! Mam dla ciebie prezent.*\n"
            "🧑 *Och, nie trzeba było! Dziękuję!*\n"
            "🎂 *Zapraszam cię na tort.*\n"
            "   *Upiekłam go sama.*\n"
            "🧑 *Wygląda pysznie! Dziękuję za wszystko.*\n\n"
            "📝 *Tarjima:*\n"
            "🎂 Tug'ilgan kuningiz bilan tabriklayman!\n"
            "🧑 Katta rahmat!\n"
            "🎂 Yuz yil yashang! Siz uchun sovg'am bor.\n"
            "🧑 Voy, kerak emasdi! Rahmat!\n"
            "🎂 Tortga taklif qilaman. O'zim pishdim.\n"
            "🧑 Juda mazali ko'rinadi! Hamma narsaga rahmat."
        ),
        "exercises": [
            {"q": "🎉 *'Boże Narodzenie'* nima degani?",
             "opts": ["Pasxa", "Yangi yil", "Rojdestvo", "Mustaqillik kuni"], "ans": 2},
            {"q": "🎉 *'Sto lat!'* nima degani?",
             "opts": ["Bayramingiz muborak!", "Yuz yil yashang!", "Tabriklayman!", "Omad!"], "ans": 1},
            {"q": "🇺🇿 *'Tug'ilgan kun'* polyakchada?",
             "opts": ["Imieniny", "Urodziny", "Rocznica", "Święto"], "ans": 1},
            {"q": "🎉 *'Imieniny'* nima degani?",
             "opts": ["Tug'ilgan kun", "Ism kuni", "Bayram", "Nikoh"], "ans": 1},
            {"q": "🎉 *'Gratulacje!'* nima degani?",
             "opts": ["Omad!", "Rahmat!", "Tabriklayman!", "Yaxshi!"], "ans": 2},
            {"q": "🇺🇿 *'Sovg'a'* polyakchada?",
             "opts": ["Tort", "Prezent", "Świeczka", "Karta"], "ans": 1},
            {"q": "🎉 *'Wesołych Świąt!'* nima degani?",
             "opts": ["Omad!", "Bayramingiz muborak!", "Tabriklayman!", "Rahmat!"], "ans": 1},
            {"q": "🎉 *'Powodzenia!'* nima degani?",
             "opts": ["Yaxshi ishtaha!", "Sog'ligingizga!", "Omad!", "Rahmat!"], "ans": 2},
            {"q": "🎉 *'Sylwester'* qachon?",
             "opts": ["25 dekabr", "1 yanvar", "31 dekabr", "11 noyabr"], "ans": 2},
            {"q": "🇺🇿 *'Oling, uyalmang!'* polyakchada?",
             "opts": ["Zapraszam!", "Proszę!", "Częstuj się!", "Smacznego!"], "ans": 2},
        ],
    },

    "a2_l14": {
        "title": "Do'stlik va Munosabatlar",
        "emoji": "🤝",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: His-tuyg'ular va munosabatlar*\n\n"
            "*His-tuyg'ular:*\n"
            "→ *Cieszę się.* — Xursandman.\n"
            "→ *Smucę się.* — Xafa bo'lyapman.\n"
            "→ *Tęsknię za tobą.* — Seni sog'inaman.\n"
            "→ *Martwię się.* — Xavotirlanayapman.\n\n"
            "*Munosabat:*\n"
            "→ *Lubimy się.* — Bir-birimizni yaxshi ko'ramiz.\n"
            "→ *Kłócimy się.* — Janjallashamiz.\n"
            "→ *Przepraszam.* — Uzr so'rayman.\n"
            "→ *Wybacz mi.* — Meni kechir."
        ),
        "vocab": [
            {"pl": "przyjaźń",          "ph": "pshi-YAZHN",        "uz": "do'stlik"},
            {"pl": "przyjaciel",        "ph": "pshi-YA-chel",      "uz": "do'st (erkak)"},
            {"pl": "przyjaciółka",      "ph": "pshi-ya-CHUW-ka",   "uz": "do'st (ayol)"},
            {"pl": "znajomy",           "ph": "zna-YO-mi",         "uz": "tanish (erkak)"},
            {"pl": "koleżanka",         "ph": "ko-le-ZHAN-ka",     "uz": "hamkasb/do'st (ayol)"},
            {"pl": "miłość",            "ph": "MI-voshch",         "uz": "muhabbat / sevgi"},
            {"pl": "Tęsknię za tobą",  "ph": "TENS-nye za TO-bon","uz": "Seni sog'inaman"},
            {"pl": "Cieszę się",        "ph": "CHE-she she",       "uz": "Xursandman"},
            {"pl": "Martwię się",       "ph": "MART-vye she",      "uz": "Xavotirlanaman"},
            {"pl": "Wybacz mi",         "ph": "VY-bach mi",        "uz": "Meni kechir"},
            {"pl": "Przepraszam cię",   "ph": "pshe-PRA-sham che", "uz": "Senden uzr so'rayman"},
            {"pl": "Dziękuję za pomoc", "ph": "djen-KU-ye za PO-mots","uz": "Yordam uchun rahmat"},
            {"pl": "Liczę na ciebie",   "ph": "LI-che na CHE-bye", "uz": "Senga ishonaman"},
            {"pl": "Brakuje mi ciebie", "ph": "bra-KU-ye mi CHE-bye","uz": "Seni sog'inaman (chuqur)"},
            {"pl": "Jesteś ważny/a",    "ph": "YES-tesh VAZH-ni/a","uz": "Sen muhim (erkak/ayol)"},
        ],
        "dialog": (
            "💬 *Dialog: Do'stlar*\n\n"
            "📞 *Hej! Jak się masz? Dawno się nie widzieliśmy!*\n"
            "🧑 *Tęskniłem za tobą! Wszystko dobrze.*\n"
            "   *Ale ciężko pracuję.*\n"
            "📞 *Rozumiem. Kiedy możemy się spotkać?*\n"
            "🧑 *Może w weekend? Mam trochę wolnego czasu.*\n"
            "📞 *Świetnie! Możemy iść do kawiarni.*\n"
            "🧑 *Chętnie! Cieszę się, że zadzwoniłeś.*\n"
            "📞 *Ja też się cieszę. Do zobaczenia!*\n\n"
            "📝 *Tarjima:*\n"
            "📞 Hey! Qalaysan? Ko'rishganimizga ko'p bo'ldi!\n"
            "🧑 Seni sog'ingandim! Hammasi yaxshi. Lekin ko'p ishlayman.\n"
            "📞 Tushunaman. Qachon uchrashamiz?\n"
            "🧑 Balki dam olish kunlari? Biroz bo'sh vaqtim bor.\n"
            "📞 Zo'r! Qahvaxonaga borishimiz mumkin.\n"
            "🧑 Xursan dilan! Qo'ng'iroq qilganing uchun xursandman.\n"
            "📞 Men ham xursandman. Ko'rishguncha!"
        ),
        "exercises": [
            {"q": "🤝 *'Przyjaźń'* nima degani?",
             "opts": ["Sevgi", "Do'stlik", "Tanishlik", "Hamkorlik"], "ans": 1},
            {"q": "🤝 *'Tęsknię za tobą'* nima degani?",
             "opts": ["Seni yaxshi ko'raman", "Seni sog'inaman", "Sen bilan xursandman", "Senga rahmat"], "ans": 1},
            {"q": "🇺🇿 *'Xursandman'* polyakchada?",
             "opts": ["Smucę się", "Martwię się", "Cieszę się", "Złoszczę się"], "ans": 2},
            {"q": "🤝 *'Wybacz mi'* nima degani?",
             "opts": ["Rahmat", "Salom", "Meni kechir", "Kechirasiz"], "ans": 2},
            {"q": "🤝 *'Martwię się'* nima degani?",
             "opts": ["Xursandman", "Xavotirlanaman", "Xafa bo'laman", "Charchadim"], "ans": 1},
            {"q": "🇺🇿 *'Do'st (erkak)'* polyakchada?",
             "opts": ["Kolega", "Znajomy", "Przyjaciel", "Sąsiad"], "ans": 2},
            {"q": "🤝 *'Liczę na ciebie'* nima degani?",
             "opts": ["Seni sanayapman", "Senga ishonaman", "Seni kutaman", "Seni ko'raman"], "ans": 1},
            {"q": "🤝 *'Miłość'* nima degani?",
             "opts": ["Do'stlik", "Sevgi/muhabbat", "Hurmat", "Tanishlik"], "ans": 1},
            {"q": "🇺🇿 *'Senden uzr so'rayman'* polyakchada?",
             "opts": ["Dziękuję ci", "Przepraszam cię", "Proszę cię", "Lubię cię"], "ans": 1},
            {"q": "🤝 *'Brakuje mi ciebie'* nima degani?",
             "opts": ["Sen yetishmaysan", "Seni sog'inaman (chuqur)", "Sen bilan yaxshi", "Seni ko'raman"], "ans": 1},
        ],
    },

    "a2_l15": {
        "title": "Texnologiya",
        "emoji": "💻",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Texnologiya haqida gapirish*\n\n"
            "*Kompyuter fe'llari:*\n"
            "• *włączyć* — yoqmoq\n"
            "• *wyłączyć* — o'chirmoq\n"
            "• *zapisać* — saqlash\n"
            "• *pobrać* — yuklab olmoq\n"
            "• *wysłać* — yubormoq\n"
            "• *zainstalować* — o'rnatmoq\n\n"
            "*Muammo aytish:*\n"
            "→ *Komputer się zawiesił.* — Kompyuter qotib qoldi.\n"
            "→ *Internet nie działa.* — Internet ishlamayapti.\n"
            "→ *Bateria jest rozładowana.* — Batareya quridi."
        ),
        "vocab": [
            {"pl": "komputer",          "ph": "kom-PU-ter",        "uz": "kompyuter"},
            {"pl": "laptop",            "ph": "LAP-top",           "uz": "noutbuk"},
            {"pl": "telefon",           "ph": "te-LE-fon",         "uz": "telefon"},
            {"pl": "internet",          "ph": "IN-ter-net",        "uz": "internet"},
            {"pl": "aplikacja",         "ph": "ap-li-KATS-ya",     "uz": "ilova"},
            {"pl": "hasło",             "ph": "HAS-vo",            "uz": "parol"},
            {"pl": "e-mail",            "ph": "i-meyl",            "uz": "elektron pochta"},
            {"pl": "strona internetowa","ph": "STRO-na",           "uz": "veb-sayt"},
            {"pl": "drukarka",          "ph": "dru-KAR-ka",        "uz": "printer"},
            {"pl": "kamera",            "ph": "KA-me-ra",          "uz": "kamera"},
            {"pl": "głośnik",           "ph": "GVUSH-nik",         "uz": "dinamik"},
            {"pl": "klawiatura",        "ph": "kla-vya-TU-ra",     "uz": "klaviatura"},
            {"pl": "mysz",              "ph": "mysh",              "uz": "sichqoncha (kompyuter)"},
            {"pl": "ekran",             "ph": "EK-ran",            "uz": "ekran"},
            {"pl": "chmura (cloud)",    "ph": "HMUS-ra",           "uz": "bulut (cloud)"},
        ],
        "dialog": (
            "💬 *Dialog: IT muammo*\n\n"
            "🧑 *Przepraszam, nie mogę się połączyć z internetem.*\n"
            "💻 *Czy sprawdził Pan hasło Wi-Fi?*\n"
            "🧑 *Tak, hasło jest prawidłowe.*\n"
            "💻 *Proszę wyłączyć i włączyć router.*\n"
            "🧑 *Dobra. Chwilę... Już działa!*\n"
            "💻 *Świetnie. Jeśli będzie problem, proszę dzwonić.*\n"
            "🧑 *Dziękuję za pomoc!*\n\n"
            "📝 *Tarjima:*\n"
            "🧑 Kechirasiz, internetga ulana olmayapman.\n"
            "💻 Wi-Fi parolini tekshirdingizmi?\n"
            "🧑 Ha, parol to'g'ri.\n"
            "💻 Routerni o'chiring va yoqing.\n"
            "🧑 Xo'p. Bir oz... Ishlayapti!\n"
            "💻 Zo'r. Muammo bo'lsa, qo'ng'iroq qiling.\n"
            "🧑 Yordam uchun rahmat!"
        ),
        "exercises": [
            {"q": "💻 *'Hasło'* nima degani?",
             "opts": ["Foydalanuvchi", "Parol", "Havola", "Ilova"], "ans": 1},
            {"q": "💻 *'Aplikacja'* nima degani?",
             "opts": ["Veb-sayt", "Ilova", "Fayl", "Papka"], "ans": 1},
            {"q": "🇺🇿 *'Klaviatura'* polyakchada?",
             "opts": ["Mysz", "Ekran", "Klawiatura", "Głośnik"], "ans": 2},
            {"q": "💻 *'Drukarka'* nima degani?",
             "opts": ["Skaner", "Kamera", "Printer", "Monitor"], "ans": 2},
            {"q": "💻 *'Strona internetowa'* nima degani?",
             "opts": ["Ilova", "Veb-sayt", "Email", "Fayl"], "ans": 1},
            {"q": "🇺🇿 *'Sichqoncha (kompyuter)'* polyakchada?",
             "opts": ["Klawiatura", "Mysz", "Ekran", "Głośnik"], "ans": 1},
            {"q": "💻 *'Chmura'* texnologiya kontekstida nima?",
             "opts": ["Ob-havo", "Bulut (cloud)", "Internet", "Saqlash"], "ans": 1},
            {"q": "💻 *'Głośnik'* nima degani?",
             "opts": ["Mikrofon", "Kamera", "Dinamik", "Ekran"], "ans": 2},
            {"q": "🇺🇿 *'Ekran'* polyakchada?",
             "opts": ["Klawiatura", "Mysz", "Ekran", "Monitor"], "ans": 2},
            {"q": "💻 *'Kamera'* nima degani?",
             "opts": ["Printer", "Kamera", "Skaner", "Telefon"], "ans": 1},
        ],
    },

    "a2_l16": {
        "title": "Tabiat va Ekologiya",
        "emoji": "🌿",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Tabiat haqida gapirish*\n\n"
            "*Tabiat fe'llari:*\n"
            "• *chronić* — himoya qilmoq\n"
            "• *zanieczyszczać* — ifloslashtirmoq\n"
            "• *oszczędzać* — tejash\n"
            "• *wyrzucać* — tashlamoq\n"
            "• *segregować* — ajratish\n\n"
            "*Ekologiya iboralari:*\n"
            "→ *Trzeba chronić środowisko.*\n"
            "   Atrof-muhitni himoya qilish kerak.\n"
            "→ *Segreguję śmieci.* — Chiqindilarni ajrataman.\n"
            "→ *Oszczędzam wodę.* — Suvni tejaman."
        ),
        "vocab": [
            {"pl": "środowisko",        "ph": "shro-do-VIS-ko",    "uz": "atrof-muhit"},
            {"pl": "natura",            "ph": "na-TU-ra",          "uz": "tabiat"},
            {"pl": "las",               "ph": "las",               "uz": "o'rmon"},
            {"pl": "rzeka",             "ph": "ZHE-ka",            "uz": "daryo"},
            {"pl": "morze",             "ph": "MO-zhe",            "uz": "dengiz"},
            {"pl": "góry",              "ph": "GU-ri",             "uz": "tog'lar"},
            {"pl": "zwierzęta",         "ph": "zvye-ZHEN-ta",      "uz": "hayvonlar"},
            {"pl": "rośliny",           "ph": "rosh-LI-ni",        "uz": "o'simliklar"},
            {"pl": "zanieczyszczenie",  "ph": "za-nye-chish-CHE-nye","uz": "ifloslanish"},
            {"pl": "recykling",         "ph": "re-TSIK-ling",      "uz": "qayta ishlash"},
            {"pl": "śmieci",            "ph": "SHMYE-chi",         "uz": "chiqindilar"},
            {"pl": "energia odnawialna","ph": "e-NER-gya",         "uz": "qayta tiklanadigan energiya"},
            {"pl": "klimat",            "ph": "KLI-mat",           "uz": "iqlim"},
            {"pl": "Trzeba...",         "ph": "TSHE-ba",           "uz": "...kerak / zarur"},
            {"pl": "Warto...",          "ph": "VAR-to",            "uz": "...arziydi / foydali"},
        ],
        "dialog": (
            "💬 *Dialog: Ekologiya*\n\n"
            "👩 *Czy segregujesz śmieci?*\n"
            "🧑 *Tak, staram się. Mamy pojemniki na papier,*\n"
            "   *plastik i szkło.*\n"
            "👩 *To dobrze. A co jeszcze robisz dla środowiska?*\n"
            "🧑 *Staram się oszczędzać wodę i energię.*\n"
            "   *Chodzę pieszo zamiast jeździć autem.*\n"
            "👩 *Świetnie! Każdy może coś zrobić dla planety.*\n\n"
            "📝 *Tarjima:*\n"
            "👩 Chiqindilarni ajratасizmi?\n"
            "🧑 Ha, harakat qilaman. Bizda qog'oz, plastik va shisha uchun idishlar bor.\n"
            "👩 Yaxshi. Atrof-muhit uchun yana nima qilasiz?\n"
            "🧑 Suv va energiyani tejashga harakat qilaman. Mashina o'rniga piyoda yuraman.\n"
            "👩 Zo'r! Har kim sayyora uchun bir nima qila oladi."
        ),
        "exercises": [
            {"q": "🌿 *'Środowisko'* nima degani?",
             "opts": ["Tabiat", "Atrof-muhit", "Iqlim", "O'rmon"], "ans": 1},
            {"q": "🌿 *'Recykling'* nima degani?",
             "opts": ["Ifloslanish", "Chiqindi", "Qayta ishlash", "Tejash"], "ans": 2},
            {"q": "🇺🇿 *'O'rmon'* polyakchada?",
             "opts": ["Rzeka", "Las", "Góry", "Morze"], "ans": 1},
            {"q": "🌿 *'Śmieci'* nima degani?",
             "opts": ["O'simliklar", "Hayvonlar", "Chiqindilar", "Suvlar"], "ans": 2},
            {"q": "🌿 *'Trzeba...'* nima degani?",
             "opts": ["...mumkin", "...kerak/zarur", "...arziydi", "...yaxshi"], "ans": 1},
            {"q": "🇺🇿 *'Dengiz'* polyakchada?",
             "opts": ["Rzeka", "Jezioro", "Morze", "Ocean"], "ans": 2},
            {"q": "🌿 *'Klimat'* nima degani?",
             "opts": ["Ob-havo", "Iqlim", "Fasl", "Tabiat"], "ans": 1},
            {"q": "🌿 *'Warto...'* nima degani?",
             "opts": ["...kerak", "...mumkin emas", "...arziydi/foydali", "...majbur"], "ans": 2},
            {"q": "🇺🇿 *'Hayvonlar'* polyakchada?",
             "opts": ["Rośliny", "Zwierzęta", "Ptaki", "Ryby"], "ans": 1},
            {"q": "🌿 *'Zanieczyszczenie'* nima degani?",
             "opts": ["Tozalash", "Ifloslanish", "Qayta ishlash", "Saqlash"], "ans": 1},
        ],
    },

    "a2_l17": {
        "title": "Sog'lom Turmush",
        "emoji": "🥗",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Maslahat va tavsiya*\n\n"
            "*Maslahat berish:*\n"
            "• *Powinieneś...* — ...kerak (erk.)\n"
            "• *Powinnaś...* — ...kerak (ay.)\n"
            "• *Warto...* — ...arziydi\n"
            "• *Zalecam...* — ...tavsiya qilaman\n"
            "• *Proszę...* — ...qiling (rasmiy)\n\n"
            "*Maslahat olish:*\n"
            "→ *Co Pan radzi?* — Nima maslahat berasiz?\n"
            "→ *Jak mogę poprawić...?*\n"
            "   ...ni qanday yaxshilasam bo'ladi?\n\n"
            "*Sog'liq:*\n"
            "→ *Prowadzę zdrowy tryb życia.*\n"
            "   Sog'lom hayot kechiraman."
        ),
        "vocab": [
            {"pl": "zdrowie",           "ph": "ZDRO-vye",          "uz": "sog'lik"},
            {"pl": "dieta",             "ph": "DYE-ta",            "uz": "parhеz / dieta"},
            {"pl": "ćwiczenia",         "ph": "chvi-CHE-nya",      "uz": "mashqlar"},
            {"pl": "sen",               "ph": "sen",               "uz": "uyqu"},
            {"pl": "stres",             "ph": "stres",             "uz": "stress"},
            {"pl": "odpoczynek",        "ph": "od-po-CHI-nek",     "uz": "dam olish"},
            {"pl": "witaminy",          "ph": "vi-ta-MI-ni",       "uz": "vitaminlar"},
            {"pl": "woda",              "ph": "VO-da",             "uz": "suv"},
            {"pl": "świeże powietrze",  "ph": "SHVYE-zhe po-VYET-she","uz": "toza havo"},
            {"pl": "niepalący",         "ph": "nye-pa-LON-tsi",    "uz": "chekmaydigan"},
            {"pl": "alkohol",           "ph": "al-KO-hol",         "uz": "alkogol"},
            {"pl": "ruch",              "ph": "ruh",               "uz": "harakat"},
            {"pl": "równowaga",         "ph": "ruv-no-VA-ga",      "uz": "muvozanat"},
            {"pl": "Powinieneś...",     "ph": "po-vi-NYE-nesh",    "uz": "...kerak (erk.)"},
            {"pl": "Unikam...",         "ph": "u-NI-kam",          "uz": "...dan uzoq turaman"},
        ],
        "dialog": (
            "💬 *Dialog: Sog'lom hayot*\n\n"
            "👨‍⚕️ *Jak Pan dba o zdrowie?*\n"
            "🧑 *Staram się jeść zdrowo i ćwiczyć.*\n"
            "   *Ale przez pracę mam mało czasu.*\n"
            "👨‍⚕️ *Powinieneś spać przynajmniej 7 godzin.*\n"
            "   *I pić dużo wody.*\n"
            "🧑 *Wiem, ale łatwo powiedzieć...*\n"
            "👨‍⚕️ *Proszę też unikać stresu.*\n"
            "   *Warto robić przerwy w pracy.*\n\n"
            "📝 *Tarjima:*\n"
            "👨‍⚕️ Sog'lig'ingizga qanday g'amxo'rlik qilasiz?\n"
            "🧑 Sog'lom ovqatlanishga va mashq qilishga harakat qilaman. Lekin ish tufayli vaqtim kam.\n"
            "👨‍⚕️ Kamida 7 soat uxlashingiz kerak. Va ko'p suv ichish.\n"
            "🧑 Bilaman, lekin aytish oson...\n"
            "👨‍⚕️ Stressdan ham uzoq turing. Ishda tanaffus qilish foydali."
        ),
        "exercises": [
            {"q": "🥗 *'Zdrowie'* nima degani?",
             "opts": ["Kasallik", "Sog'lik", "Dori", "Shifokor"], "ans": 1},
            {"q": "🥗 *'Dieta'* nima degani?",
             "opts": ["Ovqat", "Parhеz/dieta", "Vitaminlar", "Oshxona"], "ans": 1},
            {"q": "🇺🇿 *'Mashqlar'* polyakchada?",
             "opts": ["Dieta", "Sport", "Ćwiczenia", "Ruch"], "ans": 2},
            {"q": "🥗 *'Odpoczynek'* nima degani?",
             "opts": ["Ish", "Dam olish", "Uyqu", "Stress"], "ans": 1},
            {"q": "🥗 *'Powinieneś...'* nima degani?",
             "opts": ["...mumkin (erk.)", "...kerak (erk.)", "...xohlayman", "...yaxshi"], "ans": 1},
            {"q": "🇺🇿 *'Stres'* polyakchada?",
             "opts": ["Sen", "Odpoczynek", "Stres", "Ruch"], "ans": 2},
            {"q": "🥗 *'Unikam...'* nima degani?",
             "opts": ["...qilaman", "...xohlayman", "...dan uzoq turaman", "...sevaman"], "ans": 2},
            {"q": "🥗 *'Sen'* (uyqu kontekstida) nima degani?",
             "opts": ["Uyqu", "Stres", "Dam olish", "Harakat"], "ans": 0},
            {"q": "🇺🇿 *'Vitaminlar'* polyakchada?",
             "opts": ["Leki", "Witaminy", "Tabletki", "Suplementy"], "ans": 1},
            {"q": "🥗 *'Świeże powietrze'* nima degani?",
             "opts": ["Toza suv", "Toza havo", "Yashil o'simlik", "Ochiq osmon"], "ans": 1},
        ],
    },

    "a2_l18": {
        "title": "Polsha Tarixi va Madaniyati",
        "emoji": "🏛️",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Tarix haqida gapirish*\n\n"
            "*O'tgan haqida:*\n"
            "→ *Polska była pod zaborami.*\n"
            "   Polsha bosqin ostida bo'lgan.\n\n"
            "→ *W 1918 roku Polska odzyskała niepodległość.*\n"
            "   1918 yilda Polsha mustaqilligini qaytardi.\n\n"
            "*Sana aytish:*\n"
            "→ *W roku tysiąc dziewięćset osiemnastym*\n"
            "   — 1918 yilda\n\n"
            "*Muhim sanalar:*\n"
            "• 1918 — mustaqillik\n"
            "• 1939-1945 — Ikkinchi jahon urushi\n"
            "• 1989 — kommunizmdan chiqish"
        ),
        "vocab": [
            {"pl": "historia",          "ph": "his-TOR-ya",         "uz": "tarix"},
            {"pl": "kultura",           "ph": "kul-TU-ra",          "uz": "madaniyat"},
            {"pl": "Polska",            "ph": "POL-ska",            "uz": "Polsha"},
            {"pl": "Warszawa",          "ph": "var-SHA-va",         "uz": "Varshava"},
            {"pl": "Kraków",            "ph": "KRA-kuf",            "uz": "Krakov"},
            {"pl": "niepodległość",     "ph": "nye-pod-LEG-voshch", "uz": "mustaqillik"},
            {"pl": "wojsko",            "ph": "VOY-sko",            "uz": "qo'shin / armiya"},
            {"pl": "król",              "ph": "krul",               "uz": "qirol"},
            {"pl": "zamek",             "ph": "ZA-mek",             "uz": "qal'a / qasр"},
            {"pl": "kościół",           "ph": "KOSH-chuw",          "uz": "cherkov"},
            {"pl": "muzeum",            "ph": "mu-ZE-um",           "uz": "muzey"},
            {"pl": "tradycja",          "ph": "tra-DITS-ya",        "uz": "an'ana"},
            {"pl": "zwyczaj",           "ph": "ZVY-chay",           "uz": "odat / urf-odat"},
            {"pl": "język polski",      "ph": "YEN-zyk POL-ski",    "uz": "polyak tili"},
            {"pl": "Chopin",            "ph": "SHO-pen",            "uz": "Shopen (mashhur polyak)"},
        ],
        "dialog": (
            "💬 *Dialog: Polsha haqida*\n\n"
            "👩 *Czy wiesz coś o historii Polski?*\n"
            "🧑 *Trochę. Wiem, że Polska odzyskała niepodległość*\n"
            "   *w 1918 roku.*\n"
            "👩 *Tak. I w 1939 roku zaczęła się II Wojna Światowa.*\n"
            "🧑 *To musiało być bardzo trudne.*\n"
            "👩 *Tak. Ale Polacy są silnym narodem.*\n"
            "   *A czy wiesz, kto to Chopin?*\n"
            "🧑 *Oczywiście! To słynny polski kompozytor.*\n\n"
            "📝 *Tarjima:*\n"
            "👩 Polsha tarixi haqida biror narsa bilasizmi?\n"
            "🧑 Biroz. Polsha 1918 yilda mustaqilligini qaytarganini bilaman.\n"
            "👩 Ha. Va 1939 yilda Ikkinchi jahon urushi boshlandi.\n"
            "🧑 Bu juda qiyin bo'lgan bo'lsa kerak.\n"
            "👩 Ha. Lekin polyaklar kuchli xalq. Siz Shopenni bilasizmi?\n"
            "🧑 Albatta! Bu mashhur polyak bastakor."
        ),
        "exercises": [
            {"q": "🏛️ *'Historia'* nima degani?",
             "opts": ["Madaniyat", "Tarix", "An'ana", "San'at"], "ans": 1},
            {"q": "🏛️ *'Niepodległość'* nima degani?",
             "opts": ["Urush", "Tinchlik", "Mustaqillik", "Birlik"], "ans": 2},
            {"q": "🇵🇱 Polsha qachon mustaqillik oldi?",
             "opts": ["1918", "1945", "1989", "1939"], "ans": 0},
            {"q": "🏛️ *'Kultura'* nima degani?",
             "opts": ["Tarix", "Madaniyat", "San'at", "Til"], "ans": 1},
            {"q": "🏛️ *'Tradycja'* nima degani?",
             "opts": ["Odat/urf-odat", "An'ana", "Ikkala ham to'g'ri", "Farq qiladi"], "ans": 2},
            {"q": "🏛️ *'Król'* nima degani?",
             "opts": ["Prezident", "Qirol", "Ministr", "General"], "ans": 1},
            {"q": "🏛️ *'Zamek'* nima degani?",
             "opts": ["Muzey", "Cherkov", "Qal'a/qasr", "Bozor"], "ans": 2},
            {"q": "🏛️ Chopin kim?",
             "opts": ["Rассom", "Yozuvchi", "Bastakor", "Siyosatchi"], "ans": 2},
            {"q": "🇵🇱 Polshaning poytaxti?",
             "opts": ["Kraków", "Wrocław", "Gdańsk", "Warszawa"], "ans": 3},
            {"q": "🏛️ *'Muzeum'* nima degani?",
             "opts": ["Teatr", "Muzey", "Kutubxona", "Galereya"], "ans": 1},
        ],
    },

    "a2_l19": {
        "title": "Kelajak Rejalari",
        "emoji": "🚀",
        "level": "A2.1",
        "grammar": (
            "🇵🇱 *Grammatika: Orzu va maqsad*\n\n"
            "*Niyat bildirish:*\n"
            "• *Planuję...* — Rejalashtiryapman\n"
            "• *Mam zamiar...* — Niyatim bor\n"
            "• *Marzę o...* — Orzuyim...\n"
            "• *Chcę...* — Xohlayman\n"
            "• *Postanowiłem...* — Qaror qildim\n\n"
            "*Umid:*\n"
            "• *Mam nadzieję, że...* — Umid qilamanki...\n"
            "• *Liczę na...* — ...ga umid qilaman\n\n"
            "*Shartli:*\n"
            "→ *Jeśli zarobię, kupię...*\n"
            "   Pul topib okim, ... sotib olaman."
        ),
        "vocab": [
            {"pl": "plan",              "ph": "plan",              "uz": "reja"},
            {"pl": "cel",               "ph": "tsel",              "uz": "maqsad"},
            {"pl": "marzenie",          "ph": "ma-ZHE-nye",        "uz": "orzu"},
            {"pl": "nadzieja",          "ph": "na-DJE-ya",         "uz": "umid"},
            {"pl": "sukces",            "ph": "SUK-tses",          "uz": "muvaffaqiyat"},
            {"pl": "przyszłość",        "ph": "pshi-SHVOSHCH",     "uz": "kelajak"},
            {"pl": "awans",             "ph": "A-vans",            "uz": "lavozim oshishi"},
            {"pl": "oszczędzać",        "ph": "o-SHEN-dzach",      "uz": "tejash"},
            {"pl": "inwestować",        "ph": "in-ves-TO-vach",    "uz": "investitsiya qilish"},
            {"pl": "wrócić do kraju",   "ph": "VRU-chich do KRA-yu","uz": "vatanga qaytish"},
            {"pl": "zostać w Polsce",   "ph": "ZOS-tach v POL-ste","uz": "Polshada qolish"},
            {"pl": "sprowadzić rodzinę","ph": "spro-VA-djich",     "uz": "oilani olib kelish"},
            {"pl": "Mam nadzieję",      "ph": "mam na-DJE-ye",     "uz": "Umid qilaman"},
            {"pl": "Planuję...",        "ph": "pla-NU-ye",         "uz": "Rejalashtiryapman..."},
            {"pl": "Marzę o tym",       "ph": "MA-zhe o tym",      "uz": "Bunga orzuyim bor"},
        ],
        "dialog": (
            "💬 *Dialog: Kelajak haqida*\n\n"
            "👩 *Jakie masz plany na przyszłość?*\n"
            "🧑 *Mam nadzieję, że za rok dostanę kartę pobytu.*\n"
            "   *I sprowadzę rodzinę do Polski.*\n"
            "👩 *To piękny plan. A co z pracą?*\n"
            "🧑 *Chcę awansować lub znaleźć lepszą pracę.*\n"
            "   *Planuję też nauczyć się lepiej po polsku.*\n"
            "👩 *A czy chcesz zostać w Polsce na stałe?*\n"
            "🧑 *Nie wiem jeszcze. Marzę o własnym biznesie.*\n"
            "   *Może tu, może w Uzbekistanie.*\n\n"
            "📝 *Tarjima:*\n"
            "👩 Kelajak rejalaring qanday?\n"
            "🧑 Bir yildan keyin yashash kartasi olaman, deb umid qilaman. Va oilami Polshaga olib kelaman.\n"
            "👩 Yaxshi reja. Ish haqida-chi?\n"
            "🧑 Lavozimim oshishini yoki yaxshiroq ish topishni xohlayman. Polyakchani ham yaxshiroq o'rganmoqchiman.\n"
            "👩 Doimiy Polshada qolmoqchimisan?\n"
            "🧑 Hali bilmayman. O'z biznesim bo'lishiga orzuyim bor. Balki bu yerda, balki O'zbekistonda."
        ),
        "exercises": [
            {"q": "🚀 *'Marzenie'* nima degani?",
             "opts": ["Maqsad", "Orzu", "Reja", "Umid"], "ans": 1},
            {"q": "🚀 *'Nadzieja'* nima degani?",
             "opts": ["Orzu", "Maqsad", "Umid", "Reja"], "ans": 2},
            {"q": "🇺🇿 *'Muvaffaqiyat'* polyakchada?",
             "opts": ["Cel", "Plan", "Sukces", "Awans"], "ans": 2},
            {"q": "🚀 *'Awans'* nima degani?",
             "opts": ["Ishdan bo'shatish", "Lavozim oshishi", "Maosh oshishi", "Yangi ish"], "ans": 1},
            {"q": "🚀 *'Mam nadzieję'* nima degani?",
             "opts": ["Umid qilaman", "Xohlayman", "Rejalashtiryapman", "Qaror qildim"], "ans": 0},
            {"q": "🇺🇿 *'Kelajak'* polyakchada?",
             "opts": ["Przeszłość", "Teraźniejszość", "Przyszłość", "Historia"], "ans": 2},
            {"q": "🚀 *'Oszczędzać'* nima degani?",
             "opts": ["Sarflash", "Tejash", "Investitsiya", "Topish"], "ans": 1},
            {"q": "🚀 *'Planuję...'* nima degani?",
             "opts": ["Xohlayman", "Rejalashtiryapman", "Umid qilaman", "Qaror qildim"], "ans": 1},
            {"q": "🚀 *'Sprowadzić rodzinę'* nima degani?",
             "opts": ["Oilaga borish", "Oilani olib kelish", "Oilani topish", "Oilaga qo'ng'iroq"], "ans": 1},
            {"q": "🇺🇿 *'Bunga orzuyim bor'* polyakchada?",
             "opts": ["Planuję to", "Mam nadzieję", "Marzę o tym", "Chcę to"], "ans": 2},
        ],
    },

    "a2_l20": {
        "title": "Yakuniy Takrorlash — A2",
        "emoji": "🎓",
        "level": "A2.1",
        "grammar": (
            "🎓 *A2.1 Darsi — Yakuniy Takrorlash*\n\n"
            "*Siz o'rganganlaring:*\n\n"
            "✅ O'tgan zamon (-ł/-ła)\n"
            "✅ Kelasi zamon (będę + infinitiv)\n"
            "✅ Shart gaplari (jeśli/gdyby)\n"
            "✅ Kelishiklar (Akk./Gen./Dat./Instr.)\n"
            "✅ Restoran va mehmonxona\n"
            "✅ Sport va hobbi\n"
            "✅ Sayohat\n"
            "✅ Mehnat huquqi\n"
            "✅ Soliq va hujjatlar\n"
            "✅ Maktab va bolalar\n"
            "✅ Bayramlar\n"
            "✅ Do'stlik va his-tuyg'ular\n"
            "✅ Texnologiya\n"
            "✅ Ekologiya\n"
            "✅ Sog'lom turmush\n"
            "✅ Polsha tarixi\n"
            "✅ Kelajak rejalari\n\n"
            "🦉 *Tabriklaymiz! Siz A2 darajasiga yetdingiz!*"
        ),
        "vocab": [
            {"pl": "Gratulacje!",        "ph": "gra-tu-LATS-ye",     "uz": "Tabriklayman!"},
            {"pl": "Osiągnięcie",        "ph": "o-shong-NYE-che",    "uz": "Yutuq / muvaffaqiyat"},
            {"pl": "Postęp",             "ph": "POS-temp",           "uz": "Taraqqiyot"},
            {"pl": "Umiejętności",       "ph": "u-mye-YEN-tno-shi", "uz": "Ko'nikmalar"},
            {"pl": "Świadectwo",         "ph": "shvya-DETS-tvo",    "uz": "Sertifikat / guvohnoma"},
            {"pl": "Egzamin",            "ph": "eg-ZA-min",          "uz": "Imtihon"},
            {"pl": "Poziom",             "ph": "PO-ziom",            "uz": "Daraja"},
            {"pl": "Komunikacja",        "ph": "ko-mu-ni-KATS-ya",  "uz": "Muloqot"},
            {"pl": "Rozumiem wszystko",  "ph": "ro-ZU-myem VSHY-stko","uz": "Hammasini tushunaman"},
            {"pl": "Mówię płynnie",      "ph": "MU-vye PVIN-nye",   "uz": "Ravon gapiraman"},
            {"pl": "Potrzebuję więcej",  "ph": "pot-SHE-bu-ye VYEN-tsey","uz": "Ko'proq kerak"},
            {"pl": "Ćwiczę codziennie", "ph": "CHVI-che tso-DJYEN-nye","uz": "Har kuni mashq qilaman"},
            {"pl": "Polsku mówię lepiej","ph": "POL-sku MU-vye LEP-yey","uz": "Polyakcha yaxshiroq gapiraman"},
            {"pl": "Dziękuję za naukę!", "ph": "djen-KU-ye za NA-u-ke","uz": "O'rganish uchun rahmat!"},
            {"pl": "Do następnego razu!","ph": "do nas-TEP-ne-go RA-zu","uz": "Keyingisida ko'rishguncha!"},
        ],
        "dialog": (
            "💬 *Dialog: Yakuniy baholash*\n\n"
            "👩‍🏫 *Gratulacje! Ukończyłeś kurs A2.*\n"
            "🧑 *Dziękuję! To był ciężki, ale ciekawy kurs.*\n"
            "👩‍🏫 *Twój postęp jest ogromny.*\n"
            "   *Mówisz znacznie lepiej niż na początku.*\n"
            "🧑 *Staram się ćwiczyć codziennie.*\n"
            "   *Bot bardzo mi pomógł!*\n"
            "👩‍🏫 *Co było najtrudniejsze?*\n"
            "🧑 *Przypadki. Ale powoli rozumiem.*\n"
            "👩‍🏫 *Świetnie! Teraz możesz zacząć poziom B1.*\n"
            "🧑 *Nie mogę się doczekać! Dziękuję za wszystko!*\n\n"
            "📝 *Tarjima:*\n"
            "👩‍🏫 Tabriklayman! A2 kursini tugatdingiz.\n"
            "🧑 Rahmat! Bu qiyin, lekin qiziqarli kurs bo'ldi.\n"
            "👩‍🏫 Sizning taraqqiyotingiz juda katta. Boshidан ancha yaxshi gapirmoqdasiz.\n"
            "🧑 Har kuni mashq qilishga harakat qilaman. Bot juda yordam berdi!\n"
            "👩‍🏫 Nima eng qiyin bo'ldi?\n"
            "🧑 Kelishiklar. Lekin asta-sekin tushunayapman.\n"
            "👩‍🏫 Zo'r! Endi B1 darajasini boshlashingiz mumkin.\n"
            "🧑 Kuta olmayman! Hamma narsaga rahmat!"
        ),
        "exercises": [
            {"q": "🎓 *'Gratulacje!'* nima degani?",
             "opts": ["Rahmat!", "Tabriklayman!", "Omad!", "Xayr!"], "ans": 1},
            {"q": "🎓 *'Postęp'* nima degani?",
             "opts": ["Muvaffaqiyatsizlik", "Taraqqiyot", "Imtihon", "Daraja"], "ans": 1},
            {"q": "🎓 O'tgan zamon (erkak) qo'shimchasi?",
             "opts": ["-ła", "-ło", "-łem", "-ły"], "ans": 2},
            {"q": "🎓 *'Będę pracować'* — bu qaysi zamon?",
             "opts": ["O'tgan", "Hozirgi", "Kelasi", "Davomiy"], "ans": 2},
            {"q": "🎓 *'Jeśli'* nima degani?",
             "opts": ["Chunki", "Agar", "Lekin", "Shuning uchun"], "ans": 1},
            {"q": "🎓 Akkuzativda ayol otlar qanday tugaydi?",
             "opts": ["-i", "-ę", "-a", "-e"], "ans": 1},
            {"q": "🎓 *'Nie mam pracy'* — bu qaysi kelishik?",
             "opts": ["Akkuzativ", "Nominativ", "Genitiv", "Dativ"], "ans": 2},
            {"q": "🎓 *'Jestem spawaczem'* — bu qaysi kelishik?",
             "opts": ["Nominativ", "Akkuzativ", "Dativ", "Instrumental"], "ans": 3},
            {"q": "🎓 *'Mam nadzieję'* nima degani?",
             "opts": ["Xohlayman", "Umid qilaman", "Rejalashtiryapman", "Bilaman"], "ans": 1},
            {"q": "🎓 *'Poziom'* nima degani?",
             "opts": ["Kurs", "Daraja", "Imtihon", "Sertifikat"], "ans": 1},
        ],
    },
}
