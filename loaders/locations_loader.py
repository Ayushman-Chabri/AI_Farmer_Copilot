import loaders.base_loader
from base_loader import load_json
def load_locations_data(region):
    '''
    Docstring for load_locations_data
    
    Method that calls location data 
    '''
    return load_json(f"location/{region.lower()}_locations.json")