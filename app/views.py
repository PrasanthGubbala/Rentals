from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.template.context_processors import media
from app.models import ProviderDetails,ConsumerDetails,Services

#main phase
def main(request):
    return render(request, 'main/main.html')

#providerlogin
def provider_login(request):
    return render(request, 'main/provider_login.html')

def provider_login_check(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        provider = ProviderDetails.objects.get(email=email)
        if email == provider.email and password == provider.password:
            return render(request, 'provider/provider_home.html',{'provider':provider})
        else:
            messages.error(request,'Invalid Email and Password')
            return redirect('provider_login')
    except ProviderDetails.DoesNotExist as de:
        messages.error(request, de)
        return redirect('provider_login')

def provider_registration(request):
    return render(request, 'main/provider_registration.html')

def provider_registration_save(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    gender = request.POST.get('gender')
    contact = request.POST.get('contact')
    address = request.POST.get('address')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    photo = request.FILES['photo']
    if password == password2:
        try:
            ProviderDetails(first_name=fname, last_name=lname, gender=gender, contact=contact, address=address,
                            email=email, password=password, photo=photo).save()
            messages.success(request, 'Registered Successfully')
            return redirect('provider_login')
        except IntegrityError as ie:
            messages.error(request, 'User detail are already exist')
            return redirect('provider_registration')
    else:
        messages.error(request, "Password did'nt match")
        return redirect('provider_registration')


#consumer login
def consumer_login(request):
    return render(request, 'main/consumer_login.html')

def consumer_login_check(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        consumer = ConsumerDetails.objects.get(con_email=email)
        if email == consumer.con_email and password == consumer.password:
            return render(request, 'consumer/consumer_home.html',{'consumer':consumer})
        else:
            messages.error(request,'Invalid Email and Password')
            return redirect('consumer_login')
    except ConsumerDetails.DoesNotExist as de:
        messages.error(request, de)
        return redirect('consumer_login')

def consumer_registration(request):
    return render(request, 'main/consumer_registration.html')

def consumer_registration_save(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    address = request.POST.get('address')
    contact = request.POST.get('contact')
    con_email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    photo = request.FILES['photo']
    if password == password2:
        try:
            ConsumerDetails(name=name, age=age, gender=gender, address=address, contact=contact,
                            con_email=con_email, password=password, photo=photo).save()
            messages.success(request, 'Registered Successfully')
            return redirect('consumer_login')
        except IntegrityError as ie:
            messages.error(request, 'User details are already exist')
            return redirect('consumer_registration')
    else:
        messages.error(request, "Password did'nt match")
        return redirect('consumer_registration')



#provider phase
def provider_profile(request):
    email = request.GET.get('email')
    provider = ProviderDetails.objects.get(email=email)
    return render(request,'provider/provider_profile.html',{'provider':provider})

def provider_home(request):
    email = request.GET.get('email')
    try:
        provider = ProviderDetails.objects.get(email=email)
        return render(request, 'provider/provider_home.html', {'provider': provider})
    except ProviderDetails.DoesNotExist as de:
        messages.error(request,de)
        return render(request,'provider/provider_home.html')

def add_service(request):
    email = request.GET.get('email')
    provider = ProviderDetails.objects.get(email=email)
    return render(request, 'provider/add_service.html', {'provider': provider})

def save_service(request):
    email = request.POST.get('email')
    service_type = request.POST.get('service_type')
    rooms = request.POST.get('rooms')
    square_feets = request.POST.get('square_feets')
    price = request.POST.get('price')
    city = request.POST.get('city')
    area = request.POST.get('area')
    street = request.POST.get('street')
    door_no = request.POST.get('door_no')
    image = request.FILES['image']
    Services(email=email,service_type=service_type,rooms=rooms,square_feets=square_feets,price=price,city=city,area=area,street=street,door_no=door_no,image=image).save()
    provider = ProviderDetails.objects.get(email=email)
    messages.success(request,'Uploaded Successfully')
    return render(request,'provider/provider_home.html',{'provider':provider})

def view_all_service(request):
    email = request.GET.get('email')
    provider = ProviderDetails.objects.get(email=email)
    try:
        qs = Services.objects.all()
        return render(request,'provider/view_all_service.html',{'provider':provider,'services':qs})
    except:
        return render(request, 'provider/view_all_service.html', {'provider': provider, 'message': 'Not Available Data'})



#consumer phase
def consumer_profile(request):
    con_email = request.GET.get('con_email')
    consumer = ConsumerDetails.objects.get(con_email=con_email)
    return render(request,'consumer/consumer_profile.html',{'consumer':consumer})

def consumer_home(request):
    con_email = request.GET.get('con_email')
    try:
        consumer = ConsumerDetails.objects.get(con_email=con_email)
        return render(request, 'consumer/consumer_home.html', {'consumer': consumer})
    except ConsumerDetails.DoesNotExist as de:
        messages.error(request,de)
        return render(request,'consumer/consumer_home.html')

def available_rental_services(request):
    con_email = request.GET.get('con_email')
    consumer = ConsumerDetails.objects.get(con_email=con_email)
    try:
        qs = Services.objects.all()
        return render(request, 'consumer/available_rental_services.html', {'consumer': consumer, 'services': qs})
    except:
        return render(request, 'consumer/available_rental_services.html',
                      {'consumer': consumer, 'message': 'Not Available Data'})


def logout(request):
    return redirect('main')
