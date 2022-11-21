from django.urls import path
from .views import book_list

app_name = "library"

urlpatterns = [
    path('book_list', book_list, name='book_list'),
]