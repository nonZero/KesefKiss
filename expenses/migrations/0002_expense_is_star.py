# Generated by Django 3.0.5 on 2020-06-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='is_star',
            field=models.BooleanField(default=False),
        ),
    ]
