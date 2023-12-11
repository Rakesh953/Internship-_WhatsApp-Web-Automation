from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class profile(models.Model):
    username=models.OneToOneField(User,models.CASCADE,related_name='pro_pic')
    profile_pic=models.ImageField(upload_to='pro',null=True)
    about=models.CharField(max_length=100,null=True)


class useres(models.Model):
    pass
    
class Usermessages(models.Model):
    username=models.ForeignKey(User,models.CASCADE)
    message=models.TextField(max_length=1000,blank=True)
    send_Date=models.DateField(null=True)
    send_Time=models.TimeField(auto_now_add=True)
    reusername=models.CharField(max_length=100)
    replay=models.CharField(max_length=200,blank=True)
    imagevideo=models.FileField(upload_to='image',null=True)
    pdf_file=models.FileField(upload_to='pdf',null=True)
    '''def __str__(self) -> str:
        return self.username'''
class user_status(models.Model):
    username=models.ForeignKey(User,models.CASCADE,related_name='status_user')
    status_file=models.FileField(upload_to='status')
    status_time=models.DateTimeField()
    status_end=models.DateTimeField()
    duration=models.DurationField(null=True)

