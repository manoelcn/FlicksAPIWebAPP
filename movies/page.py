import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from movies.service import MovieService
from actors.service import ActorService
from genres.service import GenreService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.title('Lista de filmes')
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        AgGrid(
            data=movies_df,
            reload_data=True,
            key='movies_grid',
        )
    else:
        st.warning('Nenhum filme encontrado.')

    st.divider()

    st.title('Opções')

    @st.experimental_dialog("Cadastrar novo filme", width='small')
    def modal_movie():
        title = st.text_input('Título')
        genre_service = GenreService()
        genres = genre_service.get_genres()
        genre_names = {genre['name']: genre['id'] for genre in genres}
        selected_genre_name = st.selectbox('Gênero', list(genre_names.keys()))
        release_date = st.date_input(
            label='Data de lançamento',
            value=datetime.today(),
            min_value=datetime(1800, 1, 1),
            max_value=datetime.today(),
            format='DD/MM/YYYY',
        )
        actor_service = ActorService()
        actors = actor_service.get_actors()
        actor_names = {actor['name']: actor['id'] for actor in actors}
        selected_actors_name = st.multiselect('Ator', list(actor_names.keys()), placeholder='Selecione os atores')
        selected_actors_ids = [actor_names[name] for name in selected_actors_name]
        resume = st.text_area('Resumo')

        if st.button('Cadastrar'):
            new_movie = movie_service.create_movie(
                title=title,
                genre=genre_names[selected_genre_name],
                release_date=release_date,
                actors=selected_actors_ids,
                resume=resume
            )
            if new_movie:
                st.rerun()
            else:
                st.error('Erro ao cadastrar o filme. Verifique os campos')

    if st.button("Cadastrar Filme"):
        modal_movie()
