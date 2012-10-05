from django.contrib import admin

from parliament.bills.models import *

class BillOptions(admin.ModelAdmin):
    search_fields = ['number']
    raw_id_fields = ('sponsor_member','sponsor_politician')
    list_display = ('number', 'name', 'session', 'privatemember', 'sponsor_politician', 'added', 'introduced')
    list_filter = ('institution', 'privatemember', 'added', 'sessions', 'introduced')
    ordering = ['-introduced']

class BillInSessionOptions(admin.ModelAdmin):
    list_display = ['bill', 'session']

class BillTextOptions(admin.ModelAdmin):
    list_display = ['bill', 'docid', 'created']
    search_fields = ['bill__number', 'bill__name', 'docid']
    
class VoteQuestionOptions(admin.ModelAdmin):
    list_display = ('number', 'date', 'bill', 'description', 'result')
    raw_id_fields = ('bill',)
    
class MemberVoteOptions(admin.ModelAdmin):
    list_display = ('politician', 'votequestion', 'vote')
    raw_id_fields = ('politician', 'member')
    
class PartyVoteAdmin(admin.ModelAdmin):
    list_display = ('party', 'votequestion', 'vote', 'disagreement')
    

admin.site.register(Bill, BillOptions)
admin.site.register(BillInSession, BillInSessionOptions)
admin.site.register(BillText, BillTextOptions)
admin.site.register(VoteQuestion, VoteQuestionOptions)
admin.site.register(MemberVote, MemberVoteOptions)
admin.site.register(PartyVote, PartyVoteAdmin)