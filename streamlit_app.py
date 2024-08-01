import streamlit as st

# Set the page title
st.title("Streamlit App Endpoint")

# Get query parameters
params = st.experimental_get_query_params()

# Display received parameters
st.write("Received Parameters:")
st.write(params)

# Extract and display individual parameters
for key, value in params.items():
    st.write(f"{key}: {value}")

# To run this streamlit app use command in terminal
# streamlit run streamlit_app.py
