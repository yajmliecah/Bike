from ..models import Item, Brand, Edition
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView


class CategoryListView(ListView):
    model = Item
    context_object_name = 'category'
    
    def __init__(self, **kwargs):
        super(CategoryListView, self).__init__(**kwargs)
        
        self.car = Item.get_car()
        self.motorcycle = Item.get_motorcycle()
        self.vehicle = Item.get_vehicle()
        
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['car'] =    self.car
        context['motorcycle'] = self.motorcycle
        context['vehicle'] = self.vehicle
        
        return context
 
 
class CarListView(CategoryListView):
    
    template_name = 'bike/car_list.html'
    context_object_name = 'car'
    
    def get(self, request, *args, **kwargs):
        car = Item.get_car()
        
        return super(CarListView, self).get(request, car=car, *args, **kwargs)
    
    
class MotorcycleListView(CategoryListView):
    template_name = 'bike/motorcycle_list.html'
    context_object_name = 'motorcycle'
    
    def get(self, request, *args, **kwargs):
        motorcycle = Item.get_motorcycle()
        
        return super(MotorcycleListView, self).get(request, motorcycle=motorcycle, *args, **kwargs)
    
    
class VehicleListView(CategoryListView):
    template_name = 'bike/vehicles_list.html'
    context_object_name = 'vehicle'
    
    def get(self, request, *args, **kwargs):
        vehicle = Item.get_vehicle()
        
        return super(VehicleListView, self).get(request, vehicle=vehicle, *args, **kwargs)