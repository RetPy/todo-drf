from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'alias', 'email')
    list_display_links = ('id', 'alias')
    list_filter = ('group', 'direction',)
    search_fields = ('id', 'alias', 'email')
