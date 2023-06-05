# Generated by Django 4.1.7 on 2023-06-03 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(max_length=255)),
                ('state', models.CharField(choices=[('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar')], max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField(choices=[(2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], verbose_name='year')),
                ('condition', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('car_photo', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('car_photo_1', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('car_photo_2', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('car_photo_3', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('car_photo_4', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('features', models.CharField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags')], max_length=100)),
                ('body_style', models.CharField(max_length=100)),
                ('engine', models.CharField(max_length=100)),
                ('transmission', models.CharField(max_length=100)),
                ('interior', models.CharField(max_length=100)),
                ('miles', models.IntegerField()),
                ('doors', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=100)),
                ('passengers', models.IntegerField()),
                ('vin_no', models.CharField(max_length=100)),
                ('milage', models.IntegerField()),
                ('fuel_types', models.CharField(max_length=100)),
                ('no_of_owners', models.CharField(max_length=100)),
                ('is_featured', models.BooleanField(max_length=100)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]