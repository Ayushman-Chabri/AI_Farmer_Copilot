# 📁 Dataset Structure: `weather`

## 📌 Overview
The **`weather`** dataset stores region-specific weather and climate information along with seasonal patterns and extreme event risks.  
It helps the system determine the suitability of crops based on seasonal weather conditions and environmental risks.

This dataset is region-bound and must be accessed using the farmer’s location context.

---

## 🗂️ Structure
```python
profile_id                 # System ID
region                     # Region identification
climate_zone               # Climate classification for region

season_profiles{
    season_name{
        months: List
        temperature_band: String
        rainfall_level: String
        humidity_level: String
        common_risks: List
    }
}

extreme_event_patterns{
    cyclone_prone
    drought_probability
    flood_probability
}

rainfall_classification_mapping{
    …
}

temperature_classification_mapping{
    …
}
```
---

## 📊 Season Profile Parameters

| Parameter           | Key                 | Type   | Example |
|--------------------|--------------------|--------|--------|
| Period              | `months`           | List   | `["june","july","august"]` |
| Temperature range   | `temperature_band` | String | `"warm_to_hot"` |
| Rainfall level      | `rainfall_level`   | String | `"moderate"` |
| Humidity level      | `humidity_level`   | String | `"high"` |
| Common risks        | `common_risks`     | List   | `["flooding","waterlogging"]` |

---

## 🌪️ Extreme Event Patterns

Stores probability or presence of extreme climate events in a region:

| Field                 | Description |
|----------------------|-------------|
| `cyclone_prone`      | Indicates cyclone risk |
| `drought_probability`| Likelihood of drought |
| `flood_probability`  | Likelihood of floods |

---

## 🔢 Classification Mappings

### Rainfall Classification Mapping
Maps textual rainfall categories to numerical values for model usage.
```python
rainfall_classification_mapping{
    …
}
### Temperature Classification Mapping
Maps textual temperature bands to numerical values.
temperature_classification_mapping{
    …
}
```
These mappings help regression and prediction models process weather data efficiently.

---

## 🎯 Purpose

In the final model, this dataset will be used to:

- Determine suitable cropping season
- Evaluate climate suitability for crop
- Identify weather-related risks
- Warn farmers about extreme events
- Suggest alternative planning if risk is high

This dataset is **region-bound** and not independently accessible.

---

## 🧠 Workflow Logic (Planned)

1. Farmer inputs:
   - Crop name  

2. System determines:
   - Farmer location  
   - Soil profile  
   - Regional weather profile  

3. Weather dataset used to:
   - Identify suitable season  
   - Check climate compatibility  

4. Farmer confirmation:
   - If farmer agrees → Continue planning  
   - If disagrees → Warn about possible loss and risks  
   - Provide referrals if needed  

5. Risk analysis:
   - Enumerate climate risks  
   - Suggest preventive techniques  
   - Recommend policies if required  

---

## ⚙️ Demo Constraints

- No major constraints for demo
- Simplified seasonal and risk mapping may be used
- Limited regions supported

---

## 🧠 Musings

**(12/02/2026 — Ayushman Chabri)**  

The farmer will input the crop he wants to grow.  
The system will access location and soil profile, then determine the appropriate cropping season using weather data.  

- If farmer disagrees with suggested season → warn about potential losses and provide referrals  
- If farmer agrees → enumerate risks and continue planning  