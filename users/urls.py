from  django.urls import path
from .views import SignUpView
urlpatterns = [
    # path('sign-in/', )
    path('sign-up/',SignUpView.as_view())
]