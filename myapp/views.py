# myapp/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Alert
import json

@csrf_exempt
def receive_alert(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        status = data.get('status')
        
        # Alert 객체 생성 및 저장
        Alert.objects.create(title=title, status=status)
        
        return JsonResponse({"message": "Alert received successfully"})
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)
