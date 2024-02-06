import streamlit as st
import numpy as np

# Initialize session state variables
if 'angle' not in st.session_state:
    st.session_state.angle = 0.0  # Starting angle
if 'direction' not in st.session_state:
    st.session_state.direction = 1  # Start with incrementing

# Function to update angle
def update_angle():
    max_angle = np.pi
    min_angle = -np.pi
    step = 0.5  # Increment/Decrement step
    
    # Update the angle based on the current direction
    st.session_state.angle += st.session_state.direction * step
    
    # Reverse direction at bounds
    if st.session_state.angle >= max_angle or st.session_state.angle <= min_angle:
        st.session_state.direction *= -1

st.title("4D Tesseract Rotation")

# Display current angle
st.write(f"Current Angle: {st.session_state.angle}")

# Button to manually trigger angle update
if st.button('Update Angle'):
    update_angle()
