from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from report_code.models import ReportCode
from report_code.api.serializers import ReportCodeSerializer

@api_view(['GET',])
def api_detail_report_code_view(request, id):
    try:
        reportcode = ReportCode.objects.get(pk=id)
    except ReportCode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ReportCodeSerializer(reportcode)
        return Response(serializer.data)

@api_view(['PUT',])
def api_update_report_code_view(request, id):
    try:
        reportcode = ReportCode.objects.get(pk=id)
    except ReportCode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = ReportCodeSerializer(reportcode, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            data["message"] = "Report Code updated successfully."
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_delete_report_code_view(request, id):
    try:
        reportcode = ReportCode.objects.get(pk=id)
    except ReportCode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = reportcode.delete()
        data = {}
        if operation:
            data["message"] = "Report Code deleted sucessfully."
        else:
            data["message"] = "Report Code delete failed"
        return Response(data=data) 


@api_view(['POST',])
def api_create_report_code_view(request):
    
    reportcode = ReportCode()

    if request.method == "POST":
        serializer = ReportCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)