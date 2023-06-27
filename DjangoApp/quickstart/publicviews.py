from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics


# class Register(APIView):
#     def post(self, request):
#         return Response({"Message":"HELLO PO"})
    




  # Class based view to Get User Details using Token Authentication


#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer