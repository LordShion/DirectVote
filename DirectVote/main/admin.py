from django.contrib import admin
from DirectVote.main.models import ValidUser

class ValidUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'idcard')
    pass
admin.site.register(ValidUser, ValidUserAdmin)