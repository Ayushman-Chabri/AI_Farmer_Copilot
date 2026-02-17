# 📁 Dataset Structure: `prices`

## 📌 Overview
The **`prices`** dataset stores 25 years (1999–2023) of historical crop price data, including:

- Pre-cropping prices (before sowing)
- Post-cropping prices (after harvest)

This dataset is region- and crop-specific and will be used to help predict farmer profit/loss using regression models and financial estimation.

---

## 🗂️ Structure
```python
profile_id        # System ID
region            # Region selector (e.g., odisha)
unit              # Unit of crop pricing (e.g., per quintal)

crop_name{
    years: List
    pre: List
    post: List
}
```
---

## 📊 Parameters

| Parameter               | Key     | Type | Example |
|------------------------|---------|------|--------|
| Year                   | `years` | List | `[1999, 2000, ..., 2023]` |
| Pre-cropping prices    | `pre`   | List | `[1500, 1520, 1580, ..., 3000]` |
| Post-cropping prices   | `post`  | List | `[2400, 2480, 2100, ...]` |

Additional fields:

| Field        | Description |
|-------------|-------------|
| `profile_id` | Stores system ID for dataset |
| `region`     | Region associated with the price data |
| `unit`       | Price unit (e.g., per quintal, per kg) |

---

## 🎯 Purpose

In the final model, this dataset will be used along with regression and prediction models to:

- Estimate farmer investment
- Predict expected selling price
- Calculate profit or loss
- Warn farmers about risky crop choices
- Suggest better crop alternatives if required

This dataset is **not independent** and must always be referenced using:
- Region  
- Crop type  

---

## 🤖 Model Usage Logic (Planned)

### Step 1: Crop Selection
The system will ask:
- Which crop the farmer wants to grow
- Expected quantity of production

### Step 2: Investment Estimation
Using regression models:
- Estimate seed cost
- Estimate fertilizer & irrigation cost
- Allow farmer to input additional expenses

### Step 3: Profit/Loss Prediction
- Compare total investment with predicted post-cropping price
- Determine:
  - Expected profit  
  - Expected loss  
- Warn farmer if risk is high

### Step 4: Recommendation
- Suggest alternative crops if loss predicted
- Suggest policies or subsidies if needed

---

## ⚙️ Demo Constraints

For demonstration purposes:

- Only **25 years (1999–2023)** of data included
- Data is **synthetically generated**
- Assumptions used:
  - Gradual price increase due to inflation
  - Post-cropping price generally higher than pre-cropping price
  - Stable growth trend with limited volatility

---

## 🧠 Musings

**(12/02/2026 — Ayushman Chabri)**  

This model may use **two regression instances**:

1. **Investment Prediction Model**
   - Ask crop type and quantity
   - Predict seed and initial investment cost
   - Add farmer-provided additional expenses
   - Calculate total investment

2. **Profit/Loss Prediction Model**
   - Use historical post-cropping price data
   - Compare with total investment
   - Predict expected profit or loss

If required, randomness and volatility may be introduced into the dataset for more realistic predictions.