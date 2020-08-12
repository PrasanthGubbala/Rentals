from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.template.context_processors import media
from app.models import ProviderDetails,Services

#main phase
def main(request):
    return render(request, 'main/main.html')

def provider_login(request):
    return render(request, 'main/provider_login.html')

def provider_login_check(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        provider = ProviderDetails.objects.get(email=email)
        if email == provider.email and password == provider.password:
            return render(request, 'provider/provider_home.html',{'provider':provider})
        elif email != provider.email:
            messages.error(request, 'Invalid Username')
            return redirect('provider_login')
        elif password != provider.password:
            messages.error(request, "Password did'nt match")
            return redirect('provider_login')
        else:
            messages.error(request, 'Invalid Username/Password')
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

#provider phase
def provider_profile(request):
    email = request.GET.get('email')
    provider = ProviderDetails.objects.get(email=email)
    return render(request,'provider/provider_profile.html',{'provider':provider})


def provider_home(request):
    email = request.GET.get('email')
    provider = ProviderDetails.objects.get(email=email)
    return render(request, 'provider/provider_home.html', {'provider': provider})

def add_service(request):
    email = request.GET.get('email')
    provider = ProviderDetails.objects.get(email=email)
    return render(request, 'provider/add_service.html', {'provider': provider})

def save_service(request):
    service_type = request.POST.get('service_type')
    rooms = request.POST.get('rooms')
    square_feets = request.POST.get('square_feets')
    price = request.POST.get('price')
    city = request.POST.get('city')
    area = request.POST.get('area')
    street = request.POST.get('street')
    door_no = request.POST.get('door_no')
    image = request.FILES['image']
    Services(service_type=service_type,rooms=rooms,square_feets=square_feets,price=price,city=city,
             area=area,street=street,door_no=door_no,image=image).save()
    messages.success(request,'House Details Are Uploaded Successfully')
    return redirect('provider_home')