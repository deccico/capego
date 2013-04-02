from django.contrib import admin
from models import Badge, UserBadge, BadgeType, UserExtraData, UserActivity

admin.site.register(Badge)
admin.site.register(UserBadge)
admin.site.register(BadgeType)
admin.site.register(UserExtraData)
admin.site.register(UserActivity)
