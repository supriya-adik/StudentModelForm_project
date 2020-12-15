from django.shortcuts import render
from .forms import StudentForm
from .models import Student
# Create your views here.

def home_page_view(request) :
    form=StudentForm()
    if request.method=='POST' :
        form=StudentForm(request.POST)
        if form.is_valid() :
            form.save(commit=True)
            form=StudentForm()
    return render(request,'ModelApp/home.html',{'form':form})

def list_view(request) :
    list_obj=Student.objects.all()
    return render(request,'ModelApp/list.html',{'list_obj':list_obj})
