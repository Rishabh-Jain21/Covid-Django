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


def covid_tracker_view(request):
    country_list = []
    no_of_results = int(response['results'])
    for x in range(no_of_results):
        country_list.append(response['response'][x]['country'])
    country_list.sort()
    if request.method == "POST":
        selected_country = request.POST['selected_country']

        for x in range(0, no_of_results):
            if selected_country == response['response'][x]['country']:

                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total)-int(active)-int(recovered)
                context = {'country_list': country_list, 'selected_country': selected_country, 'new': new, 'active': active, 'critical': critical,
                           "recovered": recovered, 'total': total, "deaths": deaths}
                return render(request, 'covid_tracker.html', context)
    context = {'country_list': country_list}
    return render(request, 'covid_tracker.html', context)
