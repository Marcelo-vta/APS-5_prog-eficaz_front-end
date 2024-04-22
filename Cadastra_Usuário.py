import streamlit as st
import pandas as pd
from api import API
import requests
import time

st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

def post_user(user):
    return requests.post(f"{API}/usuarios", json=user)
def validate_email(str):
    for var in ['@', '.com']:
        if var not in str:
            return False
    if len(str.replace('.com', '').split('@')) < 2 or str[:4] == '.com':
        return False
    for part in str.replace('.com', '').split('@'):
        if not part:
            return False
    return True

users = requests.get(f"{API}/usuarios").json()

email_novo = False
val_email = False

st.title("Cadastrar novo Usuário")
st.subheader("Nome")
nome = st.text_input('nome', placeholder="Nome", label_visibility="hidden")

st.subheader("E-mail")
email = st.text_input('email', placeholder="E-mail", label_visibility="hidden")

if email:
    val_email = validate_email(email)
    if not val_email:
        st.error("E-mail inserido inválido")
    email_novo = email not in [user['email'] for user in users]
    if not email_novo:
        st.error("Usuário com este e-mail já existe")

vld_email = val_email and email_novo
    
st.subheader("Senha")
senha = st.text_input('senha', placeholder="Senha", label_visibility="hidden", type="password")

validate = nome and vld_email and senha

if st.button("Cadastrar", disabled=not(validate)):
    try:
        post_user({'nome': nome, 'email': email, 'senha': senha})
    except:
        st.error("Erro ao cadastrar usuário")
    else:
        st.success("Usuário cadastrado com sucesso")
        time.sleep(0.5)
        st.switch_page("pages/main.py")

    

