@echo off
setlocal EnableDelayedExpansion

:loop
cls
echo This is the scrolling text.
timeout /nobreak /t 1 >nul
goto loop

