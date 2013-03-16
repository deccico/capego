echo "delete from user_data_usersbadge;" | ./manage.py dbshell
echo "delete from social_auth_usersocialauth;" | ./manage.py dbshell
echo "delete from auth_user where is_staff = false;" | ./manage.py dbshell

