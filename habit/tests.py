from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="1111@gmail.com")
        self.habit = Habit.objects.create(
            owner=self.user,
            action="Тест",
            is_pleasant_habit=False,
            periodicity=2,
            is_published=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        url = reverse("habits:habit_create")
        data = {
            "action": "Тест2",
            "is_pleasant_habit": False,
            "periodicity": 1,
            "is_published": True,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_list(self):
        url = reverse("habits:habits")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 4,
                    "place": None,
                    "time": None,
                    "action": "Тест",
                    "is_pleasant_habit": False,
                    "periodicity": 2,
                    "reward": None,
                    "duration": None,
                    "is_published": True,
                    "owner": 3,
                    "associated_habit": None,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_update(self):
        url = reverse("habits:habit_update", args=(self.habit.pk,))
        data = {
            "action": "Тест3",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "Тест3")

    def test_habit_delete(self):
        url = reverse("habits:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
