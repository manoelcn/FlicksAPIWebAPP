import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    col1, col2 = st.columns(2, gap='small')
    with col1:
        if genres:
            st.title('Lista de gêneros')
            genres_df = pd.json_normalize(genres)
            AgGrid(
                data=genres_df,
                reload_data=True,
                key='genres_grid',
            )
        else:
            st.warning('Nenhum gênero encontrado.')

    with col2:
        st.title('Opções')

        @st.experimental_dialog("Cadastrar novo gênero", width='small')
        def modal_genre():
            name = st.text_input('Nome do gênero')
            if st.button('Cadastrar'):
                new_genre = genre_service.create_genre(
                    name=name,
                )
                if new_genre:
                    st.rerun()
                else:
                    st.error('Erro ao cadastrar o gênero. Verifique os campos')

        if st.button("Cadastrar Gênero"):
            modal_genre()
