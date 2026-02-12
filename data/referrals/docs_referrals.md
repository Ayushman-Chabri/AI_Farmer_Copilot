**The Folder Structure**
*referrals*-: This is the database for region specific help line contacts stored in the following manner-:
    profile_id      #System id
    region          #region identification
    referrals[
        {
            Parameter                 Key                Type                   Example
            System Id for referral    referral_id        String                 referral_id:"agriculture_dept_odisha"
            Display name              display_name       String                 display_name: "Odisha Agriculture Department"
            Contact number            contact            String                 contact:"1551"
            Type                      type               String                 type: "state_animal_fisheries_support"
            Purpose                   purpose            String                 purpose: "Support for fisheries, livestock and poultry farmers"
        }
    ]

    Purpose-: In the final model the referral phase will be used in all the three stages
    This will work largely in co-ordination with policies folder. This is also a region referenced
    file and hence is not independent

    Demo Constraint-: For the sake of demo, we have taken only 10 referrals per region

    Musings-:
    (12/02/2026)-: (Ayushman Chabri)-: Musings same as purpose