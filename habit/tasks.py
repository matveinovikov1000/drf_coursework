from celery import shared_task

from habit.models import Habit
from habit.services import send_tg_message


@shared_task
def time_reminders_tg():
    habits_list = []
    time_list = []
    habits = Habit.objects.all()
    message = f"Привычки {habits_list} необходимо выполнить в {time_list}"

    for habit in habits:
        habits_list.append(habit.action)
        time_list.append(habit.time)

        if habit.owner.tg_chat_id:
            send_tg_message(message, habit.owner.tg_chat_id)
