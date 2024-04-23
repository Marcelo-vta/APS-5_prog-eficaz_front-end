import streamlit as st
from requests_func import get_users, update_user
from validations import validate_cpf

st.title("Editar usuário")

if "user_id" not in st.session_state:
    st.switch_page("pages/Usuarios.py")

user = get_users(st.session_state.user_id)

nome = st.text_input("nome", value=user["nome"])

cpf = st.text_input("CPF", value=user["CPF"])

if cpf:
    if not validate_cpf(cpf):
        st.error("CPF inserido de forma incorreta")
cpf_exists = len(["a" for u in get_users() if u["CPF"] == cpf and u['id'] != st.session_state.user_id])
if cpf_exists:
    st.error("CPF já cadastrado")

data = st.text_input("Data de nascimento", value=user["data"])

upd_auth = nome and validate_cpf(cpf) and not cpf_exists and data

if st.button("Atualizar credenciais", disabled=not(upd_auth)):
    try:
        update_user(st.session_state.user_id, {"nome": nome, "CPF": cpf, "data": data})
    except:
        st.error("Error ao atualizar usuário")
    else:
        st.success("Usuário atualizado com sucesso")










