# Generated by Django 4.0.1 on 2022-01-31 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookid',
            field=models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Book id'),
        ),
    ]
