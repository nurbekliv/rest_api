
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Parents, Children, WorkHistory, Educations

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Parents)
admin.site.register(Children)
admin.site.register(WorkHistory)
admin.site.register(Educations)
