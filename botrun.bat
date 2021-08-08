@echo off

call %~dp0\venv\Scripts\activate

cd %~dp0bot\

set TOKEN="....."

python botrun.py

pause
