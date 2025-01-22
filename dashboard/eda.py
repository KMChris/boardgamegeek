import streamlit as st
import matplotlib.pyplot as plt

st.title("Zależności między zmiennymi")

st.header("Wykres korelacji")
fig, ax = plt.subplots()
corr = st.session_state.df.select_dtypes(include=['number']).corr()
cax = ax.matshow(corr)
fig.colorbar(cax)
ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=90, fontsize=8)
ax.set_yticklabels(corr.columns, fontsize=8)
plt.title('Korelacje między zmiennymi numerycznymi', pad=20)
st.pyplot(fig)

st.header("Wykres punktowy")
st.text("Wybierz dwie zmienne, aby zobaczyć ich zależność na wykresie punktowym.")
cols = st.session_state.cols_dict
x_var = st.selectbox('Wybierz zmienną X', cols.keys(), index=0)
y_var = st.selectbox('Wybierz zmienną Y', cols.keys(), index=1)
fig, ax = plt.subplots()
ax.scatter(st.session_state.df[cols[x_var]], st.session_state.df[cols[y_var]], alpha=0.6)
ax.set_title(f"{y_var} vs {x_var}")
ax.set_xlabel(x_var)
ax.set_ylabel(y_var)
st.pyplot(fig)

st.header("Rozkład zmiennej")
st.text("Wybierz zmienną, aby zobaczyć jej rozkład.")
var = st.selectbox('Wybierz zmienną', cols.keys(), index=0)
fig, ax = plt.subplots()
st.session_state.df[cols[var]].plot(kind='hist', bins=30, ax=ax)
ax.set_title(f'Rozkład zmiennej {var}')
ax.set_xlabel(var)
ax.set_ylabel('Liczba obserwacji')
st.pyplot(fig)
