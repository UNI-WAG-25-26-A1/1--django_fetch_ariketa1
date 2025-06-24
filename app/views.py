from django.http import JsonResponse
from django.shortcuts import render

def api_view(request):
    return JsonResponse({"message": "¡Hola desde Django!"})

def home_view(request):
    return render(request, 'index.html')
