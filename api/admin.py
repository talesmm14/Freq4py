from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.forms import CustomUserChangeForm, CustomUserCreationForm

from api.models import CustomUser, Not_Working_Day, Schedule, Sheet, Sheet_Title, Sheet_Value, Not_Work_Type

# Register your models here.
admin.site.register(Sheet_Value)
admin.site.register(Sheet_Title)
admin.site.register(Sheet)
admin.site.register(Schedule)
admin.site.register(Not_Working_Day)
admin.site.register(Not_Work_Type)

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