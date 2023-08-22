from rest_framework.response import Response
from rest_framework import status

from .models import Client
from .serializers import ClientSerializer, ClientPostSerializer
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from .utils import post_response_schema_dict, put_response_schema_dict


@swagger_auto_schema(
    method='post',
    request_body=ClientPostSerializer,
    responses=post_response_schema_dict
)
@api_view(['GET', 'POST', 'DELETE'])
def client_list(request):
    """
        List or delete all clients, or create a new client.
    """
    if request.method == 'GET':
        obj = Client.objects.all()
        serializer = ClientSerializer(obj, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Client.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='put',
    request_body=ClientPostSerializer,
    responses=put_response_schema_dict
)
@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    """
        Retrieve, update or delete a client.
    """
    try:
        obj = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClientPostSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)