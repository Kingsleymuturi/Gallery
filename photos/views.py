from django.shortcuts import render
from .models import Image, Location


def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'photos/index.html', {'images': images[::-1], 'locations': locations})


def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'photos/location.html', {'location_images': images})

def image(request, image_id):
    try:
        image = Image.objects.get(id=image_id)
        print(image.category.id)
    except ObjectDoesNotExist:
        message = "Image does not exist or may have been deleted!"
        return render(request, 'image.html', {"message":message})
    return render(request, 'copy.html', {"image":image})


def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'photos/search_results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'photos/search_results.html', {"message": message})