import streamlit as st
from requests_func import get_bikes, delete_bikes
import pandas as pd

st.title("Bikes")
st.subheader("Filtrar por:")

try:
    bikes = list(get_bikes())   
    filtered_bikes = bikes
except:
    st.error("Erro na requisicao de usuários")

tp_filtro = (st.radio("filtros", ["ID", "Modelo", "Marca", "Cidade", "Status"], label_visibility="collapsed"))
filtro = st.text_input("filtro", placeholder=f"Digite o {tp_filtro}", label_visibility="collapsed")
st.text("")
st.text("")
tp_filtro = tp_filtro.lower()

if filtro:
    if tp_filtro == "id":
        filtro = int(filtro)

filtered_bikes = [bike for bike in bikes if bike[tp_filtro] == filtro or not filtro]

df_bikes = pd.DataFrame(filtered_bikes)

if len(filtered_bikes) > 0:
    cols = st.columns((0.6,1.2,1.2,1.3,1.25,1.9,1.3,1.3))
    fields = ["ID", "Modelo", "Marca", "Cidade", "Status", "Empréstimos", "Editar", "Apagar"]
    for col, field_name in zip(cols, fields):
        col.write(field_name)

    for i, id in enumerate(df_bikes["id"]):
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns((0.6,1.2,1.2,1.3,1.25,1.9,1.3,1.3))
        col1.write(str(id))
        col2.write(df_bikes["modelo"][i])
        col3.write(df_bikes["marca"][i])
        col4.write(df_bikes["cidade"][i])
        col5.write(df_bikes["status"][i])
        button_phold = col6.empty()
        emps = button_phold.button("Empréstimos", key=f"{i}a")
        button2_phold = col7.empty()
        update = button2_phold.button("Editar", key=f"{i}b")
        button3_phold = col8.empty()
        delete = button3_phold.button("Apagar", key=f"{i}c")

        if update:
            st.session_state.bike_id = id
            st.switch_page('pages/Edit_bike.py')

        if delete:
            try:
                delete_bikes(id)
            except:
                st.error("Erro ao apagar bicicleta")
            else:
                st.success("Bicicleta removida com sucesso")

        if emps:
            st.session_state.bike_id = id
            st.switch_page('pages/Emprestimos.py')
else:
    st.error("Bicicleta não encontrada")

        


