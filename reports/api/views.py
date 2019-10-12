from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from reports.models import Report
from reports.api.serializers import ReportSerializer

@api_view(['GET',])
def api_detail_reports_view(request, id):
    try:
        report = Report.objects.get(pk=id)
    except Report.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ReportSerializer(report)
        return Response(serializer.data)

@api_view(['PUT',])
def api_update_reports_view(request, id):
    try:
        report = Report.objects.get(pk=id)
    except Report.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = ReportSerializer(report, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            data["message"] = "Report updated successfully."
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_delete_reports_view(request, id):
    try:
        report = Report.objects.get(pk=id)
    except Report.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = report.delete()
        data = {}
        if operation:
            data["message"] = "Report deleted sucessfully."
        else:
            data["message"] = "Report delete failed"
        return Response(data=data) 


@api_view(['POST',])
def api_create_reports_view(request):
    
    report = Report()

    if request.method == "POST":
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)