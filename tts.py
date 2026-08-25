# -*- coding: utf-8 -*-
"""
🦉 POLYAKCHA BOT — OVOZLI TALAFFUZ (TTS) MODULI
Microsoft Edge TTS orqali tabiiy va toza polyakcha ovoz hosil qilish.
"""

import os
import re
import hashlib
import logging
import asyncio
import edge_tts

logger = logging.getLogger(__name__)

CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio_cache")
os.makedirs(CACHE_DIR, exist_ok=True)

# Polyakcha tabiiy ovozlar
VOICE_MALE = "pl-PL-MarekNeural"
VOICE_FEMALE = "pl-PL-ZofiaNeural"
DEFAULT_VOICE = VOICE_MALE

def clean_text_for_tts(text: str) -> str:
    """Belgilarni va emojilarni tozalab, faqat toza matnni qoldiradi."""
    # Markdown va belgilarni tozalash
    text = re.sub(r"[*_`#~\[\]\(\)]", "", text)
    # Emojilarni olib tashlash (agar bo'lsa)
    text = re.sub(r"[^\w\s\.,!\?'-]", "", text, flags=re.UNICODE)
    return text.strip()

def get_cache_path(text: str, voice: str = DEFAULT_VOICE) -> str:
    """Matn va ovoz uchun kesh fayl yo'lini yaratadi."""
    clean = clean_text_for_tts(text)
    hash_key = hashlib.md5(f"{clean}_{voice}".encode("utf-8")).hexdigest()
    return os.path.join(CACHE_DIR, f"{hash_key}.mp3")

async def generate_speech(text: str, voice: str = DEFAULT_VOICE) -> str | None:
    """
    Berilgan polyakcha matnni audio faylga aylantiradi.
    Keshda mavjud bo'lsa darhol qaytaradi, bo'lmasa yaratadi.
    """
    clean = clean_text_for_tts(text)
    if not clean:
        return None

    file_path = get_cache_path(clean, voice)
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        return file_path

    try:
        communicate = edge_tts.Communicate(clean, voice)
        await communicate.save(file_path)
        return file_path
    except Exception as e:
        logger.error(f"TTS xatoligi ({text}): {e}")
        return None

async def generate_vocab_audio(vocab_list: list, voice: str = DEFAULT_VOICE) -> str | None:
    """
    Darsdagi barcha so'zlarni pauzalar bilan bitta chiroyli audio faylga yig'adi.
    Masalan: 'Dzień dobry. ... Cześć. ... Dziękuję.'
    """
    words = [item.get("pl", "") for item in vocab_list if item.get("pl")]
    if not words:
        return None
    
    full_text = " ... ".join(words)
    return await generate_speech(full_text, voice)
