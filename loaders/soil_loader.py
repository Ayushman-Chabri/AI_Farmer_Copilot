from loaders.base_loader import load_json


def load_soil_data():
    """
    Loads soil type district-wise for Odisha.
    """
    return load_json("soil/odisha_soil.json")
