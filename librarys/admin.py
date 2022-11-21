from django.contrib import admin
from .models import Book, Borrow, Category
# Register your models here.
class Bookadmin(admin.ModelAdmin):
    pass

admin.site.register(Book, Bookadmin)
admin.site.register(Borrow)
admin.site.register(Category)