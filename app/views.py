from django.shortcuts import render
from .models import Item

# Create your views here.


def index(request):
    item = Item.objects.all()
    context={
        "data":item
    }





    return render(request,"index.html" , context)