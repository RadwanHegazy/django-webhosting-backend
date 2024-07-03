from rest_framework.views import APIView
from ..serializers import HostSerializer, Host
from rest_framework import status, permissions
from rest_framework.response import Response
from django.shortcuts import HttpResponse

class get_host_list(APIView) : 
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HostSerializer

    def get(self, request, **kwargs) : 
        user = request.user
        query = Host.objects.filter(user=user)
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class get_host_view(APIView) : 
    serializer_class = HostSerializer

    def get(self, request, host_name,file_name, **kwargs) : 
        try : 
            host = Host.objects.get(name=host_name, active=True)
        except Host.DoesNotExist:
            return Response({
                'message' : 'host not found'
            }, status=status.HTTP_404_NOT_FOUND)
        file = open(f"media/hosting/{host.user}/{host.name}/{file_name}",'r')
        return HttpResponse(file.read())