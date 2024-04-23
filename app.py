import streamlit as st
import requests
from api_url import URL
from validations import validate_cpf
import time

st.title("Aluguel de bicicletas")

col1, col2, col3 = st.columns(3)

if col1.button("Usuários"):
    st.switch_page("pages/Usuarios.py")

if col2.button("Bikes"):
    time.sleep(2)
    st.switch_page("pages/Bikes.py")

if col3.button("Emprestimos"):
    time.sleep(2)
    st.switch_page("pages/Emprestimos.py")

