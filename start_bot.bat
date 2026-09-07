@echo off
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
title PolUzAcademy Telegram Bot
color 0A
echo ===================================================
echo     POLYAKCHA BOT (PolUzAcademy) ISHGA TUSHMOQDA...
echo ===================================================
echo.
cd /d "%~dp0"

echo Eski bot jarayonlari tekshirilmoqda...
powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*bot.py*' -and $_.ProcessId -ne $PID } | Stop-Process -Force" >nul 2>&1

echo Bot ishga tushirildi!
py bot.py
pause

