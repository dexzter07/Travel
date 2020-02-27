from django.shortcuts import render
from . models import Destinations, Contact, Inquiry, Package, Orders
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
        thank = True
        return render(request, 'home/contact.html', {'thank': thank})
    return render(request, 'home/contact.html')


def inquiry(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        inquiry = Inquiry(name=name, email=email, contact=phone)
        inquiry.save()
        thank = True

        return render(request, 'home/index.html', {'thank': thank})
    return render(request, 'home/index.html')


def package(request):
    allPack = []
    catdest = Package.objects.values('category', 'id')
    cats = {item['category'] for item in catdest}
    for cat in cats:
        dest = Package.objects.filter(category=cat)
        n = len(dest)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))

        allPack.append([dest, range(1, nSlides), nSlides])
    params = {'allPack': allPack}
    return render(request, 'home/package.html', params)


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        firstName = request.POST.get('firstName', '')
        lastName = request.POST.get('lastName', '')

        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        address1 = request.POST.get('address1', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zipcode = request.POST.get('zipcode', '')
        amount = request.POST.get('amount', '')

        order = Orders(items_json=items_json, firstName=firstName, lastName=lastName, email=email, phone=phone, address=address,
                       address1=address1, city=city, state=state, zipcode=zipcode, amount=amount)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'home/checkout.html', {'thank': thank, 'id': id})

    return render(request, 'home/checkout.html')
