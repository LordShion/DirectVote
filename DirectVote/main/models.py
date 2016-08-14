from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class ValidUser(models.Model):
    user = models.OneToOneField(User)
    idcard = models.BigIntegerField(primary_key=True)

    class Meta:
        unique_together = ('user', 'idcard',)


    def __unicode__(self):
            return self.user.username

# Proposals
class Proposal(models.Model):
    name = models.CharField(default='Proposal Title', max_length=512)
    text = models.TextField(default='Proposal text', max_length=20000)
    authors = models.ManyToManyField(ValidUser)
    created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='Proposal_created_by', on_delete=models.CASCADE)
    modified = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey(User,related_name='Proposal_modified_by', on_delete=models.CASCADE)

    def __unicode__(self):
            return self.name

    def get_authors(self):
        return " - ".join([p.user.username for p in self.authors.all()])


# Votations
class Votation(models.Model):
    name = models.CharField(default='Proposal Title', max_length=512)
    proposal = models.OneToOneField(Proposal)
    nb_pro_votes = models.IntegerField(default=0)
    nb_con_votes = models.IntegerField(default=0)
    nb_blank_votes = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    total_available_voters = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='Votation_created_by', on_delete=models.CASCADE)
    modified = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey(User,related_name='Votation_modified_by', on_delete=models.CASCADE)

    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)


    def __unicode__(self):
            return self.name


