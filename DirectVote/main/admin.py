from django.contrib import admin
from DirectVote.main.models import ValidUser, Proposal, Votation

class ValidUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'idcard')
    pass
admin.site.register(ValidUser, ValidUserAdmin)

class VotationAdmin(admin.ModelAdmin):
    list_display = (
                        'proposal',
                        'nb_pro_votes',
                        'nb_con_votes',
                        'nb_blank_votes',
                        'total_votes',
                        'total_available_voters',
                        'start_date',
                        'end_date',
                        'created',
                        'created_by',
                        'modified',
                        'modified_by',
                        )
    pass
admin.site.register(Votation, VotationAdmin)

#class UsersInline(admin.TabularInline):
#    model = ValidUser
#    extra = 1


class ProposalAdmin(admin.ModelAdmin):
    #inlines = (UsersInline,)
    list_display = (
                        'text',
                        #'authors',
                        'created',
                        'created_by',
                        'modified',
                        'modified_by',
                        )
    pass
admin.site.register(Proposal, ProposalAdmin)

