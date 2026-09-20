# -*- coding: utf-8 -*-
"""
🦉 POLYAKCHA BOT — TO'LOV TIZIMI (PAYMENTS)
BLIK va Karta orqali to'lov (Stripe Checkout Veb-havolasi orqali)
Tariflar: 1 oylik (24.99 zł), 3 oylik (59.99 zł), 1 yillik (179.99 zł)
Dastlabki 5 ta dars (a1_l01 – a1_l05) barcha uchun bepul.
"""

import os
import logging
import sqlite3
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import stripe

logger = logging.getLogger(__name__)

# ═══════════════════════════════════════════
# SOZLAMALAR
# ═══════════════════════════════════════════
CURRENCY = "PLN"
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY", "")

NARXLAR = {
    "oylik": {
        "narx": 2499,
        "days": 30,
        "label": "1 Oylik Premium",
        "desc": "24.99 zł / oy",
        "tag": "🔥 Eng ommabop"
    },
    "3oylik": {
        "narx": 5999,
        "days": 90,
        "label": "3 Oylik Premium",
        "desc": "59.99 zł (oyiga ~20 zł • 20% tejash)",
        "tag": "⭐ Tejamkor"
    },
    "yillik": {
        "narx": 17999,
        "days": 365,
        "label": "1 Yillik Premium",
        "desc": "179.99 zł (oyiga ~15 zł • 40% tejash)",
        "tag": "👑 Eng katta chegirma"
    },
}

# Dastlabki 5 ta dars har doim bepul
BEPUL_DARSLAR = ["a1_l01", "a1_l02", "a1_l03", "a1_l04", "a1_l05"]

DB_PATH = "polyakcha.db"

# ═══════════════════════════════════════════
# BAZA BILAN ISHLASH
# ═══════════════════════════════════════════
def init_payment_db():
    con = sqlite3.connect(DB_PATH)
    con.executescript("""
        CREATE TABLE IF NOT EXISTS premium (
            user_id       INTEGER PRIMARY KEY,
            plan          TEXT,
            started_at    TEXT,
            expires_at    TEXT,
            payment_id    TEXT,
            amount        INTEGER,
            status        TEXT DEFAULT 'active'
        );
        CREATE TABLE IF NOT EXISTS payments (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id       INTEGER,
            plan          TEXT,
            amount        INTEGER,
            payment_id    TEXT,
            status        TEXT,
            created_at    TEXT
        );
    """)
    # Eski demo/test ma'lumotlarini tozalash
    con.execute("DELETE FROM payments WHERE payment_id LIKE 'test_%'")
    con.execute("DELETE FROM premium WHERE payment_id LIKE 'test_%'")
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

def is_premium(user_id: int) -> bool:
    """Foydalanuvchida hozirgi vaqtda faol premium obuna bor-yo'qligini tekshiradi."""
    row = db("SELECT expires_at FROM premium WHERE user_id=? AND status='active'", (user_id,), "one")
    if not row:
        return False
    try:
        expires = datetime.fromisoformat(row["expires_at"])
        return datetime.now() < expires
    except Exception:
        return False

def get_premium_info(user_id: int) -> dict | None:
    """Foydalanuvchining premium ma'lumotlarini oladi."""
    row = db("SELECT * FROM premium WHERE user_id=? AND status='active'", (user_id,), "one")
    return dict(row) if row else None

