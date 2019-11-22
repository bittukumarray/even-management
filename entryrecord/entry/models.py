from django.db import models
from django.core.validators import RegexValidator
import uuid


class Host(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    event_address = models.CharField(max_length=255)
    # phone_regex = RegexValidator(
    #     regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], max_length=17)  # validators should be a list


    def __str__(self):
        return self.name +"("+str(self.event_address)+")"


class Guest(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    token = models.CharField(max_length=10, unique=True, blank=True)
    email = models.EmailField(max_length=255)
    check_in = models.TimeField(auto_now=False, auto_now_add=True)
    check_out = models.TimeField(auto_now=True, auto_now_add=False)
    phone_number = models.CharField(validators=[RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], max_length=17)

    def __str__(self):
        return self.name