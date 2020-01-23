URLs:----

```
http://localhost:8000/entry/
```

This is the Landing page for this system.

```
http://localhost:8000/entry/host/
```

This is the Host registration page. Here Host will enter his details and submit the form, after successful registration it will show the successful registration message.

```
http://localhost:8000/entry/checkin/
```

This is for Guest check in. Here Guest will select the host from the list of all the hosts and fill the form. After successful registration one mail and one SMS will be send to corresponding host with user's details, and it will generate a token for the guest to use it while check out. That is the guest will have to only fill the token while checking out and the system will verify him/her and then send all the required details to the host through both phone SMS and Email.

The Token is of length 7 characters and it is unique, I have created my own unique token generator function.

```
http://localhost:8000/entry/checkout/
```

This page is for Check out. The guest  will have to only submit the token which was given to him/her while checking in and all the guest's details including host name, and address will be sent out to the guest through both Email and phone SMS. 



REQUIREMENTS:--

- Django version 2.x i.e greater than 2.
- Python 3.6
- Twilio :-- for Phone SMS
- SMPT server setup :-- for Email sending



INSTALLATION OF REQUIREMENTS:--  on ubuntu 18.04

​	   For Phone SMS

- ```
  pip3 install twilio 
  ```

  Django installation

- ```
  sudo apt install python3-django
  ```



For Twilio to work on your machine:

1. First of all install twilio on your machine by the above given command (on ubuntu)
2. Buy a number on twilio website so that you can use it to send SMS on any number which are verified on twilio(on trial version, because I used only trial version of it)
3. Then Set these two things in "entryrecord.settings.py"
    	1. account_sid = "your twilio account_sid"
    	2. auth_token = "Your twilio auth_token"

Enter your email and password in "entryrecord.settings.py" in place of  "email" and "password".

Type :--   "python3 manage.py runserver" in the "entryrecord directory" on terminal to run the project locally on your machine. 



I have tried my best to explain you all the things which are necessary to run this system.

Thank You. 
