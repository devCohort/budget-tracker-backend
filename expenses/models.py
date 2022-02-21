from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


BUDGET_TYPE_CHOICES = (
    ('daily', 'daily' ),
    ('weekly', 'weekly'),
    ('monthly', 'monthly'),
    ('yearly', 'yearly')
)
BUDGET_CURRENCY = (
    ('dollar', 'dollar' ),
    ('yuan', 'yuan'),
    ('naira', 'naira'),
    ('euro', 'euro')
)

class Budget(models.Model):
    user = models.ForeignKey(Client, related_name='budgets', on_delete=models.CASCADE)
    budget_name = models.CharField(max_length=15)
    amount = models.IntegerField()
    budget_description = models.CharField(max_length=200)
    budget_type = models.CharField(max_length=15, choices= BUDGET_TYPE_CHOICES, default='daily')
    currency = models.CharField(max_length=15, choices= BUDGET_CURRENCY, default='naira')


class Budget_item(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=15)
    item_amount = models.IntegerField()
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, default=1)

