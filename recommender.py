from loaders.soil_loader import load_soil_data
from loaders.weather_loader import load_weather_data
from loaders.region_loader import load_region_data
from loaders.disease_loader import load_disease_data
from loaders.technique_loader import load_technique_data

from loaders.validation import validate_district


def recommend_full(district):
    soil_data = load_soil_data()
    weather_data = load_weather_data()
    region_data = load_region_data()

    disease_data = load_disease_data()
    technique_data = load_technique_data()

    # ✅ Validate district
    if not validate_district(district, soil_data):
        return f"❌ District '{district}' not found."

    # --- Get soil + rainfall ---
    soil_type = None
    rainfall = None
    crops = []

    for s in soil_data:
        if s["district"].lower() == district.lower():
            soil_type = s["soil_type"]

    for w in weather_data:
        if w["district"].lower() == district.lower():
            rainfall = w["avg_rainfall_mm"]

    for r in region_data:
        if r["district"].lower() == district.lower():
            crops = r["recommended_crops"]

    # --- Add diseases + techniques ---
    crop_details = []

    for crop in crops:

        # Find diseases
        diseases = []
        for d in disease_data:
            if d["crop"].lower() == crop.lower():
                diseases = [x["name"] for x in d["common_diseases"]]

        # Find techniques
        techniques = []
        for t in technique_data:
            if t["crop"].lower() == crop.lower():
                techniques = t["recommended_techniques"]

        crop_details.append({
            "crop": crop,
            "diseases": diseases,
            "techniques": techniques
        })

    return {
        "district": district,
        "soil_type": soil_type,
        "avg_rainfall_mm": rainfall,
        "recommended_crops": crop_details
    }
