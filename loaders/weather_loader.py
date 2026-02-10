from loaders.base_loader import load_json


def load_weather_data():
    """
    Loads district-wise rainfall + temperature data for Odisha.
    """
    return load_json("weather/odisha_weather.json")
