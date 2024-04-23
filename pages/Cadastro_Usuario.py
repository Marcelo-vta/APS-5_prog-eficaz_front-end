import streamlit as st
import requests
from api_url import URL
from validations import validate_cpf
import time
from requests_func import post_user, get_users

# st.markdown("""
#     <style>
#         section[data-testid="stSidebar"][aria-expanded="true"]{
#             display: none;
#         }
#     </style>
#     """, unsafe_allow_html=True)

st.title("Cadastrar Usuário")

nome = st.text_input("Nome: ", placeholder="Insira o nome aqui")

cpf = st.text_input("CPF: ", placeholder="Insira o CPF aqui")
if cpf:
    if not validate_cpf(cpf):
        st.error("CPF inserido de forma incorreta")

cpf_exists = len(["a" for u in get_users() if u["CPF"] == cpf])
if cpf_exists:
    st.error("CPF já cadastrado")

data = st.text_input("Data de nascimento: ", placeholder="Insira a Data de nascimento aqui")

register_auth = nome and validate_cpf(cpf) and data and not cpf_exists

if st.button("Cadastrar Usuário", disabled=not(register_auth)):
    try:
        post_user({"nome": nome, "CPF": cpf, "data": data,})
    except:
        st.error("Falha ao cadastrar usuário")
    else:
        st.success("Usuário cadastrado com sucesso")
        time.sleep(2)
        st.switch_page("pages/Cadastro_Usuario.py")





