from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import *
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):

        data=request.data
        print('registering')

        name = data['name']
        username = data['username']
        password = data['password']
        email = data['email']
        re_password = data['re_password']

        if password == re_password:
            if len(password) >=8:
                if not User.objects.filter(username=username).exists() and not User.objects.filter(email=email):
                    User.objects.create_user(
                        username = username,
                        password = password,
                        email = email
                    )

                    user = User.objects.get(username = username)
                    client =Client.objects.create(
                        name = name,
                        user = user,
                        email = email,

                    )
                    client.save()
                    if User.objects.filter(username=username).exists():
                        return Response(
                            {'success':'Account created successfully'},
                            status = status.HTTP_201_CREATED
                        )
                    else:
                        return Response(
                            {'error': 'Something went wrong when trying to create'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response (
                        {'error': 'username or Email already exist'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )

            else:
                return Response(
                    {'error': 'passwords must be at least 8 char'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        else:
            return Response(
                {'error': 'passwords do not match'},
                status=status.HTTP_400_BAD_REQUEST
            )


class loaduserview(APIView):
    def get(self, request, format=None):
        try:
            user=request.user
            client = Client.objects.get(user=user)
            user = UserSerializer(client)
            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'something went wrong when trying to load user'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )




@api_view(['GET'])
def apilist(request):
    api_urls = {
        'login' : '/api/token/',
        'refresh token': 'api/token/refresh/',
        'register' : '/api/account/register',
        'all budgets' : '/api/account/allBudgets',
        'all budget items' : '/api/account/allBudgetItems/slug/',
        'budget delete': "/api/account/BudgetDelete/<str:slug>/",
        'budgetItem delete': "/api/account/BudgetItemsDelete/<str:slug>/"
    }
    message = 'pending'
    return Response(api_urls)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allBudget(request):
    user = request.user

    budget = Budget.objects.filter(user=user)
    print(budget)
    budget = BudgetSerializer(budget, many=True)
    return Response(budget.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allBudgetItem(request, slug):
    try:
        user = request.user
        budgetItem = Budget_item.objects.filter(budget_id = slug, user=user)
        budgetItem = BudgetItemSerializer(budgetItem, many=True)
        return Response(budgetItem.data)

    except:

        return Response(
            {'error': 'requested budget id is invalid or access is denied'},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def budget_create(request):
    serializer = BudgetSerializer(data=request.data)
    user = request.user
    client = Client.objects.get(user=user)
    if serializer.is_valid():
        serializer.save(user=client)
        status="success"
    else:
        print(serializer.errors)
        print('request not valid')
        status = 'fail'
    return Response(status)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def budget_delete(request, slug):
    try:
        user = request.user
        budget = Budget.objects.get(id=slug)
        if budget.user == user:
            budget.delete()
            return Response(
                {'success':'Budget deleted'},
            )
        else:
            return Response(
                {'error':'Budget does not belong to user'},
            )
    except:
        return Response(
            {'error':'Something went wrong'},

        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def budgetItem_create(request):
    user = request.user
    serializer = BudgetItemSerializer(data=request.data)
    client = Client.objects.get(user=user)
    if serializer.is_valid():
        serializer.save(user = client)
        status ='success'
    else:
        print(serializer.errors)
        print('request not valid')
        status = 'fail'
    return Response(status)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def budgetitem_delete(request, slug):
    try:
        user = request.user
        budget = Budget_item.objects.get(id=slug)
        if budget.user == user:
            budget.delete()
            return Response(
                {'success':'BudgetItem deleted'},
            )
        else:
            return Response(
                {'error':'BudgetItem does not belong to user'},
            )
    except:
        return Response(
            {'error':'Something went wrong'},

        )
