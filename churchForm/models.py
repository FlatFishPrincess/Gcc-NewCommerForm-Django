from django.db import models

class Person(models.Model):
    class Meta:
        verbose_name_plural = 'people'
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    birthday = models.DateField()
    def __str__(self):
        return self.first_name

class Duty(models.Model):
    class Meta:
        verbose_name_plural = 'duties'
    duty = models.CharField(max_length=10, blank=True, default='')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.duty

class Church_info(models.Model):
    baptized_date = models.DateField(blank=True, null=True)
    baptized_church = models.CharField(max_length=15, blank=True, default='' )
    aquaintance = models.CharField(max_length=30,blank=True, default='')
    service_experience = models.CharField(max_length=30, blank=True, default='')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.baptized_church

class Person_detail(models.Model):
    community = models.CharField(max_length=15)
    status = models.CharField(max_length=15)
    job = models.CharField(max_length=25)
    company_name = models.CharField(max_length=25)
    person = models.ForeignKey( Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.community        

class Contact(models.Model):
    mobile_phone = models.CharField(max_length=15)
    residential_phone = models.CharField(max_length=15, blank=True, default='')
    email = models.EmailField()
    person = models.ForeignKey( Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.mobile_phone

class Address(models.Model):
    class Meta:
        verbose_name_plural = 'addresses'
    street1 = models.CharField(max_length = 20)
    street2 = models.CharField(max_length = 20, blank=True, default='')
    city = models.CharField(max_length = 20)
    postal_code = models.CharField(max_length = 15)
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    def __str__(self):
        return self.street1

class Vehicle(models.Model):
    licence_plate = models.CharField(max_length = 15, blank=True, default='')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.licence_plate

class Family(models.Model):
    class Meta:
        verbose_name_plural = 'families'
    family_relationship = models.CharField(max_length = 15, blank=True, default='')
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    def __str__(self):
        return self.family_relationship