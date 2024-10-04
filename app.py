import streamlit as st
import numpy as np
import joblib
import pandas as pd
# Load the model
model = joblib.load('prediction1.pkl')

# Page styling
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://content.api.news/v3/images/bin/7e24714a1f449f21607db66357b2c60a");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0.5);
    color: white;
}
[data-testid="stToolbar"] {
    right: 2rem;
}
[data-testid="stSidebar"] > div:first-child {
    background-image: url("neo.jpg");
    background-position: center;
}
.stTextInput > div > div > input {
    color: white;
    background-color: rgba(0,0,0,0.5);
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Near Earth Objects(NEO) Assessor")

# Input fields
am = st.text_input("Absolute Magnitude")
edmin = st.text_input("Estimated Diameter Min (km)")
edmax = st.text_input("Estimated Diameter Max (km)")
rv = st.text_input("Relative Velocity (km/s)")
md = st.text_input("Miss Distance (km)")

if st.button('Predict'):
    input_data = np.array([[am, edmin, edmax, rv, md]])

    # Make prediction
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[:, 1]

    st.write('Prediction:')
    if prediction[0] == 0:
        st.success('All clear! This space traveler poses no danger to Earth.')
    else:
        st.error('Alert! This space traveler may pose danger to Earth.')

    st.write(f'Probability of being hazardous: {probability[0]:.2%}')


st.sidebar.title("About NEOs")
st.sidebar.write("""
Near Earth Objects (NEOs) are asteroids or comets that come close to or cross Earth's orbit.
While most NEOs pose no immediate danger, it's crucial to monitor and study them to ensure Earth's safety.""")
