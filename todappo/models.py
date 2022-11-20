from django.db import models

# Create your models here.


class Todo(models.Model):
    text = models.CharField(max_length=255)
    create_at = models.DateField(auto_now=True)