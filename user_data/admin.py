from django.contrib import admin
from models import Badge, UsersBadge, BadgeType, UserExtraData, UserActivity

admin.site.register(Badge)
admin.site.register(UsersBadge)
admin.site.register(BadgeType)
admin.site.register(UserExtraData)
admin.site.register(UserActivity)
