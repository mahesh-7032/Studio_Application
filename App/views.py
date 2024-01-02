from django.shortcuts import render, redirect
from django.views.generic import FormView,TemplateView
from .forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

class home(TemplateView):
    template_name = 'home.html'

class my_work(TemplateView):
    template_name = 'my_work.html'

class photo_frames(TemplateView):
    template_name = 'photo_frames.html'

class packages(TemplateView):
    template_name = 'packages.html'


class about(TemplateView):
    template_name = 'about.html'

class contact_us(FormView):
    template_name = 'contact_us.html'
    form_class = RegistrationForm
    success_url = '/thank-you/' 

    def form_valid(self, form):
        
        registration_instance = form.save()

        
        send_mail(
            'New Registration',
            (f'A new user has registered:\n\nName: {registration_instance.name}\nEmail: {registration_instance.email}\nContact No: {registration_instance.contact_no}'),
            'ganireddy8121@gmail.com', 
            ['v.ganeswarareddy@gmail.com'],  
            fail_silently=False,
        )
        
        send_mail(
            'Thank You for Registering',
            (f'Thank you for registering! We appreciate your interest.\n Visit again !!!😇'),
            'ganireddy8121@gmail.com', 
            [registration_instance.email],  
            fail_silently=False,
        )

       
        return HttpResponse('Thank you for registering!')
    
    


    
        
    
