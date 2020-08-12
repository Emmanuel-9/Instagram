from django.shortcuts import render
from django.http import HttpResponse
from .models import Images,Profile

from django.utils import timezone


# Create your views here.
def home(request):
    return render(request,'base.html')

def images(request):
    images = Images.objects.all().filter(created_time__lte=timezone.now()).order_by('-created_time')
    return render(request,'images.html',{"images": images})    

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Images.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def profile(request):
    profiles = Profile.objects.all()
    return render(request,'profile.html',{"profiles": profiles})        

