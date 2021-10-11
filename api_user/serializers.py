from rest_framework import serializers                       
from django.contrib.auth import authenticate                 # use to declare auth model type
from rest_framework import status                            # uses to get status response message
#from.models import Registration                              # calls declared class name from the models            
from rest_framework.authtoken.models import Token            # uses while generate token
from api_admin.models import *
from webroot.utilities import*


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(max_length = 255)

    def validate(self,data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            user=Registration.objects.filter(email=email).first()
            
        if (user.check_password(password)==True):
            token,created = Token.objects.get_or_create(user = user)
            data['token'] = token.key
        
        return data