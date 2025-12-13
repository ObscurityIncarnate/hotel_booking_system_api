from .serializers.common import BranchSerializer
from .models import Branch
from rest_framework import generics
from utils.permissions import IsOwner, IsStaffOrReadOnly
# Create your views here.
class BranchView(generics.ListCreateAPIView):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
class BranchDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchDetailRoomView():
    pass
class BranchDetailRoomDetailView():
    pass