from django.db import models
from django.conf import settings
from django.db.models.base import Model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect



class RasaKoni(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Kon(models.Model):
    imie = models.CharField(max_length=250)
    rasa_koni = models.ForeignKey(RasaKoni, related_name='konie', on_delete=models.CASCADE)
    birthday_date = models.DateField()
    added_time = models.DateTimeField(auto_now_add=True)
    date_hierarchy = 'birthday_date'

    def __str__(self):
        return self.imie

    @property
    def average_grade(self):
        grades = Grade.objects.filter(kon=self)
        listOfGrades = []
        for object in grades:
            listOfGrades.append(object.grade)
        if len(listOfGrades) != 0:
            return sum(listOfGrades) / len(listOfGrades)
        else:
            return -1

class Parametry(models.Model):
    kon = models.ForeignKey(Kon, related_name='konie', on_delete=models.CASCADE)
    wzrost = models.IntegerField(max_length=3)
    popreg = models.IntegerField(max_length=3)
    nadpecie = models.IntegerField(max_length=3)
    added_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('kon', 'wzrost', 'popreg', 'nadpecie')

    def __str__(self):
        return self.kon + ',' + self.wzrost + ',' + self.popreg + ',' + self.nadpecie


class Bonitacja(models.Model):
    kon = models.ForeignKey(Kon, related_name='%(class)s_konie', on_delete=models.CASCADE)
    typ = models.IntegerField(max_length=2)
    glowa = models.IntegerField(max_length=1)
    kloda = models.IntegerField(max_length=2)
    noga_przod = models.IntegerField(max_length=1)
    noga_tyl = models.IntegerField(max_length=1)
    kopyta = models.IntegerField(max_length=1)
    step = models.IntegerField(max_length=2)
    klus = models.IntegerField(max_length=2)
    ogolny = models.IntegerField(max_length=2)
    razem = models.IntegerField(max_length=2)

    class Meta:
        ordering = (
            'kon', 'typ', 'glowa', 'kloda', 'noga_przod', 'noga_tyl', 'kopyta', 'step', 'klus', 'ogolny', 'razem')

    def __str__(self):
        return self.kon + ',' + self.typ + ',' + self.glowa + ',' + self.kloda + ',' + self.noga_przod + ',' + self.noga_tyl + ',' + self.kopyta + ',' + self.step + ',' + self.klus + ',' + self.ogolny + ',' + self.razem




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
@csrf_protect
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)




class Grade(models.Model):
    grade = models.IntegerField(validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kon = models.ForeignKey(Kon, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.kon) + " : " + str(self.grade)
