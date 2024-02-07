from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.



#returning string as response by using function and Class based Views

def fun_base_views_str(request):

    return HttpResponse('<center> <h1> This is function Based view in string')

class Class_Base_Views_Str(View):
    def get(self,request):

        return HttpResponse('<center> <h1> This is Class Based view in string')
    

#returning HTML page as response by using function and Class based Views
    
def fun_base_view_html(request):

    return render(request,'fun_base_view_html.html')

class Class_Base_view_html(View):
    def get(self,request):

        return render(request,'Class_Base_view_html.html')
    

#Sending HTML form page and taking the data from user and insert into database by using function and Class based Views
    
def insert_data_FBV(request):
    EFO = CollegeForm()
    d={'EFO':EFO}
    if request.method == 'POST':
        FOD = CollegeForm(request.POST)
        if FOD.is_valid():
            FOD.save()
            return HttpResponse('<center><h1> Your Data Has Been Submitted Successfully')

    return render(request,'insert_data_FBV.html',d)


class insert_data_CBV(View):
    def get(self,request):
        EFO = CollegeForm()
        d={'EFO':EFO}
        return render(request,'insert_data_CBV.html',d)
    
    def post(self,request):
        DFO = CollegeForm(request.POST)
        if DFO.is_valid():
            DFO.save()
            return HttpResponse('<center><h1> Your Data Has Been Submitted Successfully')

    
class insert_CBV_TemplateView(TemplateView):
    template_name = 'insert_CBV_TemplateView.html'