import streamlit as st
import plotly.express as px
from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Estatísticas dos filmes')

    col1, col2 = st.columns(2, gap='medium')
    with col1:
        if len(movie_stats['movies_by_genre']) > 0:
            fig = px.pie(
                movie_stats['movies_by_genre'],
                values='count',
                names='genre__name',
                title='Filmes por Gênero',
            )
            st.plotly_chart(fig)

    with col2:
        st.subheader('Total de filmes cadastrados')
        st.write(f':gray-background[{movie_stats["total_movies"]}]')

        st.subheader('Total de avaliações cadastradas')
        st.write(f':gray-background[{movie_stats["total_reviews"]}]')

        st.subheader('Quantidade de filmes por gênero')
        for genre in movie_stats['movies_by_genre']:
            st.write(f':gray-background[{genre["genre__name"]}: {genre["count"]}]')
