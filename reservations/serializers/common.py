from rest_framework import serializers
from ..models import Reservation
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Reservation
        fields = "__all__"
        read_only_fields = ['reserved_by', 'reserved_room', 'cost']

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError({'end_date': 'End date must take place after start date'})
        return data