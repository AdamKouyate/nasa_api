from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        api_key = 'wuHP1xtIcOXQMfpF98LbJRa8ZUOB4BQtzYlpRijr'
        url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}'
        response = requests.get(url)
        asteroids = response.json()
    return render(request, 'home.html', {'asteroids': asteroids})

def asteroid_detail(request, asteroid_id):
    api_key = 'wuHP1xtIcOXQMfpF98LbJRa8ZUOB4BQtzYlpRijr'
    url = f'https://api.nasa.gov/neo/rest/v1/neo/{asteroid_id}?api_key={api_key}'
    response = requests.get(url)
    asteroid = response.json()
    return render(request, 'asteroid_detail.html', {'asteroid': asteroid})
