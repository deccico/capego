./manage.py sqlclear user_data |./manage.py dbshell
./manage.py sqlclear listener |./manage.py dbshell

./manage.py syncdb

./manage.py loaddata user_data db/user_data.json
./manage.py loaddata listener db/listener.json