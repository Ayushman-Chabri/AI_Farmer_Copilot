# 🦠 Disease Database Structure

## 📁 Folder: `Diseases`

This database stores structured information about all crop diseases.

**Note:**  
`crop_name` is **not a simple string key** but a key mapped to a **list of diseases associated with that crop**.

Each disease entry follows the format below:

| Parameter                | Key                     |
|--------------------------|-------------------------|
| Disease ID               | `disease_id`            |
| Name of Disease          | `display_name`          |
| Causing Agent            | `disease_type`          |
| Favorable Conditions     | `favorable_conditions`  |
| Early Symptoms           | `early_symptoms`        |
| Progression Severity     | `severity_progression`  |
| Risks                    | `associated_risks`      |

---

## 🎯 Purpose

In the final model, this database will be used alongside the **computer vision system** to:

- Predict crop diseases from visual input (leaf, stem, fruit images).
- Suggest next steps and preventive measures.
- Provide contextual disease information.

Key Characteristics:

- This dataset is defined **with respect to crop type**.
- It is **not directly provided by the user**.
- The model will **infer crop type and disease** using computer vision and stored data.
- Therefore, this dataset is **not completely independent** and works in combination with other modules.

---

## ⚙️ Demo Constraints

For demonstration purposes:

- Only **2 diseases per crop** will be included.
- This keeps inference simple and fast for demo presentation.

---

## 💡 Musings & Model Vision

**(12/02/2026 — Ayushman Chabri)**  

Current conceptual approach for the computer vision model:

1. Multi-layer Recognition System:
   - **Layer 1:** Recognize crop type  
   - **Layer 2:** Recognize visible symptoms  

2. After crop and symptoms detection:
   - Model may ask user about **favorable environmental conditions**  
   - Or infer them from stored environmental/location data *(to be explored later)*  

3. Disease Prediction Logic:
   - Each recognition layer contributes a **confidence score**
   - Combined confidence determines probable disease
   - Based on confidence level:
     - High confidence → Suggest treatment/prevention steps  
     - Medium confidence → Ask follow-up questions  
     - Low confidence → Recommend expert/agriculture officer referral  

This layered approach allows the system to act as a **practical AI farming assistant** rather than just a static classifier.