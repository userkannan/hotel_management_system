# Generated by Django 5.0.1 on 2024-05-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0007_add_salarys'),
    ]

    operations = [
        migrations.AddField(
            model_name='online_booking',
            name='Booking_ID',
            field=models.CharField(blank=True, max_length=5, unique=True),
        ),
    ]
