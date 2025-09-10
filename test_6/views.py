from django.shortcuts import render

def admin_view(request):
    return render(request, 'test_6/admin.html')

def viewer_view(request):
    return render(request, 'test_6/viewer.html')
