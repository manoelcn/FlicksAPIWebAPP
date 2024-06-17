import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    col1, col2 = st.columns(2, gap='small')
    with col1:
        if actors:
            st.title('Lista de atores')
            actors_df = pd.json_normalize(actors)
            AgGrid(
                data=actors_df,
                reload_data=True,
                key='actors_grid',
            )
        else:
            st.warning('Nenhum Ator encontrado')

    with col2:
        st.title('Opções')

        @st.experimental_dialog("Cadastrar novo gênero", width='small')
        def modal_actor():
            name = st.text_input('Nome do ator')
            birthday = st.date_input(
                label='Data de nascimento',
                value=datetime.today(),
                min_value=datetime(1800, 1, 1),
                max_value=datetime.today(),
                format='DD/MM/YYYY',
            )
            nationality_dropdown = ['BR', 'EUA', 'OUTROS']
            nationality = st.selectbox(
                label='Nacionalidade',
                options=nationality_dropdown,
            )

            if st.button('Cadastrar'):
                new_actor = actor_service.create_actor(
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                )
                if new_actor:
                    st.rerun()
                else:
                    st.error('Erro ao cadastrar ator. Verifique os campos')

        if st.button("Cadastrar Ator"):
            modal_actor()
