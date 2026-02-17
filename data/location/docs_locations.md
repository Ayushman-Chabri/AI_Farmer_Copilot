# 📍 Location Database Structure

## 📁 Folder: `location`

This database stores soil and weather-related data for each **sub-region (district)** inside a region.<br>
It acts as an environmental reference layer for crop suitability and advisory.

### Structure

```python
profile_id      # System unique ID
region          # Region identifier

districts{
    district_name{

        dominant_soil       # Type of dominant soil
        rainfall_level      # Rainfall category
        temperature_band    # Temperature range category
        land_topography     # Topography of land

    }
}
```

### 📊 Parameter Details

|Parameter          |Key              |Type   |Example                        |
|-------------------|-----------------|-------|-------------------------------|
|Dominant Soil      |dominant_soil    |String |dominant_soil: "red_soil"      |
|Rainfall level     |rainfall_level   |String |rainfall_level: "moderate"     | 
|Temperature range  |temperature_band |String |temperature_band: "warm_to_hot"|
|Region topography  |land_topography  |String |land_topography: "undulating"  |

⸻

### 🎯 Purpose

1. In the final model, this database will function as the location intelligence layer.

2. It will be used to:
	- Identify farmer location using region/district
	- Provide suitable crop recommendations
	- Issue warnings for unsuitable crop choices
	- Support environmental compatibility checks (soil, rainfall, temperature, topography)

3. Key Characteristics:
	- Addressed using location name (region/district)
	- Works as a reference dataset for other modules
	- Not completely independent — used alongside crop and prediction systems

⸻

### ⚙️ Demo Constraints
- No strict demo constraints defined.
- Dataset can be expanded or reduced based on demo requirements.

⸻

## 💡 Musings & Model Vision

**(12/02/2026 — Ayushman Chabri)**  


1. Purpose and musings remain aligned.

2. This module will act as the core environmental decision layer of the system, enabling:
	- Smart crop selection guidance
	- Region-specific farming insights
	- Early warnings before cultivation decisions

3. It will serve as the foundation for making the AI farming assistant context-aware and practical for real-world usage.