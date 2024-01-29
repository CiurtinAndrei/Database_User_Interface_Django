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

    def __str__(self):
        return f"{self.nume} {self.prenume} (ID: {self.id_avocat})"

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

    def __str__(self):
        return f"{self.nume} {self.prenume} (ID: {self.id_client})"

class Contract(models.Model):
    id_contract = models.BigAutoField(primary_key=True)
    id_avocat_ctr = models.ForeignKey(Avocat, on_delete=models.CASCADE, to_field='id_avocat', db_column='id_avocat_ctr')
    id_client_ctr = models.ForeignKey(Client, on_delete=models.CASCADE, to_field='id_client', db_column='id_client_ctr')
    valoare = models.DecimalField(max_digits=10, decimal_places=2)
    data_start = models.DateField()
    data_sfarsit = models.DateField(null=True, blank=True)
    judecatorie = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'contract'