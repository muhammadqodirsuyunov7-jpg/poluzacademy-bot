@echo off
title PolUzAcademy Telegram Bot
color 0A
echo ===================================================
echo     POLYAKCHA BOT (PolUzAcademy) ISHGA TUSHMOQDA...
echo ===================================================
echo.
cd /d "%~dp0"

echo Eski jarayonlar tozalanmoqda...
taskkill /F /IM py.exe /FI "PID ne %$" >nul 2>&1
taskkill /F /IM python.exe /FI "PID ne %$" >nul 2>&1

echo Bot ishga tushirildi!
py bot.py
pause
