from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from .forms import PersonForm, ContactForm, DutyForm, Church_infoForm, Person_detailForm, AddressForm, VehicleForm, FamilyForm

from .models import Contact, Person, Duty, Church_info, Person_detail, Address, Vehicle, Family

def home(request):
    persons = Person.objects.all()
    return render(request,'home.html', {'persons':persons,})

def person_info(request,id):
    try:
        person_info = Person.objects.get(id=id)
        duty = Duty.objects.get(id=id)
        church_info = Church_info.objects.get(id=id)
        person_detail = Person_detail.objects.get(id=id)
        address = Address.objects.get(id=id)
        vehicle = Vehicle.objects.get(id=id)
        family = Family.objects.get(id=id)
        contacts = Contact.objects.get(id=id)
    except Person.DoesNotExist:
        raise Http404('person not found!')
    return render(request, 'person_info.html', {'person_info':person_info, 'duty':duty,'church_info':church_info,
                                                'person_detail':person_detail, 'address':address,'vehicle':vehicle,
                                                'family':family,'contacts':contacts,})

def create(request):
    personForm = PersonForm(request.POST or None)
    contactForm = ContactForm(request.POST or None)
    dutyForm = DutyForm(request.POST or None)
    church_infoForm = Church_infoForm(request.POST or None)
    detailForm = Person_detailForm(request.POST or None)
    addressForm = AddressForm(request.POST or None)
    vehicleForm = VehicleForm(request.POST or None)
    familyForm = FamilyForm(request.POST or None)

    if personForm.is_valid() and contactForm.is_valid() and dutyForm.is_valid() and church_infoForm.is_valid and detailForm.is_valid and addressForm.is_valid and vehicleForm.is_valid and familyForm.is_valid:
        personForm.save()
        contactForm.save()
        dutyForm.save()
        church_infoForm()
        detailForm()
        addressForm()
        vehicleForm()
        familyForm()
        return redirect('/')

    return render(request, 'person_form.html', {'personForm':personForm,'contactForm':contactForm,
                                                'dutyForm':dutyForm,'church_infoForm':church_infoForm,'detailForm':detailForm,
                                                'addressForm':addressForm,'vehicleForm':vehicleForm,'familyForm':familyForm})

def update(request,id):
    person = Person.objects.get(id=id)
    form = PersonForm(request.POST or None, instance=person)
    
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'person_form.html', {'form':form}, {'person':person})

def delete(request,id):
    person = Person.objects.get(id=id)
    
    if request.method == 'POST':
        person.delete()
        return redirect('home')
    
    return render(request, 'delete_confirm.html',{'person': person})