# Birth_Rate

Introduction:
I wanted to take a look if education level played a part when women were having babies.  According to the CDC, in 2021, the birth rates for women in their early 20s declined and increased mostly in a woman's early 30s.  

The dataset that I am analyzing is the US births from 2016-2021 according to education level and age by state.  The purpose of this project is to provide a look into the value of education, bringing stability and marketability, over starting a family early or vice versa.

# Data Description

I used a dataset from Kaggle that provided me with the necessary data points that I needed for the project.  The data set was broken down into fields; State,	State Abbreviation,	Year,	Gender,	Education Level of Mother,	Education Level Code,	Number of Births,	Average Age of Mother (years), and	Average Birth Weight (g). This dataset has four quantitative fields: Education Level of Mother, Education Level Code, Number of Births, and Average Age of Mother (years).  The summarized category Average Birth Weight, will not be used for analysis.  There were no NAN values within the dataset. 

# Data Inquiry:

According to the dataset, one of the questions I asked myself was; At the highest levels of education are the birth rates increasing? and for anecdotal inquiry at what age are they having babies?  The age is a summarized field as the average age of the mother, though I used it as a snapshot it was not my major hypothesis.  I was looking for the trend in the US birth rate, the relationship between education level and birth rate, and whether people are deciding to have babies later in life based on education level.

# Project Value:

This project has value in the sense that it can help project the trend of the US population.  The value of understanding birthrate in relation to education level is useful because pursuing these higher education ranks could push having babies later in life.  As me and my wife did, we pursued higher education, my wife had our first baby at 32, second at 37, and third at 40.  This is important because at higher ages you become "High-risk", my wife was high risk due to age since our second baby, of course, there are other factors that I don't get into that cause high-risk status.

# Data Cleaning and Analysis:

I created functions to clean the dataset, I removed columns that I didn't need, state abbreviations, gender (of the baby), and baby weight.  I will insert graphs, visualizations, and data here.

![North Carolina Education of Mother](https://github.com/Chris-Vicks/Birth_Rate/assets/135290086/a1280783-87b7-46db-b7ee-bd630de0dcc6)
| State | Year | Birth_Per_Year |
|-----------------|-----------------|-----------------|
North Carolina |	2016 |	120779
North Carolina |	2017 |	120125
North Carolina |	2018 | 	118954
North Carolina |	2019 |	118725
North Carolina |	2020 |	116730
North Carolina |	2021 |	120466

| State | Year | Education level of Mother | Number of births |
|-----------------|-----------------|-----------------|----------------|
|North Carolina |	2016 |	8th grade or less |	4529
North Carolinaz|	2016 |9th through 12th grade with no diploma	|12793
North Carolina|	2016	| Associate degree (AA, AS)	|11044
North Carolina|	2016	|Bachelor's degree (BA, AB, BS)	|24234
North Carolina	|2016	|Doctorate (PhD, EdD) or Professional Degree (MD, DDS, DVM, LLB, JD)	|2942
North Carolina|	2016	|High school graduate or GED completed	|27443
North Carolina|	2016	|Master's degree (MA, MS, MEng, MEd, MSW, MBA)	|10217
North Carolina|	2016	|Some college credit, but not a degree	|27240
North Carolina|	2016	|Unknown or Not Stated	|337
North Carolina|	2017	|8th grade or less	|4390
North Carolina|	2017	|9th through 12th grade with no diploma	|12421
North Carolina|	2017	|Associate degree (AA, AS)	|11148
North Carolina|	2017	|Bachelor's degree (BA, AB, BS)	|23506
North Carolina|	2017	|Doctorate (PhD, EdD) or Professional Degree (MD, DDS, DVM, LLB, JD)	|3017
North Carolina|	2017	|High school graduate or GED completed	|28252
North Carolina|	2017	|Master's degree (MA, MS, MEng, MEd, MSW, MBA)	|10254
North Carolina|	2017	|Some college credit, but not a degree	|26866
North Carolina|	2017	|Unknown or Not Stated	|271
North Carolina|	2018	|8th grade or less	|3943
North Carolina|	2018	|9th through 12th grade with no diploma	|11694
North Carolina|	2018	|Associate degree (AA, AS)	|11226
North Carolina|	2018	|Bachelor's degree (BA, AB, BS)	|24110
North Carolina|	2018	|Doctorate (PhD, EdD) or Professional Degree (MD, DDS, DVM, LLB, JD)	|3018
North Carolina|	2018	|High school graduate or GED completed	|28321
North Carolina|	2018	|Master's degree (MA, MS, MEng, MEd, MSW, MBA)	|10446
North Carolina|	2018	|Some college credit, but not a degree	|25807
North Carolina|	2018	|Unknown or Not Stated	|389
North Carolina|	2019	|8th grade or less	|3942
North Carolina|	2019	|9th through 12th grade with no diploma	|11254
North Carolina|	2019	|Associate degree (AA, AS)	|11332
North Carolina|	2019	|Bachelor's degree (BA, AB, BS)	|23941
North Carolina|	2019	|Doctorate (PhD, EdD) or Professional Degree (MD, DDS, DVM, LLB, JD)	|3117
North Carolina|	2019	|High school graduate or GED completed	|29577
North Carolina	|2019	|Master's degree (MA, MS, MEng, MEd, MSW, MBA)	|10606
North Carolina	|2019	|Some college credit, but not a degree	|24528
North Carolina	|2019	|Unknown or Not Stated	|428
North Carolina|	2020	|8th grade or less	|3884
North Carolina	|2020	|9th through 12th grade with no diploma	|10616
North Carolina|	2020	|Associate degree (AA, AS)	|11198
North Carolina|	2020	|Bachelor's degree (BA, AB, BS)	|24225
North Carolina|	2020	|Doctorate (PhD, EdD) or Professional Degree (MD, DDS, DVM, LLB, JD)	|3191
North Carolina|	2020	|High school graduate or GED completed	|29290
North Carolina|	2020	|Master's degree (MA, MS, MEng, MEd, MSW, MBA)	|10438
North Carolina|	2020	|Some college credit, but not a degree	|23565
North Carolina|	2020	|Unknown or Not Stated	|323
North Carolina|	2021	|8th grade or less	|3627
North Carolina|	2021	|9th through 12th grade with no diploma	|10187
North Carolina|	2021	|Associate degree (AA, AS)	|11743
North Carolina|	2021	|Bachelor's degree (BA, AB, BS)	|26112
North Carolina|	2021	|Doctorate (PhD, EdD) or Professional Degree (MD, DDS, DVM, LLB, JD)	|3425
North Carolina|	2021	|High school graduate or GED completed	|30032
North Carolina|	2021	|Master's degree (MA, MS, MEng, MEd, MSW, MBA)	|11680
North Carolina|	2021	|Some college credit, but not a degree	|23322
North Carolina|	2021	|Unknown or Not Stated	|338



As I was looking 

![North Carolina Average Age of Mother](https://github.com/Chris-Vicks/Birth_Rate/assets/135290086/f15799d5-a475-402a-a5ac-a8f55c261ad3)
Conclusion:
