**The Folder Structure**
*diseases*-: This database stores information about all crop diseases in the following format-:
    crop_name  #This isn't a key for a string but key to a list
        Parameter                Key
        Disease ID               disease_id
        Name of disease          display_name
        Causing agent            disease_type
        Favorable conditions     favorable_conditions
        Early symptoms           early_symptoms
        Progression severity     severity_progression
        Risks                    associated_risks
    
    Purpose-: In the final model this will be used alongside computer vision to predict the disease and suggest further steps. This data set is defined with respect to a crop type and is not directly passed as an input by the user but is instead inferred by our model.So it is not completely independent

    Demo Constraints-: For the purpose of demo, we are taking only 2 diseases per crop

    Musings-: 
    (11/02/2026)-: As per my(Ayushman Chabri) current estimation in the computer vision model, we might have one aspect or layer to recognize the crop and another aspect/layer to  recognize the symptoms. Based on that our model may ask the user about favorable conditions or infer it from stored data(we might think about it later) and thereafter it can predict the disease category. Each layer would add some confidence to the disease type and based on it we can either suggest referral or further steps

