from django.contrib import admin

from .models import Contact, Person, Duty, Church_info, Person_detail, Address, Vehicle, Family


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','gender','birthday']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['mobile_phone','residential_phone','email','person']

@admin.register(Duty)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['duty','person']

@admin.register(Church_info)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['baptized_date','baptized_church','aquaintance','service_experience','person']

@admin.register(Person_detail)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['community','status','job','company_name','person']

@admin.register(Address)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['street1','street2','city','postal_code','person']

@admin.register(Vehicle)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['licence_plate','person']

@admin.register(Family)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['family_relationship','person']