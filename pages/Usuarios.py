import streamlit as st
from requests_func import get_users, delete_user
import pandas as pd

st.title("Usuários")
st.subheader("Filtrar por:")

try:
    users = list(get_users())   
    filtered_users = users
except:
    st.error("Erro na requisicao de usuários")

tp_filtro = (st.radio("filtros", ["id", "nome", "CPF", "data"], label_visibility="collapsed"))
filtro = st.text_input("filtro", placeholder=f"Digite o {tp_filtro}", label_visibility="collapsed")
st.text("")
st.text("")

if filtro:
    if tp_filtro == "id":
        filtro = int(filtro)

filtered_users = [user for user in users if user[tp_filtro] == filtro or not filtro]

df_users = pd.DataFrame(filtered_users)

if len(filtered_users) > 0:
    cols = st.columns((1,1,2,1.5,1.8,1.3,1.3))
    fields = ["ID", "Nome", "CPF", "data", "Empréstimos", "Editar", "Apagar"]
    for col, field_name in zip(cols, fields):
        col.write(field_name)

    for i, id in enumerate(df_users["id"]):
        col1, col2, col3, col4, col5, col6, col7 = st.columns((1,1,2,1.5,1.8,1.3,1.3))
        col1.write(str(id))
        col2.write(df_users["nome"][i])
        col3.write(df_users["CPF"][i])
        col4.write(df_users["data"][i])
        button_phold = col5.empty()
        emps = button_phold.button("Empréstimos", key=f"{i}a")
        button2_phold = col6.empty()
        update = button2_phold.button("Editar", key=f"{i}b")
        button3_phold = col7.empty()
        delete = button3_phold.button("Apagar", key=f"{i}c")

        if update:
            st.session_state.user_id = id
            st.switch_page('pages/Edit_user.py')

        if delete:
            try:
                delete_user(id)
            except:
                st.error("Erro ao apagar usuário")
            else:
                st.success("Usuário removido com sucesso")

        if emps:
            st.session_state.user_id = id
            st.switch_page('pages/Emprestimos.py')
else:
    st.error("Usuário não encontrado")

        


