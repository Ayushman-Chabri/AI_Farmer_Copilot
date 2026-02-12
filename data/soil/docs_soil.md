**The Folder Structure**
    *soil*-: This database stores information about the soil types in the following format-:
    profile_id  #ID for system
    region      #For selecting region
    soil type {

        Parameter         Key                     Type                   Example
        Water retention   water_retention         String                 water_retention:"high_moderate"
        Drainage          drainage                String                 drainage:"moderate"
        Fertility level   fertility_level         String                 fertility_level:"high"
        Common risks      common_risks            List                   common_risks:["cracking","waterlogging"]
    }
        Purpose-: In the final model this will be used alongside location file to determine the soil 
        and various aspects related to it. The farmer will only give crop data and based on the crop
        database and the farmer's location we will check if the attributes of the particular soil
        available there are suitable for the crop. This soil type is referenced by region and hence
        is not independent.

        Demo Constraints-: For the sake of demo, we don't take more than 15 crops. 

        Musings-:
        (12/02/2026)-: I (Ayushman Chabri) musings same as purpose
            