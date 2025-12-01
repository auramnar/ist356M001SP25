'''
Create a streamlit with the fast food dataset. 

`fast_food_nutrition_cleaned.csv` 

Let' input the macro nutrient: protein, fat, carbs, and sugar as a dropdown.

Create a heatmap of the calories vs. the macro nutrient broken down by the type fast food restaurant.

You'll have to pivot the data to create the heatmap. So use a mean aggregation to create the heatmap... average carbs, etc...

How can you interpret the heatmap you see?


Noticeable differences emerge between brands and nutrient types. 
Higher-calorie food items generally contain more fat, sodium, and sugars, resulting in darker shading in those regions of the heatmap. 
Some companies consistently show darker values across several nutrient categories, indicating richer and more calorie-dense menu items, 
while others remain lighter, suggesting comparatively lower nutritional counts. 
The visual layout makes it easy to identify which chains offer items with higher concentrations of macronutrients and 
where the most nutritionally dense foods cluster in terms of calorie level. Overall, the heatmap highlights variation in 
nutritional quality across brands and suggests that calorie increases usually correlate with higher macronutrient and sodium content.

'''



import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ff = pd.read_csv("./6-viz/data/fast_food_nutrition_cleaned.csv")
print(ff.columns)

companies = sorted(list(ff['company'].unique()))
print(companies)

value = st.selectbox("Select Macronutrient", ['fat_g', 'carbs_g', 'sugars_g', 'protein_g', 'sodium_mg'])

ffp = ff.pivot_table(index='company', columns='calories',values=value, aggfunc=np.mean)

figure, series1 = plt.subplots()
sns.heatmap(ffp, ax=series1)
st.pyplot(figure)
