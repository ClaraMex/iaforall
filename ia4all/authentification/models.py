from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    photo = models.ImageField()

class FilesUpload(models.Model): #table por creer les fichiers et les champs, le plus important fichiers 
    file = models.FileField() #taille etc à mettre majorité des chanmsp non nulle 
    userid = models.IntegerField() # quand qq lance le formulaire on recupere cet id  puis en bas migrer MVT
#table des fichiers 
#models file field 
#id de utilisateur que stocke les données 
#Makemigrations et migrate dans le terminal python3 manage.py makemigrations et migrate après
