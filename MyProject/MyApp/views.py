from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

import json

# Create your views here.

class Index(View):
    def get(self, request):
        # body_data: dict = json.loads(self.request.body.decode('utf-8'))
        return HttpResponse("Index Get Page!!!")
    
    def post(self, request):
        # body_data: dict = json.loads(self.request.body.decode('utf-8'))
        return HttpResponse("Index Post Page!!!")
    
    def put(self, request):
        return HttpResponse('Index Put Page!!!')
    
    def patch(self, request):
        return HttpResponse('Index Patch Page!!!')
    
    def delete(self, request):
        return HttpResponse('Index delete Page!!!')
    
class JsonResponseToFrontendIntegration(View):
    def get(self, request):
        data = {
            "January": ["Learn a new coding language", "Read 2 books", "Start a daily exercise routine"],
            "February": ["Celebrate Valentine's Day with a loved one (or yourself!)", 
                        "Complete a 28-day fitness challenge", 
                        "Declutter your home"],
            "March": ["Participate in a spring cleaning challenge", 
                        "Learn a new recipe each week", 
                        "Plant a garden"],
            "April": ["Write a poem or short story", 
                        "Take a daily nature walk", 
                        "Volunteer in your community"],
            "May": ["Practice gratitude every day", 
                        "Learn a new skill", 
                        "Spend time with friends and family"],
            "June": ["Go on a weekend getaway", 
                        "Try a new outdoor activity", 
                        "Read a book outside"],
            "July": ["Celebrate Independence Day (if applicable)", 
                        "Beat the heat with refreshing activities", 
                        "Learn about a new culture"],
            "August": ["Back-to-school prep (if applicable)", 
                        "Enjoy summer evenings outdoors", 
                        "Host a backyard barbecue"],
            "September": ["Celebrate fall with seasonal activities", 
                        "Start a new learning project", 
                        "Organize your workspace"],
            "October": ["Get ready for Halloween", 
                        "Read a spooky book", 
                        "Carve a pumpkin"],
            "November": ["Be thankful for what you have", 
                        "Help others in need", 
                        "Plan for the holidays"],
            "December": ["Celebrate the holidays with loved ones", 
                        "Reflect on the year and set goals for the next", 
                        "Enjoy some well-deserved rest and relaxation"]
            }
        return render(request, 'MyApp/JsonResponseToFrontendIntegration.html', {'data': data})

    def post(self, request):
        pass
        # data = {
        #     'key1': 'value1',
        #     'key2': 'value2',
        #     'key3': 'value3',
        # }
        # return JsonResponse(data)    
class Challenges(View):
    month_challenges = {
        "January": ["Learn a new coding language", "Read 2 books", "Start a daily exercise routine"],
        "February": ["Celebrate Valentine's Day with a loved one (or yourself!)", 
                    "Complete a 28-day fitness challenge", 
                    "Declutter your home"],
        "March": ["Participate in a spring cleaning challenge", 
                    "Learn a new recipe each week", 
                    "Plant a garden"],
        "April": ["Write a poem or short story", 
                    "Take a daily nature walk", 
                    "Volunteer in your community"],
        "May": ["Practice gratitude every day", 
                    "Learn a new skill", 
                    "Spend time with friends and family"],
        "June": ["Go on a weekend getaway", 
                    "Try a new outdoor activity", 
                    "Read a book outside"],
        "July": ["Celebrate Independence Day (if applicable)", 
                    "Beat the heat with refreshing activities", 
                    "Learn about a new culture"],
        "August": ["Back-to-school prep (if applicable)", 
                    "Enjoy summer evenings outdoors", 
                    "Host a backyard barbecue"],
        "September": ["Celebrate fall with seasonal activities", 
                    "Start a new learning project", 
                    "Organize your workspace"],
        "October": ["Get ready for Halloween", 
                    "Read a spooky book", 
                    "Carve a pumpkin"],
        "November": ["Be thankful for what you have", 
                    "Help others in need", 
                    "Plan for the holidays"],
        "December": ["Celebrate the holidays with loved ones", 
                    "Reflect on the year and set goals for the next", 
                    "Enjoy some well-deserved rest and relaxation"]
        }

    def get(self, request, month):
        months: tuple = tuple(self.month_challenges.keys())
        if month in months:
            Challenge = self.month_challenges[f"{month}"]
        else:
            Challenge = "enter the spelling of the month correctly!!!!!"

        return JsonResponse({"challenge": Challenge, "optional_months": months})