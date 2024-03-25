from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import *

class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("title", "author",)
    search_fields = ("title__startswith",)
    list_filter = ("title",)

class CustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("CustomerID", "CustomerName", "ContactName", "Address", "City", "PostalCode", "Country", "image_tag")
    search_fields = ("CustomerName__startswith",)
    list_filter = ("CustomerName",)

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("CategoryID", "CategoryName", "Description",)
    search_fields = ("CategoryName__startswith",)
    list_filter = ("CategoryName",)

class EmployeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("EmployeeID", "LastName", "FirstName", "BirthDate", "image_tag", "Notes",)
    search_fields = ("FirstName__startswith",)
    list_filter = ("FirstName",)

class OrderDetailAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("OrderDetailID", "OrderID", "ProductID", "Quantity")
    search_fields = ("ProductID__startswith",)
    list_filter = ("ProductID",)

class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("OrderID", "CustomerID", "EmployeeID", "OrderDate", "ShipperID",)
    search_fields = ("CustomerID__startswith",)
    list_filter = ("CustomerID",)

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("ProductID", "ProductName", "Description", "SupplierID", "CategoryID", "Unit", "Price", "image_tag")
    search_fields = ("ProductName__startswith",)
    list_filter = ("ProductName",)

class ShipperAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("ShipperID", "ShipperName", "Phone")
    search_fields = ("ShipperName__startswith",)
    list_filter = ("ShipperName",)

class SupplierAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("SupplierID", "SupplierName", "ContactName", "Address", "City", "PostalCode", "Country", "Phone",)
    search_fields = ("SupplierName__startswith",)
    list_filter = ("SupplierName",)

class ContactsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('ContactName', 'ContactEmail', 'Message')
    search_fields = ('ContactName',)

class ReviewAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("product_id", "cust_name", "cust_email", "cust_review",)
    search_fields = ("cust_name__startswith",)
    list_filter = ("cust_name",)

admin.site.site_header = "Admin Toko Buku"
admin.site.site_title = "Toko Buku"
admin.site.index_title = "Admin Malik"

admin.site.register(Book, BookAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Shipper, ShipperAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Review, ReviewAdmin)