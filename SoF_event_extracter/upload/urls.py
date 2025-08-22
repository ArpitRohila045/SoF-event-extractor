from . import views
from django.urls import path

urlpatterns = [
    path('upload/', views.upload_sof, name='upload_sof'),
    path('success/', views.upload_success, name='upload_success'),
]