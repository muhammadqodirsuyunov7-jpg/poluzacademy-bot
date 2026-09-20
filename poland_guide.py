# -*- coding: utf-8 -*-
"""
🦉 POLUZACADEMY — POLSHA HAYOTI QO'LLANMASI (POLAND GUIDE)
Polshada yashayotgan, ishlayotgan va o'qiyotgan vatandoshlarimiz uchun
eng amaliy va hayotiy mavzular: Urząd, Karta Pobytu, Ish joyi, SOS va Transport.
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

GUIDE_SECTIONS = {
    "urzad": {
        "title": "🏛 Urząd va Karta Pobytu",
        "desc": "Urząd (viloyat boshqarmasi)da Karta Pobytu, PESEL va meldunek uchun kerakli so'zlar va dialoglar.",
        "terms": [
            ("Karta pobytu", "Karta pobitu", "Yashash guvohnomasi (Karta pobytu)"),
            ("Pobyt czasowy", "Pobit chasovi", "Vaqtinchalik yashash ruxsati"),
            ("Wniosek", "Vnyosek", "Ariza formasi"),
            ("Załącznik nr 1", "Zalonchnik numer yeden", "Ish beruvchi to'ldiradigan 1-ilova"),
            ("Zameldowanie", "Zamel-dovanye", "Yashash joyi bo'yicha ro'yxatdan o'tish (Meldunek)"),
            ("Numer PESEL", "Numer pesel", "Shaxsiy identifikatsiya raqami (PESEL)"),
            ("Decyzja", "Detsizya", "Urząd qarori (ijobiy yoki rad)"),
            ("Odciski palców", "Odchishki paltsev", "Barmoq izlari topshirish"),
            ("Opłata skarbowa", "Oplata skarbova", "Davlat boji to'lovi (440 zł yoki boshqa)"),
            ("Zezwolenie na pracę", "Zezvolenye na prantse", "Ishlash uchun rasmiy ruxsatnoma"),
            ("Urząd Wojewódzki", "Uzjond voyevudzki", "Viloyat hokimligi / Voyevodalik"),
            ("Urząd Skarbowy", "Uzjond skarbovi", "Soliq idorasi (Skarbuvka)"),
            ("ZUS (Zakład Ubezpieczeń Społecznych)", "Zus", "Ijtimoiy sug'urta jamg'armasi"),
            ("Umowa o pracę", "Umova o prontse", "Asosiy mehnat shartnomasi"),
            ("Umowa zlecenie", "Umova zletsenye", "Buyurtma asosidagi shartnoma (Zlecheniye)"),
        ],
        "dialog": (
            "💬 *Dialog: Urządda hujjat topshirish*\n\n"
            "🧑 Vatandosh: *Dzień dobry! Przepraszam, mam wizytę na godzinę dziesiątą.*\n"
            "   (Xayrli kun! Kechirasiz, soat 10 ga navbatim bor edi.)\n\n"
            "🏛 Xodim: *Dzień dobry. Proszę paszport i potwierdzenie wizyty.*\n"
            "   (Xayrli kun. Pasportingizni va navbat tasdig'ini bering.)\n\n"
            "🧑 Vatandosh: *Oto moje dokumenty: wniosek, załącznik numer jeden i opłata skarbowa.*\n"
            "   (Mana mening hujjatlarim: ariza, 1-ilova va davlat boji to'lovi.)\n\n"
            "🏛 Xodim: *Wszystko w porządku. Teraz pobierzemy odciski palców. Proszę położyć palec tutaj.*\n"
            "   (Hamma narsa joyida. Endi barmoq izi olamiz. Barmog'ingizni bu yerga qo'ying.)\n\n"
            "🧑 Vatandosh: *Dziękuję. Ile będę czekać na decyzję?*\n"
            "   (Rahmat. Qarorni qancha kutaman?)\n\n"
            "🏛 Xodim: *Powiadomienie przyjdzie listem lub SMS-em. Do widzenia!*\n"
            "   (Xabarnoma xat yoki SMS orqali boradi. Xayr!)"
        )
    },
    "praca": {
        "title": "💼 Ish joyi (Magazyn, Zavod, Kuryer, Qurilish)",
        "desc": "Ish jarayonida boshliqlar va hamkasblar bilan tushunishish uchun eng zarur iboralar.",
        "terms": [
            ("Kierownik / Lider", "Kyerovnik / Lider", "Boshliq / Smena boshlig'i"),
            ("Wózek widłowy", "Vuzek vidlovi", "Yuk ko'taruvchi kara (Forklift)"),
            ("Skaner", "Skaner", "Magazindagi tovar skaneri"),
            ("Paleta / Karton", "Paleta / Karton", "Palet / Quti"),
            ("Linia produkcyjna", "Linya produktsiyna", "Ishlab chiqarish konveyeri"),
            ("Przerwa", "Pshezhva", "Tanaffus / Obyed"),
            ("Nadgodziny", "Nad-godzini", "Qo'shimcha ish soatlari (Overtime)"),
            ("Zwolnienie lekarskie (L4)", "Zvolnyenye lekarskye", "Kasal bo'lgandagi byulleten (L4)"),
            ("BHP (Bezpieczeństwo)", "Be-ha-pe", "Xavfsizlik texnikasi qoidalari"),
            ("Gdzie to postawić?", "Gjye to postavich?", "Buni qayerga qo'yay?"),
            ("Skończyłem pracę", "Skonchilem prontse", "Men ishni tugatdim"),
            ("Potrzebuję pomocy", "Potshebuye pomotsi", "Menga yordam kerak"),
            ("Dojazd / Adres", "Doyazd / Adres", "Borish yo'li / Manzil (Kuryer/Taxi)"),
            ("Kod do klatki", "Kod do klatki", "Podyezd domofon kodi"),
            ("Napiwek", "Napivek", "Choychaqa (Tip)"),
        ],
        "dialog": (
            "💬 *Dialog: Ish joyida smena boshlig'i bilan*\n\n"
            "🧑 Ishchi: *Cześć Marek! Gdzie mam dzisiaj pracować?*\n"
            "   (Salom Marek! Bugun qayerda ishlayman?)\n\n"
            "👨‍💼 Lider: *Cześć! Dzisiaj idziesz na strefę pakowania. Palety są przy rampie numer cztery.*\n"
            "   (Salom! Bugun qadoqlash zonasiga borasan. Paletlar 4-rampa yonida.)\n\n"
            "🧑 Ishchi: *Rozumiem. Czy te kartony trzeba okleić taśmą?*\n"
            "   (Tushundim. Bu qutilarni skotch bilan yopishtirish kerakmi?)\n\n"
            "👨‍💼 Lider: *Tak, dokładnie. Pamiętaj o butach BHP i kamizelce!*\n"
            "   (Ha, aynan shunday. Maxsus oyoq kiyim va nimchangni unutmang!)\n\n"
            "🧑 Ishchi: *Jasne, wszystko mam. O której mamy przerwę?*\n"
            "   (Tushunarli, hammasi yonimda. Tanaffus soat nechada?)\n\n"
            "👨‍💼 Lider: *Przerwa jest o godzinie dwunastej. Dobrej pracy!*\n"
            "   (Tanaffus soat 12 da. Yaxshi ishlang!)"
        )
    },
    "sos": {
        "title": "🚑 SOS / Favqulodda vaziyatlar & Elchixona",
        "desc": "Tez yordam, dorixona, politsiya va O'zbekiston elchixonasi ma'lumotlari.",
        "terms": [
            ("Numer alarmowy: 112", "Numer alarmovi: sto dvanaście", "Umumiy favqulodda raqam (Yevropa bo'yicha 112)"),
            ("Pogotowie ratunkowe: 999", "Pogotove ratunkove", "Tez tibbiy yordam (999)"),
            ("Policja: 997", "Politsya", "Politsiya (997)"),
            ("Straż pożarna: 998", "Strazh pozharna", "O't o'chiruvchilar (998)"),
            ("Boli mnie głowa / brzuch", "Boli mnye gvova / bzhuh", "Boshim / qornim og'riyapti"),
            ("Mam gorączkę", "Mam goronchke", "Isitmayapman"),
            ("Apteka / Recepta", "Apteka / Retsepta", "Dorixona / Shifokor retsepti"),
            ("Lek przeciwbólowy", "Lek pshechiv-bulovi", "Og'riq qoldiruvchi dori"),
            ("Zgubiłem paszport", "Zgubilem pashport", "Pasportimni yo'qotib qo'ydim"),
            ("Potrzebuję lekarza", "Potshebuye lekazha", "Menga shifokor kerak"),
            ("Wypadek", "Vipadek", "Baxtsiz hodisa / Avariya"),
            ("Szpital / SOR", "Shpital / Sor", "Shifoxona / Tezkor qabul bo'limi (SOR)"),
        ],
        "dialog": (
            "💬 *Dialog: Dorixonada (W aptece)*\n\n"
            "🧑 O'quvchi: *Dzień dobry! Źle się czuję. Czy ma pan coś na ból gardła i gorączkę?*\n"
            "   (Xayrli kun! O'zimni yomon his qilyapman. Tomoq og'rig'i va isitmaga biror dori bormi?)\n\n"
            "💊 Farmatsevt: *Dzień dobry. Czy ma pan kaszel albo katar?*\n"
            "   (Xayrli kun. Yo'tal yoki burun oqishi bormi?)\n\n"
            "🧑 O'quvchi: *Tak, mam silny katar i temperaturę trzydzieści osiem.*\n"
            "   (Ha, kuchli tumov va 38 daraja isitmam bor.)\n\n"
            "💊 Farmatsevt: *Polecam te tabletki i syrop. Proszę brać dwie tabletki dziennie po jedzeniu.*\n"
            "   (Bu dorilar va siropni tavsiya qilaman. Kuniga 2 ta tabletka ovqatdan keyin iching.)\n\n"
            "🧑 O'quvchi: *Dziękuję bardzo. Ile płacę?*\n"
            "   (Katta rahmat. Qancha to'layman?)\n\n"
            "💊 Farmatsevt: *Razem czterdzieści pięć złotych. Płatność kartą czy gotówką?*\n"
            "   (Jami 45 zlotiy. Karta bilanmi yoki naqd?)"
        ),
        "embassy_info": (
            "🇺🇿 *O'zbekiston Respublikasining Polshadagi Elchixonasi:*\n\n"
            "📍 *Manzil:* ul. Piękna 11B, 00-549 Warszawa\n"
            "📞 *Telefon:* +48 22 895 65 88\n"
            "🚨 *Favqulodda Konsullik aloqasi:* +48 601 228 178\n"
            "🌐 *Veb-sayt:* uzbekistan.pl\n\n"
            "Passport yo'qolganda yoki huquqiy muammolarda darhol elchixona konsullik bo'limiga murojaat qiling!"
        )
    },
    "transport": {
        "title": "🚌 Transport va Shahar hayoti",
        "desc": "Avtobus, tramvay, poezd chiptalari va shahar ichida qulay harakatlanish.",
        "terms": [
            ("Bilet jednorazowy", "Bilet yodno-razovi", "Bir martalik chipta"),
            ("Bilet 20-minutowy", "Bilet dvadzestu-minutovi", "20 daqiqalik chipta"),
            ("Bilet miesięczny", "Bilet mysyenchni", "1 oylik yo'l chiptasi"),
            ("Kasownik", "Kasovnik", "Chiptani uradigan apparat (Kompostor)"),
            ("Przystanek", "Pshistanek", "Avtobus/Tramvay bekati"),
            ("Dworzec kolejowy (PKP)", "Dvozhets koleyovi", "Temir yo'l vokzali"),
            ("Dworzec autobusowy", "Dvozhets avtobusovi", "Avtovokzal"),
            ("Rozkład jazdy", "Rozkvad yazdi", "Qatnov jadvali (Grafik)"),
            ("Jak dojechać do...?", "Yak doye-hach do...?", "...ga qanday borsa bo'ladi?"),
            ("Proszę skasować bilet", "Proshe skasovach bilet", "Iltimos, chiptangizni uring"),
        ],
        "dialog": (
            "💬 *Dialog: Chipta sotib olish va yo'l so'rash*\n\n"
            "🧑 Yo'lovchi: *Przepraszam, jak dojechać na Dworzec Centralny?*\n"
            "   (Kechirasiz, Markaziy vokzalga qanday borsa bo'ladi?)\n\n"
            "🚏 Yo'lovchi 2: *Może pan wsiąść w tramwaj numer siedem lub autobus sto siedemdziesiąt pięć.*\n"
            "   (7-tramvayga yoki 175-avtobusga o'tirishingiz mumkin.)\n\n"
            "🧑 Yo'lovchi: *A gdzie mogę kupić bilet?*\n"
            "   (Chiptani qayerdan sotib olsam bo'ladi?)\n\n"
            "🚏 Yo'lovchi 2: *W biletomacie na przystanku lub wewnątrz pojazdu płacąc kartą.*\n"
            "   (Bekatdagi biletomatdan yoki avtobus ichida karta orqali.)\n\n"
            "🧑 Yo'lovchi: *Dziękuję bardzo za pomoc!*\n"
            "   (Yordamingiz uchun katta rahmat!)"
        )
    }
}

def kb_guide_main():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏛 Urząd va Karta Pobytu", callback_data="guide:urzad")],
        [InlineKeyboardButton("💼 Ish joyi (Sklad, Zavod, Kuryer)", callback_data="guide:praca")],
        [InlineKeyboardButton("🚑 SOS & Elchixona", callback_data="guide:sos"),
         InlineKeyboardButton("🚌 Transport & Do'kon", callback_data="guide:transport")],
        [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
    ])

def kb_guide_section(sec_id: str):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔊 Lug'atni audio eshitish", callback_data=f"guide_audio:{sec_id}")],
        [InlineKeyboardButton("◀️ Qo'llanmaga qaytish", callback_data="poland_guide"),
         InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")]
    ])
