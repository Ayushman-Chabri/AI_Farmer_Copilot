**The Folder Structure**
*prices*-: This database stores information about 25 years (1999-2023) of pre-cropping and post-cropping prices for different crops in the following manner-:
    profile_id  #Stores the id for the system
    region      #Required for selecting region
    unit        #Decides the unit of crop prices
    crop_name{
        Parameter                 Key              Type                     Example
        year                      years            List                     years:[1999,2000,....2023]
        pre-cropping prices       pre              List                     pre:[1500,1520,1580,.....3000]
        post-cropping prices      post             List                     post:[2400,2480,2100,...]
    }

    Purpose-: In the final model this will be used along with regression models to predict
    the loss or profit of the farmer and warn him accordingly.This data is linked to the region
    as well as the crop type and hence has to be referenced using both. It isn't independent

    Demo Constraints-:For the purpose of demo we are taking data of only 25 years. This is
    synthetically generated data and has assumptions like steady increase of pre and post cropping
    prices due to inflation, higher post cropping price than pre cropping price etc.

    Musings-:
    (12/02/2026)-: I (Ayushman Chabri) believe that this model can be use two instances of regression models.
    Firstly our model will ask the kind of crop he/she wants to grow and the amount he wants to. Then based on 
    it our model will predictthe investment the farmer has to make for purchasing the seeds. The farmer may 
    also specify the other investments that he has made or has got to make and adding up the total expenses, 
    we can compare with the post cropping prices and determine the profit or loss.

    If required we might introduce some randomness and volatility to the data for realism.

