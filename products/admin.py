from django.contrib import admin

# Register your models here.
from .models import Product #relative import-same directory

admin.site.register(Product)