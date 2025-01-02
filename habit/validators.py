from rest_framework.serializers import ValidationError


class ValidateAssociatedHabitOrReward:
    def __init__(self, associated_habit, reward):
        self.associated_habit = associated_habit
        self.reward = reward

    def __call__(self, value):
        mean_associated_habit = dict(value).get(self.associated_habit)
        mean_reward = dict(value).get(self.reward)

        if mean_associated_habit and mean_reward:
            raise ValidationError(f"Поле {"Связанная привычка"} не может быть заполнено одновременно с полем {"Вознаграждение"}")


class ValidateDuration:
    def __init__(self, duration):
        self.duration = duration

    def __call__(self, value):
        mean_time_complete = dict(value).get(self.duration)

        if int(mean_time_complete) > 120:
            raise ValidationError("Время выполнения привычки должно быть не более 120 секунд")


class ValidateAssociatedHabit:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        mean_field = value.get(self.field)

        if mean_field:
            if mean_field.is_pleasant_habit is False:
                raise ValidationError("Связанные привычки могут быть только приятными")


class ValidatePleasantHabit:
    def __init__(self, is_pleasant_habit, associated_habit, reward):
        self.is_pleasant_habit = is_pleasant_habit
        self.associated_habit = associated_habit
        self.reward = reward

    def __call__(self, value):
        mean_is_pleasant_habit = dict(value).get(self.is_pleasant_habit)
        mean_associated_habit = dict(value).get(self.associated_habit)
        mean_reward = dict(value).get(self.reward)

        if mean_is_pleasant_habit and mean_associated_habit or mean_reward:
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")


class ValidatePeriodicity:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        mean_field = dict(value).get(self.field)

        if int(mean_field) == 0:
            raise ValidationError("Периодичность выполнения привычки должна быть не реже 1 раза в 7 дней")
