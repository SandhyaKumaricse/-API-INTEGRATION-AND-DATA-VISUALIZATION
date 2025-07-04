import requests
import matplotlib.pyplot as plt
import seaborn as sns


API_KEY = '6886dfdd9c004befaae2dc3e6842546c'
CITY = 'Jharkhand'
UNITS = 'metric' 

# Fetching data from OpenWeatherMap API
url = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&units={UNITS}&appid={API_KEY}'
response = requests.get(url)
data = response.json()

 
if response.status_code != 200 or 'list' not in data:
    print("Error fetching data from API:")
    print(data)
else:
    dates = []
    temperatures = []
    humidities = []

    
    for forecast in data['list']:
        dates.append(forecast['dt_txt'])
        temperatures.append(forecast['main']['temp'])
        humidities.append(forecast['main']['humidity'])

    # Data Visualization
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")

    # Plotting the temperature and humidity data using seaborn and matplotlib
    plt.subplot(2, 1, 1)
    sns.lineplot(x=dates, y=temperatures, marker='o', color='tomato')
    plt.title(f'Temperature Forecast for {CITY}')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()

   
    plt.subplot(2, 1, 2)
    sns.lineplot(x=dates, y=humidities, marker='o', color='skyblue')
    plt.title(f'Humidity Forecast for {CITY}')
    plt.ylabel('Humidity (%)')
    plt.xlabel('Date & Time')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Displaying the plots
    plt.show()
