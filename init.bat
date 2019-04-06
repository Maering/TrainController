@ECHO OFF

# Use this inside your venv

if exist .\TrainControllerProject\db.sqlite3 del .\TrainControllerProject\db.sqlite3
if exist .\TrainControllerProject\TrainControllerApp\migrations\0001_initial.py del .\TrainControllerProject\TrainControllerApp\migrations\0001_initial.py

python.exe .\manage.py makemigrations TrainControllerApp
python.exe .\manage.py migrate

python.exe .\manage.py loaddata users.json
python.exe .\manage.py loaddata commands.json

python.exe .\manage.py runserver

PAUSE