from  django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import SignUpView, MyTokenObtainPairView
urlpatterns = [
    # path('sign-in/', )
    path('sign-up/',SignUpView.as_view()),
    path('sign-in/', MyTokenObtainPairView.as_view())
]