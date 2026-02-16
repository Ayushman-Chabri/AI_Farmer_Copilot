**System Flow (Designed by Ayushman)**-:
    0. Access region
    [Edge Case-:Border District -> Handling-: Focus only on central areas during demo]
        0.1> Set Default Language
        0.2> Set District  (Location is hardcoded/GPS use)
        0.3> Initialize voice model and greet(In all preferred languages and proceed as per farmer input)
        0.4> Give options for Modes(pre-cropping/cropping/post-cropping)
        **If precropping**-:
        1. Collect all inputs
            1.1> Collect crop names
            [Edge Cases-:
            Crop is not available in the database | Handling-> Only focus on crops that are present during demo
            User's audio is not comprehendable-: Ask to repeat
            ]

            1.2> Collect Land area
            [Edge Cases-:
            Land area unit is comprehendable | Handling -> Gemma and only those units that we are sure that they exist
            If land area not provided or couldn't be extracted-> Ask to repeat
            ]
            1.3> Collect Investment (Past loans/debts, New fixed capital, purchase of seeds)
            [Edge Cases-: 
            If data not provided or missing-: Ask to repeat
            ]
            1.4> Collect when are you planning to crop (Month)
            [Edge Cases-:
            Month name in other language | Handling-> Gemma translates month into English]
            1.5>Collect Seed variety (HYV/Normal)
            1.6> Initialize the confidence to some arbitary value (Returnable value)
            (Confidence Arbitary value initialization-: 10)

            [Algorithm -: initial_confidence=10]

        2. Based on crop name
            2.1> Access the Crop Database

                [Algorithm-: 
                crop_data=crop_loader.py 
                ]

            2.2> Access the location Database

                [Algorithm-:
                crop_data=crop_loader.py 
                location_data=locations_loader.py]

            Match soil type 
               -If Matched-: Confidence unchanged
               -If not matched-: Confidence lowered by w1
                              -: Solution-:
                                           a> Check the soil's water rentention    *Add crop's required water retention*
                                              a.1>Match with crop's water retention
                                                  a.1.1> If equal- No suggestions here
                                                  a.1.2> If lesser-: Refer to techniques and irrigation
                                                  a.1.3> If higher-: Refer to techniques
                                           b>Check the common risks and warn the farmer
                [Algorithm-:
                if not location_data[dominant_soil] in crop_data[suitable_soils]:
                     soil_data=soil_loader.py
                     soil_data[location_data[dominant_soil]][water_retention]]
            Match rainfall level along with season in the location file
               -If matched-: Confidence unchanged
               -If not matched-: Confidence lowered by w2
                              -: Solution-:
                                          a>Check region's rainfall
                                            a.1> If lower-: Ask to arrange for irrigation
                                            a.2> If higher-: Refer to technique
            Match temperature level along with season in the location file
              -If matched-: Confidence unchanged
              -If not matched-: Confidence lowered by w3
                             -: Solution -:
                                        a> If higher-> Refer to techniques
                                        b> If lower refer to techniques
            Match topography-:
                -If matched-: Confidence unchanged
                -If not matched-: Confidence lowered by w3
                               -: Solution-: Refer to techniques
            Check for threats through risk and match with season-:        *Add seasonal risks to locations*
                -If risks exist-: Confidence lowered by w4
                               -: Refer to insurance policies    
                -If not-: Confidence is unchanged
            
        
        3. Based on yield of crop per unit area and variety of seeds      *Add this detail to soil database*
           3.1 Multiply with Land area and find revenue
        
        4. Subtract the investment from revenue and calculate net value
           4.1> If net value>0:
                        Indicate Profit
           4.2> If net value< 0:
                        Indicate Loss
        5.Suggest Policies
            5.1> If profit, suggest freeloader policies  and insurance policies only and recommend referral (for these policies)
            5.2> If loss, suggest special policies in addition to 5.1 if any and recommend referral( for freeloader policies and overall advice)
        
        ** If cropping **-:
        1. Ask the farmer about problem
        2. If the problem is-:
                             within the list:[Problems not related to the crop itself]:            *Decide this list later*
                                  Refer to techniques
                             if the problem is a crop disease:
                                  a> Activate photo module
                                      a.1> Check the photo and identify the disease using Vision model(based on symptoms)
                                           If disease identified:
                                                          Suggest remedies and referral
                                           If not identified:
                                                          Suggest referrals only
        
        ** If post cropping **-:
        1. Ask the farmer his yield
        2. Ask the farmer about his further decisions(whether wants to sale, or is unsatisfied with yield)
           If unsatisfied with yield:
                 Recommend suitable referrals and policies
           If wants to sale:
                 Recommend suitable referrals and policies
