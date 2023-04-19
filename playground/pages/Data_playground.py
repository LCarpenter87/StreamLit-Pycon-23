import numpy as np
import pandas as pd
import streamlit as st

# Create your titile, header, and subheader
st.title("Let's play with some data!")

# Create a random dataframe
n_cols = 5
df = pd.DataFrame(np.random.randn(20, n_cols), columns=[f"col{i}" for i in range(n_cols)])

############################################################################
st.header("A dataframe written using st.write()")



############################################################################
st.header("A sortable dataframe written using st.dataframe()")
st.subheader("We can control width when using st.dataframe()")


############################################################################
st.header("A static table, created from a dataframe, written using st.table()")


############################################################################
st.header("Editable Dataframes!")
viz_libs = pd.DataFrame(
    [
        {"library": "Plotly", "rating": np.NaN, "used? 🎈": False},
        {"library": "Altair", "rating": np.NaN, "used? 🎈": False},
        {"library": "Matplotlib", "rating": np.NaN, "used? 🎈": False}
    ]
)
