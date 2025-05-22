# app.py

import streamlit as st
import matplotlib.pyplot as plt

# Title
st.title("Hello, World with a Pie Chart")

# Sample data
data = {
    'Apples': 30,
    'Bananas': 15,
    'Cherries': 45,
    'Dates': 10
}

# Display data
st.subheader("Fruit Distribution")
st.write("Here's a pie chart of some sample data:")

# Create pie chart
fig, ax = plt.subplots()
ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show pie chart in Streamlit
st.pyplot(fig)
