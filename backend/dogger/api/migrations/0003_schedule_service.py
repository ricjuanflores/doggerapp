# Generated by Django 3.1.7 on 2021-02-22 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210222_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small', models.BooleanField()),
                ('medium', models.BooleanField()),
                ('big', models.BooleanField()),
                ('hour_start', models.TimeField()),
                ('hour_finish', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_schedule', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'reservation'), (2, 'offer')])),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'confirm'), (2, 'reject')])),
                ('dogs', models.ManyToManyField(blank=True, to='api.Dog')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner_service', to=settings.AUTH_USER_MODEL)),
                ('schedule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedule_service', to='api.schedule')),
                ('walker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='walker_service', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
