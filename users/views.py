from django.shortcuts import render
from .models import User
from reports.models import Report
from report_code.models import ReportCode

# Create your views here.

def index(request):
    return render(request, 'users/index.html')

def login(request):
    name = request.POST.get('name', "Default")
    person = User.objects.filter(name=name)
    reports = Report.objects.filter(lawyer = person[0].id, status=1)
    ipc = {}
    for report in reports:
        codes = ReportCode.objects.filter(report=report)
        for code in codes:
            if report.id in ipc:
                ipc[report.id].append(code.ipc_code)
            else:
                ipc[report.id] = [code.ipc_code,]
        
    for codes in ipc:
        ipc[codes] = ", ".join(map(str, ipc[codes]))
    print(ipc)    
    context = {
        "name" : name,
        "reports": reports,
        "ipc": ipc
    }
    return render(request,'users/home.html',context)

