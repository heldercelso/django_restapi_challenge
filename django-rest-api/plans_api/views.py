from rest_framework.response import Response
from rest_framework import status
 
from .models import Plans
from .serializers import PlansSerializer, PlansPostSerializer
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from .utils import post_response_schema_dict, put_response_schema_dict

@swagger_auto_schema(
    method='post',
    request_body=PlansPostSerializer,
    responses=post_response_schema_dict
)
@api_view(['GET', 'POST', 'DELETE'])
def plans_list(request):
    """
        List or delete all plans, or create a new plan.
    """
    if request.method == 'GET':
        obj = Plans.objects.all()
        serializer = PlansSerializer(obj, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PlansPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Plans.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='put',
    request_body=PlansPostSerializer,
    responses=put_response_schema_dict
)
@api_view(['GET', 'PUT', 'DELETE'])
def plans_detail(request, pk):
    """
        Retrieve, update or delete a plan.
    """
    try:
        obj = Plans.objects.get(pk=pk)
    except Plans.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlansSerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlansPostSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)