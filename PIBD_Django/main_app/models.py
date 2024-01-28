from django.db import models

class Avocat(models.Model):
    id_avocat = models.BigAutoField(primary_key=True)
    nume = models.CharField(max_length=64)
    prenume = models.CharField(max_length=64)
    telefon = models.CharField(max_length=64)
    cnp = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    specializare = models.CharField(max_length=64)
    speta = models.CharField(max_length=64)

    class Meta:
        db_table = 'avocat'

class Client(models.Model):
    id_client = models.BigAutoField(primary_key=True)
    nume = models.CharField(max_length=64)
    prenume = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    telefon = models.CharField(max_length=64)
    cnp = models.CharField(max_length=64)
    adresa = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'client'
