# Generated by Django 5.1.4 on 2025-01-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habit", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="habit",
            name="time_complete",
        ),
        migrations.AddField(
            model_name="habit",
            name="duration",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Укажите продолжительность выполнения привычки в секундах",
                null=True,
                verbose_name="Продолжительность выполнения в секундах",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="periodicity",
            field=models.SmallIntegerField(
                default=1,
                help_text="Укажите периодичность выполнения привычки, раз в 7 дней",
                verbose_name="Периодичность",
            ),
        ),
    ]