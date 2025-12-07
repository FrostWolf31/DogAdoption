from django.shortcuts import render
from django.core.mail import send_mail 


def Index(request):
    return render(request, 'index.html', {})

def contact(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Phone_Number = request.POST['Phone_Number']
        Email = request.POST['Email']
        Message = request.POST['Message']

        #send
        send_mail(
            'Email From: ' + Name,#subject
            Message + " Phone Number: " + Phone_Number + " Email: " + Email,#message
            Email,#from
           ['jacksanimalrescue@gmail.com'], #To email
        )

        return render(request, 'contact.html', {'Name':Name})
    
    else:
        return render(request, 'contact.html', {})

def adopt(request):
    return render(request, 'adopt.html',{})

def pet(request):
    return render(request, 'pet.html' , {})

def about(request):
    return render(request, 'about.html', {})

def faq(request):
    return render(request, 'faq.html' , {})

def select(request):
    try:
        from .models import Dog
        dogs = Dog.objects.filter(is_available=True).order_by('order')
    except Exception:
        dogs = []
    return render(request, 'dogselect.html', {'dogs': dogs})

def story(request):
    return render(request, 'stories.html', {})


def article1(request):
    return render(request,"article1.html", {})


