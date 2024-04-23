import streamlit as st
import requests
from api_url import URL
from validations import validate_cpf
import time
from requests_func import post_bikes, get_bikes

st.title("Registrar bike")

modelo = st.text_input("Nome: ", placeholder="Insira o nome aqui")

marca = st.text_input("Marca: ", placeholder="Insira a Marca aqui")

cidade = st.text_input("Cidade: ", placeholder="Insira a Cidade aqui")

register_auth = modelo and marca and cidade

if st.button("Cadastrar Bike", disabled=not(register_auth)):
    try:
        post_bikes({"modelo": modelo, "marca": marca, "cidade": cidade, "status": "Disponivel"})
    except:
        st.error("Falha ao cadastrar Bike")
    else:
        st.success("Bike cadastrada com sucesso")
        time.sleep(2)
        st.switch_page("pages/Registrar_Bike.py")





