from django.shortcuts import render, get_object_or_404
from .models import Youtuber
# Create your views here.

def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        "tubers": tubers
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_details(request, id):
    tube = get_object_or_404(Youtuber, pk=id)
    data = {
        "tube": tube
    }
    return render(request, 'youtubers/youtubers_detail.html', data)

def search(request):
    tubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(name__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)

    data = {
        "tubers": tubers,
        "city_search": city_search,
        "camera_type_search": camera_type_search,
        "category_search": category_search
    }

    for tube in tubers:
        print(tube.name)

    return render(request, 'youtubers/search.html', data)