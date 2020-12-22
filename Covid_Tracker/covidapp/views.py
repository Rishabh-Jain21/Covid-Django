from django.shortcuts import render
import requests
# Create your views here.

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "d9cbda2f6dmshc2bba4bd0e71c1ap1ab42fjsnc01c43dd2e87",
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
