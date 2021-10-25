from django.contrib import admin

from api.models import Not_Working_Day, Schedule, Sheet, Sheet_Title, Sheet_Value

# Register your models here.
admin.site.register(Sheet_Value)
admin.site.register(Sheet_Title)
admin.site.register(Sheet)
admin.site.register(Schedule)
admin.site.register(Not_Working_Day)