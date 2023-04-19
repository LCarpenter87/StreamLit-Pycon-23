import streamlit as st

# Create your title, header, and subheader
st.title("Welcome to the playground")
st.header("Let's play with some toys!")
st.subheader("Yeah!")

# Play with some nifty text
st.text("""    

  I'll use whatever spacing 
              and formatting you put in""")

st.divider()

# Create a button
my_button = st.button(label="CLICK ME TO CELEBRATE!")
st.code("""my_button = st.button(label="CLICK ME TO CELEBRATE!")
if my_button:
    st.balloons()""")

# Add an action to your button - the best action in streamlit
if my_button:
    st.balloons()

st.divider()


# Create an updateable placeholder
text_1 = st.empty()

# Lets try to make a clicker counter! Create an empty placeholder and a button
my_counter = 0
second_button = st.button(label="Click to add one!")

# Add the button action
if second_button:
    my_counter += 1
    text_1.write(f"Button clicked {my_counter} time(s)")

# Doesn't work?! What's wrong!

# Use the session state
if 'counter' not in st.session_state:
    st.session_state['counter'] = 0

st.code("""
        if 'counter' not in st.session_state:
            st.session_state['counter'] = 0      
        """)

# Recreate the button and assign the action
if second_button:
    st.session_state.counter += 1
    text_1.write(f" Yay button clicked {st.session_state.counter} times!")

st.divider()
