# Generated by Django 5.0.3 on 2024-03-22 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryID', models.IntegerField(default=0)),
                ('CategoryName', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.IntegerField()),
                ('CustomerName', models.CharField(default='', max_length=200)),
                ('ContactName', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
                ('PostalCode', models.IntegerField(default=0)),
                ('Country', models.CharField(max_length=200)),
                ('Upload', models.ImageField(default='', upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeID', models.IntegerField(default=0)),
                ('LastName', models.CharField(max_length=200)),
                ('FirstName', models.CharField(max_length=200)),
                ('BirthDate', models.DateField(blank=True, default='', null=True)),
                ('Photo', models.ImageField(default='', upload_to='')),
                ('Notes', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderID', models.IntegerField()),
                ('CustomerID', models.CharField(max_length=200)),
                ('EmployeeID', models.CharField(max_length=200)),
                ('OrderDate', models.DateField(blank=True, default='', null=True)),
                ('ShipperID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderDetailID', models.IntegerField()),
                ('OrderID', models.IntegerField()),
                ('ProductID', models.IntegerField()),
                ('Quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductID', models.IntegerField()),
                ('ProductName', models.CharField(max_length=200)),
                ('Description', models.TextField(max_length=500)),
                ('SupplierID', models.IntegerField()),
                ('CategoryID', models.IntegerField()),
                ('Unit', models.CharField(max_length=200)),
                ('Price', models.IntegerField(default=0)),
                ('Image', models.ImageField(default='', upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShipperID', models.IntegerField()),
                ('ShipperName', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SupplierID', models.IntegerField()),
                ('SupplierName', models.CharField(max_length=200)),
                ('ContactName', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
                ('PostalCode', models.CharField(max_length=200)),
                ('Country', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=200)),
            ],
        ),
    ]
