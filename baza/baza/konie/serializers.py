from rest_framework import serializers
from .models import Kon, RasaKoni, Parametry, Bonitacja, Grade
from django.contrib.auth.models import User


class RasaKoniSerializer(serializers.HyperlinkedModelSerializer):
    konie = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='kon-detail')

    class Meta:
        model = RasaKoni
        fields = ['pk', 'url', 'name', 'konie']


class KonSerializer(serializers.HyperlinkedModelSerializer):
    rasa_koni = serializers.SlugRelatedField(queryset=RasaKoni.objects.all(), slug_field='name')
    average_grade = serializers.ReadOnlyField()


    class Meta:
        model = Kon
        fields = ['imie', 'rasa_koni', 'birthday_date', 'added_time', 'id', 'average_grade']


class ParametrySerializer(serializers.HyperlinkedModelSerializer):
    kon = serializers.SlugRelatedField(queryset=Kon.objects.all(), slug_field='imie')

    class Meta:
        model = Parametry
        fields = ['url', 'wzrost', 'popreg', 'nadpecie', 'kon']

class BonitacjaSerializer(serializers.HyperlinkedModelSerializer):
    kon = serializers.SlugRelatedField(queryset=Kon.objects.all(), slug_field='imie')

    class Meta:
        model = Bonitacja
        fields = ['url', 'kon', 'typ', 'glowa', 'kloda', 'noga_przod', 'noga_tyl', 'kopyta', 'step', 'klus', 'ogolny', 'razem']




class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id', 'grade', 'user', 'kon',)
        read_only_fields = ('user', 'kon',)
