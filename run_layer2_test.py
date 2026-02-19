from logic.context_builder import build_context
from logic.risk_analysis import analyze_crop

# -------------------------------
# DEMO TEST INPUT
# -------------------------------

region = "odisha"
district = "Koraput"
crop_id = "ragi"
season = "rabi"

# -------------------------------
# Load context bundle
# -------------------------------

context = build_context(region)

# -------------------------------
# Run Layer 2 analysis
# -------------------------------

report = analyze_crop(
    crop_id=crop_id,
    district=district,
    season=season,
    context=context
)

# -------------------------------
# Print Output
# -------------------------------

print("\n===== LAYER 2 OUTPUT =====\n")

print("Crop:", report["crop"])
print("District:", report["district"])
print("Confidence Score:", report["confidence"])

print("\n--- Warnings ---")
for w in report["warnings"]:
    print("•", w)

print("\n--- Suggestions ---")
for s in report["suggestions"]:
    print("•", s)

print("\n--- Seasonal Risks ---")
for r in report["seasonal_risks"]:
    print("•", r)

print("\n==========================\n")
