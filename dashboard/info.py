import streamlit as st

st.title("Analiza gier planszowych")
st.markdown("""
## O autorze
Krzysztof Mizgała,  
student na kierunku Matematyka II stopnia,  
Politechnika Wrocławska

## Cel analizy
Analiza danych ma na celu odpowiedzenie na następujące pytania:
1. Czy istnieją zależności między zmiennymi, np. czy złożoność gry wpływa na czas gry?
2. Jakie cechy gier mają wpływ na lepszą ocenę gry?
3. Które cechy wpływają na największą spójność ocen, czyli czy gra jest oceniana podobnie przez różnych użytkowników?

## Opis danych
Dane o&nbsp;grach planszowych pochodzą z&nbsp;serwisu [BoardGameGeek](https://boardgamegeek.com/).
Mamy przygotowane 10&nbsp;tys. wierszy i&nbsp;36 kolumn, z&nbsp;których 6&nbsp;to zmienne
kategoryczne, a&nbsp;30 to kolumny z&nbsp;danymi liczbowymi.
Zebrane dane zostały podzielone na kilka kategorii:

#### Podstawowe informacje
- Nazwa (`name`)
- Rok wydania (`year`)
- Opis (`description`)
- Wymagana liczba graczy (`min_players`, `max_players`)
- Czas gry (`min_playtime`, `max_playtime`)
- Wymagany wiek (`min_age`)
- Złożoność gry (`complexity`)
- Alternatywne nazwy (`alternate_names`)
- Projektanci (`designers`)
- Artyści (`artists`)
- Wydawcy (`publishers`)

#### Opinie
- Liczba ocen (`ratings`)
- Średnia ocena (`avg_rating`)
- Odchylenie standardowe (`std_rating`)
- Rozkład ocen (`ratings_1`, `ratings_2`, ..., `ratings_10`)

#### Statystyki gry
- Liczba komentarzy (`comments`)
- Liczba fanów (`fans`)
- Wyświetlenia strony (`page_views`)

#### Statystyki rozgrywek
- Liczba rozgrywek (`plays`)
- Liczba rozgrywek w tym miesiącu (`plays_month`)

#### Dane na temat posiadania gry
- Liczba osób posiadających grę (`owners`)
- Liczba osób, które posiadały grę (`prev_owned`)
- Liczba osób, które chcą sprzedać grę (`for_trade`)
- Liczba osób, które chcą kupić grę (`want_in_trade`)
- Liczba osób, które mają grę na liście życzeń (`wishlist`)

## Korzyści z analizy
Dzięki niniejszej analizie możliwe będzie zidentyfikowanie kluczowych czynników,
które decydują o&nbsp;popularności i&nbsp;jakości gier planszowych.
Analiza może również pomóc w zrozumieniu, jakie cechy przyciągają różnych użytkowników,
co może być przydatne zarówno dla projektantów gier, jak i&nbsp;dla społeczności graczy.
""")
