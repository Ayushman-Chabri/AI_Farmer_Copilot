from loaders.base_loader import load_json

def load_region_data():
    """
    Loads region from data folder.
    """
    return load_json("metadata/regions.json")