def activate_premium(user_id: int, plan: str, payment_id: str, amount: int, days: int = None):
    """Foydalanuvchiga premium beradi yoki muddatini uzaytiradi."""
    now = datetime.now()
    if days is None:
        days = NARXLAR.get(plan, {}).get("days", 30)

    # Agar allaqachon faol premium bo'lsa, qolgan muddatga qo'shamiz
    current = get_premium_info(user_id)
    if current:
        try:
            curr_exp = datetime.fromisoformat(current["expires_at"])
            if curr_exp > now:
                expires = curr_exp + timedelta(days=days)
            else:
                expires = now + timedelta(days=days)
        except Exception:
            expires = now + timedelta(days=days)
    else:
        expires = now + timedelta(days=days)

    db("""INSERT INTO premium (user_id, plan, started_at, expires_at, payment_id, amount, status)
          VALUES (?, ?, ?, ?, ?, ?, 'active')
          ON CONFLICT(user_id) DO UPDATE SET
          plan=?, started_at=?, expires_at=?, payment_id=?, amount=?, status='active'""",
       (user_id, plan, now.isoformat(), expires.isoformat(), payment_id, amount,
        plan, now.isoformat(), expires.isoformat(), payment_id, amount))
    
    db("""INSERT INTO payments (user_id, plan, amount, payment_id, status, created_at)
          VALUES (?, ?, ?, ?, 'success', ?)""",
       (user_id, plan, amount, payment_id, now.isoformat()))
    
    return expires

def can_access_lesson(user_id: int, lesson_id: str) -> bool:
    """Darsga kirish mumkinligini tekshiradi (1-5 darslar bepul, qolganlari premium)."""
    if lesson_id in BEPUL_DARSLAR:
        return True
    return is_premium(user_id)

def get_payment_stats() -> dict:
    """Admin uchun to'lovlar statistikasini chiqaradi."""
    now = datetime.now().isoformat()
    active_premium_count = db("SELECT COUNT(*) as cnt FROM premium WHERE expires_at > ? AND status='active'", (now,), "one")
    total_payments = db("SELECT COUNT(*) as cnt, SUM(amount) as total_sum FROM payments WHERE status='success'", (), "one")
    
    cnt_active = active_premium_count["cnt"] if active_premium_count else 0
    cnt_payments = total_payments["cnt"] if total_payments and total_payments["cnt"] else 0
    sum_total = (total_payments["total_sum"] / 100) if total_payments and total_payments["total_sum"] else 0.0

    return {
        "active_users": cnt_active,
        "total_payments_count": cnt_payments,
        "total_revenue_pln": sum_total
    }

# ═══════════════════════════════════════════
# KLAVIATURALAR
# ═══════════════════════════════════════════
def kb_premium_menu(user_id: int):
    if is_premium(user_id):
        info = get_premium_info(user_id)
        expires = datetime.fromisoformat(info["expires_at"])
        days_left = max((expires - datetime.now()).days, 0)
        return InlineKeyboardMarkup([
            [InlineKeyboardButton(f"✅ Premium faol — {days_left} kun qoldi", callback_data="premium_info")],
            [InlineKeyboardButton("💳 1 Oylik uzaytirish (24.99 zł)", callback_data="buy_oylik")],
            [InlineKeyboardButton("⭐ 3 Oylik uzaytirish (59.99 zł)", callback_data="buy_3oylik")],
            [InlineKeyboardButton("👑 1 Yillik uzaytirish (179.99 zł)", callback_data="buy_yillik")],
            [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")],
        ])
    else:
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("💳 1 Oylik — 24.99 zł", callback_data="buy_oylik")],
            [InlineKeyboardButton("⭐ 3 Oylik — 59.99 zł (20% tejash)", callback_data="buy_3oylik")],
            [InlineKeyboardButton("👑 1 Yillik — 179.99 zł (40% tejash)", callback_data="buy_yillik")],
            [InlineKeyboardButton("🎁 Promo kod kiritish", callback_data="promo_code")],
            [InlineKeyboardButton("🏠 Bosh menyu", callback_data="main")],
        ])

