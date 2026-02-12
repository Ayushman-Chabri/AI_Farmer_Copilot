**The Folder Structure**
*policies*-: This is the database that stores the national and regional policies for helping the farmers in the following format-:
national_policies.json
    profile_id    #System id
    policies[
        Parameter                   Key              Type                  Example
        Policy name(System id)      policy_id        String                policy_id: "pm_kisan_samman_nidhi"
        Policy name(display)        display_name     String                display_name: "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)"
        Category                    category         String                category: "Crop Insurance"
        Description                 description      String                description: "Provides direct income support to small and marginal farmers to help meet agricultural and domestic needs."
        Benefits                    benefits         List                  benefits: ["₹6,000 per year paid in three equal installments","Cash transfers directly to farmer bank accounts"]
        Eligibility                 eligibility      List                  eligibility: ["All small and marginal landholding farmers","Must have linked bank account and Aadhaar"]
        How to Apply?               application      String                application: "Apply on PM-KISAN portal or through Common Service Centres"
    ]
odisha_policies.json
    profile_id       #System id
    region           #region selector
    policies[
        #Same structure as national_policy.json
    ]

Purpose-: In our final model the policies folder will be used to guide in all stage of production
During precropping(just before the farmer sows the seeds) the system would evaluate the risk
and investment of the farmer to recommend insurance policies and easy money schemes
After sowing, our model can help with schemes related to irrigation,fertilizers and diseases
Post cropping our model may help with getting fair prices for the crops. Policies are also region specific and
not independent

Demo Constraints-:For the purpose of demo we are taking only 5 national schemes and 10 state schemes

Musings-:
(12/02/2026)-: (Ayushman Chabri) Musings same as purpose