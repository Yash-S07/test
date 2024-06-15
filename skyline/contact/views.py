# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from .forms import ContactFormForm

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactFormForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'message': 'Form submitted successfully'})
#         else:
#             return JsonResponse({'errors': form.errors}, status=400)
#     else:
#         form = ContactFormForm()
#     return render(request, 'contact/contact_form.html', {'form': form})

# def index_view(request):
#     return render(request, 'contact/index.html')

# def login_view(request):
#     return render(request, 'contact/login.html')

# def profile_view(request):
#     return render(request, 'contact/profile.html')


# contact/views.py

from django.shortcuts import render,HttpResponseRedirect
from .forms import ContactFormForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactFormForm()
    return render(request, 'contact/contact_form.html', {'form': form})

def index_view(request):
    return render(request, 'contact/index.html')

def login_view(request):
    return render(request, 'contact/login.html')

def profile_view(request):
    return render(request, 'contact/profile.html')

def checkin_view(request):
    return render(request, 'contact/checkin.html')  

def manage_view(request):
    return render(request, 'contact/manage.html')

def flightstatus_view(request):
    return render(request, 'contact/flightstatus.html')


def contact_us_image(request):
    return render(request , 'contact/contact_us.jpg')