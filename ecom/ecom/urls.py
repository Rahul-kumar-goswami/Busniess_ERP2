"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.login, name='login'),        # login page
    path('index/', views.index, name='index'),      # home/index page after login
    path('calendar/', views.calendar, name='calendar'), 
    path('index_HR/', views.index_HR, name='index_HR'),
    path('profile/', views.profile, name='profile'), 
    path('emi/', views.emi, name='emi'),  # HR home page after login
    path('pay/', views.pay, name='pay'),
    path('r/', views.r, name='r'),
    path('att/', views.att, name='att'),
    path('lm/', views.lm, name='lm'),
    path('a1/', views.a1, name='a1'),
    path('a2/', views.a2, name='a2'),
    path('a3/', views.a3, name='a3'),
    path('a4/', views.a4, name='a4'),
    path('HR_profile/', views.HR_profile, name='HR_profile'),
    path('HR_calendar/', views.HR_calendar, name='HR_calendar'),
    path('projects/', views.projects, name='projects'),
    path('projects_HR/', views.projects_HR, name='projects_HR'),
    path('notice/', views.notice, name='notice'),
    path('notice_HR/', views.notice_HR, name='notice_HR'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
