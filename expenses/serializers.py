from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username, name, email', 'password' ]


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Budget
        fields = '__all__'


class BudgetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Budget_item
        fields = '__all__'

