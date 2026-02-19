from loaders.base_loader import load_json

def load_prices_data(region):
    '''
    Method to load prices
    '''
    return load_json(f"prices/{region.lower()}_prices.json")