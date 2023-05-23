import os
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_image(request):
    print(request.FILES)
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        file_path = os.path.join(settings.MEDIA_ROOT, 'images', image.name)
        #print(dir(request.FILES))
        with open(file_path, 'wb') as file:
            for chunk in image.chunks():
                file.write(chunk)
        
        return JsonResponse({'message': 'Image uploaded successfully.'})
    if request.method == 'GET':
        return JsonResponse({'message':'Send image in a post request'})
    return JsonResponse({'error': 'Invalid request.'})
