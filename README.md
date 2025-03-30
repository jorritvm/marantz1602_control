# marantz1602_control
Contains a module with reverse engineered Marantz Web API endpoint wrappers.  
Contains another module that turns of the AVR for energy saving.  

## How to deploy
- `git@github.com:jorritvm/marantz1602_control.git`
- `cd marantz1602_control`
- `poetry install --no-root`

## How to run once locally
- `poetry shell`
- `cd src`
- `python energy_saver.py`

## How to schedule overnight execution in windows task scheduler
- Open task scheduler
- Create a new task
- Give it a name
- Set the trigger to daily at 00:00 (or any other time)
- Set the action to start a program
- In the program/script field, enter the path to the `launch_marantz_energy_saver.bat` file

## To do
- Add APScheduler to allow for more scheduling without using the windows task scheduler
- Add dockerfile with HOST network

## Author
Jorrit Vander Mynsbrugge