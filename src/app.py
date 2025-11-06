import streamlit as st

# Streamlit UI
st.title("Power Calculator")
st.write("Enter  a number to calculate its square, qube and its fifth power. ")

# Input from user
number = st.number_input("Enter a number:", value = 1, step = 1)

# Calculations
square = number ** 2
cube = number ** 3
fifth_power = number ** 5

# Display results
st.write(f"The square of {number} is: {square}")
st.write(f"The cube of {number} is: {cube}")
st.write(f"The fifth power of {number} is: {fifth_power}")