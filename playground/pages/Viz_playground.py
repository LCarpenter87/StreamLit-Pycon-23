import streamlit as st
import requests
import altair as alt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Visualisation Playground", layout="wide")
st.title("Visualisation Playground")

############################################################################
st.header("Using the Metrics Label")
# requests.get(f"https://wttr.in/{city_url}?format=%t").text
# ['London', 'Salt Lake City', 'Paris', 'Orlando']


############################################################################
# Generate sample data for scatterplots
np.random.seed(42)
n = 100
data = pd.DataFrame({
    'x': np.random.randn(n),
    'y': np.random.randn(n),
    'c': np.random.randint(0, 2, n)
})

# Altair charts
st.header("Altair Charts")
scatter_plot = alt.Chart(data).mark_circle().encode(
    x='x',
    y='y',
    color='c:N'
)


# Seaborn charts
st.header("Seaborn Charts")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='x', y='y', hue='c', ax=ax)

# Matplotlib charts
st.header("Matplotlib Charts")
fig, ax = plt.subplots()
scatter = ax.scatter(data['x'], data['y'], c=data['c'], cmap='viridis')
legend1 = ax.legend(*scatter.legend_elements(), title="Categories")
ax.add_artist(legend1)

# Seaborn charts
st.header("Seaborn Charts")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='x', y='y', hue='c', ax=ax)
