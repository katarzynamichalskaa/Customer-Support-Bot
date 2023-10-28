import nltk
from nltk.chat.util import Chat, reflections
from CheckOpinion import initRequest
from CheckOpinion import LowestPrice
from CheckOpinion import Find
from CheckOpinion import BestRated
import threading

pairs = [
    [
        r"Sprawdź (.*)",
        ["Już sprawdzam, daj mi chwilę..."]

    ],
    [
        r"witaj|cześć|hej",
        ["Cześć!"]
    ],
    [
        r"jak się masz?",
        ["Dobrze, dziękuję! Jak mogę ci dzisiaj pomóc?"]
    ],
    [
        r".*",
        ["Przepraszam, nie rozumiem Cię."]
    ],
    [
        r"co możesz zrobić",
        ["Jestem prostym chatbotem i mogę pomóc Ci znaleźć . Spróbuj zapytać o coś!"]
    ],
    [
        r"zamówienie|kupić|produkt",
        ["Przepraszam, ale jestem tylko chatbotem i nie mogę dokonywać zakupów. Jednak mogę ci doradzić w wyborze produktu."]
    ],
    [
        r"jak mogę cię kontaktować",
        ["Jestem dostępny tutaj przez ten chat. Jak mogę ci pomóc?"]
    ],
    [
        r"do widzenia",
        ["Do widzenia! Miłego dnia!"]
    ],
]

# Ustawienia rozpoznawania
def chatbot():
    user_input = ""  # Inicjalizacja zmiennej do przechowywania wpisanego słowa
    print("Witaj! Jestem twój chatbot. Jaki produkt mam dla Ciebie sprawdzić?")
    chat = Chat(pairs, reflections)

    chat.converse()

    while True:
        user_message = input("> ")
        user_input_match = reflections.match(r"Sprawdź (.*)", user_message)
        if user_input_match:
            print("ok")
            user_input = user_input_match.group(1)
            URL = initRequest(user_input)
            find = Find(URL)
            # LowestPrice(tab)
            BestRated(find)