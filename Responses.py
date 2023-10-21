import nltk
from nltk.chat.util import Chat, reflections

pairs = [
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
        ["Jestem prostym chatbotem i mogę odpowiadać na twoje pytania. Spróbuj zapytać o coś!"]
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
    print("Witaj! Jestem twój chatbot. Pytaj mnie o cokolwiek, a postaram się odpowiedzieć.")
    chat = Chat(pairs, reflections)
    chat.converse()