import numpy as np
import pandas as pd
import streamlit as st

# Create your titile, header, and subheader
st.title("Let's play with some data!")


# Create a random dataframe
n_cols = 5

df = pd.DataFrame(
    np.random.randn(20, n_cols), columns=[f"col{i}" for i in range(n_cols)]
)

# We can use write

st.header("A dataframe written using st.write()")

st.write(df)

# We can use st.dataframe
st.header("A sortable dataframe written using st.dataframe()")
st.subheader("We can control width when using st.dataframe()")
st.dataframe(df, use_container_width=True)

# We can use st.table()
st.header("A static table, created from a dataframe, written using st.table()")
st.table(df)


viz_libs = pd.DataFrame(
    [
        {"library": "Plotly", "rating": np.NaN, "used? 🎈": False},
        {"library": "Altair", "rating": np.NaN, "used? 🎈": False},
        {"library": "Bokeh", "rating": np.NaN, "used? 🎈": False},
        {"library": "Matplotlib", "rating": np.NaN, "used? 🎈": False}
    ]
)

edited_df = st.experimental_data_editor(viz_libs, num_rows="dynamic")

if edited_df['rating'].isna().all():
    favorite_library = "a mystery as you haven't rated anything!"
else:
    favorite_library = edited_df.loc[edited_df["rating"].idxmax()]["library"]


st.subheader(f"Your favorite library is {favorite_library}")

st.download_button(
    label="Download data as CSV",
    data= edited_df.to_csv(),
    file_name='edited_df.csv',
    mime='text/csv',
)
