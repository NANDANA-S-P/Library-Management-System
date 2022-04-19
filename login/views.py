from django.shortcuts import render, redirect
from django.contrib.auth import logout
#from record import views
# Create your views here.


def home(request):
    return render(request, 'login/home.html')


# def dashboard(request):
#     currentuser = request.user
#     userdetail = {}
#     department = {
#         'AE': 'Aeronautical Engineering',
#         'AU': 'Automobile Engineering',
#         'BT': 'Biotechnology',
#         'CE': 'Civil Engineering',
#         'CS': 'ComputerScience Engineering',
#         'EE': 'Electrical and Electronics Engineering',
#         'EC': 'Electronics and Communication Engineering',
#         'EI': 'Electronics and Instrumentation Engineering',
#         'FT': 'Fashion Technology',
#         'IS': 'Information Science and Engineering',
#         'IT': 'Information Technology',
#         'ME': 'Mechanical Engineering',
#         'MC': 'Mechatronics Engineering',
#         'TT': 'Textile Technology'
#     }
#     nameroll = currentuser.username.split('.')
#     userdetail['username'] = nameroll[0]
#     userdetail['rollnum'] = nameroll[1]
#     userdetail['email'] = currentuser.email
#     d = nameroll[1]
#     dept = d[3:5]
#     userdetail['department'] = department[dept]

#     print(userdetail)
#     return render(request, 'login/category.html', {'userdet': userdetail})


def log_out(request):
    logout(request)
    return redirect('/')
