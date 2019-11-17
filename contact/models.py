from django.db import models
from django.contrib.auth.models import User

# Create your models here.

INDCHOICES = (
    ('FINANCE', 'FINANCE'),
    ('HEALTHCARE', 'HEALTHCARE'),
    ('INSURANCE', 'INSURANCE'),
    ('LEGAL', 'LEGAL'),
    ('MANUFACTURING', 'MANUFACTURING'),
    ('PUBLISHING', 'PUBLISHING'),
    ('REAL ESTATE', 'REAL ESTATE'),
    ('SOFTWARE', 'SOFTWARE'),
)

class Account(models.Model):
    nom = models.CharField("Nom du Compte", "nom", max_length=64)
    email = models.EmailField(blank = True, null = True)
    telephone = models.CharField(max_length=20, blank = True, null = True)
    entreprise = models.CharField("Industry Type", max_length=255, choices=INDCHOICES, blank=True, null=True)
    website = models.URLField("Website", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    creerPar = models.ForeignKey(User, related_name='account_creer_par', on_delete=models.CASCADE)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class ContactSource(models.Model):
    status = models.CharField("Contact Source", max_length=20)

    def __str__(self):
        return self.status

class ContactStatus(models.Model):
    status = models.CharField("Contact Status", max_length=20)

    def __str__(self):
        return self.status

class Contact(models.Model):
    nom = models.CharField("Votre Nom", max_length=255, blank = True, null = True)
    prenom = models.CharField("Votre Prénom", max_length=255, blank = True, null = True)
    account = models.ForeignKey(Account, related_name='lead_account_contacts', on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank = True, null = True)
    adresse = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    creerPar = models.ForeignKey(User, related_name='contact_creer_par', on_delete=models.CASCADE)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class ActivityStatus(models.Model):
    status = models.CharField("Activity Status", max_length=20)

    def __str__(self):
        return self.status

class Activity(models.Model):
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.description