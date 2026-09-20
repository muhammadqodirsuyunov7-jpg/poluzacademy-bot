# -*- coding: utf-8 -*-
"""
🦉 POLUZACADEMY — LUG'AT, FLASHCARD VA XATOLAR XIZMATI
Barcha 40 ta dars lug'atini yagona indeksda birlashtirish,
tezkor qidiruv, flashcards va xatolar ustida ishlash moduli.
"""

import sqlite3
import re
from datetime import datetime
from lessons_a1 import A1_LESSONS
from lessons_a2 import A2_LESSONS

DB_PATH = "polyakcha.db"

# Barcha darslar lug'atini yagona lug'atga birlashtirish va indekslash
ALL_LESSONS = {**A1_LESSONS, **A2_LESSONS}

def _build_vocab_index():
    """Barcha darslardan noyob so'zlarni to'playdi."""
    index = []
    seen = set()
    for lid, ldata in ALL_LESSONS.items():
        title = ldata.get("title", lid)
        for item in ldata.get("vocab", []):
            pl = item.get("pl", "").strip()
            uz = item.get("uz", "").strip()
            ph = item.get("ph", "").strip()
            key = f"{pl.lower()}_{uz.lower()}"
            if key not in seen and pl:
                seen.add(key)
                index.append({
                    "pl": pl,
                    "ph": ph,
                    "uz": uz,
                    "lesson_id": lid,
                    "lesson_title": title,
                })
    return index

VOCAB_INDEX = _build_vocab_index()

def normalize_text(text: str) -> str:
    """Qidiruv uchun matnni soddalashtiradi (polyakcha maxsus belgilarni hisobga olgan holda)."""
    t = text.lower().strip()
    replace_map = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'
    }
    for k, v in replace_map.items():
        t = t.replace(k, v)
    return t

def search_vocab(query: str, limit: int = 6) -> list:
    """
    Foydalanuvchi yozgan so'zni o'zbekcha yoki polyakcha bo'yicha qidiradi.
    Natija eng mos keladigan so'zlar ro'yxati shaklida qaytadi.
    """
    q_raw = query.lower().strip()
    q_norm = normalize_text(q_raw)
    if not q_raw or len(q_raw) < 2:
        return []

    exact_matches = []
    starts_matches = []
    contains_matches = []

    for item in VOCAB_INDEX:
        pl_raw = item["pl"].lower()
        uz_raw = item["uz"].lower()
        pl_norm = normalize_text(pl_raw)
        uz_norm = normalize_text(uz_raw)

        # Aniq moslik
        if q_raw == pl_raw or q_raw == uz_raw or q_norm == pl_norm:
            exact_matches.append(item)
        # So'z boshidan moslik
        elif pl_raw.startswith(q_raw) or uz_raw.startswith(q_raw) or pl_norm.startswith(q_norm):
            starts_matches.append(item)
        # So'z ichida moslik
        elif q_raw in pl_raw or q_raw in uz_raw or q_norm in pl_norm or q_norm in uz_norm:
            contains_matches.append(item)

    combined = exact_matches + starts_matches + contains_matches
    result = []
    seen = set()
    for item in combined:
        key = item["pl"].lower()
        if key not in seen:
            seen.add(key)
            result.append(item)
        if len(result) >= limit:
            break
    return result

# ═══════════════════════════════════════════
# FLASHCARDS BAZASI
# ═══════════════════════════════════════════
def init_dict_db():
    con = sqlite3.connect(DB_PATH)
    con.executescript("""
        CREATE TABLE IF NOT EXISTS flashcards (
            user_id    INTEGER,
            lesson_id  TEXT,
            word_pl    TEXT,
            status     INTEGER DEFAULT 0,
            updated_at TEXT,
            PRIMARY KEY (user_id, lesson_id, word_pl)
        );
        CREATE TABLE IF NOT EXISTS mistakes (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id    INTEGER,
            lesson_id  TEXT,
            question   TEXT,
            opts_json  TEXT,
            correct_idx INTEGER,
            wrong_choice TEXT,
            created_at TEXT,
            UNIQUE(user_id, question)
        );
    """)
    con.commit()
    con.close()

def mark_card_learned(user_id: int, lesson_id: str, word_pl: str, learned: bool = True):
    status = 1 if learned else 0
    now = datetime.now().isoformat()
    con = sqlite3.connect(DB_PATH)
    con.execute("""
        INSERT INTO flashcards (user_id, lesson_id, word_pl, status, updated_at)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(user_id, lesson_id, word_pl) DO UPDATE SET status=?, updated_at=?
    """, (user_id, lesson_id, word_pl, status, now, status, now))
    con.commit()
    con.close()

def get_lesson_flashcards_progress(user_id: int, lesson_id: str):
    """Darsdagi o'zlashtirilgan so'zlar sonini qaytaradi."""
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute(
        "SELECT COUNT(*) FROM flashcards WHERE user_id=? AND lesson_id=? AND status=1",
        (user_id, lesson_id)
    )
    row = cur.fetchone()
    learned = row[0] if row else 0
    con.close()
    return learned

# ═══════════════════════════════════════════
# XATOLAR USTIDA ISHLASH (MISTAKES)
# ═══════════════════════════════════════════
import json

def record_mistake(user_id: int, lesson_id: str, question: str, opts: list, correct_idx: int, wrong_choice: str):
    """Foydalanuvchi testda qilgan xatosini saqlaydi."""
    now = datetime.now().isoformat()
    opts_json = json.dumps(opts, ensure_ascii=False)
    con = sqlite3.connect(DB_PATH)
    con.execute("""
        INSERT INTO mistakes (user_id, lesson_id, question, opts_json, correct_idx, wrong_choice, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(user_id, question) DO UPDATE SET
            lesson_id=?, opts_json=?, correct_idx=?, wrong_choice=?, created_at=?
    """, (user_id, lesson_id, question, opts_json, correct_idx, wrong_choice, now,
          lesson_id, opts_json, correct_idx, wrong_choice, now))
    con.commit()
    con.close()

def get_user_mistakes(user_id: int, limit: int = 10) -> list:
    """Foydalanuvchining hal qilinmagan xatolarini qaytaradi."""
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    rows = cur.execute(
        "SELECT * FROM mistakes WHERE user_id=? ORDER BY id DESC LIMIT ?",
        (user_id, limit)
    ).fetchall()
    con.close()
    result = []
    for r in rows:
        d = dict(r)
        d["opts"] = json.loads(d["opts_json"]) if d.get("opts_json") else []
        result.append(d)
    return result

def get_user_mistakes_count(user_id: int) -> int:
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM mistakes WHERE user_id=?", (user_id,))
    row = cur.fetchone()
    cnt = row[0] if row else 0
    con.close()
    return cnt

def resolve_mistake(user_id: int, question: str):
    """Xato to'g'ri yechilganda uni bazadan o'chiradi."""
    con = sqlite3.connect(DB_PATH)
    con.execute("DELETE FROM mistakes WHERE user_id=? AND question=?", (user_id, question))
    con.commit()
    con.close()

def clear_all_mistakes(user_id: int):
    con = sqlite3.connect(DB_PATH)
    con.execute("DELETE FROM mistakes WHERE user_id=?", (user_id,))
    con.commit()
    con.close()
