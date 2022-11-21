from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100, unique=True)
    national_code = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.user.username


class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100, unique=True)
    national_code = models.CharField(max_length=100, unique=True)
    salary_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username