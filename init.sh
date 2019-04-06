rm .\TrainControllerProject\db.sqlite3
rm .\TrainControllerProject\TrainControllerApp\migrations\0001_initial.py

python3 manage.py makemigrations TrainControllerApp
python3 manage.py migrate

python3 manage.py loaddata users.json
python3 manage.py loaddata commands.json

python3 manage.py runserver
