# 📁 Dataset Structure: `soil`

## 📌 Overview
The **`soil`** dataset stores region-specific soil information and characteristics.  
It helps the system determine whether a particular crop is suitable for the soil available in a farmer’s location.

This dataset works alongside the **location/region dataset** and crop database to provide accurate crop suitability recommendations.

---

## 🗂️ Structure
```python
profile_id      # System ID
region          # Region selector (e.g., odisha)

soil_type{
    water_retention: String
    drainage: String
    fertility_level: String
    common_risks: List
}
```
---

## 📊 Parameters

| Parameter         | Key               | Type   | Example |
|------------------|------------------|--------|--------|
| Water retention  | `water_retention` | String | `"high_moderate"` |
| Drainage         | `drainage`        | String | `"moderate"` |
| Fertility level  | `fertility_level` | String | `"high"` |
| Common risks     | `common_risks`    | List   | `["cracking", "waterlogging"]` |

Additional fields:

| Field        | Description |
|-------------|-------------|
| `profile_id` | System identifier |
| `region`     | Region associated with the soil type |

---

## 🎯 Purpose

In the final model, this dataset will be used to:

- Identify soil characteristics based on farmer location
- Match soil properties with crop requirements
- Check if selected crop is suitable for local soil
- Warn farmers if crop–soil mismatch exists
- Suggest better crop alternatives if required

### 🧠 Workflow Logic

1. Farmer provides:
   - Location  
   - Crop choice  

2. System determines:
   - Region and soil type from dataset  
   - Soil attributes (fertility, drainage, etc.)  

3. AI compares:
   - Crop requirements vs soil attributes  

4. Output:
   - Suitability confirmation  
   - Risk warnings  
   - Alternative crop suggestions  

This dataset is **region-referenced** and must be used with region/location data.  
It is **not an independent dataset**.

---

## ⚙️ Demo Constraints

For demonstration purposes:

- Only limited soil types per region will be included
- Crop compatibility will be tested for **up to 15 crops**
- Simplified soil attributes will be used

---

## 🧠 Musings

**(12/02/2026 — Ayushman Chabri)**  
Musings same as Purpose.