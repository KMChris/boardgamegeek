import streamlit as st

st.title("Tabela danych")

cols = st.session_state.df.columns
selected_cols = st.multiselect('Wybierz kolumny', cols, default=['name', 'year', 'complexity', 'ratings', 'avg_rating', 'std_rating', 'comments', 'plays'])
st.write(st.session_state.df[selected_cols])
