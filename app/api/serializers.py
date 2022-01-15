from rest_framework import serializers
from app.models import User, Blog, Comment
from rest_framework.exceptions import ValidationError

#Mapping Comment Model to a Serializer
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        exclude = ('like','dislike','id','blog')

#Mapping Blog Model to a Serializer
class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        exclude = ('author','id')
        
#Mapping User Model to a Serializer
class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=30,write_only=True,style={'input_type':'password'})
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password','password2']
        extra_kwargs = {
            'password' : {
                'write_only': True
            }
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        print('pasword is ',password)
        print("username is ",self._validated_data['username'])
        if password != password2:
            raise ValidationError({'Error':'Both Passwords are not same'})
    
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise ValidationError({'Error':'Email is already registered'})
        
        if User.objects.filter(username=self.validated_data['username']).exists():
            raise ValidationError({'Error':'Username is already registered'})
        
        account = User(first_name=self.validated_data['first_name'],last_name=self.validated_data['last_name'],
                         email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account
