from django.urls import path, include
from .views import RoomDetailsView,RoomView

urlpatterns = [
    path("", RoomView.as_view()),
    path("<:pk>/", RoomDetailsView.as_view())
]

