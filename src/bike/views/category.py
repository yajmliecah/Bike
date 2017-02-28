from ..models import Item
from django.shortcuts import render, get_object_or_404


def cars(request):
    cars = Item.objects.filter(category='CAR')
    return render(request, 'bike/cars.html', {'cars': cars})


def motors(request):
    motors = Item.objects.filter(category='MOTORCYCLE')
    return render(request, 'bike/motors.html', {'motors': motors})
    

def vehicles(request):
    vehicles = Item.objects.filter(category='VEHICLE')
    return render(request, 'bike/vehicles.html', {'vehicles': vehicles})