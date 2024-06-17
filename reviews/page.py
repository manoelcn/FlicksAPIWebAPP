import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from reviews.service import ReviewService
from movies.service import MovieService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    col1, col2 = st.columns(2, gap='small')
    with col1:
        if reviews:
            st.title('Lista de avaliações')
            reviews_df = pd.json_normalize(reviews)
            AgGrid(
                data=reviews_df,
                reload_data=True,
                key='reviews_grid',
            )
        else:
            st.warning('Nenhuma avaliação encontrada.')

    with col2:

        st.title('Opções')

        @st.experimental_dialog("Cadastrar nova avaliação", width='small')
        def modal_review():
            movie_service = MovieService()
            movies = movie_service.get_movies()
            movie_titles = {movie['title']: movie['id'] for movie in movies}
            selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))
            stars = st.number_input(
                label='Estrelas',
                min_value=0,
                max_value=5,
                step=1
            )
            comment = st.text_area('Comentário', max_chars=200)

            if st.button('Cadastrar'):
                new_review = review_service.create_reviews(
                    movie=movie_titles[selected_movie_title],
                    stars=stars,
                    comment=comment
                )
                if new_review:
                    st.rerun()
                else:
                    st.error('Erro ao cadastrar a avaliação. Verifique os campos.')

        if st.button("Cadastrar avaliação"):
            modal_review()
