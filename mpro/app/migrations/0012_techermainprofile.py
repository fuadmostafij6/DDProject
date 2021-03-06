# Generated by Django 3.2.4 on 2021-06-26 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_teacherprofile_dept_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TecherMainProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('qualifications', models.CharField(blank=True, max_length=500, null=True)),
                ('reaserce_detail', models.CharField(blank=True, max_length=1000, null=True)),
                ('username', models.OneToOneField(default='Teacher', on_delete=django.db.models.deletion.CASCADE, to='app.teacherprofile')),
            ],
        ),
    ]
