# Generated by Django 4.2.6 on 2023-11-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0010_mutualinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='review1',
            new_name='rating',
        ),
        migrations.AddField(
            model_name='cycleinfo',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
