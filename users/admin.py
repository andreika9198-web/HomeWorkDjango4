from django.contrib import admin

from users.models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email','last_name', 'first_name',)
    search_fields = ('last_name',)
    # list_filter = ('is_staff', 'is_active')
    # ordering = ('id',)
