from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    voter_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.voter_name} voted for {self.candidate.name}'

class Voter(models.Model):
    voter_name = models.CharField(max_length=120, default="default_voter_name")
    voter_id = models.CharField(max_length=8, unique=True,default="default_voter_id" )

    def __str__(self):
        return f"{self.voter_name} ({self.voter_id})"

  