# ═══════════════════════════════════════════
# XABARLAR VA HANDLERLAR
# ═══════════════════════════════════════════
async def show_premium(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if is_premium(user_id):
        info = get_premium_info(user_id)
        expires = datetime.fromisoformat(info["expires_at"])
        days_left = max((expires - datetime.now()).days, 0)
        text = (
            "💎 *Sizning Premium Obunangiz*\n\n"
            f"✅ Holat: *Faol*\n"
            f"📋 Reja: *{info['plan'].capitalize()}*\n"
            f"📅 Tugash sanasi: *{expires.strftime('%d.%m.%Y')}*\n"
            f"⏳ Qolgan vaqt: *{days_left} kun*\n\n"
            "🎉 Barcha 40+ ta dars, lug'atlar, audio talaffuz va testlar siz uchun ochiq!"
        )
    else:
        text = (
            "💎 *PolUzAcademy Premium Obunasi*\n\n"
            "🆓 *Bepul versiyada:*\n"
            "• Faqat dastlabki 5 ta dars (A1.1)\n"
            "• Cheklangan mashqlar\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "💎 *Premium obuna bilan nimalarga ega bo'lasiz?*\n"
            "✅ *Barcha 40+ darslar* (A1.1, A1.2, A2.1, A2.2 to'liq)\n"
            "✅ *🔊 Tabiiy polyakcha ovozli talaffuz* (har bir so'z va dialog)\n"
            "✅ *Amaliy mavzular:* Ish, Urząd (idora), Karta Pobytu, Do'kon, Tibbiyot\n"
            "✅ *Cheksiz ❤️ yuraklar* (xato qilsangiz ham dars to'xtamaydi)\n"
            "✅ *Grammatika kartochkalari va testlar*\n"
            "✅ *Reklama va cheklovlarsiz*\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "💳 *Qulay to'lov:* **BLIK**, **Karta (Visa/Mastercard)**, **Apple/Google Pay**\n\n"
            "💰 *Tariflar:*\n"
            "• 💳 **1 Oylik:** `24.99 zł / oy`\n"
            "• ⭐ **3 Oylik:** `59.99 zł` _(oyiga ~20 zł • 20% tejash)_\n"
            "• 👑 **1 Yillik:** `179.99 zł` _(oyiga ~15 zł • 40% tejash)_\n\n"
            "⬇️ *Obunani tanlang va bir zumda to'lang:*"
        )
    if update.callback_query:
        await update.callback_query.edit_message_text(text, parse_mode="Markdown", reply_markup=kb_premium_menu(user_id))
    else:
        msg = update.message
        await msg.reply_text(text, parse_mode="Markdown", reply_markup=kb_premium_menu(user_id))

async def send_invoice(update: Update, ctx: ContextTypes.DEFAULT_TYPE, plan: str):
    q = update.callback_query
    user_id = q.from_user.id
    narx_info = NARXLAR.get(plan, NARXLAR["oylik"])
    bot_obj = await ctx.bot.get_me()
    bot_username = bot_obj.username or "PolUzAcademyBot"

    # Stripe API key
    stripe_key = os.environ.get("STRIPE_SECRET_KEY", "")
    stripe.api_key = stripe_key
    pay_url = None

    if stripe_key:
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=["card", "blik"],
                line_items=[{
                    "price_data": {
                        "currency": CURRENCY,
                        "product_data": {"name": f"PolUzAcademy — {narx_info['label']}"},
                        "unit_amount": narx_info["narx"],
                    },
                    "quantity": 1,
                }],
                mode="payment",
                success_url=f"https://t.me/{bot_username}?start=success_{plan}_{user_id}",
                cancel_url=f"https://t.me/{bot_username}?start=cancel",
                metadata={"user_id": str(user_id), "plan": plan}
            )
            pay_url = checkout_session.url
        except Exception as e:
            logger.error(f"Stripe Checkout yaratishda xatolik: {e}")
            pay_url = None

    if not pay_url:
        pay_url = f"https://t.me/{bot_username}?start=simpay_{plan}"

    keyboard = []
    if pay_url:
        keyboard.append([InlineKeyboardButton("💳 To'lov sahifasiga o'tish (BLIK / Karta)", url=pay_url)])
    keyboard.append([InlineKeyboardButton("◀️ Orqaga", callback_data="premium_menu")])

    await q.answer("💳 To'lov havolasi tayyorlandi!")
    await q.edit_message_text(
        f"💳 *{narx_info['label']} uchun to'lov havolasi!*\n\n"
        f"💰 Narxi: *{narx_info['desc']}*\n"
        f"⏳ Amal qilish muddati: *{narx_info['days']} kun*\n\n"
        "📱 *To'lash yo'riqnomasi:*\n"
        "1. Quyidagi **To'lov sahifasiga o'tish** tugmasini bosing.\n"
        "2. **BLIK** kodingizni yoki karta ma'lumotlaringizni kiriting.\n"
        "3. To'lov amalga oshishi bilan botda barcha darslar avtomatik ochiladi!",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ═══════════════════════════════════════════
# PROMO KODLAR
# ═══════════════════════════════════════════
PROMO_KODLAR = {
    "POLUZ2026": {"chegirma": 100, "reja": "trial", "kunlar": 30},
    "START5":     {"chegirma": 100, "reja": "trial", "kunlar": 7},
    "USTOZ":      {"chegirma": 100, "reja": "trial", "kunlar": 365},
    "POLSHA":     {"chegirma": 100, "reja": "trial", "kunlar": 14},
}

async def handle_promo(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.edit_message_text(
        "🎁 *Promo Kod*\n\nMaxsus promo kodingizni yozing (masalan: `POLUZ2026`):",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("◀️ Orqaga", callback_data="premium_menu")]])
    )
    ctx.user_data["waiting_promo"] = True

