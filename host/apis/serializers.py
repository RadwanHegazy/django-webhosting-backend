from rest_framework import serializers
from ..models import Host

class HostSerializer (serializers.ModelSerializer) : 
    file = serializers.FileField(write_only=True)
    active = serializers.BooleanField(read_only=True)
    class Meta:
        model = Host
        fields = ['id','name','file','active']

    
    def validate(self, attrs):
        attrs['user'] = self.context.get('user')
        return attrs
    