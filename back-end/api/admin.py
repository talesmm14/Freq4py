from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.forms import CustomUserChangeForm, CustomUserCreationForm

from api.models import CustomUser, NotWorkingDay, Schedule, Sheet, SheetTitle, SheetValue, NotWorkType

# Register your models here.
admin.site.register(SheetValue)
admin.site.register(SheetTitle)
admin.site.register(Sheet)
admin.site.register(Schedule)
admin.site.register(NotWorkingDay)
admin.site.register(NotWorkType)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)