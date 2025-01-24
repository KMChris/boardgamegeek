# Analiza danych o grach planszowych

*Pozyskiwanie i wizualizacja danych o grach planszowych z BoardGameGeek*

## Przegląd

Projekt składa się z dwóch głównych części:

1. **Scraper**: Narzędzie do zbierania szczegółowych danych o grach planszowych z [BoardGameGeek](https://boardgamegeek.com).
2. **Dashboard**: Interaktywny interfejs do wizualizacji i analizy zebranych danych.

Repozytorium zostało stworzone, aby pomóc entuzjastom, analitykom i deweloperom w eksplorowaniu trendów, statystyk i innych ciekawych informacji o grach planszowych.

## Funkcje

- **Scraper**:\
  Zbiera dane, takie jak tytuły gier planszowych, oceny, złożoność gry, projektanci i wiele innych z BoardGameGeek.\
  Szczegółowe instrukcje dotyczące konfiguracji i użytkowania znajdują się w pliku `scraper/raport.pdf`.

- **Dashboard**:\
  Interaktywna wizualizacja zebranych danych z wykorzystaniem [Streamlit](https://streamlit.io).\
  Zawiera sortowalne tabele z filtrami i interaktywne wykresy.

## Pierwsze kroki

### Wymagania

- Python 3.9+
- Wszystkie wymagane biblioteki są wymienione w pliku `requirements.txt`.

### Instalacja

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/KMChris/boardgamegeek.git
   cd boardgamegeek
   ```
2. Zainstaluj wymagane zależności:
   ```bash
   pip install -r requirements.txt
   ```

### Uruchamianie Dashboardu

Aby uruchomić dashboard, użyj:
```bash
streamlit run dashboard.py
```

Dashboard uruchomi się w domyślnej przeglądarce internetowej.

### Używanie Scraper'a

Instrukcje dotyczące konfiguracji i uruchamiania scraper'a znajdują się w pliku `scraper/raport.pdf`.\
Upewnij się, że postępujesz zgodnie z krokami opisanymi w dokumencie, aby poprawnie skonfigurować narzędzie.

## Licencja

Projekt jest licencjonowany na zasadach licencji MIT. Szczegóły znajdują się w pliku [LICENSE](LICENSE).
