from django.contrib import admin
from .models import Notice, Profile
from django.contrib.admin.options import ModelAdmin

# Register your models here.

class UserProfile(ModelAdmin):
    list_display = ['name', 'gender', 'age']
    search_fields = ['name', 'gender', 'age']
    list_filter = ['age']


admin.site.register(Profile, UserProfile)

class NoticeAdmin(ModelAdmin):
    list_display = ['subject', 'cr_date']
    search_fields = ['subject', 'msg']
    list_filter = ['cr_date']


admin.site.register(Notice, NoticeAdmin)
