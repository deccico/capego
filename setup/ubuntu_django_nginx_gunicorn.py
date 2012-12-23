"""This configuration holds the list of cmds that are going to be applied to a list of ami's. 
This is part of the normal Bellatrix process. The new configuration will be burned into a new ami.

The available set of commands can be found in https://bitbucket.org/adeccico/bellatrix/src/tip/bellatrix/lib/cmds.py
"""




env = "django_app"
project_name = "app"
django_app_dir = "/home/ubuntu/django_app"

def configureNginx():
    #prepare directories
    commands = cmds.sudo(cmds.mkdir("/opt/django/logs/nginx/"))
    #Create directories and softlinks for static content and templates
    commands += cmds.mkdir("$HOME/django_app/static")
    commands += cmds.mkdir("$HOME/django_app/templates")
    commands += cmds.sudo(cmds.createSoftLink("$HOME/django_app/static", "/opt/django"))
    #download and set up Nginx configuration. Basically it will listen in port 80 and forward to port 8000 dynamic content
    commands += cmds.sudo(cmds.copy("/etc/nginx/sites-available/default", "/etc/nginx/sites-available/default.backup"))
    commands += cmds.wget("https://bitbucket.org/deccico/django_gunicorn/raw/tip/server/etc/nginx/sites-available/default")
    commands += cmds.sudo(cmds.copy("default", "/etc/nginx/sites-available/default"))
    return commands

def appendTemplateDir(settings_file):
    cmd = cmds.wget("https://bitbucket.org/deccico/django_gunicorn/raw/tip/django_app/template_dirs")
    cmd += ['cat %s >> %s' % ('template_dirs', settings_file)]
    return cmd

import logging
import os

#common variables
user = "ubuntu"             #user of the ami's 
amis = [["ami-fd589594",  "ubuntu1104-ff36-mysql51-x64"],] #list of AMI's that 'bellatrix bewitch' will configure.
key_name = "key"          #Name of the key-pair name that will be applied to your instance. 
security_groups = "default"   #comma separated list (with no spaces) of the security groups that will be applied to the new instance. It can be only one. Usually is. e.g. mysecurity_group
instance_type = "t1.micro"    #type of instance that will be used for applying the configuration. Usually t1.micro should be enough. List of codes here: http://aws.amazon.com/ec2/instance-types for more
#------------------------------------------------------------------------------------------------

from bellatrix.lib import cmds

#list of cmds to execute
commands = []
commands = cmds.install_pip() 
commands += cmds.pip_install("virtualenv") 
commands += cmds.install_nginx() 
commands += cmds.createVirtualEnv(env) 
commands += cmds.installPackageInVirtualEnv(env, package="django", verification_command="django-admin.py --version")
commands += cmds.installPackageInVirtualEnv(env, package="gunicorn")

commands += cmds.executeInVirtualEnv(env, cmds.create_django_project(project_name, dir_name=env + os.path.sep))
commands += configureNginx()

#setting up Django app
commands += appendTemplateDir(django_app_dir + "/app/app/settings.py")
commands += cmds.wget("https://bitbucket.org/deccico/django_gunicorn/raw/tip/django_app/urls.py", django_app_dir + "/app/app/urls.py")
commands += cmds.wget("https://bitbucket.org/deccico/django_gunicorn/raw/1587f68db41e/templates/test_static.html", \
                      django_app_dir + "/templates/test_static.html")
commands += cmds.wget("https://bitbucket.org/deccico/django_gunicorn/raw/tip/static/django.png", \
                      django_app_dir + "/static/django.png")


##setting up Upstart to automatically launch Django application 
commands += cmds.wget("https://bitbucket.org/deccico/django_gunicorn/raw/tip/run.sh", django_app_dir + "/run.sh")
commands += cmds.chmod("a+x", django_app_dir + "/run.sh")
commands += cmds.sudo(cmds.wget("https://bitbucket.org/deccico/django_gunicorn/raw/tip/server/etc/init/django_app.conf", \
                      "/etc/init/django_app.conf"))

logging.info("commands generated: %s" % commands)

