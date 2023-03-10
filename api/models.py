from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.TextField(max_length=140, default='SOME STRING')
    email=models.EmailField(max_length=140, default='SOME STRING')
    password=models.TextField(max_length=140, default='SOME STRING')
    def __str__(self):
        return self.name


class Hello(models.Model):
    email=models.EmailField(max_length=50)
    created_at=models.DateTimeField()
    def __str__(self):
        return self.name