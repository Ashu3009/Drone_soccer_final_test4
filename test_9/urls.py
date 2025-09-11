from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panel, name='admin_panel'),
    path('admin/', views.admin_panel, name='admin_panel_alt'),
    path('v1/', views.scoreboard_display, name='scoreboard'),
    path('v2/', views.video_display, name='video_display'),
]