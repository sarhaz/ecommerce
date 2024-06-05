from django.contrib import admin
from .models import Category, Product, Logos, Contact, Cart
from import_export.admin import ImportExportModelAdmin


@admin.register(Cart)
class CartAdmin(ImportExportModelAdmin):
    list_display = ('id',)
    search_fields = ('id', 'products__name')
    ordering = ('id', )


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('id', 'name', )
    ordering = ('id', )


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'price', 'image')
    search_fields = ('id', 'name', 'price', 'image')
    ordering = ('id', )


@admin.register(Logos)
class LogosAdmin(ImportExportModelAdmin):
    list_display = ('id', 'image')
    search_fields = ('id', 'image')
    ordering = ('id', )


@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', )
    search_fields = ('id', 'name', 'email', )
    ordering = ('id', )
