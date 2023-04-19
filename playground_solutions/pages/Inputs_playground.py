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

viz_selected = st.radio(label=question, options=viz_lib)
st.write(f"Your favourite viz is {viz_selected}")

############################################################################
st.divider()
st.header("Drop down box aka select box")
st.subheader("You can only pick one")

viz_selected_drop_down = st.selectbox(question, options=viz_lib)
st.write(f"Your favourite viz is {viz_selected_drop_down}")

############################################################################
st.divider()
st.header("Multi select")
st.subheader("You can pick many")

viz_selected_multi = st.multiselect(question, options=viz_lib)
st.write(f"Your favourite viz is {viz_selected_multi}")

############################################################################
st.divider()
st.header("Checkboxes")

# Create a dictionary of the labels and the current state
options = {option: None for option in viz_lib}

# Loop through the dictionary to create the checkbox and write the current value
for option, checkbox in options.items():
    options[option] = st.checkbox(option)

for option, checkbox in options.items():
    if checkbox:
        st.write(f"You like {option}")

############################################################################
st.divider()
st.header("Sliders")

slider_value = st.slider(
    f"As a %, How much do you love {viz_selected}",
    min_value=0,
    max_value=100,
    value=100,
    step=5,
    format="%d%%",
    help="Pick something between 0 and 100",
)

st.write(f"You like {viz_selected} {slider_value}%!")

############################################################################
st.divider()
st.header("Item Sliders")

slider_item = st.select_slider(
    label = f"How much do you like {viz_selected_drop_down}",
    options = ['Very Much', 'Somewhat', 'A little', 'Not at all']
)


st.write(f"You like {viz_selected_drop_down} {slider_item.lower()}!")
############################################################################
st.divider()
st.header("Text inputs")

user_text = st.text_input(label=question)

if user_text:
    st.write(f"You've entered {user_text}")

############################################################################

st.divider()
st.header("Text Area")

user_text = st.text_area(label=question)

if user_text:
    st.write(f"You've entered {user_text}")

############################################################################
st.divider()
st.header("Number inputs")

user_number = st.number_input(label=f"As a %, How much do you love {viz_selected}",
                            min_value = 0,
                            max_value = 100,
                            step=10)


if user_number:
    st.write(f"You've entered {user_number}")


############################################################################
st.divider()
st.header("Dates")

user_date= st.date_input(label=f"When is your birthday?")

st.write(f'Your Birthday is {user_date}')