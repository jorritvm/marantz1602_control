@echo off
call poetry shell
cd src
python energy_saver.py > ../launch_log.txt 2>&1