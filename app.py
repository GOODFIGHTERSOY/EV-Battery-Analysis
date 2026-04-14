import streamlit as st

st.title("EV Battery Analyzer")

voltage = st.number_input("Voltage (V)", 24)
current = st.number_input("Current (A)", 5)
time = st.number_input("Time (hours)", 1)

power = voltage * current
energy = power * time

st.write("Power (W):", power)
st.write("Energy (Wh):", energy)