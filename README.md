# Covid-Django

## Localhost webiste to find covid cases in any country.

## Steps to use it

1.Clone the repo where you want to keep it.

2.Install the python modules/packages requirments from requirments.txt.

```
pip install -r requiremnts.txt
```

3.Make an account on [rapidapi](https://rapidapi.com/).

4.Go to [api](https://rapidapi.com/api-sports/api/covid-193) and copy the api key from code snippet for python.

5.In the 'covidapp' folder ,in 'config.py' and paste key with variable name 'api_key' or use store key with environment variable with accordingly.

6.Change terminal or cmd path to the directory 'Covid_tracker' folder inside the repo.

7.Run the following command

```
python manage.py runserver
```

8.Go to localhost:8000 or 127.0.0.1:8000 at your browser.
