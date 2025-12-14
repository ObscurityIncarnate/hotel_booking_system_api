from  django.urls import path
from .views import userDetailReservationDetailView, userDetailReservationView,userDetail
urlpatterns = [
    # path('sign-in/', )
    path('<int:pk>/', userDetail.as_view()),
    path('<int:user_id>/reservations/', userDetailReservationView.as_view()),
    path('<int:user_id>/reservations/<int:pk>/', userDetailReservationDetailView.as_view())
]