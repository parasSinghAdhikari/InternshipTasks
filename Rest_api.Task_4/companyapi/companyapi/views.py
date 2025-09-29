from django.http import HttpResponse,JsonResponse

def home_page(request):
    return JsonResponse(["home","agent"],safe=False)