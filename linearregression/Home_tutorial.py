import streamlit as st
import numpy as np
import pandas as pd
import pickle
import glob

# Title element
st.title("Car Pricing Predictor for Volkswagen!!")

df = pd.read_csv("Master_Data.csv")

# Load Volkswagen model and transform
linreg_model = pickle.load(open(r'models\Volkswagen_LinReg.sav', 'rb'))
preprocessing = pickle.load(open(r'transforms\Volkswagen_Transform.pkl', 'rb'))

############################################################################################################# 
#####
#####
##### Add your inputs after this section
#####
#####
############################################################################################################# 


##  Manual setting to the best car in the world
model = 'Up!'
mileage = 42000
transmission_type = 'Manual'
fuel_type = 'Petrol'
previous_owners = 1
body_type = 'Hatchback'
engine_size = 1.2
year = 2012

############################################################################################################# 
#####
##### Make the prediction! 
#####
############################################################################################################# 

# Button element to display
if st.button('predict!'):
    d = {'model':[model],
     'mileage':[mileage], 
     'transmission':[transmission_type], 
     'fuel':[fuel_type], 
     'owners':[previous_owners], 
     'body':[body_type], 
     'engine':[engine_size], 
     'year':[year]}
    inference_data = pd.DataFrame(data=d)
    data = preprocessing.transform(inference_data)
    price = linreg_model.predict(data)
    # Conditional to avoid negative prices being displayed
    if price[0]<0:
        st.text_area("Price Prediction!", value=f"Apologies, your car seems too unique for accurate pricing!", label_visibility="visible")
    else:
        st.markdown("Your Car")
        st.dataframe(data=inference_data, use_container_width=True)
        st.header(f"Your car is worth: £{price[0]:.2f}!")
        st.snow()