from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json 
from models import Resturant

# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data['name']
        address = data['address']
        phone = data['phone']
        new_resto =  Resturant(name=name, address=address, phone_num = phone)
        new_resto.save()
        return HttpResponse("Added sucessfully")
    