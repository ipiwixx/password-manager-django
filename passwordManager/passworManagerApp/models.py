from django.db import models

class Site(models.Model):
    nom = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    identifiant = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.nom