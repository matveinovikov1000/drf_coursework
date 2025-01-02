from rest_framework import serializers

from habit.models import Habit
from habit.validators import ValidateAssociatedHabitOrReward, ValidateDuration, ValidateAssociatedHabit, ValidatePleasantHabit, ValidatePeriodicity


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            ValidateAssociatedHabitOrReward(associated_habit="associated_habit", reward="reward"),
            ValidateDuration(duration="duration"),
            ValidateAssociatedHabit(field="associated_habit"),
            ValidatePleasantHabit(is_pleasant_habit="is_pleasant_habit", associated_habit="associated_habit", reward="reward"),
            ValidatePeriodicity(field="periodicity"),
        ]
