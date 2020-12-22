from .api_config import api_key
from django.shortcuts import render
import requests
# Create your views here.

url = "https://covid-193.p.rapidapi.com/statistics"
headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()


def helloworldview(request):

    noofresult = int(response['results'])
    mylist = []
    for x in range(noofresult):
        mylist.append(response['response'][x]['country'])
    context = {'mylist': mylist}
    return render(request, 'helloworld.html', context)
