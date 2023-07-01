from django.contrib import admin
from .models import Product, Review, Distillery

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'product')

@admin.register(Distillery)
class DistilleryAdmin(admin.ModelAdmin):
    pass