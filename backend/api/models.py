from django.db import models

# Create your models here.

class Colonne(models.Model):
    id_col = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    pos = models.IntegerField( blank=True, null=True)
    class Meta:
        db_table = 'colonne'

class Tache(models.Model):
    id_task = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    descr = models.CharField(max_length=255 , blank=True, null=True)
    pos = models.IntegerField( blank=True, null=True)
    id_col = models.ForeignKey('colonne', on_delete=models.CASCADE, db_column='id_col', blank=True, null=True)
    class Meta:
        db_table = 'tache'