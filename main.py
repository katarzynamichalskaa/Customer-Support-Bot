import Responses
from Responses import ChatBot

counter = 0
chatBot = ChatBot()

if __name__ == "__main__":
    while True:
        chatBot.start_conversation(counter)
        counter = counter + 1
