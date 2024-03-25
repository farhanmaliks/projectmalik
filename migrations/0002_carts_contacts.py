# Generated by Django 5.0.3 on 2024-03-22 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokobuku', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Coupon', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ContactName', models.CharField(max_length=200)),
                ('ContactEmail', models.EmailField(max_length=200)),
                ('Message', models.TextField()),
            ],
        ),
    ]