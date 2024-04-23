import streamlit as st
from requests_func import get_emp, get_bikes, delete_emp, get_users, post_emp
import pandas as pd

prefiltro_bike, prefiltro_user, index_filtro = None, None, 0

if "bike_id" in st.session_state:
    prefiltro_bike = st.session_state.bike_id
    index_filtro = 2
if "user_id" in st.session_state:
    prefiltro_user = st.session_state.user_id
    index_filtro = 1

emprestimos = get_emp()
bikes = get_bikes()
usuarios = get_users()

st.title("Empréstimos: ")

st.subheader("Realizar empréstimo:")
col1, col2 = st.columns(2)

with col1:
    id_usuario = st.selectbox("usuario", options=[user['id'] for user in usuarios], label_visibility="collapsed", index=None, placeholder="ID do Usuário")

with col2:
    bikes_disp = [bike['id'] for bike in bikes if bike["status"] == "Disponivel"]
    if len(bikes_disp):
        pholder = "ID da Bike"
    else:
        pholder = "Sem bikes disponíveis"

    id_bike = st.selectbox("bikes disponiveis", options=[bike['id'] for bike in bikes if bike["status"] == "Disponivel"], label_visibility="collapsed", index=None, placeholder=pholder, ) 

auth_emp = id_usuario and id_bike
if st.button("Concluir empréstimo", disabled=not(auth_emp)):
    try:
        post_emp(id_usuario, id_bike)
    except:
        st.error("Erro ao realizar empréstimo")

st.text("")

st.subheader("Filtrar por:")
tp_filtro = st.radio("Filtrar por:", ["ID do empréstimo", "ID de Usuário", "ID da Bike"], label_visibility="collapsed", index=index_filtro)
if prefiltro_user:
    filtro = st.text_input("filtro", placeholder=f"Buscar por {tp_filtro}", label_visibility="collapsed", value=prefiltro_user)
else:
    filtro = st.text_input("filtro", placeholder=f"Buscar por {tp_filtro}", label_visibility="collapsed", value=prefiltro_bike)
if filtro:
    filtro = int(filtro)
st.text("")
st.text("")

trad = {"ID do empréstimo": "id", "ID de Usuário": "usuario_id", "ID da Bike": "bicicleta_id"}

emprestimos_filtrado = [emp for emp in emprestimos if emp[trad[tp_filtro]] == filtro or not filtro]

df_emprestimos = pd.DataFrame(emprestimos_filtrado)

if len(emprestimos_filtrado) > 0:
    cols = st.columns((1.5,1.5,1.5,1.5,1))
    fields = ["ID do empréstimo", "ID do usuário", "ID da bike", "data", "Apagar"]
    for col, field_name in zip(cols, fields):
        col.write(field_name)

    for i, id in enumerate(df_emprestimos["id"]):
        col1, col2, col3, col4, col5 = st.columns((1.5,1.5,1.5,1.5,1))
        col1.write(str(id))
        col2.write(str(df_emprestimos["usuario_id"][i]))
        col3.write(str(df_emprestimos["bicicleta_id"][i]))
        col4.write("data")
        button_phold = col5.empty()
        delete = button_phold.button("Apagar", key=f"{i}a")

        if delete:
            try:
                delete_emp(id)
            except:
                st.error("Erro ao apagar empréstimo")
            else:
                st.success("Empréstimo removido com sucesso")
else:
    st.error("Empréstimo não encontrado")


