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
        else:
            return render(request, 'log_in.html', {'password_text': "Password is incorrect"})
    return render(request, 'log_in.html', {'password_text': ""})

def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        birthday = request.POST.get('bd')
        usernames = User.objects.values_list('name', flat=True)
        if name in usernames:
            return render(request, 'sign_up.html', {'name_text': "User with this name already exists"})
        else:
            user = User.objects.create(name=name, password=password, birthday=birthday)
            request.session['user_id'] = user.id
            return redirect('places_list')
    
    return render(request, 'sign_up.html', {'name_text': ""})

def places_list(request):
    places = Place.objects.all()
    return render(request, 'places_list.html', {'places': places})

def booking(request):
    return render(request, 'booking.html')
