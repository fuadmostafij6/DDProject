# Generated by Django 3.2.4 on 2021-07-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_studentsattendence_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsattendence',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
