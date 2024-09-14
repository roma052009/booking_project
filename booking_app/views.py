from django.shortcuts import render, get_object_or_404, redirect
from booking_app.models import User, Place, Reservation
from django.db.models import Q
from datetime import datetime

def log_in(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = User.objects.get(name=name)

        if password == user.password:
            request.session['user_id'] = user.id
            return redirect('places_list')
        else:
            return render(request, 'log_in.html', {'password_text': "Пароль невірний"})
    return render(request, 'log_in.html', {'password_text': ""})

def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        birthday = request.POST.get('bd')
        usernames = User.objects.values_list('name', flat=True)
        if name in usernames:
            return render(request, 'sign_up.html', {'name_text': "Користувач з цим іменем вже існує"})
        else:
            user = User.objects.create(name=name, password=password, birthday=birthday)
            request.session['user_id'] = user.id
            return redirect('places_list')
    
    return render(request, 'sign_up.html', {'name_text': ""})

def places_list(request):
    places = Place.objects.all()
    return render(request, 'places_list.html', {'places': places})

def booking(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'book':
            people = request.POST.get('people')
            date_from = request.POST.get('date_from')
            date_to = request.POST.get('date_to')

            if not people or not date_from or not date_to:
                return render(request, 'booking.html', {'place': place, 'error': 'Заповніть всі поля щоб забронювати'})

            from_date = datetime.strptime(date_from, '%Y-%m-%d').date()
            to_date = datetime.strptime(date_to, '%Y-%m-%d').date()

            conflicting_reservations = Reservation.objects.filter(Q(from_date__lte=to_date, to_date__gte=from_date), place=place)

            if conflicting_reservations.exists():
                return render(request, 'booking.html', {'place': place, 'error': 'В цей період часу вже є бронювання'})
            else:
                Reservation.objects.create(place=place, reservant=User.objects.get(id=request.session['user_id']), from_date=from_date, to_date=to_date)
                return render(request, 'booking.html', {'place': place, 'error': 'Бронювання успішно зроблено!'})

    return render(request, 'booking.html', {'place': place, 'looking_text': ""})
