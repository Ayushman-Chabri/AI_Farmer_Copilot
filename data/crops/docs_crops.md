**The Folder Structure**
    *crops*-: This database stores information about the top 15 most grown crops in Odisha in the following format-:
        Parameter         Key
        Crop Name         crop_id(for system), display_name(for viewers)
        Suitable Soil     suitable_soil
        Rain requirement  rainfall_range(Precise numbers create false confidence)
        Temperature range temperature_pref(Precise numbers create false confidence)
        Season            season
        SuitedTopography  topography
        additional        additional_senitivities

        Purpose-:
        Demo Constraints-: For the sake of demo, we don't take more than 15 crops. 
            