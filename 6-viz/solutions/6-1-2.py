
'''
Write a streamlit to load the `data/mobile_user_behavior_dataset.csv` file, and display the conrents.

which columns are be used the x-axis of a line plot?

Create a plot to show the relationship between someone's age and their data usage.

Create another plot to show the relationship between someone's age and gender and their data usage.

mobile = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")
st.dataframe(mobile)

plot, series =plt.subplots()
sns.barplot(data =mobile, 
            x = "Data Usage (MB/day)", 
            y = 'Device Model', 
            estimator = "mean",
            errorbar=None, 
            ax=series).set_title(f"Data Usage")

st.pyplot(plot)
    

Part 2

figure, series1 = plt.subplots()

sns.lineplot(data =mobile, 
            x = "Age", 
            y = 'Number of Apps Installed', 
            estimator = "mean",
            errorbar=None, 
            ax=series1).set_title(f"Apps Installed")

st.pyplot(figure)
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


mobile = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")
st.dataframe(mobile)

category = st.selectbox("Select a category", ["Age", "Operating System"])
quantity = st.selectbox("Select  a measure", ["Data Usage (MB/day)", "Battery Drain (mAh/day)", "Screen On Time (hours/day)", "App Usage Time (min/day)"])


figure, series1 = plt.subplots()
sns.lineplot(data =mobile, x = "Age", y = quantity, hue= "Gender", estimator = "mean", ax=series1).set_title(f"Data Usage")
st.pyplot(figure)
