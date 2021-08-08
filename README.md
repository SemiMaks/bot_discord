# bot_discord
***
Бот для Дискорда.
Для запуска бота нужен батник в корневую папку следующего содержания:
***
@echo off

call %~dp0\venv\Scripts\activate

cd %~dp0bot\

set TOKEN=токен вставить свой

python botrun.py

pause
***
