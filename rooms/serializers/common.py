from rest_framework.serializers import ModelSerializer
from ..models import Room
# Create your views here.

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
