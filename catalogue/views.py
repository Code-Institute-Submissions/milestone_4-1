from django.shortcuts import render
from .models import Catalogue, FullDocument

# Create your views here.

def total_catalogue(request):
    catalogue = Catalogue.objects.all()
    return render(request, "catalogue.html", {"catalogue": catalogue})

    