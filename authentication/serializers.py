from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}



    def validate(self, attrs):
        email =attrs.get('email','')
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'email is already taken'}) 
        return super().validate(attrs)
    

    
    def create(self, validated_data):
        request = self.context.get('request')
        role = validated_data.get('role', 'user')

        validated_data['username'] = validated_data['email']
        # If request exists and the role is not 'user', check if user is admin
        if request and role in ['admin', 'pharmacist','procurement','director']:
            if not request.user or not request.user.is_staff:
                raise serializers.ValidationError("Only admin can assign this role.")
        elif role not in ['user','supplier','delivery']:  # in case someone tries to bypass with a wrong role
            raise serializers.ValidationError("Invalid role assignment.")

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=role 
        )
        return user


        