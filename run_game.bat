@echo off
title CodeAlpha Hangman Game
cd /d "%~dp0"
python hangman.py
if %errorlevel% neq 0 (
    echo.
    echo Trying with 'py' launcher...
    py hangman.py
)
pause
