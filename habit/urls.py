from django.urls import path

from habit.apps import HabitConfig
from habit.views import HabitCreateAPIView, HabitUpdateAPIView, HabitDestroyAPIView


app_name = HabitConfig.name

urlpatterns = [
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_delete"),
]
