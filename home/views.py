from django.shortcuts import render
import requests
import json

def home(request):
  competitions = 'http://api.football-data.org/v4/competitions'
  headers = {'X-Auth-Token':'8aeff6991b114ca48fce34ed17ea547f'}
  response = requests.get(competitions, headers=headers)
  todos = json.loads(response.content)

  return render(request, 'home.html', {'competitions':todos['competitions']})