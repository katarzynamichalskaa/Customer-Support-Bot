import Responses
from Responses import chatbot

counter = 0

if __name__ == "__main__":

    while True:
        chatbot(counter)
        counter = counter + 1
