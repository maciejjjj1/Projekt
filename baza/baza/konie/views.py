from rest_framework import generics, status
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Kon, RasaKoni, Parametry, Bonitacja, Grade
from .serializers import RasaKoniSerializer, KonSerializer, ParametrySerializer, BonitacjaSerializer, GradeSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User
from .custompermission import ISCurrentOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.decorators.csrf import requires_csrf_token




def index (request):
    print(request.user)
    return render(request, 'index.html')

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class RasaKoniList(generics.ListCreateAPIView):
    queryset = RasaKoni.objects.all()
    serializer_class = RasaKoniSerializer
    name = 'rasakoni-list'


class RasaKoniDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RasaKoni.objects.all()
    serializer_class = RasaKoniSerializer
    name = 'rasakoni-detail'



class KonList(generics.ListCreateAPIView):
    queryset = Kon.objects.all()
    serializer_class = KonSerializer
    name = 'kon-list'
    filter_fields = ['imie', 'rasa_koni', 'birthday_date', 'added_time']
    search_fields = ['imie', 'rasa_koni']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, ISCurrentOwnerOrReadOnly,)




class KonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kon.objects.all()
    serializer_class = KonSerializer
    name = 'kon-detail'


class ParametryList(generics.ListCreateAPIView):
    queryset = Parametry.objects.all()
    serializer_class = ParametrySerializer
    name = 'parametry-list'



class ParametryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parametry.objects.all()
    serializer_class = ParametrySerializer
    name = 'parametry-detail'

class BonitacjaList(generics.ListCreateAPIView):
    queryset = Bonitacja.objects.all()
    serializer_class = BonitacjaSerializer
    name = 'bonitacja-list'



class BonitacjaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bonitacja.objects.all()
    serializer_class = BonitacjaSerializer
    name = 'bonitacja-detail'



class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'kon-categories': reverse(RasaKoniList.name, request=request),
                         'konie': reverse(KonList.name, request=request),
                         'parametry': reverse(ParametryList.name, request=request),
                         'bonitacja': reverse(BonitacjaList.name, request=request),


})



#wyswietlenie koni od najlepiej do najgorzej ocenianych
class ListRecommendedKonie(APIView):
    def get(self, request):
        konie = Kon.objects.all()
        sortedkonie = sorted(
            konie, key=lambda Kon: Kon.average_grade, reverse=True)
        serializer = KonSerializer(sortedkonie, many=True)

        return Response(serializer.data)

#widok testowy - wyswietla wszystkie oceny
class ListGrades(APIView):
    name = 'list-grades'
    def get(self, request):
        grades = Grade.objects.all()
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)

#widok pozwalajacy na ocene konia\

class RateKon(APIView):
    permission_classes = [IsAuthenticated, ]
    @csrf_protect
    def post(self, request, pk):
        kon = get_object_or_404(Kon, pk=pk)
        try:
            #sprawdzenie czy zalogowany uzytkownik ocenil juz konia
            print(request.user)
            alreadyRated = Grade.objects.get(kon=kon, user=request.user)
        except Grade.DoesNotExist:
            serializer = GradeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, kon=kon)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Grade.MultipleObjectsReturned:
            return Response({'response': "You've already rated this horse"})
        else:
            return Response({'response': "You've already rated this horse"})

