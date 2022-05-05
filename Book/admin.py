from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ("username",'fio',"password","class_title")


admin.site.register(Topic)


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)