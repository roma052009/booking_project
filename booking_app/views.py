from django.shortcuts import render
from booking_app.models import User, Place, Reservation
from django.shortcuts import redirect

def log_in(request):
    return render(request, 'log_in.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        # dob = request.POST.get('dob')
        
        user = User.objects.create(username=username, password=password)#, dob=dob
        return redirect('places_list')
    
    return render(request, 'sign_up.html')

def places_list(request):
    places = Place.objects.all()
    return render(request, 'places_list.html', {'places': places})

def booking(request):
    return render(request, 'booking.html')
