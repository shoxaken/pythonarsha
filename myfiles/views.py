from django.shortcuts import render
from myfiles.models import Portfolio , Baza , Team ,Contact , Join
# Create your views here.
import datetime
def index(malumot):
    if 'gmail' in malumot.POST:
        email = malumot.POST.get('gmail')
        Join(email = email,date=datetime.datetime.now()).save()
    elif malumot.method=="POST":
        ismi = malumot.POST.get('name')
        email = malumot.POST.get('email')
        subject = malumot.POST.get('subject')
        message = malumot.POST.get('message')
        Contact(name=ismi,email=email,subject=subject,description=message,date=datetime.datetime.now()).save()

    ishlar = Portfolio.objects.all()
    server = Baza.objects.all()
    team = Team.objects.all()
    contact = Contact.objects.all()
    return render(malumot,'index.html' , {"works":ishlar,"server":server,"team":team})








def portfolio(malumot,id):
    ishlar = Portfolio.objects.get(id=id)
    return render(malumot , 'portfolio-details.html', {"work":ishlar})
