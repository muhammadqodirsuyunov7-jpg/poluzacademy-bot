#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PolUzAcademy Bot Starter
Render.com yoki serverda python main.py yoki python bot.py deb chaqirilganda ishlaydi.
"""
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import bot

if __name__ == "__main__":
    bot.main()
