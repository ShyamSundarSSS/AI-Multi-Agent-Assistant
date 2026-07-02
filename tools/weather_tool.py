import requests


def get_weather(city: str) -> str:
    """
    Fetches current weather information for a given city.
    """

    # -------------------------
    # Step 1: Get Latitude & Longitude
    # -------------------------

    geo_url = (
        f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    )

    geo_response = requests.get(geo_url).json()

    if "results" not in geo_response:
        return f"Could not find location: {city}"

    latitude = geo_response["results"][0]["latitude"]
    longitude = geo_response["results"][0]["longitude"]

    # -------------------------
    # Step 2: Get Weather
    # -------------------------

    weather_url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,"
        "relative_humidity_2m,"
        "wind_speed_10m"
    )

    weather = requests.get(weather_url).json()

    current = weather["current"]

    temperature = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    wind = current["wind_speed_10m"]

    return (
        f"Weather in {city}\n\n"
        f"Temperature : {temperature}°C\n"
        f"Humidity : {humidity}%\n"
        f"Wind Speed : {wind} km/h"
    )