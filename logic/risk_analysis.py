from logic.rules import (
    INITIAL_CONFIDENCE,
    W_SOIL_MISMATCH,
    W_RAINFALL_MISMATCH,
    W_TEMP_MISMATCH,
    W_TOPOGRAPHY_MISMATCH,
    W_SEASONAL_RISK,
    MIN_CONFIDENCE
)


def analyze_crop(crop_id, district, season, context):
    """
    Main crop analysis function.

    Inputs:
        crop_id (str)
        district (str)
        season (str)
        context (dict)

    Returns:
        report (dict)
    """
    season = season.lower()

    confidence = INITIAL_CONFIDENCE
    suggestions = []
    warnings = []

    # -------------------------------
    # Load crop + location data
    # -------------------------------
    crop_data = next(
        (c for c in context["crops"]["crops"] if c["crop_id"] == crop_id),
        None
    )

    if not crop_data:
        return {"error": "Crop not found in database"}

    district_data = context["locations"]["districts"].get(district)

    if not district_data:
        return {"error": "District not found in database"}

    dominant_soil = district_data["dominant_soil"]

    # -------------------------------
    # 1. Soil Matching
    # -------------------------------
    if dominant_soil not in crop_data["suitable_soils"]:
        confidence -= W_SOIL_MISMATCH
        warnings.append("Soil type is not ideal for this crop.")

        soil_profile = context["soil"]["soil_types"].get(dominant_soil)

        if soil_profile:
            retention = soil_profile["water_retention"]

            suggestions.append(
                f"Soil water retention is {retention}. Consider irrigation or soil improvement techniques."
            )

    # -------------------------------
    # 2. Rainfall Matching
    # -------------------------------
    rainfall_data = district_data.get("rainfall_level")

    # Case 1: rainfall is stored season-wise (dictionary)
    if isinstance(rainfall_data, dict):
        region_rainfall = rainfall_data.get(season.capitalize())

    # Case 2: rainfall is stored directly (string)
    elif isinstance(rainfall_data, str):
        region_rainfall = rainfall_data

    # Case 3: Missing rainfall info
    else:
        region_rainfall = None


    if region_rainfall != crop_data["rainfall_range"]:
        confidence -= W_RAINFALL_MISMATCH
        warnings.append("Rainfall level mismatch detected.")

        if region_rainfall == "low":
            suggestions.append("Arrange irrigation support (PMKSY scheme recommended).")

    # -------------------------------
    # 3. Temperature Matching
    # -------------------------------
    if crop_data["temperature_pref"] not in district_data["temperature_band"]:
        confidence -= W_TEMP_MISMATCH
        warnings.append("Temperature conditions may not be optimal.")

    # -------------------------------
    # 4. Topography Matching
    # -------------------------------
    topo = district_data["land_topography"]

    if topo not in crop_data["topography"]:
        confidence -= W_TOPOGRAPHY_MISMATCH
        warnings.append("Topography mismatch: crop may face growth stress.")

    # -------------------------------
    # 5. Seasonal Risk Check
    # -------------------------------
    season_risks = context["weather"]["season_profiles"][season]["common_risks"]

    if season_risks:
        confidence -= W_SEASONAL_RISK
        warnings.append("Seasonal risks exist in this region.")

    # Confidence clamp
    confidence = max(confidence, MIN_CONFIDENCE)

    return {
        "crop": crop_data["display_name"],
        "district": district,
        "confidence": confidence,
        "warnings": warnings,
        "suggestions": suggestions,
        "seasonal_risks": season_risks
    }
