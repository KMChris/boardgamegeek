import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Zależności między zmiennymi")

st.header("Wykres korelacji")

@st.cache_data(hash_funcs={pd.DataFrame: lambda df: df.shape})
def plot_correlation_matrix(df):
    fig, ax = plt.subplots()
    corr = df.select_dtypes(include=['number']).corr()
    cax = ax.matshow(corr)
    fig.colorbar(cax)
    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=90, fontsize=8)
    ax.set_yticklabels(corr.columns, fontsize=8)
    ax.set_title('Korelacje między zmiennymi numerycznymi', pad=20)
    return fig
plot = plot_correlation_matrix(st.session_state.df)
st.pyplot(plot, clear_figure=True)

st.header("Wykres punktowy")
st.text("Wybierz dwie zmienne, aby zobaczyć ich zależność na wykresie punktowym.")
cols = st.session_state.cols_dict
x_var = st.selectbox('Wybierz zmienną X', cols.keys(), index=0)
y_var = st.selectbox('Wybierz zmienną Y', cols.keys(), index=1)

@st.cache_data(hash_funcs={pd.DataFrame: lambda df: df.shape})
def plot_boxplot(df, x_var, y_var):
    fig, ax = plt.subplots()
    df.plot.scatter(x=x_var, y=y_var, ax=ax)
    ax.set_title(f"{y_var} vs {x_var}")
    ax.set_xlabel(x_var)
    ax.set_ylabel(y_var)
    return fig
plot = plot_boxplot(st.session_state.df, cols[x_var], cols[y_var])
st.pyplot(plot, clear_figure=True)

st.header("Rozkład zmiennej")
st.text("Wybierz zmienną, aby zobaczyć jej rozkład.")
var = st.selectbox('Wybierz zmienną', cols.keys(), index=0)

@st.cache_data(hash_funcs={pd.DataFrame: lambda df: df.shape})
def plot_histogram(df, var):
    fig, ax = plt.subplots()
    df[var].plot(kind='hist', bins=30, ax=ax)
    ax.set_title(f'Rozkład zmiennej {var}')
    ax.set_xlabel(var)
    ax.set_ylabel('Liczba obserwacji')
    return fig
plot = plot_histogram(st.session_state.df, cols[var])
st.pyplot(plot, clear_figure=True)
