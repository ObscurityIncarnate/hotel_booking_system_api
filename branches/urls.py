
from django.urls import path, include
from .views import BranchView, BranchDetailView, BranchDetailRoomView,BranchDetailRoomDetailView
urlpatterns = [
    path('', BranchView.as_view()),
    path('<int:pk>/', BranchDetailView.as_view()),
    path('<int:branch_id>/room/', BranchDetailRoomView.as_view()),
    path('<int:branch_id>/room/<int:pk>',BranchDetailRoomDetailView.as_view())
]
