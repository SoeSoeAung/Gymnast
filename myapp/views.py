from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    home = Home.objects.all().order_by('id')
    access = Access.objects.all().order_by('id')[:2]
    about = About.objects.all().order_by('id')
    about1 = About1.objects.all().order_by('id')[:2]
    featue = Featue.objects.all().order_by('id')
    featue1 = Featue1.objects.all().order_by('id')
    featue2 = Featue2.objects.all().order_by('id')
    benefit = Benefit.objects.all().order_by('id')[:4]
    bmi = Bmi.objects.all().order_by('-id')
    trainer = Trainer.objects.all().order_by('id')
    client = Client.objects.all().order_by('id')[:4]
    blog = Blog.objects.all().order_by('id')[:3]
    subscribe = Subscribe.objects.all().order_by('id')
        
    context = {
        'home': home,
        'access': access,
        'about': about,
        'about1': about1,
        'featue': featue,
        'featue1': featue1,
        'featue2': featue2,
        'benefit': benefit,
        'bmi': bmi,
        'trainer': trainer,
        'client': client,
        'blog': blog,
        'subscribe': subscribe
        
    }
    
    return render(request, 'index.html', context)
    
