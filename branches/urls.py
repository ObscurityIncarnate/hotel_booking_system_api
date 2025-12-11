
from django.urls import path, include
from .views import BranchView, BranchDetailView
urlpatterns = [
    path('', BranchView.as_view()),
    path('<int:branchId>/', BranchDetailView.as_view())
]
