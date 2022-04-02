import locale
from tempfile import template
from django.http import HttpResponse
from django.shortcuts import render
from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender
import random
import datetime
from .models import Customer, Product
from django.views.generic import ListView, TemplateView

class CustomerListView(ListView):
    model = Customer
    template_name = 'tables-data.html'
    context_object_name = 'customers'

class Test(TemplateView):
    template_name = 'forms-elements.html'

class ProductListView(ListView):
    model = Product
    template_name = 'tables-products.html'
    context_object_name = 'products'

def generate(request, count):
    birth_start_date = datetime.date(1955, 1, 1)
    birth_end_date = datetime.date(1997, 1, 1)
    
    request_start_date = datetime.date(2021, 1, 1)
    request_end_date = datetime.date(2023, 1, 1)

    def get_male():
        person = Person(Locale.RU)
        return person.full_name(gender=Gender.MALE)

    def get_female():
        person = Person(Locale.RU)
        return person.full_name(gender=Gender.FEMALE)

    i = 0
    while i < count:
        list_gender_name = [get_male, get_female]
        name = random.choice(list_gender_name)()
        
        number = random.randint(1,50)
        sum = number * 50000
        
        birth_time_between_dates = birth_end_date - birth_start_date
        birth_days_between_dates = birth_time_between_dates.days
        birth_date = birth_start_date + datetime.timedelta(days=random.randrange(birth_days_between_dates))
        
        time_between_dates = request_end_date - request_start_date
        days_between_dates = time_between_dates.days
        request_date = request_start_date + datetime.timedelta(days=random.randrange(days_between_dates))

        status = random.randint(1,3)
        product_id = random.randint(1,5)

        new_customer = Customer(name=name, sum=sum, birth_date=birth_date, request_date=request_date, status=status, product_id=product_id)
        new_customer.save()

        i += 1

    return HttpResponse('Случайные данные сгенерированы!')