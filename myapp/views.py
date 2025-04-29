from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    return render(request,template_name='myapp/home.html')

def hospital_list(request):
    hospitals = Hospital.objects.all()
    context = {
        'hospitals': hospitals
    }
    return render(request, template_name='myapp/all_hospitals.html', context=context)

def about(request):
    return render(request,template_name='myapp/about.html')

def hospital_details(request, id):
    hospital = Hospital.objects.get(pk=id)
    context = {
        'hospital': hospital,
    }
    return render(request, template_name='myapp/details_hospital.html', context=context)

def upload_hospital(request):
    form = HospitalForm()
    if request.method == 'POST':
        form = HospitalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    context = {'form': form}
    return render(request, template_name='myapp/hospital_form.html', context=context)

def update_hospital(request, id):
    hospital = Hospital.objects.get(pk=id)
    form = HospitalForm(instance=hospital)
    if request.method == 'POST':
        form = HospitalForm(request.POST, request.FILES, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    context = {'form': form}
    return render(request, template_name='myapp/hospital_form.html', context=context)

def delete_hospital(request, id):
    hospital = Hospital.objects.get(pk=id)
    if request.method == 'POST':
        hospital.delete()
        return redirect('hospital_list')
    return render(request, template_name='myapp/delete_hospital.html')
