import streamlit as st
from login.service import login


def show_login():
    st.title('Login')

    with st.container(border=True):
        username = st.text_input(label='Usuário', placeholder='Digite seu usuário')
        password = st.text_input(
            label='Senha',
            type='password',
            placeholder='Digite sua senha'
        )

        if st.button('Login', use_container_width=True, type='primary'):
            login(
                username=username,
                password=password
            )
