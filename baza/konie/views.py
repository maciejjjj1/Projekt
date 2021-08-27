from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Horse, Grade
from .serializers import GradeSerializer, HorseSerializer
from rest_framework import status

#wyswietlenie koni od najlepiej do najgorzej ocenianych
class ListRecommendedHorses(APIView):
    def get(self, request):
        horses = Horse.objects.all()
        sortedHorses = sorted(
            horses, key=lambda horse: horse.average_grade, reverse=True)
        serializer = HorseSerializer(sortedHorses, many=True)
        return Response(serializer.data)

#widok testowy - wyswietla wszystkie oceny
class ListGrades(APIView):
    def get(self, request):
        grades = Grade.objects.all()
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)

#widok pozwalajacy na ocene konia
class RateHorse(APIView):
    def post(self, request, horseId):
        horse = get_object_or_404(Horse, pk=horseId)
        try:
            #sprawdzenie czy zalogowany uzytkownik ocenil juz konia
            alreadyRated = Grade.objects.get(horse=horse, user=request.user)
        except Grade.DoesNotExist:
            serializer = GradeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, horse=horse)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Grade.MultipleObjectsReturned:
            return Response({'response': "You've already rated this horse"})
        else:
            return Response({'response': "You've already rated this horse"})
