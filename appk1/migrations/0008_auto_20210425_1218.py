# Generated by Django 3.2 on 2021-04-25 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appk1', '0007_prize'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prize',
            old_name='nazwa',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='prize',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prize', to='appk1.film'),
        ),
    ]
