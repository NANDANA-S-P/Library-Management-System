# Generated by Django 4.0.4 on 2022-04-19 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0006_alter_cocurricular_and_extra_curricular_activities_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocurricular_and_extra_curricular_activities',
            name='Sponsoredorcolloboration',
            field=models.CharField(choices=[('Industry', 'Industry'), ('Foreign University', 'Foreign University'), ('Internal', 'Internal '), ('External', 'External'), ('NPTEL', 'NPTEL'), ('Coursera', 'Coursera'), ('EDX', 'EDX'), ('Udemy', 'Udemy'), ('Others', 'Others')], max_length=30),
        ),
    ]