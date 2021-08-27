from django.db import models
from django.conf import settings
from django.db.models.base import Model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Horse(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @property
    def average_grade(self):
        grades = Grade.objects.filter(horse=self)
        listOfGrades = []
        for object in grades:
            listOfGrades.append(object.grade)
        return sum(listOfGrades) / len(listOfGrades)


class Grade(models.Model):
    grade = models.IntegerField(validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    horse = models.ForeignKey(
        Horse, on_delete=models.CASCADE, related_name='horse')

    def __str__(self):
        return str(self.horse) + " : " + str(self.grade)
