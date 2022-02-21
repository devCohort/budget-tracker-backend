from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:

        model=Budget
        fields = ['budget_name', 'budget_description', 'amount', 'budget_type', 'currency']


class UserSerializer(serializers.ModelSerializer):
    budgets = BudgetSerializer(many=True, read_only=True)
    class Meta:
        model=Client
        fields = ['user', 'email', 'name', 'budgets']




class BudgetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Budget_item
        fields = ['item_name', 'item_amount', 'budget']

