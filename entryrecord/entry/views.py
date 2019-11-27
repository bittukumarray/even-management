from django.shortcuts import render
from .forms import GuestForm, HostForm, GuestCheckoutForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .generateuiniquetoken import generate
from .models import *
import datetime
from twilio.rest import Client

# Create your views here.
from django.http import HttpResponse

account_sid = 'YOUR TWILIO ACCOUNT SID'
auth_token = 'YOUR TWILIO AUTH TOKEN'

def index(request):
    return render(request, "entry/index.html",)


def guest_checkout(request):

    if request.method == "POST":

        token = request.POST.get('token')
        # print(token)
        formData = 0
        try:
            formData = Guest.objects.get(token=token)
            formData.save()
        except:
            print("except")
            messages.error(
                request, 'Invalid token')
            return render(request, 'entry/guest_checkout.html',)
        try:
            context = {
                "email": formData.email,
                'name': formData.name,
                'phone': formData.phone_number,
                'check_in': formData.check_in,
                'check_out': formData.check_out,
                'hostname': formData.host.name,
                'address_visited': formData.host.event_address,
            }
            sms = '\nYour details of meeting:--\nEmail --'+ str(formData.email)+ '\nName --' + str(formData.name)+'\nphone --'+ str(formData.phone_number) +'\ncheck_in time --'+ str(formData.check_in) + '\ncheck_out time --'+ str(formData.check_out) + '\nhostname --' + str(formData.host.name) + '\naddress_visited --'+ str(formData.host.event_address)
            # print(context)
            subject = 'Event management Guest Details'
            message = render_to_string(
                'entry/guest_email.html', context)
            text_content = strip_tags(message)
            to_email = formData.email
            email = EmailMessage(
                subject, text_content, to=[to_email]
            )
            email.send()
            client = Client(account_sid, auth_token)
            try:
                message = client.messages.create(
                                body=sms,
                                from_='+14405700753',
                                to=formData.phone_number
                            )
            except:
                messages.error(
                request, 'Email sent but, phone SMS could not send, it seems the phone was not in the desire format')
                


            return render(request, 'entry/on_checked_out.html',)
        except:
            messages.error(
                request, 'Some error occured!!')


    return render(request, 'entry/guest_checkout.html',)


def guest_entry(request):
    guestform = GuestForm()
    
    if request.method == "POST":

        form_data = GuestForm(request.POST)
        # print(form_data)

        if form_data.is_valid():
            token = generate()
            formData = form_data.save(commit=True)
            data = Guest.objects.get(id=formData.id)
            data.token = token
            data.save()
            print(formData.check_in)
            try:
                print("1st")
                context = {
                    "email": form_data.cleaned_data.get('email'),
                    'name': form_data.cleaned_data.get('name'),
                    'phone': form_data.cleaned_data.get('phone_number'),
                    'check_in': formData.check_in,
                }
                subject = 'Event management Guest Details'
                message = render_to_string(
                    'entry/host_email.html', context)
                text_content = strip_tags(message)
                host = form_data.cleaned_data.get('host')
                to_email = host.email
                email = EmailMessage(
                    subject, text_content, to=[to_email]
                )
                email.send()

                sms = '\nGuest details of meeting:--\nEmail --'+ str(context['email'])+ '\nName --' + str(context['name'])+'\nphone --'+ str(context['phone']) +'\ncheck_in time --'+ str(context['check_in'])
                client = Client(account_sid, auth_token)
                print(host.phone_number)
                try:
                    message = client.messages.create(
                                    body=sms,
                                    from_='+14405700753',
                                    to=host.phone_number
                                )
                except:
                    messages.error(
                    request, 'SMS could not send, it seems the phone was not in the desire format')
                return render(request,'entry/on_success_guest.html', {'token': token})
            except:
                messages.error(
                request, 'Some error occured!!')


        else:
            print("form data invalid")
            messages.error(
                request, 'Error occured!! Your Phone number must have to be 9 to 15 digits with country code i.e +917689767689')

    return render(request, 'entry/guest_entry.html', {'guest_form': guestform})


def host_entry(request):
    hostform = HostForm()


    if request.method == "POST":

        form_data = HostForm(request.POST)

        if form_data.is_valid():
            formData = form_data.save(commit=True)
            messages.error(
                request, 'Host Registered successfully!!')
            return render(request, "entry/index.html",)
        else:
            print("form data invalid")
            messages.error(
                request, 'Erro Occured!! Your Phone number must includes country code otherwise(9 to 15 digits) while checkout you will not get SMS on phone i.e +917689767689')

    return render(request, 'entry/host_entry.html', {'host_form': hostform})
