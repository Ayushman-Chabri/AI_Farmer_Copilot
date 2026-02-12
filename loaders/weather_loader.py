from loaders.base_loader import load_json


def load_weather_data(region):
    """
    Loads district-wise rainfall + temperature data for Odisha.
    """
    return load_json(f"weather/{region.lower()}_weather.json")
