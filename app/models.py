from django.db import models

# Create your models here.

class College(models.Model):
    clg_name = models.CharField(max_length=100)
    clg_location = models.CharField(max_length=100)
    clg_principal = models.CharField(max_length=100)
    clg_code = models.IntegerField()
    def __str__(self):
        return self.clg_name
    
