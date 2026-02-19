from loaders.base_loader import load_json

def load_nutrient_provision_data(region):
    '''
    Docstring for load_nutrient_provision_data
    
    Method to call nutrient provision data
    

    '''
    return load_json(f"nutrient_provision/{region.lower()}_nutrient_provision.json")

    