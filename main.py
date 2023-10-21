import Responses
from Responses import chatbot
import CheckOpinion
from CheckOpinion import initRequest
from CheckOpinion import CheckLowestPrice
from CheckOpinion import Find


if __name__ == "__main__":

    #chatbot()
    item = "iphone"
    URL = initRequest(item)
    tab = Find(URL)
    print(tab)
    CheckLowestPrice(tab)
