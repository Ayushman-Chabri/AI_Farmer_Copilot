**The Folder Structure**
*techniques*-: This database is used to store the cropping techniques that can produce good yield in the following format-:
    profile_id    #Used as the system id
    techniques{
        crop name{
            {
                Parameter                     Key                  Type                   Example 
                System id for technique       technique_id         String                 technique_id:"alternate_wetting_drying"
                Display name                  display_name         String                 display_name:"Alternate Wetting and Drying"
                When to use                   use_when             List                   use_when:["water_scarcity","excess-water_retention"]
                Purpose                       purpose              String                 purpose:"Optimize water usage and reduce waterlogging risk"
                Whose risk is reduced         risk_reduction       List                   risk_reduction: ["fungal_disease", "nutrient_leaching"]
            }
            {
                Same set of values as above
            }
        }
    }

    Purpose-: In the final model this techniques file will be used once after pre-cropping 
    discussion(just before the farmer is about to sow the seeds) so that the farmer can 
    prevent risks from the very beginning. Then this can be used repeatedly during the cropping
    period whenever the farmer highlights some issue. Our computer vision model would
    identify the issue and our model will suggest remedies from the techniques folder. Here each
    technique is associated with a crop and hence it is not independent

    Demo Constraints-: For the purpose of demo we have taken only 2 techniques per crop

    Musings-:
    (12/02/2026)-:(Ayushman Chabri) The musings are same as the purpose
