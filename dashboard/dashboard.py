import streamlit as st
import matplotlib as mpl
from scraper.scraper import read_games

# plot style
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.serif'] = ['Roboto', 'DejaVu Sans', 'Arial']
mpl.rcParams['font.size'] = 12
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.titlesize'] = 16
mpl.rcParams['axes.titlepad'] = 4
mpl.rcParams['axes.titleweight'] = 400

# dark mode
mpl.rcParams['figure.facecolor'] = '#0e1117'
mpl.rcParams['axes.facecolor'] = '#0e1117'
mpl.rcParams['axes.edgecolor'] = 'grey'
mpl.rcParams['axes.labelcolor'] = 'white'
mpl.rcParams['axes.titlecolor'] = 'white'
mpl.rcParams['xtick.color'] = 'white'
mpl.rcParams['ytick.color'] = 'white'
mpl.rcParams['text.color'] = 'white'

# dpi and figsize
mpl.rcParams['figure.dpi'] = 100
mpl.rcParams['figure.figsize'] = (8, 6)

# load data
st.session_state.df = read_games('scraper/games.csv')
st.session_state.cols_dict = {
    'Złożoność gry': 'complexity',
    'Średnia ocena': 'avg_rating',
    'Odchylenie standardowe ocen': 'std_rating',
    'Rok wydania gry': 'year',
    'Minimalna liczba graczy': 'min_players',
    'Maksymalna liczba graczy': 'max_players',
    'Minimalny czas gry': 'min_play_time',
    'Maksymalny czas gry': 'max_play_time',
    'Minimalny wiek graczy': 'min_age',
    'Liczba ocen': 'ratings',
    'Liczba ocen oceny 1': 'ratings_1',
    'Liczba ocen oceny 2': 'ratings_2',
    'Liczba ocen oceny 3': 'ratings_3',
    'Liczba ocen oceny 4': 'ratings_4',
    'Liczba ocen oceny 5': 'ratings_5',
    'Liczba ocen oceny 6': 'ratings_6',
    'Liczba ocen oceny 7': 'ratings_7',
    'Liczba ocen oceny 8': 'ratings_8',
    'Liczba ocen oceny 9': 'ratings_9',
    'Liczba ocen oceny 10': 'ratings_10',
    'Liczba komentarzy': 'comments',
    'Liczba fanów': 'fans',
    'Liczba wyświetleń strony': 'page_views',
    'Liczba rozgrywek': 'plays',
    'Liczba rozgrywek w miesiącu': 'plays_month',
    'Liczba posiadaczy': 'owners',
    'Liczba poprzednich posiadaczy': 'prev_owned',
    'Liczba gier na wymianę': 'for_trade',
    'Liczba gier do wymiany': 'want_in_trade',
    'Liczba gier na liście życzeń': 'wishlist',
    'Alternatywne nazwy': 'alternate_names',
    'Projektanci': 'designers',
    'Artyści': 'artists',
    'Wydawcy': 'publishers'
}

st.set_page_config(page_title='BGG Dashboard', page_icon='🎲',
                   initial_sidebar_state='expanded', menu_items={
                     'Get Help': None,
                     'Report a bug': None,
                     'About': None
                   })

info = st.Page("info.py", title="Informacje", icon=":material/article:") #icon=":material/info:")
dataset = st.Page("dataset.py", title="Zbiór danych", icon=":material/table_chart:")
statistics = st.Page("stats.py", title="Statystyki opisowe", icon=":material/bar_chart:")
eda = st.Page("eda.py", title="Analiza eksploracyjna", icon=":material/scatter_plot:")
importance = st.Page("importance.py", title="Ważność zmiennych", icon=":material/insights:")

pg = st.navigation([info, dataset, statistics, eda, importance])
pg.run()
