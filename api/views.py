from django.http import JsonResponse

def intj_api_view(request):
    data = {
        'message': 'This is my INTJ API.'
    }
    return JsonResponse(data)