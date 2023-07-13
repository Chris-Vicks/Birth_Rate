# Birth_Rate

# Introduction:
I wanted to take a look if education level played a part when women were having babies.  According to the CDC, in 2021, the birth rates for women in their early 20s declined and increased mostly in a woman's early 30s.  

The dataset that I am analyzing is the US births from 2016-2021 according to education level and age by state.  The purpose of this project is to provide a look into the value of education, bringing stability and marketability, over starting a family early or vice versa.

# Data Description

I used a dataset from Kaggle that provided me with the necessary data points that I needed for the project.  The data set was broken down into fields; State,	State Abbreviation,	Year,	Gender,	Education Level of Mother,	Education Level Code,	Number of Births,	Average Age of Mother (years), and	Average Birth Weight (g). This dataset has 4 quantitative fields: Education Level Code, Number of Births, and Average Age of Mother (years), the average weight of the baby.  The summarized category Average Birth Weight, will not be used for analysis.  There were no NAN values within the dataset. 

# Data Inquiry:

According to the dataset, one of the questions I asked myself was; At the highest levels of education are the birth rates increasing? and for anecdotal inquiry at what age are they having babies?  The age is a summarized field as the average age of the mother, though I used it as a snapshot it was not my major hypothesis.  I was looking for the trend in the US birth rate, the relationship between education level and birth rate, and whether people are deciding to have babies later in life based on education level.

# Project Value:

This project has value in the sense that it can help project the trend of the US population.  The value of understanding birthrate in relation to education level is useful because pursuing these higher education ranks could push having babies later in life.  As me and my wife did, we pursued higher education, my wife had our first baby at 32, second at 37, and third at 40.  This is important because at higher ages you become "High-risk", my wife was high risk due to age since our second baby, of course, there are other factors that I don't get into that cause high-risk status.

# Data Cleaning and Analysis:

I created functions to clean the dataset, I removed columns that I didn't need, state abbreviations, gender (of the baby), and baby weight.  

![North Carolina Education of Mother](https://github.com/Chris-Vicks/Birth_Rate/assets/135290086/a1280783-87b7-46db-b7ee-bd630de0dcc6)

My initial thought before I analyzed the data set, I thought I would find mothers with higher education, which usually leads to higher means, would have more children.  I was surprised that after achieving a bachelor's degree, those with higher levels of education drop off significantly.  

![North Carolina Average Age of Mother](https://github.com/Chris-Vicks/Birth_Rate/assets/135290086/f15799d5-a475-402a-a5ac-a8f55c261ad3)

After looking at the total number of births per education level, I was curious about the average age, and as we see in the above graph the higher education levels are having kids at a higher age, late 20s to early 30s.  although it may look like people are putting off having babies, are they having fewer babies?

| State | Year | Birth_Per_Year |
|-----------------|-----------------|-----------------|
North Carolina |	2016 |	120779
North Carolina |	2017 |	120125
North Carolina |	2018 | 	118954
North Carolina |	2019 |	118725
North Carolina |	2020 |	116730
North Carolina |	2021 |	120466

Looking at the data set, the answer would be no, but just barely. 

![Sum_All_States](https://github.com/Chris-Vicks/Birth_Rate/assets/135290086/090a117f-fdf4-4175-a671-6a63d93507c2)

As I looked at the overall data set, the North Carolina data matched up level for the level of education with who was having the most babies. 

Conclusion:
Although this data set is good in that it gives raw numbers, it did lack in answering a few questions.  The higher educated were having babies later but were they having babies while they were attaining the education or did they wait until their education was complete?  
The birth rates for women in their early 20s have declined, while rates have increased for women in their early 30s.
There is a notable relationship between education level and birth rate, with higher levels of education associated with delayed childbearing.
Pursuing higher education brings stability and marketability, potentially influencing the decision to start a family later in life.
Understanding the correlation between education level and birth rate provides valuable insights into population trends and reproductive choices.

Future Work:
In future research, it would be interesting to delve deeper into the factors influencing the decline in birth rates among women in their early 20s and the increase among women in their early 30s. Additionally, investigating the impact of socioeconomic factors and career aspirations on the decision to delay childbearing could provide further insights. Furthermore, exploring the relationship between education level, birth rate, and its implications for healthcare systems and policy development would be valuable.



