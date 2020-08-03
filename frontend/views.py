from django.shortcuts import render


# Create your views here.
# Simple view to connect React to django URL configs.
def index(request):
    return render(request, "frontend/index.html")
