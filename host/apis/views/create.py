from rest_framework.views import APIView
from ..serializers import HostSerializer
from rest_framework import status, permissions
from rest_framework.response import Response


class create_host_view(APIView) : 
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HostSerializer

    def post(self, request, **kwargs) : 
        user = request.user
        serializer = self.serializer_class(data=request.data, context={'user':user})
        if serializer.is_valid() : 
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)