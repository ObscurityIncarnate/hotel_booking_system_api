from rest_framework import serializers
from ..models import Reservation
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Reservation
        fields = "__all__"
        read_only_fields = ['reserved_by', 'reserved_room', 'cost']

    def validate(self, data):
        start_date = data['start_date'] 
        end_date = data['end_date']

        if end_date<start_date:
            raise serializers.ValidationError({'end_date': 'End date must take place after start date'})
        urlparams = self.context.get('view')
        room_reservations = Reservation.objects.filter(reserved_room =urlparams.kwargs['room_id'])
        # check if a reservation overlaps another 
        for res in room_reservations:
            if start_date < res.end_date and res.start_date < end_date :
                raise serializers.ValidationError({'detail': 'A reservation for this room already exists within the duration you have specified.'})
      
        return data
    