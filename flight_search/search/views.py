from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
import requests

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class SearchView(View):
     def post(self, request):
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        cabin = request.POST.get('cabin')

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }

        json_data = {
            'origin': 'SYD',
            'destination': 'JFK',
            'partnerPrograms': [
                'Air Canada',
                'United Airlines',
                'KLM',
                'Qantas',
                'American Airlines',
                'Etihad Airways',
                'Alaska Airlines',
                'Qatar Airways',
                'LifeMiles',
            ],
            'stops': 2,
            'departureTimeFrom': '2024-07-09T00:00:00Z',
            'departureTimeTo': '2024-10-07T00:00:00Z',
            'isOldData': False,
            'limit': 302,
            'offset': 0,
            'cabinSelection': [
                'Business',
            ],
            'date': '2024-07-09T12:00:17.796Z',
        }



        response = requests.post('https://cardgpt.in/apitest', headers=headers, json=json_data)
        
        # Check if the response is successful
        if response.status_code == 200:
            results = response.json()
        else:
            results = {'error': 'Failed to retrieve data'}

        return JsonResponse(results)
     
     