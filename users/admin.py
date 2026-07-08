from django.contrib import admin

from users.models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'telegram', 'is_staff', 'is_active')
    search_fields = ('email', 'phone')
    list_filter = ('is_staff', 'is_active')
    ordering = ('id',)
