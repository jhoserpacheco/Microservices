from django.contrib import admin
from .models import Request, Log
# Register your models here.

class RequestAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)

class LogAdmin(admin.ModelAdmin):
    readonly_fields = ('entrance_time',)

admin.site.register(Request, RequestAdmin)
admin.site.register(Log, LogAdmin)