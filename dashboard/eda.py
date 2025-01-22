import streamlit as st
import pandas as pd
import altair as alt

st.title("Zależności między zmiennymi")

st.header("Wykres korelacji")

@st.cache_data(hash_funcs={pd.DataFrame: lambda df: df.shape})
def plot_correlation_matrix(df):
    corr = df.select_dtypes(include=['number']).corr().stack().reset_index()
    corr.columns = ['Zmienna 1', 'Zmienna 2', 'Korelacja']
    chart = alt.Chart(corr).mark_rect().encode(
        x=alt.X('Zmienna 1:O', title=None),
        y=alt.Y('Zmienna 2:O', title=None),
        color='Korelacja:Q'
    ).properties(
        width=600,
        height=600,
        title='Korelacje między zmiennymi numerycznymi'
    )
    return chart
plot = plot_correlation_matrix(st.session_state.df)
st.altair_chart(plot, use_container_width=True)

st.header("Wykres punktowy")
st.text("Wybierz dwie zmienne, aby zobaczyć ich zależność na wykresie punktowym.")
cols = st.session_state.cols_dict
x_var = st.selectbox('Wybierz zmienną X', cols.keys(), index=0)
y_var = st.selectbox('Wybierz zmienną Y', cols.keys(), index=1)

@st.cache_data(hash_funcs={pd.DataFrame: lambda df: df.shape})
def plot_scatter(df, x_var, y_var, cols):
    chart = alt.Chart(df).mark_point().encode(
        x=alt.X(cols[x_var], scale=alt.Scale(zero=False), title=x_var),
        y=alt.Y(cols[y_var], scale=alt.Scale(zero=False), title=y_var),
        tooltip=[cols[x_var], cols[y_var]]
    ).properties(
        title=f"{y_var} vs {x_var}",
        width=600,
        height=500
    )
    return chart
plot = plot_scatter(st.session_state.df, x_var, y_var, cols)
st.altair_chart(plot, use_container_width=True)

st.header("Rozkład zmiennej")
st.text("Wybierz zmienną, aby zobaczyć jej rozkład.")
var = st.selectbox('Wybierz zmienną', cols.keys(), index=0)

@st.cache_data(hash_funcs={pd.DataFrame: lambda df: df.shape})
def plot_histogram(df, var, cols):
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X(cols[var], bin=alt.Bin(maxbins=30), title=var),
        y=alt.Y('count()', title='Liczba obserwacji'),
        tooltip=[cols[var], 'count()']
    ).properties(
        title=f'Rozkład zmiennej {var}',
        width=600,
        height=400
    )
    return chart
plot = plot_histogram(st.session_state.df, var, cols)
st.altair_chart(plot, use_container_width=True)
