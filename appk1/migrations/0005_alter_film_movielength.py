# Generated by Django 3.2 on 2021-04-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appk1', '0004_auto_20210424_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='movielength',
            field=models.IntegerField(default=1),
        ),
    ]
