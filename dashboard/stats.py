import streamlit as st
import pandas as pd

st.title("Statystyki opisowe")

st.header("Opis danych liczbowych")
st.write(st.session_state.df.describe().T[['mean', 'std', 'min', '25%', '50%', '75%', 'max']])

st.header("Najczęściej występujące wartości")
cols = {
    'Artyści': 'artists',
    'Projektanci': 'designers',
    'Wydawcy': 'publishers',
    'Alternatywne nazwy': 'alternate_names'
}
col = st.selectbox('Wybierz kolumnę', cols.keys(), index=0)
data = st.session_state.df[cols[col]].explode().value_counts().reset_index().values
st.write(pd.DataFrame(data, columns=[col, 'Liczba gier']).set_index(col))
