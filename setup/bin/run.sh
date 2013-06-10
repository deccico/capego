#!/bin/bash
set -e
LOGFILE=/var/log/gunicorn/capego.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=9  #recommended formula here is 1 + 2 * NUM_CORES
 
#we don't want to run this as root..
USER=www-data
GROUP=www-data
 
cd /home/ubuntu/capego
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django -w $NUM_WORKERS \
  --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE \
  --user=$USER --group=$GROUP
