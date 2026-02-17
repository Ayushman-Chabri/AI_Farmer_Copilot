## 📁 Folder Structure

### `nutrient_provision`
This database stores details about **when and what fertilizers and manure** should be provided to farmers.

### Structure
```python
nutrient_provision{
    profile_id        # System ID
    region            # Region identifier
    unit_prices_note  # Metadata for prices per unit

    crops{
        crop_name{
            manure_interval_days: 25,
            fertilizer_interval_days: 30,

            recommended_manure: [
                {"name": "Farm Yard Manure (FYM)", "avg_price_per_ton": 1500}
            ],

            recommended_fertilizers: [
                {"name": "Urea", "avg_price_per_45kg_bag": 266}
            ],

            affordable_arrangement: 
            "Use composted FYM locally; apply split nitrogen doses to reduce wastage; avail subsidy via cooperative societies."
        }
    }
}
```

### Parameters

| Parameter                     | Key                      | Type                           | Example |
|------------------------------|--------------------------|--------------------------------|--------|
| When to give manure?         | manure_interval_days     | Integer                        | manure_interval_days: 25 |
| When to give fertilizer?     | fertilizer_interval_days | Integer                        | fertilizer_interval_days: 30 |
| Recommended manure           | recommended_manure       | List of objects (name, price)  | `[{"name":"FYM","avg_price_per_ton":1500}]` |
| Recommended fertilizer       | recommended_fertilizers  | List of objects (name, price)  | `[{"name":"Urea","avg_price_per_45kg_bag":266}]` |
| Affordable arrangement guide | affordable_arrangement   | String                         | Cost-saving arrangement advice |

---

## 🎯 Purpose
In the final model, this dataset will be used mainly during the **pre-cropping stage**:

- Suggest manure and fertilizer based on selected crop  
- Recommend based on farmer investment capacity  
- Notify farmer to arrange inputs before required date  
- May also be used during cropping period when needed  

---

## ⚙️ Demo Constraints
For demo purposes, only a **limited number of manure and fertilizer options** are included for each crop.

---

## 🧠 Musings
**(12/02/2026 — Ayushman Chabri)**  

Musings same as Purpose.