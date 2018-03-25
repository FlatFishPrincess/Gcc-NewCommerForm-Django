from django import forms
from .models import Contact, Person, Duty, Church_info, Person_detail, Address, Vehicle, Family

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','last_name','gender','birthday']

class Person_detailForm(forms.ModelForm):
    class Meta:
        model = Person_detail
        fields = ['community','status','job','company_name']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['mobile_phone','residential_phone','email']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street1','street2','city','postal_code']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['licence_plate']


class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['family_relationship']

class DutyForm(forms.ModelForm):
    class Meta:
        model = Duty
        fields = ['duty']

class Church_infoForm(forms.ModelForm):
    class Meta:
        model = Church_info
        fields = ['baptized_date','baptized_church','aquaintance','service_experience']