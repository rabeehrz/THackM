from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from reports.models import Report
from reports.api.serializers import ReportSerializer

# from final import findLawyer
from cases.models import Case
from users.models import User
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

def checkLawyer(llist, id):
    for i in range(len(llist)):
        if llist[i]['id'] == id:
            return i
    
    return -1

@api_view(['POST',])
def api_create_reports_view(request):
    
    report = Report()

    if request.method == "POST":
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            data = []
            serializer.save()
            tempList = Case.objects.all()
            lawyersList = []
            for lawyer in tempList:
                id = checkLawyer(lawyersList, lawyer.id)
                if id != -1:
                    lawyersList[id]['ipc'].append(lawyer.ipc_code)
                else:
                    user = User.objects.filter(id = lawyer.id)
                    
                    lawyersList.append({'ipc':[{'key': lawyer.ipc_code, 'value': lawyer.count}], 'name': user[0].name, 'id':lawyer.id})
            # lawyersList=[{"ipc":[{'key': 319, 'value': 6}, {'key': 300, 'value': 2}, {'key': 304, 'value': 0}, {'key': 312, 'value': 3}], "name": "Person1", "id": 1},{"ipc":[{'key': 319, 'value': 6}, {'key': 300, 'value': 0}, {'key': 304, 'value': 1}, {'key': 312, 'value': 4}], "name": "Person2", "id": 2}]
            print(lawyersList)
            # data = findLawyer(serializer.data['description'], lawyersList)
            print(data)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)