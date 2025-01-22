import streamlit as st

st.title("Tabela danych")

df = st.session_state.df

st.subheader("Filtrowanie danych")

rating_filter = st.slider('Średnia ocena', min_value=0.0, max_value=10.0, value=(0.0, 10.0))
std_filter = st.slider('Odchylenie standardowe', min_value=df.std_rating.min(), max_value=df.std_rating.max(), value=(df.std_rating.min(), df.std_rating.max()))

col1, col2 = st.columns(2)
with col1:
    min_year = st.number_input('Minimalny rok', min_value=int(df['year'].min()), max_value=int(df['year'].max()), value=int(df['year'].min()))
    min_players = st.number_input('Minimalna liczba graczy', min_value=int(df['min_players'].min()), max_value=int(df['max_players'].max()), value=int(df['min_players'].min()))
    min_time = st.number_input('Minimalny czas gry (minuty)', min_value=int(df['min_play_time'].min()), max_value=int(df['max_play_time'].max()), value=int(df['min_play_time'].min()))
with col2:
    max_year = st.number_input('Maksymalny rok', min_value=int(df['year'].min()), max_value=int(df['year'].max()), value=int(df['year'].max()))
    max_players = st.number_input('Maksymalna liczba graczy', min_value=int(df['min_players'].min()), max_value=int(df['max_players'].max()), value=int(df['max_players'].max()))
    max_time = st.number_input('Maksymalny czas gry (minuty)', min_value=int(df['min_play_time'].min()), max_value=int(df['max_play_time'].max()), value=int(df['max_play_time'].max()))

complexity_filter = st.slider('Złożoność gry', min_value=1.0, max_value=5.0, value=(1.0, 5.0))

filtered_df = df[
    (df['year'] >= min_year) & (df['year'] <= max_year) &
    (df['min_players'] >= min_players) & (df['max_players'] <= max_players) &
    (df['min_play_time'] >= min_time) & (df['max_play_time'] <= max_time) &
    (df['avg_rating'] >= rating_filter[0]) & (df['avg_rating'] <= rating_filter[1]) &
    (df['std_rating'] >= std_filter[0]) & (df['std_rating'] <= std_filter[1]) &
    (df['complexity'] >= complexity_filter[0]) & (df['complexity'] <= complexity_filter[1])
]

cols = df.columns
selected_cols = st.multiselect('Wybierz kolumny do wyświetlenia', cols, default=['name', 'year', 'complexity', 'ratings', 'avg_rating', 'std_rating', 'comments', 'plays'])

st.write(filtered_df[selected_cols])
