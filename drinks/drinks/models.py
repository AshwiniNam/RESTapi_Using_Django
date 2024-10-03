from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    #used to return specified name instead of obj1 in the web app
    def __str__(self):
        return self.name
