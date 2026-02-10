from loaders.base_loader import load_json

def load_disease_data():
    """
    Loads crop-wise disease information.
    """
    return load_json("diseases/diseases.json")
