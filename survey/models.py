from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class SurveyModels(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    