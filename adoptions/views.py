from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet
from django.http import Http404


def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})


def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        return Http404('pet not found')

    return render(request, 'pet_detail.html', {'pet': pet})
