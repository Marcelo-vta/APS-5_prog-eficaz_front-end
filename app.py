import streamlit as st
import requests
from api_url import URL
from validations import validate_cpf
import time
from streamlit_extras.let_it_rain import rain

st.title("Aluguel de bicicletas")

col1, col2, col3 = st.columns(3)

if col1.button("Usuários"):
    rain(
        emoji="👤",
        font_size=54,
        falling_speed=1,
        animation_length=2,
    )
    time.sleep(2)
    st.switch_page("pages/Usuarios.py")

if col2.button("Bikes"):
    rain(
        emoji="🚲",
        font_size=54,
        falling_speed=1,
        animation_length=2,
    )
    time.sleep(2)
    st.switch_page("pages/Bikes.py")

if col3.button("Emprestimos"):
    rain(
        emoji="🤝",
        font_size=54,
        falling_speed=1,
        animation_length=2,
    )
    time.sleep(2)
    st.switch_page("pages/Emprestimos.py")

