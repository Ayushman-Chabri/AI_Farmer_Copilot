from loaders.base_loader import load_json

def load_policy_data(region_in):
    '''
    Docstring for load_policy_data
    
    Method to Load in policies
    '''
    return load_json("policies/national_policies.json"), load_json(f"policies/{region_in.lower()}_policies.json")