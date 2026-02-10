from loaders.base_loader import load_json

def load_technique_data():
    """
    Loads crop-wise farming techniques.
    """
    return load_json("techniques/techniques.json")
