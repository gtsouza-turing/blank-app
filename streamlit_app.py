import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

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

# Configurar o escopo e autenticação
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('014-turing-430915-40bc8c784d5c.json', scope)
client = gspread.authorize(creds)

# Abrir a planilha e selecionar a worksheet
spreadsheet = client.open("Turing-Export")
worksheet = spreadsheet.sheet1  # ou use worksheet = spreadsheet.worksheet("Nome da Worksheet")

new_row = ["Testando"]
# Adicionar a nova linha na planilha
worksheet.append_row(new_row)

print("Nova linha adicionada com sucesso!")


# To run this streamlit app use command in terminal
# streamlit run streamlit_app.py
