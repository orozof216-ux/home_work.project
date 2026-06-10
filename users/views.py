import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer
from .models import ConfirmationCode


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        code = str(random.randint(100000, 999999))

        ConfirmationCode.objects.create(
            user=user,
            code=code
        )

        return Response(
            {"message": "User created. Check confirmation code.", "code": code},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors)


@api_view(['POST'])
def confirm_user(request):
    username = request.data.get('username')
    code = request.data.get('code')

    try:
        user = User.objects.get(username=username)
        confirm = ConfirmationCode.objects.get(user=user)

        if confirm.code == code:
            user.is_active = True
            user.save()
            return Response({"message": "User confirmed"})

        return Response({"message": "Wrong code"})

    except:
        return Response({"message": "User not found"})


@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        if user.is_active:
            return Response({"message": "Login success"})
        return Response({"message": "User not confirmed"})

    return Response({"message": "Invalid credentials"})