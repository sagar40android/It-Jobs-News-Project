from django.db import models

# Create your models here.
class pubeJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=40)
    title=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()