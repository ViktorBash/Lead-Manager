from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Lead model to store leads. Note that email is unique.
class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE, null=True)
