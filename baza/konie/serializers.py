from rest_framework import serializers
from .models import Horse, Grade


class HorseSerializer(serializers.ModelSerializer):
    average_grade = serializers.ReadOnlyField()

    class Meta:
        model = Horse
        fields = ('id', 'name', 'average_grade')


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id', 'grade', 'user', 'horse')
        read_only_fields = ('user', 'horse',)
