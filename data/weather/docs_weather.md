**The Folder Structure**
*weather*-: This database stores information about weather and it's allied factors in the following format-:
    profile_id     #This is used as the system id
    region         #This is used for identifying the region
    climate_zone   #This is used for calibrating the weather factors and season times
    season_profiles{
        season name:
            Parameters                 Key                  Type                    Example
            Period                     months               List                    months:["june","july","august"]
            Temperature range          temperature_band     String                  temperature_band:"warm_to_hot"
            Rainfall level             rainfall_level       String                  rainfall_level:"moderate"
            Humidity level             humidity_level       String                  humidity_level:"high"
            Common risks               common_risks         List                    common_risks:["flooding","waterlogging"]
    }

    extreme_event_patterns{     #Stores data about extreme events that happen in the region
        cyclone_prone
        drought_probability
        flood_probability
    }

    rainfall_classification_mapping{     #Assigns unique numerical categories to text categories
        .
        .
        .
    }

    temperature_classification_mapping{  #Assigns unique numerical categories to text categories
        .
        .
        .
    }

    Purpose-: In the final model this dataset will be used for accessing weather data for crops.
    This is a region bound data and hence is not independently accessible.

    Demo Constraint-: Nothing significant

    Musings-:
    (12/02/2026)-: I (Ayushman Chabri) believe that the farmer would input the crop name he wants to crop
    Then our system will access his location and soil profile. The weather directory would be accessed
    to determine the appropriate season and this will be confirmed from the farmer. If he disagrees then he will
    be warned about losses and given referrals. If he agrees further risks would be enumerated.
