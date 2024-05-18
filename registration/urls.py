from django.urls import path
from .views import *

urlpatterns = [
    path('register/', registration_APIView.as_view(), name='register'),
    path('login/', login_user_APIView.as_view(), name="login"),
]

