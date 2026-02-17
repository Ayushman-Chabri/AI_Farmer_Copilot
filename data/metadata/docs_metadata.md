# 📁 Dataset Structure: `regions`

## 📌 Overview
The **`regions`** dataset is primarily used to identify and manage Indian states within the system.  
It acts as an **umbrella dataset** that helps determine:

- Supported languages for each region
- Default language of a region
- Valid sub-regions (districts for demo)
- Region identity validation

This dataset will be used by the final model to verify whether a particular sub-region belongs to a region and to fetch language preferences.

---

## 🗂️ Structure
```python
profile_id      # System unique ID
region          # Region identifier

districts{
    district_name{

        dominant_soil       # Type of dominant soil
        rainfall_level      # Rainfall category
        temperature_band    # Temperature range
        land_topography     # Topography of land

    }
}
```

---

## 📊 Parameters

| Parameter                     | Key                 | Type   | Example                                  |
|------------------------------|--------------------|--------|------------------------------------------|
| Region name (System ID)      | `profile_id`       | String | `"odisha"`                               |
| Region name (Display Name)   | `display_name`     | String | `"Odisha"`                               |
| Preferred Languages          | `preferred_languages` | List   | `["en", "hi", "or"]`                     |
| Default Language             | `default_language` | String | `"or"`                                   |
| Sub-regions (Districts demo) | `locations`        | List   | `["Anugul", "Balangir", ..., "Sundargarh"]` |

---

## 🎯 Purpose

In the final model, this dataset will:

- Act as the **master region dataset**
- Identify supported languages for each region
- Provide default language selection
- Validate whether a sub-region belongs to a region
- Enable region-based AI responses and localization

---

## ⚙️ Demo Constraints

For demonstration purposes:

- Sub-regions will typically represent **districts**
- Only selected regions and districts may be included
- Language mapping will be limited to demo-supported languages

---

## 🧠 Musings

**(12/02/2026 — Ayushman Chabri)**  
Musings are same as Purpose.