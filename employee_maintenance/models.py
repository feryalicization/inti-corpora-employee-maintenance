from django.db import models
from djmoney.models.fields import MoneyField



class Employee(models.Model):
    name = models.CharField(max_length=255)
    nik = models.CharField(max_length=255)
    salary = MoneyField(max_digits=10, decimal_places=2, default_currency='IDR')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    