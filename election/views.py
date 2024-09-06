from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Candidate, Vote

def candidate_list(request):
    if request.method == 'POST':
 
        voter_name = request.POST.get('voter_name')
        candidate_id = request.POST.get('candidate_id')
        candidate = get_object_or_404(Candidate, id=candidate_id)

        
        Vote.objects.create(candidate=candidate, voter_name=voter_name)

       
        candidate.votes += 1
        candidate.save()

        messages.success(request, f'Thank you {voter_name}, your vote has been recorded!')
        return redirect('candidate_list')

    candidates = Candidate.objects.all()
    return render(request, 'election/candidate_list.html', {'candidates': candidates})

def vote(request, candidate_id):
    if request.method == 'POST':
       
        voter_name = request.POST.get('voter_name')
        candidate = get_object_or_404(Candidate, id=candidate_id)

        # Save vote
        Vote.objects.create(candidate=candidate, voter_name=voter_name)

        # Increment candidate votes
        candidate.votes += 1
        candidate.save()

        messages.success(request, f'Thank you {voter_name}, your vote for {candidate.name} has been recorded!')
        return redirect('candidate_list')

    # Redirect to the candidate list if the method is not POST
    return redirect('candidate_list')
