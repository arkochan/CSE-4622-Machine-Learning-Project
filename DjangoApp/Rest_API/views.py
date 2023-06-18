import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path
ML_DIR =os.path.join(Path(__file__).resolve().parent.parent.parent,'ML_Model')
import sys
sys.path.append(r'E:\ML_Project\ML_Model')
from PIL import Image

import callback
import utils

import os

dict = {} 

@csrf_exempt
def upload_image(request):
    print("POSTTT")
    if request.method == 'POST' and request.FILES.get('image'):
        qeuryDictionary = request.POST
        dict.clear
        image = request.FILES['image']
        file_path = os.path.join(settings.MEDIA_ROOT, 'images' ,image.name)
        dict[image.name] = qeuryDictionary
        # print(dict)
        #print(dir(request.FILES))
        with open(file_path, 'wb') as file:
            for chunk in image.chunks():
                file.write(chunk)
        return JsonResponse({'BaseImagePath':( image.name)})
    #     if os.path.exists(outputImagePath):
    #         with open(outputImagePath, 'rb') as f:
    #             image_data = f.read()
    #     return HttpResponse(image_data, content_type='image/jpeg')
    
    
    if request.method == 'GET':
        return JsonResponse({'message':'Send image in a post request'})

    return JsonResponse({'error': 'Invalid request.'})


from django.shortcuts import get_object_or_404

def serve_image(request, type, filename):
    #Runs ml init 
    points = dict[filename]
    outputFilepath=  callback.callback_function(filename,type,points = points)
    print("outputFilepath" , outputFilepath)

    if os.path.exists(outputFilepath):
        with open(outputFilepath, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/jpeg')
    else:
        return HttpResponse(status=404)
