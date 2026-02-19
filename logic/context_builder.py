from loaders.crop_loader import load_crop_data
from loaders.locations_loader import load_locations_data
from loaders.soil_loader import load_soil_data
from loaders.weather_loader import load_weather_data
from loaders.policy_loader import load_policy_data
from loaders.technique_loader import load_technique_data
from loaders.referral_loader import load_referral_data
from loaders.prices_loader import load_prices_data
from loaders.nutrient_provision_loader import load_nutrient_provision_data


def build_context(region: str):
    """Returns:
        dict containing all datasets
    """

    crops = load_crop_data()
    locations = load_locations_data(region)
    soil = load_soil_data(region)
    weather = load_weather_data(region)

    national_policies, state_policies = load_policy_data(region)

    techniques = load_technique_data()
    referrals = load_referral_data(region)
    prices = load_prices_data(region)
    nutrients = load_nutrient_provision_data(region)

    return {
        "crops": crops,
        "locations": locations,
        "soil": soil,
        "weather": weather,
        "policies_national": national_policies,
        "policies_state": state_policies,
        "techniques": techniques,
        "referrals": referrals,
        "prices": prices,
        "nutrients": nutrients
    }
