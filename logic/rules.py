

# Confidence starts at 100
INITIAL_CONFIDENCE = 100

# Penalty weights
W_SOIL_MISMATCH = 30
W_RAINFALL_MISMATCH = 25
W_TEMP_MISMATCH = 10
W_TOPOGRAPHY_MISMATCH = 15
W_SEASONAL_RISK = 20

# Minimum confidence allowed
MIN_CONFIDENCE = 0


# Universal policies that ALWAYS apply
UNIVERSAL_POLICIES = [
    "pm_kisan_samman_nidhi",
    "soil_health_card_scheme",
    "pradhan_mantri_krishi_sinchayee_yojana"
]

# Insurance is ALWAYS recommended if risk exists
INSURANCE_POLICY = "pradhan_mantri_fasal_bima_yojana"
