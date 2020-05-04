from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    brand_d = Brand.objects.all()
    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    about = AboutUs.objects.all()
    chef = Chef.objects.all()
    
    context = {
        'brands': brand_d,
        'meal_list' : meal_list,
        'categories': categories,
        'about': about,
        'chef':chef,
        
    }
    return render(request,'index.html',context)