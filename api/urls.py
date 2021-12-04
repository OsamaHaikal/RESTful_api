from django.urls import path 
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.GetRoutesView.as_view()),
    path('register/',views.RegisterView.as_view(),name='auth_register'),
    path('users/',views.UserView.as_view(),name="users_api"),
    path('books/', views.GetBooksView.as_view(),name="books_api"),
    path('books/<str:pk>/', views.GetBookView.as_view(),name="book_api"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
