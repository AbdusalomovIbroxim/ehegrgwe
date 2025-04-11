from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'created_at', 'updated_at')
    search_fields = ('username', 'name', 'email')
    ordering = ('-created_at',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Персональная информация', {
            'fields': ('first_name', 'last_name', 'name', 'email')
        }),
        ('Права доступа', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Даты', {
            'fields': ('last_login', 'created_at', 'updated_at')
        }),
    )

    readonly_fields = ('created_at', 'updated_at')

admin.site.register(User, UserAdmin)
