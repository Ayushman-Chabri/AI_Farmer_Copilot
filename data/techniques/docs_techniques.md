# 📁 Dataset Structure: `techniques`

## 📌 Overview
The **`techniques`** dataset stores recommended cropping and farming techniques that help farmers achieve better yield and reduce risks.

Each technique is associated with a specific crop and provides guidance on when and why it should be used.  
This dataset will be used by the AI system to recommend preventive and corrective farming methods.

---

## 🗂️ Structure
```python
profile_id      # System ID

techniques{
    crop_name{
        {
            technique_id: String
            display_name: String
            use_when: List
            purpose: String
            risk_reduction: List
        },
        {
            # Same structure repeated
        }
    }
}
```
---

## 📊 Parameters

| Parameter                   | Key              | Type   | Example |
|-----------------------------|------------------|--------|--------|
| System ID for technique     | `technique_id`   | String | `"alternate_wetting_drying"` |
| Display Name                | `display_name`   | String | `"Alternate Wetting and Drying"` |
| When to use                 | `use_when`       | List   | `["water_scarcity", "excess_water_retention"]` |
| Purpose                     | `purpose`        | String | `"Optimize water usage and reduce waterlogging risk"` |
| Risk reduction              | `risk_reduction` | List   | `["fungal_disease", "nutrient_leaching"]` |

Additional field:

| Field        | Description |
|-------------|-------------|
| `profile_id` | System identifier for dataset |

---

## 🎯 Purpose

In the final model, the **techniques dataset** will be used at multiple stages of farming to guide farmers toward better yield and risk prevention.

### 🌱 Pre-Cropping Stage
- Used after initial crop planning discussion  
- Suggest preventive techniques before sowing  
- Reduce risks from the beginning of cultivation  

### 🌾 Crop Growth Stage
- Used repeatedly during crop growth  
- Activated when farmer reports an issue  
- Integrated with computer vision model:
  - Detect disease or crop issue  
  - Suggest relevant techniques as remedy  

### 🧠 Smart Guidance
Each technique is:
- Crop-specific  
- Risk-specific  
- Situation-aware  

This dataset is **crop-referenced** and not independent.  
It must always be used with crop context.

---

## ⚙️ Demo Constraints

For demonstration purposes:

- Only **2 techniques per crop** will be included
- Limited crops will be supported
- Simplified use-case mapping will be used

---

## 🧠 Musings

**(12/02/2026 — Ayushman Chabri)**  
Musings same as Purpose.