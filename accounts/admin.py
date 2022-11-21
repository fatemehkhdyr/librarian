from django.contrib import admin
from .models import Customer, Librarian
# Register your models here.
class Customeradmin(admin.ModelAdmin):
    pass

class Librarianadmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, Customeradmin)
admin.site.register(Librarian, Librarianadmin)