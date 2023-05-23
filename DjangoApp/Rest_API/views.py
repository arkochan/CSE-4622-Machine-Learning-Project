import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path
ML_DIR =os.path.join(Path(__file__).resolve().parent.parent.parent,'ML_Model')
import sys
sys.path.append(r'E:\ML_Project\ML_Model')

import callback
import os


@csrf_exempt
def upload_image(request):
    
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        file_path = os.path.join(settings.MEDIA_ROOT, 'images', image.name)
        #print(dir(request.FILES))
        with open(file_path, 'wb') as file:
            for chunk in image.chunks():
                file.write(chunk)
        
        
        #Runs ml init 
        outputImagePath = callback.callback_function(file_path)
        print(outputImagePath)

        if os.path.exists(outputImagePath):
            with open(outputImagePath, 'rb') as f:
                image_data = f.read()
        return HttpResponse(image_data, content_type='image/jpeg')
    if request.method == 'GET':
        return JsonResponse({'message':'Send image in a post request'})
    return JsonResponse({'error': 'Invalid request.'})
