from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import UserSerializer
from books.models import Book
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import BookSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
import jwt, datetime

class GetRoutesView(APIView):
    def get(self,request):
        routes = [
            {
                "method":"GET",
                "endpoint":"/api/books/",
                "permissions":"ReadOnly",
            },
            {
                "method":"GET",
                "endpoint":"/api/book/<str:id>",
                "permissions":"ReadOnly"
            },
            {
                "method":"GET",
                "endpoint":"/api/users/",
                "permissions":"IsAdminUser",
            },
            {
                "method":"POST",
                "endpoint":"/api/token/",
            },
            {
                "method":"POST",
                "endpoint":"/api/token/refresh",
            },
            {
                "method":"POST",
                "endpoint":"/api/register/",
                "fields":[
                    "email",
                    "uersname", 
                    "password",
                ]
            }
        ]
        
        return Response(routes)
    
    
class RegisterView(APIView):
    
    def post(self,request):

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception = True )
        serializer.save()
        
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    

class UserView(APIView):
    
    def get(self,request):
        user = User.objects.all()

        serializer = UserSerializer(user,many=True)
        
        return Response(serializer.data)
    
class GetBooksView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
  

class GetBookView(APIView):
    def get(self,request,pk):
        
        book = Book.objects.filter(id=pk)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
    