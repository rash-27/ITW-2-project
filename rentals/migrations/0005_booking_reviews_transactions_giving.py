# Generated by Django 4.2.6 on 2023-11-02 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rentals', '0004_coins'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniq', models.CharField(max_length=10, unique=True)),
                ('from_time', models.DateTimeField()),
                ('to_time', models.DateTimeField()),
                ('address_at', models.TextField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username1', models.CharField(max_length=40)),
                ('username2', models.CharField(max_length=40)),
                ('desc1', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username1', models.CharField(max_length=40)),
                ('username2', models.CharField(max_length=40)),
                ('from_time', models.DateTimeField()),
                ('to_time', models.DateTimeField()),
                ('cost', models.IntegerField()),
                ('review1', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Giving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.booking')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
