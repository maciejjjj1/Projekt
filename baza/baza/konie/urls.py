from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('breeds',views.RasaKoniList.as_view(), name=views.RasaKoniList.name),
    path('breeds/<int:pk>',views.RasaKoniDetail.as_view(), name=views.RasaKoniDetail.name),
    path('', views.KonList.as_view(), name=views.KonList.name),
    path('<int:pk>', views.KonDetail.as_view(), name=views.KonDetail.name),
    path('rate/<int:pk>', views.RateKon.as_view()),
    path('parameters', views.ParametryList.as_view(), name=views.ParametryList.name),
    path('parameters/<int:pk>', views.ParametryDetail.as_view(), name=views.ParametryDetail.name),
    path('valuation', views.BonitacjaList.as_view(), name=views.BonitacjaList.name),
    path('valuation/<int:pk>', views.BonitacjaDetail.as_view(), name=views.BonitacjaDetail.name),
    path('recommended', views.ListRecommendedKonie.as_view()),
    path('grades', views.ListGrades.as_view()),
    ]

