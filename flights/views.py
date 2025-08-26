from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.shortcuts import render, redirect
from .models import Flight
from django.urls import reverse_lazy
from django.db.models import Count, Avg

class homePageView(TemplateView):
    template_name = 'home.html'


class registerFlight(CreateView):
    model = Flight
    fields = ["name", "type", "price"] 
    template_name = "register.html"
    success_url = reverse_lazy("home")


class listFlight(ListView):
    model = Flight
    template_name = "list.html"
    context_object_name = "flights"

    
    def get_queryset(self):
        return Flight.objects.all().order_by("price")


class statsFlights(TemplateView):
    template_name = "stats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        count_nacionales = Flight.objects.filter(type="Nacional").count()
        count_internacionales = Flight.objects.filter(type="Internacional").count()

        avg_nacionales = Flight.objects.filter(type="Nacional").aggregate(Avg("price"))["price__avg"]

        context["count_nacionales"] = count_nacionales
        context["count_internacionales"] = count_internacionales
        context["avg_nacionales"] = avg_nacionales if avg_nacionales else 0

        return context
