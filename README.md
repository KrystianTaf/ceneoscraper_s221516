# ceneoscraper_s221516

## Struktura opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|Składowa opinii|Selektor|Nazwa zmiennej|Typ danych|
|---------------|--------|--------------|----------|
|opinia|div.js_product-review|opinion|bs4.element.Tag|
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id||
|autor opinii|span.user-post__author-name|author||
|rekomendacja autora|span.user-post__author-recomendation > em|recomendation||
|liczba gwiazdek|span.user-post__score-count|stars||
|treść opinii|div.user-post__text|content||
|lista zalet|div[class$=positives] ~ div.review-feature__item|pros||
|lista wad|div[class$=negatives] ~ div.review-feature__item|cons||
|dla ilu osób przydatna|button.vote-yes > span|useful||
|dla ilu osób nieprzydatna|button.vote-no > span|useless||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|published||
|data zakupu produktu|span.user-post__published > time:nth-child(2)["datetime"]|purchased||

## Etapy pracy nad projektem struktularnym
1. Pobranie elementów pojedyńczej opinii do niezależnych zmiennych
2. Zapisanie wszystkich elementów pojedyńczej opinii do jednej zmiennej \(słownik\)
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i dodanie ich do listy 
4. Pobranie wszystkich opinii o produkcie z wszystkich stron i zapisanie ich do pliku .json
5. Dodanie możliwości podania id produktu przez użytkownika za pomkocą klawiatury
6. Refaktoryzacja \(optymalizacja\) kodu:
    a. utworzenie funkcji do pobierania składowych strony HTML
    b. utworzenie słownika opisującego atrukturę opinii wraz z selektorami poszczególnych elementów
    c. zamiana instrukcji pobierających składowe opinii do pojedyńczych zmiennych i tworzących z nich słownik na wyrażenia słownikowe \(dictionry comprehension\) tworzące słownik reprezentujący pojedynczą opinię na podstawie słownika selektorów
7. Analiza opinii o wybranym produkcie
    a. wczytywanie wszystkich opinii o wskazanym produkcie do obiektu DataFrame
    b. wyliczanie podstawowych statystyk na podstawie produktu
        - liczba wszystkich opinii o produkcie
        - liczba opinii w których autor podał listę zalet produktu
        - liczba opinii w których autor podał listę wad produktu
        - średnia ocen produktu
    c. przygotowania wykresów na podstawie zawartości opinii
        - udział poszczególnych rekomendacji w ogólnej liczbie opinii
        - hitogram częstości występowania poszczególnych oden (liczby gwiazdek)
