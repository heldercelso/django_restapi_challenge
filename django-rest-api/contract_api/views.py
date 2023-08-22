from rest_framework.response import Response
from rest_framework import status
 
from .models import Contract, Deposit, Withdraw
from .serializers import ContractSerializer, DepositSerializer, WithdrawSerializer
from .serializers import ContractPostSerializer, DepositPostSerializer, WithdrawPostSerializer
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from .utils import post_response_schema_dict, put_response_schema_dict

################################################## CONTRACTS ########################################################

@swagger_auto_schema(
    method='post',
    request_body=ContractPostSerializer,
    responses=post_response_schema_dict
)
@api_view(['GET', 'POST', 'DELETE'])
def contract_list(request):
    """
        List or delete all contracts, or create a new contract.
    """
    if request.method == 'GET':
        obj = Contract.objects.all()
        serializer = ContractSerializer(obj, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContractPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Contract.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='put',
    request_body=ContractPostSerializer,
    responses=put_response_schema_dict
)
@api_view(['GET', 'PUT', 'DELETE'])
def contract_detail(request, pk):
    """
        Retrieve, update or delete a contract.
    """
    try:
        obj = Contract.objects.get(pk=pk)
    except Contract.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContractSerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContractPostSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


################################################## DEPOSITS ############################################################

@swagger_auto_schema(
    method='post',
    request_body=DepositPostSerializer,
    responses=post_response_schema_dict
)
@api_view(['GET', 'POST', 'DELETE'])
def deposit_list(request):
    """
        List or delete all deposits, or create a new deposit.
    """
    if request.method == 'GET':
        obj = Deposit.objects.all()
        serializer = DepositSerializer(obj, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepositPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Deposit.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='put',
    request_body=DepositPostSerializer,
    responses=put_response_schema_dict
)
@api_view(['GET', 'PUT', 'DELETE'])
def deposit_detail(request, pk):
    """
        Retrieve, update or delete a deposit.
    """
    try:
        obj = Deposit.objects.get(pk=pk)
    except Deposit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DepositSerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DepositPostSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


################################################## WITHDRAW ###########################################################


@swagger_auto_schema(
    method='post',
    request_body=WithdrawPostSerializer,
    responses=post_response_schema_dict
)
@api_view(['GET', 'POST', 'DELETE'])
def withdraw_list(request):
    """
        List or delete all withdraws, or create a new withdraw.
    """
    if request.method == 'GET':
        obj = Withdraw.objects.all()
        serializer = WithdrawSerializer(obj, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WithdrawPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Withdraw.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='put',
    request_body=WithdrawPostSerializer,
    responses=put_response_schema_dict
)
@api_view(['GET', 'PUT', 'DELETE'])
def withdraw_detail(request, pk):
    """
        Retrieve, update or delete an withdraw.
    """
    try:
        obj = Withdraw.objects.get(pk=pk)
    except Withdraw.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WithdrawSerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WithdrawPostSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)