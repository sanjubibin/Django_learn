from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

import json

# Create your views here.

class Index(View):
    def get(self, request):
        body_data: dict = json.loads(self.request.body.decode('utf-8'))
        return JsonResponse(body_data) # JsonResponse --> convert python dictionary to json response
    
    def post(self, request):
        body_data: dict = json.loads(self.request.body.decode('utf-8'))
        return JsonResponse(body_data)