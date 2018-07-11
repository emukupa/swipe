from django.shortcuts import render

from . models import Food
# Create your views here.


def index(request):
    context = {"foods": Food.objects.all()}
    return render(request, 'foods/index.html', context)
