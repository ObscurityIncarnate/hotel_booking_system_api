from .models import User
from .serializers.common import UserSerializer
from rest_framework import generics
from .serializers.tokens import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from utils.permissions import IsStaff,IsOwnerOrStaff
from reservations.models import Reservation
from reservations.serializers.common import ReservationSerializer
from django.shortcuts import get_object_or_404
# Create your views here.
class SignUpView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class userDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= User
    serializer_class = UserSerializer

class userDetailReservationView(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrStaff]
    serializer_class = ReservationSerializer
    def get_queryset(self):
        user = self.kwargs['user_id']
        return Reservation.objects.filter(reserved_by = user)
    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs['user_id'])
        serializer.save(reserved_by = user)

class userDetailReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrStaff]
    serializer_class = ReservationSerializer

    def get_queryset(self):
        user = self.kwargs['user_id']
        return Reservation.objects.filter(reserved_by = user)

