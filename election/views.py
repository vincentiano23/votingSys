from django.shortcuts import render, redirect
from .models import Candidate, Vote, Voter
from django.http import HttpResponseForbidden
from django.contrib import messages

def candidate_list(request):
    candidates = Candidate.objects.all()
    voter_has_voted = False

    if request.method == 'POST':
        voter_name = request.POST.get('voter_name')
        voter_id = request.POST.get('voter_id')
        candidate_id = request.POST.get('candidate_id')
        
        voter = Voter.objects.filter(voter_id=voter_id).first()
        if voter:
            voter_has_voted = True
            messages.error(request, f"voter with id {voter_id} has already voted!")
        else:
            selected_candidate = Candidate.objects.get(id=candidate_id)
            selected_candidate.votes += 1
            selected_candidate.save()

            new_voter = Voter(voter_name= voter_name, voter_id = voter_id)
            new_voter.save()

            messages.success(request, f"Thank you, {voter_name}. Your vote has been recorded.")
            return redirect('candidate_list')
        
    context = {
        'candidates': candidates,
        'voter_has_voted': voter_has_voted,
    }
    return render(request, 'election/candidate_list.html', context)

# Define the `vote` view if needed
def vote(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    if request.method == 'POST':
        voter_name = request.POST.get('voter_name')
        if Vote.objects.filter(voter_name=voter_name).exists():
            return HttpResponseForbidden("You have already voted!")
        else:
            Vote.objects.create(candidate=candidate, voter_name=voter_name)
            candidate.votes += 1
            candidate.save()
            return redirect('candidate_list')
    
    return render(request, 'election/vote.html', {'candidate': candidate})
