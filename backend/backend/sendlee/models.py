from django.db import models

# Create your models here.


class user(models.Model):
    name =  models.CharField(max_length= 15 )
    email = models.CharField(max_length=40)
    id_user = models.IntegerField()
    def __str__(self):
        return  self.name