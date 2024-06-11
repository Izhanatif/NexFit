# Generated by Django 4.2.4 on 2024-06-10 10:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_workoutplanday_exercises_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_type', models.CharField(choices=[('weight_gain', 'Weight Gain'), ('weight_loss', 'Weight Loss'), ('bmi', 'BMI')], max_length=20)),
                ('target_value', models.FloatField(help_text='Target weight or BMI')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(help_text='Target date to achieve goal')),
                ('gym_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personal_goals', to='api.gymuser')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('current_value', models.FloatField(help_text='Current weight or BMI')),
                ('personal_goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekly_progresses', to='api.personalgoal')),
            ],
        ),
    ]
