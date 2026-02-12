**The Folder Structure**
*location*-: This database is used for storing soil and weather data for each sub region inside a region
    profile_id      #System id
    region          #region identifier
    districts{
        district name{
            Parameter          Key              Type                 Example
            Dominant Soil      dominant_soil    String               dominant_soil: "red_soil"
            Rainfall level     rainfall_level   String               rainfall_level: "moderate" 
            Temperature range  temperature_band String               temperature_band: "warm_to_hot"
            Region topography  land_topography  String               land_topography: "undulating"
        }
    }

    Purpose-: In the final dataset this would be used as a location pin-pointer of the farmer
    and based on it we can give cropping choices and warnings. This data is addressed using location
    name and may not be considered independent

    Demo Constraints-: Nothing as such

    Musings-:
    (12/02/2026)-: (Ayushman Chabri) Purpose same as musings