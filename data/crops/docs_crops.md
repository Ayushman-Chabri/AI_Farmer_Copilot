# 🌾 Crop Database Structure

## 📁 Folder: `Crops`

This database stores structured information about all supported crops.

Each crop entry follows the format below:

| Parameter            | Key                                                                       |
|----------------------|---------------------------------------------------------------------------|
| Crop Name            | `crop_id` (for system), `display_name` (for viewers)                      |
| Suitable Soil        | `suitable_soil`                                                           |
| Rain Requirement     | `rainfall_range` *(Avoid precise numbers to prevent false confidence)*    |
| Temperature Range    | `temperature_pref` *(Avoid precise numbers to prevent false confidence)*  |
| Season               | `season`                                                                  |
| Suited Topography    | `topography`                                                              |
| Additional Factors   | `additional_sensitivities`                                                |

---

## 🎯 Purpose

In the final model, this database will be used to fetch and display associated data for any selected crop.

- The crop data will be triggered by **user input** (crop name).
- This system will **not depend on external factors** for basic crop data retrieval.
- The model will use this database to evaluate crop suitability and provide intelligent feedback to farmers.

---

## ⚙️ Demo Constraints

For demonstration purposes:

- The system will support **up to 15 crops only**.
- This ensures faster processing, easier testing, and cleaner UI demonstration.

---

## 💡 Musings & Model Vision

**(12/02/2026 — Ayushman Chabri)**  

As envisioned:

1. The farmer will input the **crop they want to cultivate**.
2. Using the **location database**, the system will evaluate:
   - Soil suitability  
   - Rainfall compatibility  
   - Temperature conditions  
   - Topography  

3. If conditions are unsuitable:
   - ⚠️ The model will **warn the farmer** before planting.

4. Revenue Prediction System:
   - Using market price data, the model will estimate:
     - Expected revenue
     - Potential profit or loss
   - Farmer must input:
     - Fixed capital
     - Loans
     - Expenses  
   - If internet is available → live price prediction  
   - If offline → manual price input required

This approach ensures the farmer receives **practical, actionable insights** before cultivation begins.