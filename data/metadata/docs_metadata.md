**The Folder Structure**
*regions*-: This is the dataset that is primarily used for selecting the state of India in the following manner-:
regions{
    region name{
        Parameter                 Key                 Type               Example
        Region name(System ID)    profile_id          String             profile_id:"odisha"
        Region name(Display name) display_name        String             display_name:"Odisha"
        Preferred Language        preferred_language  List               preferred_languages:["en","hi","or"]
        Default Language          default_language    String             default_language:"or"
        Sub regions               locations           List               locations:["Anugul","Balangir",..."Sundargarh"]
    }
}

Purpose-: In our final model this dataset will be used as the umbrella dataset to identify the
supported and default languages and to also attest whether a particulatr sub region is a part of 
the region or not

Demo Constraints-: For the purpose of demo, the sub regions will usually be districts 

Musings-:
(12/02/2026)-: (Ayushman Chabri) Musings are same as Purpose

