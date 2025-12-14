from .models import User
from .serializers.common import UserSerializer
from rest_framework import generics
from .serializers.tokens import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from utils.permissions import IsStaff,IsOwnerOrStaff
from reservations.models import Reservation
from reservations.serializers.common import ReservationSerializer
from django.shortcuts import get_object_or_404
from rooms.models import Room
from datetime import datetime
# Create your views here.
class SignUpView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class userDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= User
    serializer_class = UserSerializer

class userDetailReservationView(generics.ListAPIView):
    permission_classes = [IsOwnerOrStaff]
    serializer_class = ReservationSerializer
    def get_queryset(self):
        user = self.kwargs['user_id']
        return Reservation.objects.filter(reserved_by = user)

class userDetailReservationCreateView(generics.CreateAPIView):
    permission_classes = [IsOwnerOrStaff]
    serializer_class = ReservationSerializer     
    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs['user_id'])
        #we need to know what room to match it to and then also have the user and then also calculating the price
        end_date = datetime.strptime(  self.request.data.get('end_date'), '%Y-%m-%d').date()
        start_date = datetime.strptime(  self.request.data.get('start_date'), '%Y-%m-%d').date()
        room = get_object_or_404(Room, pk=self.kwargs['room_id'])
        total_cost = end_date - start_date
        serializer.save(reserved_by = user, reserved_room = room, cost = total_cost.days * room.price_per_night )  

class userDetailReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrStaff]
    serializer_class = ReservationSerializer

    def get_queryset(self):
        user = self.kwargs['user_id']
        return Reservation.objects.filter(reserved_by = user)
    #when updating the reservation you can only update start date and end date, and indirectly the price should be recalculated, anything else will require a delete of the reservation and just recreated
    def perform_update(self, serializer):
        end_date = datetime.strptime(  self.request.data.get('end_date'), '%Y-%m-%d').date()
        start_date = datetime.strptime(  self.request.data.get('start_date'), '%Y-%m-%d').date()
        reservation = Reservation.objects.get(pk=self.kwargs['pk'])
        room = get_object_or_404(Room, pk=reservation.reserved_room.id)
        total_cost = end_date - start_date
        serializer.save(cost = total_cost.days * room.price_per_night )         

