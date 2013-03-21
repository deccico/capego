set -ex

#./manage.py clean_associations
./manage.py clean_nonces
./manage.py clearsessions

./manage.py sqlclear user_data |./manage.py dbshell
echo "delete from social_auth_usersocialauth;" | ./manage.py dbshell
echo "delete from auth_user where is_staff = false;" | ./manage.py dbshell

./manage.py syncdb
./manage.py loaddata user_data db/user_data.json
./manage.py runserver
