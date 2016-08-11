from django.contrib import admin
from models import ValidUser

class ValidUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'idcard')
    pass
admin.site.register(ValidUser, ValidUserAdmin)