from django.http import JsonResponse

def api_view(request):
    return JsonResponse({"message": "¡Hola desde Django!"})
