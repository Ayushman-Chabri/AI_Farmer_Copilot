from loaders.base_loader import load_json

def load_referral_data(region):
    '''
    Method to load referral data
    '''
    
    return load_json(f"referrals/{region.lower()}_referrals.json")
