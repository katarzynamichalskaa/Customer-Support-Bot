import nltk
from nltk.chat.util import Chat, reflections
from CheckOpinion import initRequest
from CheckOpinion import LowestPrice
from CheckOpinion import Find
from CheckOpinion import BestRated


# Ustawienia rozpoznawania
def chatbot(counter):

    if counter == 0:
        print("Hi! How can I help you?")
    else:
        print("What else can I do for you?")


    user_input = input("> ")

    if "Check" in user_input:
        parts = user_input.split("Check ", 1)
        if len(parts) == 2:
            second_part = parts[1]
            URL = initRequest(second_part)
            find = Find(URL)
            # LowestPrice(tab)
            BestRated(find)
        else:
            print("I'm sorry, the message format is incorrect. Please insert your message in this format: Check {something}")
    else:
        print("I'm sorry, I can't help you with that. Please insert your message in this format: Check {something}")