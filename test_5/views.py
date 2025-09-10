from django.shortcuts import render

def admin_view(request):
    return render(request, 'test_5/admin.html')

def viewer_view(request):
    return render(request, 'test_5/viewer.html')
