set -xe

echo "drop table user_data_usersbadge cascade" | ./manage.py dbshell
echo "drop table user_data_badge cascade" | ./manage.py dbshell
./manage.py sqlclear user_data |./manage.py dbshell
./manage.py sqlclear listener |./manage.py dbshell

./manage.py syncdb

./manage.py loaddata user_data db/user_data.json
./manage.py loaddata listener db/listener.json

./manage.py runserver
