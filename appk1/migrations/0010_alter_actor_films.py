# Generated by Django 3.2 on 2021-04-25 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appk1', '0009_actor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='films',
            field=models.ManyToManyField(related_name='actors', to='appk1.Film'),
        ),
    ]
