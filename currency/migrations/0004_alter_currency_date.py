# Generated by Django 5.0.6 on 2024-06-30 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_rename_currency_name_currency_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
