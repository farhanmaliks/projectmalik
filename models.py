# import the standard Django Model
# from built-in library
from django.db import models 
from django.utils.html import mark_safe


# declare a new model with a name "GeeksModel"
class Book(models.Model):

    # fields of the model
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return f"{self.title} {self.author}"

class Customer(models.Model):

    # fields of the model
    CustomerID = models.IntegerField()
    CustomerName = models.CharField(max_length = 200, default="")
    ContactName = models.CharField(max_length = 200)
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    PostalCode = models.IntegerField(default=0)
    Country = models.CharField(max_length=200)
    Upload = models.ImageField(upload_to='images', default='')

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return f"{self.CustomerID} {self.CustomerName} {self.ContactName} {self.Address} {self.City} {self.PostalCode} {self.Country} {self.Upload}"

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.Upload.url))
    image_tag.short_description = 'Image'

class Category(models.Model):

    # fields of the model
    CategoryID = models.IntegerField(default=0)
    CategoryName = models.CharField(max_length = 200)
    Description = models.CharField(max_length = 200)


    # renames the instances of the model
    # with their title name
    def __str__(self):
        return f"{self.CategoryID} {self.CategoryName} {self.Description}"

class Employee(models.Model):

    # fields of the model
    EmployeeID = models.IntegerField(default=0)
    LastName = models.CharField(max_length = 200)
    FirstName = models.CharField(max_length = 200)
    BirthDate = models.DateField(blank=True, null=True, default='')
    Photo = models.ImageField(default="")
    Notes = models.TextField(max_length=200)


    # renames the instances of the model
    # with their title name
    def __str__(self):
        return f"{self.EmployeeID} {self.LastName} {self.FirstName} {self.BirthDate} {self.Photo} {self.Notes}"

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.Photo.url))
    image_tag.short_description = 'Image'

class OrderDetail(models.Model):

    # fields of the model
    OrderDetailID = models.IntegerField()
    OrderID = models.IntegerField()
    ProductID = models.IntegerField()
    Quantity = models.IntegerField(default=0)


    # renames the instances of the model
    # with their title name
    def __str__(self):
        return f"{self.OrderDetailID} {self.OrderID} {self.ProductID} {Quantity}"

class Order(models.Model):

    # fields of the model
    OrderID = models.IntegerField()
    CustomerID = models.CharField(max_length = 200)
    EmployeeID = models.CharField(max_length=200)
    OrderDate = models.DateField(blank=True, null=True, default='')
    ShipperID = models.IntegerField()


    # renames the instances of the model
    # with their title name
    def __str__(self):
        return f"{self.OrderID} {self.CustomerID} {self.EmployeeID} {self.OrderDate} {self.ShipperID}"

class Product(models.Model):

    # fields of the model
    ProductID = models.IntegerField()
    ProductName = models.CharField(max_length = 200)
    Description = models.TextField(max_length = 500)
    SupplierID = models.IntegerField()
    CategoryID = models.IntegerField()
    Unit = models.CharField(max_length=200)
    Price = models.IntegerField(default=0)
    Image = models.ImageField(upload_to='images', default='')

    def __str__(self):
        return f"{self.ProductID} {self.ProductName} {self.Description} {self.SupplierID} {self.CategoryID} {self.Unit} {self.Price} {self.Image}"

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.Image.url))
    image_tag.short_description = 'Image'

class Shipper(models.Model):

    # fields of the model
    ShipperID = models.IntegerField()
    ShipperName = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200)


    # renames the instances of the model
    # with their title name
    def __str__(self):
        return f"{self.Shipperid} {self.Shippername} {Phone}"

class Supplier(models.Model):

    # fields of the model
    SupplierID = models.IntegerField()
    SupplierName = models.CharField(max_length = 200)
    ContactName = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    PostalCode = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200)


    # renames the instances of the model
    # with their title name
    def __str__(self):
        return f"{self.SupplierID} {self.SupplierName} {self.ContactName} {self.Address} {self.City} {self.PostalCode} {self.Country} {self.Phone}"
    
class Contacts(models.Model):
    ContactName = models.CharField(max_length=200)
    ContactEmail = models.EmailField(max_length=200)
    Message = models.TextField()

class Carts (models.Model):
    Coupon = models.CharField(max_length=20)

class Review(models.Model):
    product_id = models.IntegerField()
    cust_name = models.CharField(max_length=200)
    cust_email = models.EmailField(max_length=200)
    cust_review = models.TextField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)