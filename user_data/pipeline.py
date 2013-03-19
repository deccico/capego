from django.conf import settings
from models import UserExtraData

import logging
logger = logging.getLogger(settings.APP_NAME)

def add_extra_data(request, *args, **kwargs):
    username = None
    if kwargs.get('user'):
        username = kwargs['user'].username
    else:
        username = request.session.get('saved_username')
    newsletter = request.session.get('newsletter', False)
    newsletter = True if newsletter=='on' else False

    if username:
        UserExtraData.save_additional_values(username, newsletter)
    return None