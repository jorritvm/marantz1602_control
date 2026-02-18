@echo off
echo ==== %DATE% %TIME% ==== >> ../launch_log.txt
call .venv\Scripts\activate.bat
cd src
python energy_saver.py >> ../launch_log.txt 2>&1
