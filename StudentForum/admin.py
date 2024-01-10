from django.contrib import admin
from StudentForum.models import post
# Register your models here.


@admin.register(post)
class postAdmin(admin.ModelAdmin):
    pass