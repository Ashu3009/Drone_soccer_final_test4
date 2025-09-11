from django.shortcuts import render

def admin_panel(request):
    """Admin control panel"""
    return render(request, 'test_9/admin.html')

def scoreboard_display(request):
    """Scoreboard display page"""
    return render(request, 'v1.html')

def video_display(request):
    """Organization video display page"""
    return render(request, 'v2.html')