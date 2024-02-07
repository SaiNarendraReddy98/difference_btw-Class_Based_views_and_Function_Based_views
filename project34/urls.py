"""
URL configuration for project34 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),

    path('fun_base_views_str/',fun_base_views_str,name='fun_base_views_str'),
    path('Class_Base_Views_Str/',Class_Base_Views_Str.as_view(),name='Class_Base_Views_Str'),

    path('fun_base_view_html/',fun_base_view_html,name='fun_base_view_html'),
    path('Class_Base_view_html/',Class_Base_view_html.as_view(),name='Class_Base_view_html'),

    path('insert_data_FBV/',insert_data_FBV,name='insert_data_FBV'),
    path('insert_data_CBV/',insert_data_CBV.as_view(),name='insert_data_CBV'),

    path('insert_CBV_TemplateView/',insert_CBV_TemplateView.as_view(),name='insert_CBV_TemplateView'),
]
