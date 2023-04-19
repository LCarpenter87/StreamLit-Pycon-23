import streamlit as st

st.title("Input Playground")

############################################################################
# Set the options and the questions

viz_lib = ["Matplotlib", "Bokeh", "Altair", "Plotly"]
question = "What's your favourite viz library?"

############################################################################
st.divider()
st.header("Radio Buttons")
st.subheader("You can only pick one")

############################################################################
st.divider()
st.header("Drop down box aka select box")
st.subheader("You can only pick one")

############################################################################
st.divider()
st.header("Multi select")
st.subheader("You can pick many")

############################################################################
st.divider()
st.header("Checkboxes")

# Create a dictionary of the labels and the current state
options = {option: None for option in viz_lib}

# Loop through the dictionary to create the checkbox and write the current value


############################################################################
st.divider()
st.header("Sliders")

############################################################################
st.divider()
st.header("Item Sliders")

############################################################################
st.divider()
st.header("Text inputs")

############################################################################
st.divider()
st.header("Text Area")

############################################################################
st.divider()
st.header("Number inputs")

############################################################################
st.divider()
st.header("Dates")

############################################################################
