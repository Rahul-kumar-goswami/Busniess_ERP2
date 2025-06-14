from django.db import models


class Logins_emp(models.Model):  # Employee
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city_state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username

    
class HR_HR(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city_state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username
class Employee(models.Model):
    customer = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    sellings = models.IntegerField(default=0)
    def __str__(self):
        return f"Customer: {self.customer}, Order: {self.order}, Sellings: {self.sellings}" 