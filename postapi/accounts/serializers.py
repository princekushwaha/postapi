from rest_framework import serializers
from rest_auth.serializers import LoginSerializer
from rest_auth.registration.serializers import RegisterSerializer


class LoginSerializer(LoginSerializer):
    email = serializers.EmailField(required=False, read_only=True)
    username = serializers.CharField(required=True)



class RegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, allow_blank=False)
    last_name = serializers.CharField(required=False)


    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name',''),
            'last_name':self.validated_data.get('last_name',''),
        }