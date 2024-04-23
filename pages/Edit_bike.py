import streamlit as st
from requests_func import get_bikes, update_bikes
from validations import validate_cpf

status_options = ["Disponivel", "Em uso"]

st.title("Editar bicicleta")

if "bike_id" not in st.session_state:
    st.switch_page("pages/Bikes.py")

bike = get_bikes(st.session_state.bike_id)

modelo = st.text_input("modelo", value=bike["modelo"])

marca = st.text_input("marca", value=bike["marca"])

cidade = st.text_input("cidade", value=bike["cidade"])

status = st.radio("status", options=status_options, index=status_options.index(bike["status"]))

upd_auth = modelo and marca and cidade and status

if st.button("Atualizar credenciais", disabled=not(upd_auth)):
    try:
        update_bikes(st.session_state.bike_id, {"modelo": modelo, "marca": marca, "cidade": cidade, "status": status})
    except:
        st.error("Error ao atualizar usuário")
    else:
        st.success("Usuário atualizado com sucesso")










