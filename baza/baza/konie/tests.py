from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from . import views
from .models import RasaKoni
from rest_framework import status
from django.utils.http import urlencode
from django import urls
from django.contrib.auth.models import User


class RasaKoniTests(APITestCase):
    def post_rasa_koni(self, name):
        url = reverse(views.RasaKoniList.name)
        data = {'name':name}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_rasa_koni(self):
        new_rasa_koni_name = 'IT'
        response = self.post_rasa_koni(new_rasa_koni_name)
        print("PK {0}".format(RasaKoni.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert RasaKoni.objects.count() == 1
        assert RasaKoni.objects.get().name == new_rasa_koni_name