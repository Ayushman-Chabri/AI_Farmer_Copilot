**The Folder Structure**
*nutrient_provision*-: This is the database for storing details about when and what fertilizers and manure to provide in the following manner-:
    profile_id        #System id
    region            #region identifier
    unit_prices_note  #Metadata for prices per unit
    crops{
        crop name{
            Parameters               Key                     Type                          Example
            When to give manure?     manure_interval_days    Integer                       manure_interval_days: 25  
            When to give fertilizer? fetilizer_interval_days Integer                       fertilizer_interval_days: 30
            Recommended manure       recommended_manure      List of objects(name,price)   recommended_manure: [{"name": "Farm Yard Manure (FYM)","avg_price_per_ton": 1500}] 
            Recommended fertilizer   recommended_fertilizer  List of objects(name,price)   recommended_fertilizers: [{"name": "Urea","avg_price_per_45kg_bag": 266}]
            How to arrange?          affordable_arrangement  String                        affordable_arrangement: "Use composted FYM locally; apply split nitrogen doses to reduce wastage; avail subsidy via cooperative societies."

        }
    }

    Purpose-: In our final model this directory would be used especially during precropping
    where we would suggest the manure and fertilizer to the farmer based on the crop and his 
    desire to invest. Also the model would ask him/her to get that arranged by the specific date
    Within the cropping period also our system might require this dataset sometimes

    Demo Constraints-: For the purpose of demo, we have taken only a few manure and fertilizer for each crop

    Musings-:
    (12/02/2026)-: (Ayushman Chabri) Musings same as purpose