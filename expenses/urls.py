from django.urls import path

from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('allBudgets/', allBudget, name = 'budget'),
    path('allBudgetItems/<str:slug>/', allBudgetItem, name = 'budgetItems'),
    path('budgetItemCreate/', budgetItem_create, name = 'budgetItemsCreate'),
    path('budgetCreate/', budget_create, name = 'budgetCreate'),
    path('BudgetItemsDelete/<str:slug>/', budgetitem_delete, name = 'budgetItemsDelete'),
    path('BudgetDelete/<str:slug>/', budget_delete, name = 'budgetDelete'),
    path('apilist/', apilist, name = 'apilist'),
    path('user/', loaduserview.as_view(), name='user'),

    ]