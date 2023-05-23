from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from Rest_API import views

urlpatterns = [
    # Other URL patterns
    path('upload-image/', csrf_exempt(views.upload_image), name='upload_image'),
]
