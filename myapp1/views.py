import random
import string
import time

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .db import db
from email.message import EmailMessage
import smtplib
import bcrypt


# Create your views here.


def mongodb_data(request):
    collection = db["Users"]
    data = collection.find()
    data_list = list(data)
    return JsonResponse(data_list, safe=False)


def login_request(request):
    return render(request, "myapp1/login.html")


def register_request(request):
    return render(request, "myapp1/register.html")


def main_page(request):
    return render(request, "myapp1/main_page.html")


def home(request):
    return render(request, "myapp1/home.html")


def post_handle(request):
    if request.method == 'POST':
        data = {
            "_id": random.randint(1, 20),
            "Name": request.POST.get("name"),
            "Surname": request.POST.get("surname"),
            "Email": request.POST.get("email"),
            "Password": request.POST.get("password"),
            "Country": request.POST.get("country"),
            "GUID": ''.join(random.choice(string.digits + string.ascii_letters + string.ascii_uppercase) for i in
                            range(12))
        }
        try:
            collection = db['Users']
            if collection.find_one({"Email": data["Email"]}):
                return JsonResponse({"status": "error", "message": "Email address already exists"}, status=409)
            post = collection.insert_one(data)
            time.sleep(6)
            return redirect('success_registration')
        except Exception as e:
            return JsonResponse({"status": "failed", "message": f"registration failed {str(e)}"}, status=500)
    return JsonResponse({"status": "Failed", "message": "Only POST requests allowed"})


def python_content(request):
    return render(request, "myapp1/python_content.html")


def handle_login(request):
    if request.method == 'POST':
        collection = db['Users']

        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            return JsonResponse({"status": "failed", "message": "Email and Password are required"})

        user = collection.find_one()

        if not user["Email"]:
            return JsonResponse({"status": "Failed", "message": "Authentication Failed"})

        if user["Password"] == password and user['Email'] == email:
            time.sleep(6)
            return redirect('success_login')
        else:
            return JsonResponse({"status": "failed", "message": "Invalid credentials"})

    return JsonResponse({"status": "failed", "message": "Only POST requests Allowed"})


def pypy(request):
    return render(request, "myapp1/pypy.html")


def success_registration(request):
    return render(request, "myapp1/success_registration.html")


def success_login(request):
    return render(request, "myapp1/success_login.html")


def welcome_mail(request):

    if JsonResponse({"status": "success", "message": "Authentication Successful"}):

        email = request.POST.get("email")
        mail = EmailMessage()
        mail["To"] = "admusr@hassos.local"
        mail["From"] = "admin@pyexpress.net"
        mail["Subject"] = "Welcome to PyExpress – Let’s Begin Your Python Journey!"
        mail.set_content(f"""
            Hi there,

            Welcome to PyExpress! 🎉 We’re thrilled to have you join a community that’s passionate about Python and Django.
            
            At PyExpress, we’re here to support your growth with tailored tutorials, project ideas, and a vibrant community of like-minded developers.
            
            Here's how to get started:
            Explore Tutorials: Visit [Your Tutorials Page Link] for beginner to advanced guides.
            Join the Community: Collaborate on GitHub projects and share ideas.
            Stay Updated: Follow us for the latest updates and new content.
            If you have any questions or need assistance, feel free to reach out to our support team at [Support Email].
            
            Thank you for choosing PyExpress. Let’s code and create together!
            
            Best regards,
            The PyExpress Team
    """)

        with smtplib.SMTP("192.168.1.100", 25) as mta:
            mta.ehlo()
            mta.send_message(mail)
            mta.close()
            return redirect('success_registration')

    # if bcrypt.checkpw(password.encode('utf-8'), user['Password'].encode('utf-8')):


def forgot_password(request):
    return render(request, "myapp1/forgot_password.html")


def validate_forgot_password(request):
    if request.method == "POST":
        collection = db["Users"]
        email = request.POST.get("email")
        user_id = request.POST.get("user_id")
        username = collection.find_one({"Email": email})
        if not username:
            return JsonResponse({"status": "Error", "message": "User Does Not Exist"})
        if username.get('GUID') == user_id:
            time.sleep(4)
            return redirect('reset-password')
        else:
            return JsonResponse({"status":  "Failed", "message": "Details Not Matching Any Records"})
    return JsonResponse({"status": "Failed", "message": "Only POST requests Allowed"})


def sign_out(request):
    time.sleep(4)
    return render(request, "myapp1/logged_out.html")


def reset_password(request):
    return render(request, "myapp1/password_reset.html")


def execute_pass_reset(request):
    if request.method == "POST":
        collection = db["Users"]
        email = request.POST.get('email')
        password = request.POST.get('new_password')
        con_password = request.POST.get('confirm_password')

        if password != con_password:
            return JsonResponse({"status": "Failed", "message": "Password Does Not Match"})

        else:
            email = request.session.get('username')
            user = collection.find_one({"Email": email})

            print(email, user)
            pass_update = {"$set": {"Password": password}}
            data = collection.update_one({"Email": email}, pass_update)
            time.sleep(4)
            return render(request, "myapp1/success_pass_reset.html")

    return JsonResponse({"status": "failure", "message": "Only Post Requests Allowed"})


def user_profile(request):
    return render(request, "myapp1/User_Profile.html")



