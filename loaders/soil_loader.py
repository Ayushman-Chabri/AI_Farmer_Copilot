from loaders.base_loader import load_json


def load_soil_data(region):
    """
    Loads soil type district-wise for Odisha.
    """
    return load_json(f"soil/{region.lower()}_soil.json")
