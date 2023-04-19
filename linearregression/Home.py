import streamlit as st
import numpy as np
import pandas as pd
import pickle
import glob

st.set_page_config(layout="wide")

# CSS file
# Sidebar image
# rgba(0,0,0,0) is transparent but lacks IE8 support, if using IE8 then background-color: transparent; is an alternative
# Shift Toolbar
# Main app background
# https://cssgradient.io/gradient-backgrounds/ - for gradients
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

# CSS injection for page styling incliding navbar styles 
st.markdown(sb_css, unsafe_allow_html=True) # unsafe_allow_html=True <- lets all the magic happen

# Title element
st.title("Car Pricing Predictor!")

# Read all models and preprocessing pipelines into lists for later access
model_locs = glob.glob("models/*.sav")
models = []
for model in model_locs:
    models.append(pickle.load(open(model, 'rb')))

processing_locs = glob.glob("transforms/*.pkl")
transforms = []
for transform in processing_locs:
    transforms.append(pickle.load(open(transform, 'rb')))

# Used pandas for accessibility however polars is a very good option for hosting in a cpu environment as its much faster
# If you have the luxury of hosting on a GPU accelerated device then RAPIDS cuDF package is another alternative
df = pd.read_csv("Master_Data.csv")
df = df.replace('vauxhall','Vauxhall')

# most important section as it determines what data is needed to be pulled from master data
car_makes = df.make.unique()
# dropdown select box
brand = st.selectbox("Brand", options=car_makes)

# Load correct model and transform
linreg_model = models[np.where(car_makes == brand)[0].item()]
preprocessing = transforms[np.where(car_makes == brand)[0].item()]

#List of options obtained dynamically from car make
model_options = df.loc[df["make"]==brand].model.unique()
transmission_options = df.loc[df["make"]==brand].transmission.unique()
fuel_options = df.loc[df["make"]==brand].fuel.unique()
body_options = df.loc[df["make"]==brand].body.unique()

#colums to seperate entries into categorical and value inputs
col1, col2 = st.columns(2)

# categorical column
with col1:
    #Markdown
    st.markdown("## Categorical Inputs", unsafe_allow_html=True)
    model = st.selectbox("Model", options=model_options)
    body_type = st.selectbox("Body Type", options=body_options)
    transmission_type = st.selectbox("Transmission Type", options=transmission_options)
    fuel_type = st.selectbox("Fuel Type", options=fuel_options)

# numerical column
with col2:
    #HTML
    st.markdown("<H2>Numerical Inputs</H2>", unsafe_allow_html=True)
    # Text - nim/max values - default value - +/- increment size - formatting
    engine_size = st.number_input("Engine Size (Litres)", min_value=0.0, max_value=6.0, value=2.4, step=0.1, format="%.1f")
    mileage = st.number_input("Car Mileage", min_value=0, max_value=None, value=50000)
    # Min value 2000 based on data collected
    year = st.number_input("Year (yyyy)", min_value=2005, max_value=None, value=2008)

    # Radio button option with conditional numeric input
    first_owner = st.radio("Are you the first owner?", ["Yes", "No"])
    if first_owner=="No":
        other_owners = st.number_input("How many other owners were there?", min_value=1, max_value=None)
        previous_owners = 1 + other_owners
    else:
        previous_owners = 1

# Create dataframe for easy display
d = {'model':[model], 'mileage':[mileage], 'transmission':[transmission_type], 'fuel':[fuel_type], 'owners':[previous_owners], 'body':[body_type], 'engine':[engine_size], 'year':[year]}
inference_data = pd.DataFrame(data=d)

# Preprocessfor inference and predict price
data = preprocessing.transform(inference_data)
price = linreg_model.predict(data)

# Button element to display
if st.button('predict!'):
    # Conditional to avoid negative prices being displayed
    if price[0]<0:
        st.text_area("Price Prediction!", value=f"Apologies, your car seems too unique for accurate pricing!", label_visibility="visible")
    else:
        st.markdown("Your Car")
        # We can use st.dataframe to display dataframes
        #st.dataframe(data=inference_data, use_container_width=True)

        # We can also utilise jsDelivr and utilise web dev tools like bootstrap 4
        bootstrap_example=f"""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

<table class="table table-dark">
  <thead>
    <tr>
      <th scope="col">Model</th>
      <th scope="col">Mileage</th>
      <th scope="col">Transmission</th>
      <th scope="col">Fuel</th>
      <th scope="col">Owners</th>
      <th scope="col">Body</th>
      <th scope="col">Engine</th>
      <th scope="col">Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{model}</td>
      <td>{mileage}</td>
      <td>{transmission_type}</td>
      <td>{fuel_type}</td>
      <td>{previous_owners}</td>
      <td>{body_type}</td>
      <td>{engine_size}</td>
      <td>{year}</td>
    </tr>
  </tbody>
</table>
"""
        st.markdown(bootstrap_example, unsafe_allow_html=True)
        st.text_area("Your Price!", value=f"Your car is worth: £{price[0]:.2f}!", label_visibility="visible")