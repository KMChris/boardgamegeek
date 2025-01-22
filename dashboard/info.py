import streamlit as st

st.title("Strona informacyjna")
st.markdown("""
## O autorze
Krzysztof Mizgała,
student Matematyki 2 stopnia,
Politechnika Wrocławska

## Cel analizy
Celem analizy danych jest zbadanie:
- czy istnieją zależności między zmiennymi, np. czy złożoność gry wpływa na czas gry,
- jakie cechy gier mają wpływ na lepszą ocenę gry,
- jakie cechy wpływają na największą spójność ocen, czyli czy gra jest oceniana podobnie przez różnych użytkowników.

## Opis danych
Dane o grach planszowych pochodzą z serwisu [BoardGameGeek](https://boardgamegeek.com/).
Mamy przygotowane 10 tys. wierszy i 36 kolumn, z których 6 to zmienne
kategoryczne, a 30 to kolumny z danymi liczbowymi.
Zebrane dane zawierają następujące kolumny:

1. Podstawowe informacje:
   - Nazwa (name)
   - Rok wydania (year)
   - Opis (description)
   - Wymagana liczba graczy (min_players, max_players)
   - Czas gry (min_playtime, max_playtime)
   - Wymagany wiek (min_age)
   - Złożoność gry (complexity)
   - Alternatywne nazwy (alternate_names)
   - Projektanci (designers)
   - Artyści (artists)
   - Wydawcy (publishers)

2. Opinie:
   - Liczba ocen (ratings)
   - Średnia ocena (avg_rating)
   - Odchylenie standardowe (std_rating)
   - Rozkład ocen (ratings_1, ratings_2, ..., ratings_10)

3. Statystyki gry:
   - Liczba komentarzy (comments)
   - Liczba fanów (fans)
   - Wyświetlenia strony (page_views)

4. Statystyki rozgrywek:
   - Liczba rozgrywek (plays)
   - Liczba rozgrywek w tym miesiącu (plays_month)

5. Dane na temat posiadania gry:
   - Liczba osób posiadających grę (owners)
   - Liczba osób, które posiadały grę (prev_owned)
   - Liczba osób, które chcą sprzedać grę (for_trade)
   - Liczba osób, które chcą kupić grę (want_in_trade)
   - Liczba osób, które mają grę na liście życzeń (wishlist)
""")
