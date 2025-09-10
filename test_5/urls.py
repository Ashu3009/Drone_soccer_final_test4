from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin'),
    path('viewer/', views.viewer_view, name='viewer'),
]
