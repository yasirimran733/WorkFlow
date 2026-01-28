from django.db import models
from django.contrib.auth.models import User
from clients.models import Client
# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    budget = models.IntegerField()
    remainingAmount = models.IntegerField()
    client = models.ForeignKey(Client,on_delete=models.CASCADE,null=True , blank=True)
    startDate = models.DateTimeField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title