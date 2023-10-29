from CheckOpinion import WebRequester

webRequester = WebRequester()


class ChatBot:

    def user_input_holder(self):

        user_input = input("> ")

        if "Check" in user_input:
            parts = user_input.split("Check ", 1)
            if len(parts) == 2:
                second_part = parts[1]
                URL = webRequester.initRequest(second_part)
                find = webRequester.Find(URL)
                self.sort_option(find)

            else:
                print(
                    "I'm sorry, the message format is incorrect. Please insert your message in this format: Check {something}")
        else:
            print("I'm sorry, I can't help you with that. Please insert your message in this format: Check {something}")
    def start_conversation(self, counter):
        if counter == 0:
            print("Hi! How can I help you?")
        else:
            print("What else can I do for you?")

        self.user_input_holder()

    def sort_option(self, find):
        print("Should I sort list of product by rate or by price?")
        user_answer = input("> ")

        while user_answer != "rate" or user_answer != "Rate" or user_answer != "price" or user_answer != "Price":
            if user_answer == "rate" or user_answer == "Rate":
                webRequester.BestRated(find)
                break
            elif user_answer == "price" or user_answer == "Price":
                webRequester.LowestPrice(find)
                break
            else:
                print("Please answer my question first: should I sort by price or rate?")
                user_answer = input("> ")


