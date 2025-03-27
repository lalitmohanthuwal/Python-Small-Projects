from flask import Flask, render_template, request
import json
import urllib.request
import os


    
app = Flask(__name__)

# Route for the main weather function
@app.route('/', methods=['POST', 'GET'])
def weather():
    # Default city
    city = 'Noida'
    
    if request.method == 'POST':
        city = request.form.get('city', 'Noida')  # Fallback to 'Noida' if no city provided

    # Retrieve API key from environment variable
    api_key = '4ab8820cdb16e847d5c3a030fba50889'
    if not api_key:
        return "Error: API key not set. Please set the OPENWEATHER_API_KEY environment variable."

    try:
        # Fetch data from OpenWeatherMap API
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        source = urllib.request.urlopen(url).read()
        
        # Parse JSON data
        list_of_data = json.loads(source)
        
        # Prepare data to pass to the template
        data = {
            "city": city,
            "country_code": str(list_of_data.get('sys', {}).get('country', 'N/A')),
            "coordinate": f"{list_of_data.get('coord', {}).get('lon', 'N/A')} {list_of_data.get('coord', {}).get('lat', 'N/A')}",
            "temp": f"{list_of_data.get('main', {}).get('temp', 'N/A')} C",
            "pressure": list_of_data.get('main', {}).get('pressure', 'N/A'),
            "humidity": list_of_data.get('main', {}).get('humidity', 'N/A'),
        }
    except urllib.error.HTTPError as e:
        # Handle HTTP errors
        data = {"error": f"HTTP Error: {e.code}"}
    except urllib.error.URLError:
        # Handle URL errors (e.g., network issues)
        data = {"error": "Unable to connect to the weather service."}
    except (KeyError, ValueError):
        # Handle JSON parsing issues or missing keys
        data = {"error": "Invalid data received from the weather service."}

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
