from django.db import models

# Create your models here.

class Child(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return self.name