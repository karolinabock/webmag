# Generated by Django 3.2 on 2021-04-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appk1', '0002_auto_20210424_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='realase_date',
            field=models.DateField(),
        ),
    ]
