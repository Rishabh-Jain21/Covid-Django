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
    mylist = []
    noofresult = int(response['results'])
    for x in range(noofresult):
        mylist.append(response['response'][x]['country'])
    if request.method == "POST":
        selectedcountry = request.POST['selectedcountry']
        print(selectedcountry)
        for x in range(0, noofresult):
            if selectedcountry == response['response'][x]['country']:
                print(response['response'][x]['cases'])
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total)-int(active)-int(recovered)
        context = {'mylist': mylist, 'selectedcountry': selectedcountry, 'new': new, 'active': active, 'critical': critical,
                   "recovered": recovered, 'total': total, "deaths": deaths}

        return render(request, 'helloworld.html', context)
    context = {'mylist': mylist}
    return render(request, 'helloworld.html', context)
