from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class ValidUser(models.Model):
    user = models.OneToOneField(User)
    idcard = models.BigIntegerField(primary_key=True)

    class Meta:
        unique_together = ('user', 'idcard',)

# Proposals
class Proposal(models.Model):
    text = models.TextField(default='Proposal text', max_length=20000)
    authors = models.ManyToManyField(ValidUser)
    created = models.DateTimeField(editable=False)
    created_by = models.ForeignKey(User, related_name='Proposal_created_by', on_delete=models.CASCADE, editable=False)
    modified = models.DateTimeField(editable=False)
    modified_by = models.ForeignKey(User,related_name='Proposal_modified_by', on_delete=models.CASCADE, editable=False)


# Votations
class Votation(models.Model):
    proposal = models.OneToOneField(Proposal, editable=False)
    nb_pro_votes = models.IntegerField(default=0, editable=False)
    nb_con_votes = models.IntegerField(default=0, editable=False)
    nb_blank_votes = models.IntegerField(default=0, editable=False)
    total_votes = models.IntegerField(default=0, editable=False)
    total_available_voters = models.IntegerField(default=0, editable=False)
    created = models.DateTimeField(editable=False)
    created_by = models.ForeignKey(User, related_name='Votation_created_by', on_delete=models.CASCADE, editable=False)
    modified = models.DateTimeField(editable=False)
    modified_by = models.ForeignKey(User,related_name='Votation_modified_by', on_delete=models.CASCADE, editable=False)

    start_date = models.DateTimeField(editable=False)
    end_date = models.DateTimeField(editable=False)


