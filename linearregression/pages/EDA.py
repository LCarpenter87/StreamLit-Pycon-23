import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px
# import variable from Home page
from Home import car_makes, df

st.set_page_config(layout="wide")

sb_css = """
<style>
[data-testid="stSidebar"] {
background: rgb(5,10,48);
background: url(https://cutewallpaper.org/23/wallpaper-black-car/275736302.jpg);
}
[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
}
[data-testid="stToolbar"] {
right: 2rem;
}
[data-testid="stAppViewContainer"] {
background-image: radial-gradient( circle farthest-corner at 90.8% 12.5%,  rgba(3,19,46,1) 0%, rgba(28,19,19,1) 90% );
}
</style>
"""

# Identical CSS injection for consistency across pages
st.markdown(sb_css, unsafe_allow_html=True) # unsafe_allow_html=True <- lets all the magic happen

st.title("EDA of AutoTrader Data")

plot_options = ["Scatter", "Histogram", "Boxplot"]
continuous_cols = ["mileage", "price"]

tab1, tab2, tab3 = st.tabs(plot_options)

def scatterplot(df):
    # Select boxes and plotly plot
    SbS_check = st.checkbox("Side-by-side Comparison of makes?", key=1) # key to make checkboxes unique
    if SbS_check:
        x_axis_label = st.selectbox("Select x-axis data", options=df.columns[1:], key=2)
        y_axis_label = st.selectbox("Select y-axis data", options=df.columns[1:], key=3)
        col1, col2 = st.columns(2)
        with col1:
            make_1 = st.selectbox("Brand 1", options=car_makes, key=16)
            df1 = df.loc[df["make"]==make_1]
            plot1_color = st.color_picker("Select plot color", value="#00DBDE", key=18)
            plot1 = px.scatter(df1, x=x_axis_label, y=y_axis_label)
            plot1.update_traces(marker=dict(color=plot1_color))
            st.plotly_chart(plot1, use_container_width=True)   
        with col2:
            make_2 = st.selectbox("Brand 2", options=car_makes, key=17)
            df2 = df.loc[df["make"]==make_2]
            plot2_color = st.color_picker("Select plot color", value="#FC00FF", key=19)
            plot2 = px.scatter(df2, x=x_axis_label, y=y_axis_label)
            plot2.update_traces(marker=dict(color=plot2_color))
            st.plotly_chart(plot2, use_container_width=True)
    else:
        x_axis_label = st.selectbox("Select x-axis data", options=df.columns[1:], key=4)
        y_axis_label = st.selectbox("Select y-axis data", options=df.columns[1:], key=5)

        st.markdown("Click on the legend to (add/remove makes)")

        plot = px.scatter(df, x=x_axis_label, y=y_axis_label, color="make")
        st.plotly_chart(plot, use_container_width=True)

def histplot(df):
    # Select boxes and plotly plot
    SbS_check = st.checkbox("Side-by-side Comparison of makes?", key=6)
    if SbS_check:
        hist_col = st.selectbox("Select x-axis data", options=df.columns[1:], key=7)
        col1, col2 = st.columns(2)
        with col1:
            if hist_col in continuous_cols:
                nbins = st.slider("nbins", min_value=5, max_value=30)
            else:
                nbins=None
            make_1 = st.selectbox("Brand 1", options=car_makes, key=12)
            df1 = df.loc[df["make"]==make_1]
            plot1 = px.histogram(df1, x=hist_col, nbins=nbins)
            st.plotly_chart(plot1, use_container_width=True)
        with col2:
            if hist_col in continuous_cols:
                nbins = st.slider("nbins", min_value=5, max_value=30)
            else:
                nbins=None
            make_2 = st.selectbox("Brand 2", options=car_makes, key=13)
            df2 = df.loc[df["make"]==make_2]
            plot2 = px.histogram(df2, x=hist_col, nbins=nbins)
            st.plotly_chart(plot2, use_container_width=True)
    else:
        hist_col = st.selectbox("Select x-axis data", options=df.columns[1:], key=8)
        if hist_col in continuous_cols:
            nbins = st.slider("nbins", min_value=5, max_value=30)
        else:
            nbins=None
        st.markdown("Click on the legend to (add/remove makes)")

        plot = px.histogram(df, x=hist_col, nbins=nbins, color="make")
        st.plotly_chart(plot, use_container_width=True)

def boxplot(df):
    # Select boxes and plotly plot
    SbS_check = st.checkbox("Side-by-side Comparison of makes?", key=9)
    if SbS_check:
        x_axis_label = st.selectbox("Select x-axis data", options=df.columns[1:], key=10)
        y_axis_label = "price"
        col1, col2 = st.columns(2)
        with col1:
            make_1 = st.selectbox("Brand 1", options=car_makes, key=14)
            df1 = df.loc[df["make"]==make_1]
            plot1_color = st.color_picker("Select plot color", value="#00DBDE", key=20)
            plot1 = px.box(df1, x=x_axis_label, y=y_axis_label)
            plot1.update_traces(marker=dict(color=plot1_color))
            st.plotly_chart(plot1, use_container_width=True)   
        with col2:
            make_2 = st.selectbox("Brand 2", options=car_makes, key=15)
            df2 = df.loc[df["make"]==make_2]
            plot2_color = st.color_picker("Select plot color", value="#FC00FF", key=21)
            plot2 = px.box(df2, x=x_axis_label, y=y_axis_label)
            plot2.update_traces(marker=dict(color=plot2_color))
            st.plotly_chart(plot2, use_container_width=True)
    else:
        x_axis_label = st.selectbox("Select x-axis data", options=df.columns[1:], key=11)
        y_axis_label = "price"

        st.markdown("Click on the legend to (add/remove makes)")

        plot = px.box(df, x=x_axis_label, y=y_axis_label, color="make")
        st.plotly_chart(plot, use_container_width=True)
    
with tab1:
    scatterplot(df)

with tab2:
    histplot(df)

with tab3:
    boxplot(df)