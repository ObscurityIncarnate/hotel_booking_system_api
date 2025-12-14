from rest_framework.serializers import ModelSerializer
from ..models import Reservation
class ReservationSerializer(ModelSerializer):
    class Meta:
        model =Reservation
        fields = "__all__"
        read_only_fields = ['reserved_by', 'reserved_room']