# Generated by Django 5.2.3 on 2025-06-23 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('pickup_location', models.CharField(max_length=100)),
                ('drop_location', models.CharField(max_length=100)),
                ('quantity', models.FloatField()),
                ('loading_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unloading_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('other_charge', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remarks', models.TextField(blank=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.company')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.goods')),
            ],
        ),
    ]
