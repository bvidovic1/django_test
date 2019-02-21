from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.utils.timezone import now
from carsapp.models import Car
from django.contrib import messages
from carsapp.forms import CarModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.template import loader
from django.template.context import Context


class IndexView(View):
    def get(self,request,*args,**kwargs):
        context = {
            'current_time': now()
        }
        return render(request, 'carsapp/index.html', context=context)

def post(self,request):
    pass

class CarListView(View):
    """
    View for displaying list of cars
    """
    def get(self, request, *args, **kwargs):
        cars_list = Car.objects.all()
        #context = {
        #    'cars': cars
        #}
        #return render(request, 'carsapp/car_list.html', context=context)

        paginator = Paginator(cars_list, 5)
        page = request.GET.get('page')
        cars = paginator.get_page(page)
        return render(request, 'carsapp/car_list.html', {'cars' : cars})

class CarListSearch(View):

    def get(self, request):
        query = request.GET['usr_query']
        if query:
            query_results = Car.objects.filter(title__icontains=query)
        else:
            query_results = Car.objects.all()
        return render(request, 'carsapp/car_search.html', {'query_results':query_results})

class CarDetailsView(View):
    """
    View for displaying car details.
    """
    def get(self, request, car_id):
        context = {}
        try:
            car = Car.objects.get(id=car_id)
            context['car'] = car
        except Car.DoesNotExist:
            messages.error(request,
                           'No car with id {}'.format(car_id))
        return render(request, 'carsapp/car_details.html', context=context)

class CarEditView(View):

    def get(self, request, car_id):
        context = {
            'req_car_id': car_id,
        }
        try:
            car = Car.objects.get(id=car_id)
            context['car'] = car
            context['form'] = CarModelForm(instance=car)
        except Car.DoesNotExist:
            messages.error(request,
                           'No car with id: {}'.format(car_id))

        return render(request, 'carsapp/car_edit.html', context=context)

    def post(self, request, car_id):
        context = {
            'req_car_id': car_id,
        }
        try:
            car = Car.objects.get(id=car_id)
            context['car'] = car
            car_form = CarModelForm(request.POST, instance=car)
            if car_form.is_valid():
                car_form.save()
                return HttpResponseRedirect(
                    reverse('cars:car_details', kwargs={'car_id': car_id}))
            context['form'] = car_form
        except Car.DoesNotExist:
            messages.error(request,
                           'No car with id: {}'.format(car_id))

        return render(request, 'carsapp/car_edit.html', context=context)

class CarDeleteView(View):

    def get(self, request, car_id):
        car = Car.objects.get(id=car_id)
        car.delete()
        return render(request, 'carsapp/car_delete.html')

class CarNewView(View):

    def get(self, request):
        context = {}
        context['form'] = CarModelForm()

        return render(request, 'carsapp/car_new.html', context=context)

    def post(self, request):
        context = {}
        car_form = CarModelForm(request.POST)
        if car_form.is_valid():
            car_form.save()
            return HttpResponseRedirect(
                reverse(
                    'cars:car_list'))
        context['form'] = car_form

        return render(request, 'carsapp/car_new.html', context=context)