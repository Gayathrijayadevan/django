from django.db import models

# Create your models here.
class Student(models.Model):
    rollno=models.IntegerField()
    name=models.TextField()
    age=models.IntegerField()
    mark=models.IntegerField()
    address=models.TextField()