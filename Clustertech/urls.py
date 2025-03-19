"""
URL configuration for Clustertech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from clusterapp import views 

urlpatterns = [
    path("admin/", admin.site.urls),
      path('',views.home,name='home'),
      path('whoweare/',views.whoweare,name='whoweare'),
      path('migration/',views.migration,name='migration'),
      path('helpdesk/',views.helpdesk,name='helpdesk'),
      path('customersupport/',views.customersupport,name='customersupport'),
      path('uiux/',views.uiux,name='uiux'),
      path('webdev/',views.web,name='web'),
       path('forge/',views.forge,name='forge'),
       path('career/',views.career,name='career'),
       path('form/',views.form,name='form'),

]
