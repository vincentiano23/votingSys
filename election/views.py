from django.shortcuts import render, redirect
from .models import Candidate, Vote
from django.http import HttpResponseForbidden

def candidate_list(request):
    candidates = Candidate.objects.all()
    
    if request.method == 'POST':
        voter_name = request.POST.get('voter_name')
        candidate_id = request.POST.get('candidate_id')
        
        if candidate_id:
            candidate = Candidate.objects.get(id=candidate_id)
            # Check if the voter has already voted
            if Vote.objects.filter(voter_name=voter_name).exists():
                return HttpResponseForbidden("You have already voted!")
            else:
                Vote.objects.create(candidate=candidate, voter_name=voter_name)
                candidate.votes += 1
                candidate.save()
                return redirect('candidate_list')
    
    return render(request, 'election/candidate_list.html', {
        'candidates': candidates,
        'voter_has_voted': Vote.objects.filter(voter_name=request.POST.get('voter_name')).exists()
    })

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
