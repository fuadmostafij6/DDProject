# Generated by Django 3.2.4 on 2021-07-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_studentsattendence_studentsmainprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsattendence',
            name='day',
            field=models.IntegerField(),
        ),
    ]
