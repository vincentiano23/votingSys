from django.contrib import admin
from .models import Candidate, Vote

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'party', 'votes')
    search_fields = ('name', 'party')

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'voter_name', 'timestamp')
    search_fields = ('voter_name', 'candidate__name')
    list_filter = ('timestamp',)
