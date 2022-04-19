from django.shortcuts import render
from . models import *
# Create your views here.


def dashboard(request):
    currentuser = request.user
    userdetail = {}
    department = {
        'AE': 'Aeronautical Engineering',
        'AU': 'Automobile Engineering',
        'BT': 'Biotechnology',
        'CE': 'Civil Engineering',
        'CS': 'ComputerScience Engineering',
        'EE': 'Electrical and Electronics Engineering',
        'EC': 'Electronics and Communication Engineering',
        'EI': 'Electronics and Instrumentation Engineering',
        'FT': 'Fashion Technology',
        'IS': 'Information Science and Engineering',
        'IT': 'Information Technology',
        'ME': 'Mechanical Engineering',
        'MC': 'Mechatronics Engineering',
        'TT': 'Textile Technology'
    }
    nameroll = currentuser.username.split('.')
    userdetail['username'] = nameroll[0]
    userdetail['rollnum'] = nameroll[1]
    userdetail['email'] = currentuser.email
    d = nameroll[1]
    dept = d[3:5]
    userdetail['department'] = department[dept]

    print(userdetail)
    return render(request, 'record/category.html', {'userdet': userdetail})


def coex(request):
    if request.method == 'POST':
        # print("hisdjkccccccccj")
        # print(request.POST.get('event_type'))
        # print(request.POST.get('sponsoredorcolloboration'))
        # print(request.POST.get('event_name'))
        # print(request.POST.get('achievement'))
        # print(request.POST.get('level'))
        # print(request.POST.get('organizationorinstitutionname'))
        # print(request.POST.get('amountsponsored'))

        user = request.user
        eventtype = request.POST.get('event_type')
        sponsoredorcolloboration = request.POST.get('sponsoredorcolloboration')

        eventname = request.POST.get('event_name')
        achievement = request.POST.get('achievement')
        level = request.POST.get('level')
        organizationorinstitutionname = request.POST.get(
            'organizationorinstitutionname')
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        days = request.POST.get('days')
        amountsponsored = request.POST.get('amountsponsored')
        externalagency = request.POST.get('externalagency')
        amountreceived = request.POST.get('amountreceived')
        proof = request.FILES.get('proof')
        newcoex = Cocurricular_and_Extra_curricular_activities(userdet=user, event_type=eventtype, Sponsoredorcolloboration=sponsoredorcolloboration, event_name=eventname, achievement=achievement, level=level,
                                                               organizationorinstitutionname=organizationorinstitutionname, fromdate=fromdate, todate=todate, days=days, amountsponsored=amountsponsored, externalagency=externalagency, amountreceived=amountreceived, proof=proof)
        newcoex.save()
        return render(request, 'record/achadded.html')
    return render(request, 'record/co-ex.html')


def compexam(request):
    return render(request, 'record/compexam.html')


def conference(request):
    return render(request, 'record/conference.html')


def project(request):
    return render(request, 'record/project.html')


def scholarship(request):
    return render(request, 'record/scholarship.html')
