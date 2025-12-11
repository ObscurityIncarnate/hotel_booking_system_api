from .serializers.common import ReservationSerializer
from rest_framework import generics
from .models import Reservation
# Create your views here.


class reservationView (generics.ListCreateAPIView):
    queryset =Reservation.objects.all()
    serializer_class = ReservationSerializer

class reservationDetailView(generics.DestroyAPIView):
    queryset =Reservation.objects.all()
    serializer_class = ReservationSerializer
