from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from Rest_API import views

urlpatterns = [
    # Other URL patterns
    path('upload-image/', views.upload_image, name='upload_image'),
    path('media/<str:filename>', views.serve_image, name='serve_image'),
    path('media/<str:type>/<str:filename>', views.serve_image, name='serve_image')
]
