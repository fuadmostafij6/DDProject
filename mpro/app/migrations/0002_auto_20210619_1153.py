# Generated by Django 3.2.4 on 2021-06-19 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminprofile',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='adminprofile',
            name='personal_details',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
