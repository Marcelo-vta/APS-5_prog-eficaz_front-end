import streamlit as st
import requests
from api_url import URL
from validations import validate_cpf
import time
from requests_func import post_user, get_users

st.title("Registrar bike")

modelo = st.text_input("Nome: ", placeholder="Insira o nome aqui")

marca = st.text_input("CPF: ", placeholder="Insira o CPF aqui")

cidade = st.text_input("Cidade: ", placeholder="Insira a Cidade aqui")

register_auth = modelo and marca and cidade

if st.button("Cadastrar Usuário", disabled=not(register_auth)):
    try:
        post_user({"modelo": modelo, "marca": marca, "cidade": cidade, "status": "Disponivel"})
    except:
        st.error("Falha ao cadastrar usuário")
    else:
        st.success("Usuário cadastrado com sucesso")
        time.sleep(2)
        st.switch_page("pages/Cadastro_Usuario.py")





