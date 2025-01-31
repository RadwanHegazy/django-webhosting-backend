from rest_framework.views import APIView
from ..serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status

class register_view(APIView) : 
    serializer_class = RegisterSerializer

    def post(self, request, **kwargs) :
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.tokens, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)