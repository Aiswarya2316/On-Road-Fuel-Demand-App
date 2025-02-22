from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm, StafRegistrationForm, AdminRegistrationForm, DeliveryBoyRegistrationForm
from django.contrib import messages

def customer_register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer registered successfully! Please log in.")
            return redirect('user_login')  # Redirect to login page
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customer/register.html', {'form': form, 'title': 'Customer Registration'})

def staf_register(request):
    if request.method == 'POST':
        form = StafRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Staff registered successfully! Please log in.")
            return redirect('user_login')  # Redirect to login page
    else:
        form = StafRegistrationForm()
    return render(request, 'staf/register.html', {'form': form, 'title': 'Staff Registration'})

def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Admin registered successfully! Please log in.")
            return redirect('user_login')  # Redirect to login page
    else:
        form = AdminRegistrationForm()
    return render(request, 'admin/register.html', {'form': form, 'title': 'Admin Registration'})

def deliveryboy_register(request):
    if request.method == 'POST':
        form = DeliveryBoyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Delivery Boy registered successfully! Please log in.")
            return redirect('user_login')  # Redirect to login page
    else:
        form = DeliveryBoyRegistrationForm()
    return render(request, 'deliveryboy/register.html', {'form': form, 'title': 'Delivery Boy Registration'})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer, Staf, AdminReg, Deliveryboy

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_type = request.POST.get('user_type')  # Get user type from the form

        user = None  # Initialize user variable

        if user_type == "customer":
            user = Customer.objects.filter(email=email).first()
        elif user_type == "staff":
            user = Staf.objects.filter(email=email).first()
        elif user_type == "admin":
            user = AdminReg.objects.filter(email=email).first()
        elif user_type == "deliveryboy":
            user = Deliveryboy.objects.filter(email=email).first()

        if user and user.password == password:  # Basic password check (Replace this with Django authentication)
            messages.success(request, f"{user_type.capitalize()} logged in successfully!")
            request.session['user_id'] = user.id  # Store user ID in session
            request.session['user_type'] = user_type  # Store user type in session
            return redirect(f'{user_type}home')  # Redirect to respective dashboard
        else:
            messages.error(request, "Invalid email or password!")

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')  # Redirect to homepage


def home(request):
    return render(request,'home.html')



def adminhome(request):
    return render(request,'admin/adminhome.html')



def customerhome(request):
    return render(request,'customer/customerhome.html')



def deliveryboyhome(request):
    return render(request,'deliveryboy/deliveryboyhome.html')








from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FuelStationForm
from .models import FuelStation

def add_fuel_station(request):
    if request.method == "POST":
        form = FuelStationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Fuel station added successfully!")
            return redirect('fuel_station_list')
    else:
        form = FuelStationForm()
    return render(request, 'admin/add_fuel_station.html', {'form': form})





def fuel_station_list(request):
    """View to list all fuel stations"""
    stations = FuelStation.objects.all()
    return render(request, 'admin/fuel_station_list.html', {'stations': stations})






def viewusers(request):
    usrs=Customer.objects.all()
    return render(request,'admin/viewusers.html',{'usrs':usrs})
