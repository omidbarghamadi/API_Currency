# Generated by Django 5.0.6 on 2024-06-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]