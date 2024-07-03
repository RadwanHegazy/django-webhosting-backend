from rest_framework.views import APIView
from ..serializers import HostSerializer, Host
from rest_framework import status, permissions
from rest_framework.response import Response




class host_active_view(APIView) : 
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HostSerializer

    def patch(self, request, host_id, **kwargs) : 
        user = request.user
        try : 
            host = Host.objects.get(user=user,id=host_id)
        except Host.DoesNotExist:
            return Response({
                'message' : 'host not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        host.active = True
        host.save()
        return Response(status=status.HTTP_200_OK)


class host_inactive_view(APIView) : 
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HostSerializer

    def patch(self, request, host_id, **kwargs) : 
        user = request.user
        try : 
            host = Host.objects.get(user=user,id=host_id)
        except Host.DoesNotExist:
            return Response({
                'message' : 'host not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        host.active = False
        host.save()
        return Response(status=status.HTTP_200_OK)
