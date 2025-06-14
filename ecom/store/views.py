from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')
def calendar(request):
    user_id = request.session.get('user_id')
    user = Logins_emp.objects.get(id=user_id)
    return render(request, 'calendar.html', {'user': user} )
def index_HR(request):
    user_id = request.session.get('user_id')
    user = HR_HR.objects.get(id=user_id)
    return render(request, 'index_HR.html', {'user': user})


def index(request):
    emp = Employee.objects.first()
    user_id = request.session.get('user_id')
    user = Logins_emp.objects.get(id=user_id)
    context = {
        'user': user,
        'customer': emp.customer if emp else 0,
        'order': emp.order if emp else 0,
        'sellings': emp.sellings if emp else 0,
    }
    return render(request, 'index.html', context)
def emi(request):
    user_id = request.session.get('user_id')
    user = HR_HR.objects.get(id=user_id)
    return render(request, 'emi.html', {'user': user})
def pay(request):
    user_id = request.session.get('user_id')
    user = HR_HR.objects.get(id=user_id)
    return render(request, 'pay.html', {'user': user})
def r(request):
    user_id = request.session.get('user_id')
    user = HR_HR.objects.get(id=user_id)
    return render(request, 'r.html', {'user': user})
def att(request):
    user_id = request.session.get('user_id')
    user = HR_HR.objects.get(id=user_id)
    return render(request, 'att.html', {'user': user})
def lm(request):
    user_id = request.session.get('user_id')
    user = HR_HR.objects.get(id=user_id)
    return render(request, 'lm.html', {'user': user})
def a1(request):
    user_id = request.session.get('user_id')
    user = HR_HR.objects.get(id=user_id)
    return render(request, 'a1.html', {'user': user})
def a2(request):
    user_id = request.session.get('user_id')
    user = HR_HR.objects.get(id=user_id)
    return render(request, 'a2.html', {'user': user})
def a3(request):
    user_id = request.session.get('user_id')
    user = HR_HR.objects.get(id=user_id)
    return render(request, 'a3.html', {'user': user})
def a4(request):
    user_id = request.session.get('user_id')
    user = HR_HR.objects.get(id=user_id)
    return render(request, 'a4.html', {'user': user})



def HR_profile(request):
    role = request.session.get('role')
    user_id = request.session.get('user_id')
    
    if role == 'hr':
        user = HR_HR.objects.get(id=user_id)
    elif role == 'employee':
        user = Logins_emp.objects.get(id=user_id)
    else:
        return redirect('login')

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')  
        user.bio = request.POST.get('bio')
        user.country = request.POST.get('country')
        user.city_state = request.POST.get('city_state')
        user.postal_code = request.POST.get('postal_code')
        user.tax_id = request.POST.get('tax_id')
        if request.FILES.get('image'):
            user.image = request.FILES.get('image')
        user.save()
        return redirect('HR_profile')

    return render(request, 'HR_profile.html', {'user': user})
 







def HR_calendar(request):
    user_id = request.session.get('user_id')
    user = HR_HR.objects.get(id=user_id)
    return render(request, 'HR_calendar.html', {'user': user})
# change
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            hr = HR_HR.objects.get(username=username, password=password)
            request.session['user_id'] = hr.id
            request.session['role'] = 'hr'
            return redirect('index_HR')
        except HR_HR.DoesNotExist:
            pass

        try:
            emp = Logins_emp.objects.get(username=username, password=password)
            request.session['user_id'] = emp.id
            request.session['role'] = 'employee'
            return redirect('index')
        except Logins_emp.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')
def profile(request):
    role = request.session.get('role')
    user_id = request.session.get('user_id')
    
    if role == 'hr':
        user = HR_HR.objects.get(id=user_id)
    elif role == 'employee':
        user = Logins_emp.objects.get(id=user_id)
    else:
        return redirect('login')

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')  
        user.bio = request.POST.get('bio')
        user.country = request.POST.get('country')
        user.city_state = request.POST.get('city_state')
        user.postal_code = request.POST.get('postal_code')
        user.tax_id = request.POST.get('tax_id')
        if request.FILES.get('image'):
            user.image = request.FILES.get('image')
        user.save()
        return redirect('profile')

    return render(request, 'profile.html', {'user': user})
def projects(request):
    user_id = request.session.get('user_id')
    user = Logins_emp.objects.get(id=user_id)
    return render(request, 'projects.html', {'user': user})
def projects_HR(request):
    user_id = request.session.get('user_id')
    user = HR_HR.objects.get(id=user_id)
    return render(request, 'projects_HR.html', {'user': user})
def notice(request):
    user_id = request.session.get('user_id')
    user = Logins_emp.objects.get(id=user_id)
    return render(request, 'notice.html', {'user': user})
def notice_HR(request):
    user_id = request.session.get('user_id')
    user = HR_HR.objects.get(id=user_id)
    return render(request, 'notice_HR.html', {'user': user})