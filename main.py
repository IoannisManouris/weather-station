import requests
import time

# The API that we'll use to fetch the weather (note that the following API is slow & sometimes down, but free)
api = "https://wttr.in"

# Fetch the user's local city in-case he doesn't manually input it
response = requests.get("https://ipinfo.io/json")
data = response.json()

local_city = data.get("city")
local_country = data.get("country")

temperature_unit = ("F" if local_country == "US" else "C")
weather_emojis = {"Sunny":"☀️", "Clear":"🌕", "Partly cloudy":"⛅", "Cloudy":"☁️", "Overcast":"☁️", "Mist":"🌫️", "Patchy rain possible":"🌦️", "Rain":"🌧️", "Heavy rain":"🌧️", "Thunderstorm":"⛈️", "Snow":"❄️", "Fog":"🌫️", "Windy":"💨"}

# Create a function for easy use and to avoid repeating code later on
def TrackCity(city):
    weather_json = requests.get(f"{api}/{city}?format=j1").json()
    weather_info = weather_json["current_condition"][0]
    weather_emoji = weather_emojis[weather_info["weatherDesc"][0]["value"]]

    title = f"\n---- {weather_emoji} {city.upper()} WEATHER INFORMATION {weather_emoji} ----"

    print(title)
    print(f"\n| Local time: {weather_info["localObsDateTime"]}")
    print(f"| Feels like: {weather_info[f"FeelsLike{temperature_unit}"]}{temperature_unit}°")
    print(f"| Humidity: {weather_info["humidity"]}%")

    hyphens = "-" * len(title)

    print(f"\n{hyphens}")

# Create a loop so that the user can check as many cities as he wants
while True:
    city = input("State the city that you'd like to check the weather to (\"local\" for your area, or \"exit\" to leave): ").strip().lower()
    
    if city == "exit": break
    if city == "local": city = local_city

    TrackCity(city)

    next_action = input(f"Send \"loop\" to track {city} in real-time, \"next\" to track another city, and \"exit\" to exit the program: ").replace(" ", "").lower()

    if next_action == "loop":
        while True:
            time.sleep(1)
            TrackCity(city)
    elif next_action == "next":
        continue
    elif next_action == "exit":
        break
    else:
        print("W.I.P.")