from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
  class Meta(BaseUserCreateSerializer.Meta):
    fields = ['id','username','email','password','user_type','first_name','last_name', 'address','phone_number']

class UserSerializer(BaseUserSerializer):
  class Meta(BaseUserSerializer.Meta):
    ref_name = "CustomUser"
    fields = ['id','username','email','user_type','first_name','last_name', 'address','phone_number']
    