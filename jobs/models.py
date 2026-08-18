from django.db import models

from accounts.models import User

# Create your models here.
class Job(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    vacancy=models.IntegerField(null=True,blank=True)
    salary=models.CharField(max_length=100,null=True,blank=True)
    deadline=models.DateField()
    hr_email=models.EmailField(null=True,blank=True)
    hr_mobile=models.CharField(max_length=100,null=True,blank=True)
    hr_name=models.CharField(max_length=100,null=True,blank=True)
    company_website=models.URLField(null=True,blank=True)
    job_type=models.CharField(max_length=100)
    experience=models.FloatField()
    company_location=models.CharField(max_length=255)
    isActive=models.BooleanField(default=True)
    photo=models.ImageField(upload_to="Jobs/", null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    