async def check_promo_code(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if not ctx.user_data.get("waiting_promo"):
        return False
    ctx.user_data["waiting_promo"] = False
    user_id = update.effective_user.id
    kod = update.message.text.strip().upper()

    if kod not in PROMO_KODLAR:
        await update.message.reply_text(
            "❌ *Kiritilgan promo kod topilmadi yoki muddati tugagan.*\n\n"
            "Boshqa kod kiritib ko'ring yoki Premium obunani rasmiylashtiring.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💎 Premium menyusi", callback_data="premium_menu")]
            ])
        )
        return True

    promo = PROMO_KODLAR[kod]
    kunlar = promo.get("kunlar", 30)
    exp = activate_premium(user_id, "promo", f"promo_{kod}", 0, days=kunlar)
    
    await update.message.reply_text(
        f"🎉 *Tabriklaymiz! Promo kod qabul qilindi!*\n\n"
        f"✅ Sizga *{kunlar} kunlik* bepul Premium obunasi taqdim etildi.\n"
        f"📅 Tugash sanasi: *{exp.strftime('%d.%m.%Y')}*\n\n"
        "Endi barcha darslarni bemalol o'rganishingiz mumkin!",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📚 Darslarni boshlash", callback_data="lessons")]
        ])
    )
    return True

async def payment_callback(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    d = q.data
    await q.answer()
    if d == "premium_menu":
        await show_premium(update, ctx)
    elif d == "buy_oylik":
        await send_invoice(update, ctx, "oylik")
    elif d == "buy_3oylik":
        await send_invoice(update, ctx, "3oylik")
    elif d == "buy_yillik":
        await send_invoice(update, ctx, "yillik")
    elif d == "premium_renew":
        await show_premium(update, ctx)
    elif d == "premium_info":
        user_id = q.from_user.id
        info = get_premium_info(user_id)
        if not info:
            await q.answer("Premium topilmadi!", show_alert=True)
            return
        expires = datetime.fromisoformat(info["expires_at"])
        days_left = max((expires - datetime.now()).days, 0)
        await q.answer(f"✅ Premium faol. Qolgan vaqt: {days_left} kun", show_alert=True)
    elif d == "promo_code":
        await handle_promo(update, ctx)