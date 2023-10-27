import Responses
from Responses import chatbot
import CheckOpinion
from CheckOpinion import initRequest
from CheckOpinion import LowestPrice
from CheckOpinion import Find
from CheckOpinion import BestRated


if __name__ == "__main__":

    #chatbot()
    item = "lalka"
    URL = initRequest(item)
    tab = Find(URL)
    #LowestPrice(tab)
    BestRated(tab)