from .serializers.common import ReservationSerializer
from rest_framework import generics
from .models import Reservation
from utils.permissions import IsStaff
# Create your views here.


class reservationView (generics.ListCreateAPIView):
    permission_classes = [IsStaff]
    queryset =Reservation.objects.all()
    serializer_class = ReservationSerializer

class reservationDetailView(generics.DestroyAPIView):
    permission_classes = [IsStaff]
    queryset =Reservation.objects.all()
    serializer_class = ReservationSerializer
