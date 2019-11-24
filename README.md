# even-management

# home page url is :-- localhost:8000/entry/

**There are four sections 1.home page, 2.host registration, 3.guest checkin, 4.guest checkout**

**1.host registration is for the registration for host, they will have to provide name, email, phone, address**

**2.guest checkin is for guest checkin, when guest checks in an email will be sent to the corresponding host and a token will be generated to checkout. this token is needed for checkout**

**3.guest checkout is for checking out after meeting is over. guest have to submit the token that he got while checking in and then an email will be triggered to the person(guest) with all details like name, email, phone, hostname, checkin, checkout and address of host.**

# Here checkin and checkout times will be caught automatically user don't have to submit it manually.

**I have created an unique token generator function each time of length 7 character, guest needs to submit it while chicking out and the system will verify him**


# Working of SMS and email service:---

**I have used twilio SMS service and it is on free trial mode so it is sending only message to one number ie +917250073079 because it is verified**

**So if you want to check with your number you have to create an account on twilio and then have to put your accound_sid and auth_token**

**Also it needs the number must have country code**

# Installing twilio:--

**pip3 install twilio**

# Requirements:---
**Django version 2**
**twilio for phone SMS**
**and use your gmail acount instead of mine, and also your twilio account credentials instead of mine**
**For adding email, just put your email and password instead of mine in settings.py file**
**For using your twilio credentials just put your accound_sid and auth_token instead of mine in viwes.py in entry app and that's it, you can test it.**

**I have provided my all credentials only for this internship purpose**

**If the guest does not provide the phone number with country code then he will not get SMS while checking out but he will get mail anyway**