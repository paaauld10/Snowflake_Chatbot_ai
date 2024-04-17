
# Import the streamlit library
import streamlit as st

# Set the title of your app
st.title('My First Streamlit App')

# Add a welcome message
st.write('Welcome to my Streamlit app!')

# Create a text input widget
user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')

# Display the customized message
st.write('Customized Message:', user_input)
