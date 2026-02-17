# 📁 Dataset Structure: `policies`

## 📌 Overview
The **`policies`** dataset stores national and regional government policies designed to support farmers.  
This dataset enables the AI system to recommend relevant schemes and policies to farmers at different stages of farming.

The folder contains two primary files:

- `national_policies.json`
- `odisha_policies.json` (example for regional/state policies)

---

## 🗂️ File Structure

### 🌐 `national_policies.json`

**Note:**  
`profile_id` is **System ID for national policies**.
```python
    policies[
        policy{
        policy_id: String
        display_name: String
        category: String
        description: String
        benefits: List
        eligibility: List
        application: String
    }
]
```

---

## 📊 Policy Parameters

| Parameter                  | Key            | Type   | Example |
|----------------------------|---------------|--------|--------|
| Policy name (System ID)    | `policy_id`   | String | `"pm_kisan_samman_nidhi"` |
| Policy name (Display)      | `display_name`| String | `"Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)"` |
| Category                   | `category`    | String | `"Crop Insurance"` |
| Description                | `description` | String | `"Provides direct income support to small and marginal farmers to help meet agricultural and domestic needs."` |
| Benefits                   | `benefits`    | List   | `["₹6,000 per year paid in three equal installments", "Cash transfers directly to farmer bank accounts"]` |
| Eligibility                | `eligibility` | List   | `["All small and marginal landholding farmers", "Must have linked bank account and Aadhaar"]` |
| How to Apply?              | `application` | String | `"Apply on PM-KISAN portal or through Common Service Centres"` |

---

## 🎯 Purpose

In the final model, the **policies folder** will guide the system at every stage of agricultural production:

### 🌱 Pre-Cropping Stage
- Evaluate farmer risk and investment capacity  
- Recommend:
  - Insurance schemes  
  - Subsidy programs  
  - Financial support schemes  

### 🌾 Post-Sowing Stage
- Suggest policies for:
  - Irrigation support  
  - Fertilizer subsidies  
  - Disease protection schemes  

### 🌽 Post-Harvest Stage
- Help farmers:
  - Get fair crop prices  
  - Access procurement schemes  
  - Find selling and storage support policies  

Policies are **region-specific** and must be matched with the farmer's state and district.

---

## ⚙️ Demo Constraints

For demonstration purposes:

- Only **5 national schemes** will be included
- Only **10 state schemes** will be included
- Regional focus will be limited (example: Odisha)

---

## 🧠 Musings

**(12/02/2026 — Ayushman Chabri)**  
Musings same as Purpose.