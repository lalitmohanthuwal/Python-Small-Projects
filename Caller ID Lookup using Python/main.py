import requests
from bs4 import BeautifulSoup

# Function to fetch data from a URL
def getdata(url):
    r = requests.get(url)
    return r.text

# Your API key
api_key = "http://api.openweathermap.org / data / 2.5 / weather?"  # Replace with a valid API key

# Phone number and country code
number = '9756738718'
country = 'IN'

# URL to validate phone number using the API
url = f"http://apilayer.net/api/validate?access_key={api_key}&number={number}&country_code={country}&format=1"

# Fetch and parse the data
htmldata = getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup)
response = requests.get(url)
print(response.status_code, response.text)
