confidenec:
Starting from 10 gives very low resolution:
A single mismatch drops score too quickly
Starting from 100 gives percentage-style clarity:
Confidence	Meaning
90–100	Highly suitable
70–90	Mostly suitable, some precautions
50–70	Risky crop choice
<50	Not recommended
--------------------
soill Mismatch
W_SOIL_MISMATCH = 30
Soil is the foundation of crop growth.
If soil is wrong:
nutrients fail
water retention becomes unstable
crop stress increases
So this gets the highest penalty.
----------------------------
Rainfall Mismatch
W_RAINFALL_MISMATCH = 25
Rainfall determines:
irrigation requirement
flood/drought probability
Wrong rainfall is a major yield killer.
So it has strong impact.
-----------------------
Temperature Mismatch
W_TEMP_MISMATCH = 10
Temperature matters, but districts usually fall into broad bands:
warm
warm_to_hot
So mismatch is less frequent.
Penalty is moderate.
---------------------------
Topography Mismatch
W_TOPOGRAPHY_MISMATCH = 15
Land shape affects:
drainage
waterlogging
root stability
Mismatch causes stress, but manageable with techniques.
So penalty is mid-level.
------------------
Seasonal Risk Penalty
W_SEASONAL_RISK = 20
Seasonal risks include:
floods
cold stress
fungal outbreaks
Even if soil/rainfall match…
seasonal threats still reduce confidence.
So penalty is high.

//low bar//
MIN_CONFIDENCE = 0
Why Needed?

Without this:
confidence could become negative
Example:
100 - 30 - 25 - 20 - 15 - 20 = -10
But confidence should never be negative.
hence
confidence = max(confidence, 0)
Policies applicable to all farmers must ALWAYS be shown.
insurance should NOT always appear.
But it must appear when:
seasonal risks exist
confidence drops below threshold
disease probability increases.