from django.shortcuts import render, redirect
from .models import ContactMessage,UserImages,User
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Send email notification
            send_mail(
                subject=f"New Contact Form Submission from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
            )
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def admin_dashboard(request):
    # Fetch all contact messages
    messages = ContactMessage.objects.all()
    return render(request, 'admin_dashboard.html', {'messages': messages})

def project1(request):
    return render(request,'project1.html')

def project(request):
    return render(request,'project.html' )





