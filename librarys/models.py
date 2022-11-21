from django.db import models
from accounts.models import Customer

class Category(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.title

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name="category")
    code = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Borrow(models.Model):
    BORROW_CHOICES = (
    ("borrowed","امانت گرفته شده"),
    ("return", "بازگرداندن")
)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete= models.CASCADE)
    borrow_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=BORROW_CHOICES)

    def __str__(self) -> str:
        return self.book.name

