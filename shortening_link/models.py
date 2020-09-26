from django.db import models

# Create your models here.


class links(models.Model):
    old_link = models.CharField(max_length=200)
    new_link = models.CharField(max_length=200)

    


