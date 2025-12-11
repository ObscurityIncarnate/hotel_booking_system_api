
from django.urls import path, include
from .views import reservationView, reservationDetailView
urlpatterns = [
    path('', reservationView.as_view()),
    path('<int:pk>/', reservationDetailView.as_view())
]
