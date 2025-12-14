from rest_framework import generics
from .serializers.common import RoomSerializer
from .models import Room
from utils.permissions import IsStaff, IsStaffOrReadOnly
class RoomView(generics.ListAPIView):
    permission_classes = [IsStaff]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
# class RoomDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsStaff]
#     queryset =  Room.objects.all()
#     serializer_class =RoomSerializer
    