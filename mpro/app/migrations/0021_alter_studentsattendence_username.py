# Generated by Django 3.2.4 on 2021-07-04 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_studentsattendence_attndence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsattendence',
            name='username',
            field=models.CharField(default='ff', max_length=1000),
        ),
    ]
