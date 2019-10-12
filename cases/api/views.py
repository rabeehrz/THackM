from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from cases.models import Case
from cases.api.serializers import CaseSerializer

@api_view(['GET',])
def api_detail_cases_view(request, id):
    try:
        case = Case.objects.get(pk=id)
    except Case.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CaseSerializer(case)
        return Response(serializer.data)

@api_view(['PUT',])
def api_update_cases_view(request, id):
    try:
        case = Case.objects.get(pk=id)
    except Case.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = CaseSerializer(case, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            data["message"] = "Case updated successfully."
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_delete_cases_view(request, id):
    try:
        case = Case.objects.get(pk=id)
    except Case.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = case.delete()
        data = {}
        if operation:
            data["message"] = "Case deleted sucessfully."
        else:
            data["message"] = "Case delete failed"
        return Response(data=data) 


@api_view(['POST',])
def api_create_cases_view(request):
    
    case = Case()

    if request.method == "POST":
        serializer = CaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)