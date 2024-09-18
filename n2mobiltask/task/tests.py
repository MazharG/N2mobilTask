from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Users, Address, Geo, Company
from .serializers import UsersSerializer

class UsersAPITestCase(APITestCase):

    def setUp(self):
        self.address = Address.objects.create(street="sokullu", suite="H.Sami", city="Ankara", zipcode="06520")
        self.geo = Geo.objects.create(lat=42.2, lng=-1.1)
        self.company = Company.objects.create(name="Mazhar AŞ")
        self.user = Users.objects.create(
            name="Mazhar",
            username="Güzel",
            email="mazharguzel@gmail.com",
            address=self.address,
            geo=self.geo,
            phone="+0534789125",
            website="mazhargüzel.com",
            company=self.company
        )

    def test_get_users(self):
        url = reverse('users-list')
        response = self.client.get(url, format='json')
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_user(self):
        url = reverse('users-list')
        data = {
            "name": "Mazhar",
            "username": "Güzel",
            "email": "mazharguzel@gmail.com",
            "address": {
                "street": "sokullu",
                "suite": "H.Sami",
                "city": "Ankara",
                "zipcode": "06520"
            },
            "geo": {
                "lat": 2.2,
                "lng": 1.1
            },
            "phone": "+0534789125",
            "website": "mazhargüzel.com",
            "company": {
                "name": "Mazhar AŞ"
            }
        }
        response = self.client.post(url, data, format='json')
        print(response.data)  # Hata mesajını inceleyin
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Users.objects.count(), 2)  # Yeni kullanıcı eklenmiş olmalı

    def test_get_user_detail(self):
        url = reverse('users-detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.user.name)

    def test_update_user(self):
        url = reverse('users-detail', kwargs={'pk': self.user.pk})
        data = {
            "name": "Mazhar Updated",
            "username": "güzelupdated",
            "email": "mazharupdated@gmail.com",
            "address": {
                "street": "Odunpazaro",
                "suite": "ARÇ",
                "city": "Eskişehir",
                "zipcode": "26513"
            },
            "geo": {
                "lat": 1.1,
                "lng": -2.2
            },
            "phone": "+122334455",
            "website": "mazharupdated.com",
            "company": {
                "name": "New Mazhar AŞ"
            }
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Mazhar Updated")

    def test_delete_user(self):
        url = reverse('users-detail', kwargs={'pk': self.user.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Users.objects.count(), 0)
