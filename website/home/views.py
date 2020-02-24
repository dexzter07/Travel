from django.shortcuts import render
from . models import Destinations, Contact, Inquiry
from math import ceil

# Create your views here.


def index(request):

    # destinations = Destinations.objects.all()

    # n = len(destinations)
    # nSlides = n//4 + ceil((n/4)-(n/4))
    # params = {'no_of_slides': nSlides, 'range': range(
    #     1, nSlides), 'card': destinations}

    allDest = []
    catdest = Destinations.objects.values('category', 'id')
    cats = {item['category'] for item in catdest}
    for cat in cats:
        dest = Destinations.objects.filter(category=cat)
        n = len(dest)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allDest.append([dest, range(1, nSlides), nSlides])
    params = {'allDest': allDest}
    return render(request, 'home/index.html', params)


def about(request):

    return render(request, "home/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'home/contact.html')


def inquiry(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        inquiry = Inquiry(name=name, email=email, contact=phone)
        inquiry.save()
    return render(request, 'home/index.html')


def package(request):
    return render(request, "home/package.html")
