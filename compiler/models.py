from django.db import models

# Create your models here.
class Questions(models.Model):
    question_no=models.IntegerField()
    question=models.TextField()