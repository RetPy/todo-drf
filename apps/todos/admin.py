from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_done',)
    list_display_links = ('title',)
    list_editable = ('is_done',)
    list_filter = ('is_done',)
    search_fields = ('title', 'user__username',)
    # readonly_fields = ('user',)
