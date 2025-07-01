from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'realtime/dashboard.html')  # Render หน้า dashboard
