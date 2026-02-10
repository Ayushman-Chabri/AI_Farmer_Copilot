from loaders.base_loader import load_json

def load_region_data():
    """
    Loads district-wise crop recommendation mapping.
    """
    return load_json("location/locations.json")
