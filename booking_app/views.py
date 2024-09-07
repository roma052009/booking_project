from django.shortcuts import render
from booking_app.models import User, Place, Reservation
from django.shortcuts import redirect

def log_in(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = User.objects.get(name=name)

        if password == user.password:
            request.session['user_id'] = user.id
            return redirect('places_list')
    return render(request, 'log_in.html')

def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        birthday = request.POST.get('bd')

        user = User.objects.create(name=name, password=password, birthday=birthday)
        return redirect('places_list')
    
    return render(request, 'sign_up.html')

def places_list(request):
    places = Place.objects.all()
    return render(request, 'places_list.html', {'places': places})

def booking(request):
    return render(request, 'booking.html')
