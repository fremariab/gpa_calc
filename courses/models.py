from django.db import models

# Create your models here.
class Course(models.Model):
    course_id=models.CharField(primary_key=True,max_length=8)
    course_name=models.CharField(max_length=40)
    
    class Credits(models.TextChoices):
        FULL="1","Full"   
        HALF="0.5","Half"   

    credits_worth=models.CharField(choices=Credits,default=Credits.FULL,max_length=4)
    associated_major=models.ForeignKey(on_delete=models.CASCADE)
 
class Major(models.Model):
    class MajorName(models.TextChoices):
        CS="CS","Computer Science"   
        BA="BA","Business Administration"   
        CE="CE","Computer Engineering"   
        EE="EE","Electrical Engineering"   
        ME="ME","Mechanical Engineering"   
        GN="GN","General"   
        
    name=models.CharField(max_length=30,choices=MajorName,default=MajorName.GN)
    