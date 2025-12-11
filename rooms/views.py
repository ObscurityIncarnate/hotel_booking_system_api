from rest_framework import generics
from .serializers.common import RoomSerializer
from .models import Room

class RoomView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
class RoomDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Room.objects.all()
    serializer_class =RoomSerializer
    