import streamlit as st
import numpy as np
import plotly.figure_factory as ff # build a custom distribution plot

# Add histogram data
# Create three groups of normally distributed data 
x1 = np.random.randn(200) - 2 # centered  left
x2 = np.random.randn(200) # centered at 0
x3 = np.random.randn(200) + 2 # centered right

# Group data together in a list for plotting
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])
# create a smoothed histogram (KDE plot) for each group.
# each group uses a different bin_size (width of histogram bars).

# Plot!
st.plotly_chart(fig, use_container_width=True)

