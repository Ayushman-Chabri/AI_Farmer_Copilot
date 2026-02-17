# 📁 Dataset Structure: `referrals`

## 📌 Overview
The **`referrals`** dataset stores region-specific helpline and support contacts for farmers.  
It enables the system to connect farmers with the correct government departments, support centers, or emergency assistance based on their needs and region.

This dataset works closely with the **policies** dataset and is used across all stages of farming.

---

## 🗂️ Structure
```python
profile_id      # System ID
region          # Region identification (e.g., odisha)

referrals[
    {
        referral_id: String
        display_name: String
        contact: String
        type: String
        purpose: String
    }
]
```
---

## 📊 Parameters

| Parameter                    | Key           | Type   | Example |
|-----------------------------|--------------|--------|--------|
| System ID for referral      | `referral_id` | String | `"agriculture_dept_odisha"` |
| Display Name                | `display_name`| String | `"Odisha Agriculture Department"` |
| Contact Number              | `contact`     | String | `"1551"` |
| Type                        | `type`        | String | `"state_animal_fisheries_support"` |
| Purpose                     | `purpose`     | String | `"Support for fisheries, livestock and poultry farmers"` |

Additional fields:

| Field        | Description |
|-------------|-------------|
| `profile_id` | Stores system ID |
| `region`     | Region associated with referral |

---

## 🎯 Purpose

In the final model, the **referral phase** will be used across all three farming stages:

### 🌱 Pre-Cropping Stage
- Connect farmers with:
  - Financial support offices  
  - Insurance providers  
  - Seed and subsidy centers  

### 🌾 Crop Growth Stage
- Provide contacts for:
  - Disease and pest support  
  - Irrigation assistance  
  - Veterinary and fisheries support  

### 🌽 Post-Harvest Stage
- Help farmers reach:
  - Procurement centers  
  - Storage facilities  
  - Market and pricing support  
  - Government purchase agencies  

This dataset will work in coordination with the **policies dataset** to ensure farmers can directly access relevant support.

The dataset is **region-referenced** and must be used with region context.  
It is **not an independent dataset**.

---

## ⚙️ Demo Constraints

For demonstration purposes:

- Only **10 referrals per region** will be included
- Limited to selected regions (example: Odisha)
- Contacts will represent key essential services only

---

## 🧠 Musings

**(12/02/2026 — Ayushman Chabri)**  
Musings same as Purpose.