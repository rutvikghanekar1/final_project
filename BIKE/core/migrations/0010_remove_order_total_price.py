# Generated by Django 5.0.2 on 2024-03-13 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_bike_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
    ]
