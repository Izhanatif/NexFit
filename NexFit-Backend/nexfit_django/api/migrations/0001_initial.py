# Generated by Django 4.2.4 on 2024-05-07 11:27

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Gym Name')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('city', models.CharField(max_length=255, verbose_name='City Name')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='GymTrainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=15, null=True)),
                ('isAdmin', models.BooleanField(default=False)),
                ('isTrainer', models.BooleanField(default=True)),
                ('isUser', models.BooleanField(default=False)),
                ('monthly_charges', models.IntegerField(blank=True, null=True)),
                ('certification', models.CharField(blank=True, max_length=1000, null=True)),
                ('available', models.BooleanField(default=True)),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gym')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GymUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=15)),
                ('trainerSelected', models.BooleanField(blank=True, default=False, null=True)),
                ('isAdmin', models.BooleanField(default=False)),
                ('isTrainer', models.BooleanField(default=False)),
                ('isUser', models.BooleanField(default=True)),
                ('number_of_tokens', models.PositiveIntegerField(default=0)),
                ('membership', models.CharField(choices=[('active', 'Active'), ('pending', 'Pending'), ('cancelled', 'Cancelled')], default=('active', 'Active'), max_length=255)),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gym')),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainees', to='api.gymtrainer')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GymUserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('gym_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gymuser')),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.attendancetoken')),
            ],
        ),
        migrations.CreateModel(
            name='GymTokenPlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('plan_price', models.PositiveIntegerField()),
                ('number_of_tokens', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('duration_of_months', models.PositiveIntegerField()),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gym')),
            ],
        ),
        migrations.CreateModel(
            name='GymPurchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_tokens', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gym')),
                ('gym_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gymuser')),
                ('token_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gymtokenplans')),
            ],
        ),
        migrations.CreateModel(
            name='GymEquipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gym')),
            ],
        ),
        migrations.CreateModel(
            name='GymAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAdmin', models.BooleanField(default=True)),
                ('isTrainer', models.BooleanField(default=False)),
                ('isUser', models.BooleanField(default=False)),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gym')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('exercise_type', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.models.upload_to)),
                ('description', models.TextField(blank=True, null=True)),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gym')),
            ],
        ),
        migrations.AddField(
            model_name='attendancetoken',
            name='gym',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.gym'),
        ),
        
    ]
