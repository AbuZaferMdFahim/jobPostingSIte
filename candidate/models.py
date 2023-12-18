from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyApplyJobList(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    job = models.ForeignKey(CandidateApplication,on_delete = models.CASCADE)
    dateYouApply = models.DateField(auto_now_add = True)
    

class IsSortList(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    job = models.OneToOneField(JobPost, on_delete = models.CASCADE)
    dateYouApply = models.DateField(auto_now_add = True)
