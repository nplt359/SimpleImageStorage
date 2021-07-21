from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('upload', views.uploadImage),
    path('deleteImage/<str:pk>', views.deleteImage, name='deleteImage'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)