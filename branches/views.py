from .serializers.common import BranchSerializer 
from rooms.serializers.common import RoomSerializer
from reservations.serializers.common import ReservationSerializer
from reservations.models import Reservation
from rooms.models import Room
from .models import Branch
from rest_framework import generics
from utils.permissions import IsStaffOrReadOnly
from django.shortcuts import get_object_or_404
# Create your views here.
class BranchView(generics.ListCreateAPIView):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
class BranchDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchDetailRoomView(generics.ListCreateAPIView):
    permission_classes =[IsStaffOrReadOnly]
    serializer_class = RoomSerializer
    def get_queryset(self):
        branch_id = self.kwargs['branch_id']
        return Room.objects.filter(branchId=branch_id)
    def perform_create(self, serializer):
        branch =get_object_or_404(Branch, pk=self.kwargs['branch_id'] )
        serializer.save(branchId = branch  )
class BranchDetailRoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes =[IsStaffOrReadOnly]
    serializer_class = RoomSerializer

    def get_queryset(self):
        branch_id = self.kwargs['branch_id']
        return Room.objects.filter(branchId=branch_id)
    # def perform_update(self, serializer):
    #     room = get_object_or_404(Room, pk=self.kwargs['pk'])
    #     branch =get_object_or_404(Branch, pk=self.kwargs['branch_id'] )
    #     # serializer.save(room.branchId = branch  )
    #     print(room)
class BranchDetailRoomDetailReservationView(generics.ListAPIView):
    serializer_class=  ReservationSerializer
    def get_queryset(self):
        room_id =  self.kwargs['pk']
        return Reservation.objects.filter(reserved_room=room_id)