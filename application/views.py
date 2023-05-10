from unicodedata import category

import data as data
from django.http import request
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import ListView, FormView
from .models import Table, Booking
from .forms import AvailabilityForm
from application.booking_functions.availability import check_availability


# Create your views here.

class TableList(ListView):
    model = Table


class BookingList(ListView):
    model = Booking

    def get_queryset(self):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            boking_list = Booking.objects.filter(user=self.request.user)
            return boking_list


class TableDetailView(View):
    def get(self):
        table_category = self.kwargs.get('category', None)
        # table_list = Table.objects.filter(category=category)
        table = table_category[0]
        context = {
            'table_category': table_category
        }
        return render(request, '', context)

    def post(self, request, *args, **kwargs):

        table_list = Table.objects.filter(category=category)

        available_tables = []
        for table in table_list:
            if check_availability(table, data['check_in', data['check_out']]):
                available_tables.append(table)
        if len(available_tables) > 0:
            table = available_tables[0]
            booking = Booking.objects.create(
                user=self.request.user,
                table=table,
                check_in=data['check_in'],
                check_out=data['check_out'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            HttpResponse('This category of rooms is booked. Try again later or change tables')


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        table_list = Table.objects.filter(category=data['table_category'])
        available_tables = []
        for table in table_list:
            if check_availability(table, data['check_in', data['check_out']]):
                available_tables.append(table)
        if len(available_tables) > 0:
            table = available_tables[0]
            booking = Booking.objects.create(
                user=self.request.user,
                table=table,
                check_in=data['check_in'],
                check_out=data['check_out'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            HttpResponse('This category of rooms is booked. Try again later or change tables')
