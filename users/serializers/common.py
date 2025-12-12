from rest_framework import serializers
from ..models import User
from  django.contrib.auth import password_validation, hashers
import phonenumbers
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','email', 'phone_number', 'is_staff', 'password', 'confirm_password']

    def validate(self, data):
        print(data)        
        password = data['password']
        confirm_password = data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({'confirm_password': 'Passwords do not match.'})
        password_validation.validate_password(password)

        self.validate_phone_number(data['phone_number'])
        data['password'] = hashers.make_password(password=password)
        return data
    

    def validate_phone_number(self,phone_number):
        try:
            x = phonenumbers.parse(phone_number, None)
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError({'phone_number': 'Invalid phone number format'})
        if not phonenumbers.is_valid_number(x):
             raise serializers.ValidationError({'phone_number': 'Invalid phone number'})