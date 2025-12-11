from .serializers.common import BranchSerializer
from .models import Branch
from rest_framework import generics

# Create your views here.
class BranchView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
class BranchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer