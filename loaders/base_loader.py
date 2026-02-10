import json
import os

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "../data")


def load_json(relative_path):
    """
    Loads any JSON file from the data folder using relative path.
    Example: load_json("weather/odisha_weather.json")
    """

    filepath = os.path.join(DATA_FOLDER, relative_path)

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

load_json("weather/odisha_weather.json")