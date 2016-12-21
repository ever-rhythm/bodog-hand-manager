
from main.const import Const as C

class Convertor(object):
    
    def __init__(self):
        pass

    def convert(self , objHand):

        listHand = []
        listHand.append(objHand.getTable())
        listHand.append(objHand.getPreflop())
        listHand.append(objHand.getFlop())
        listHand.append(objHand.getTurn())
        listHand.append(objHand.getRiver())
        listHand.append(objHand.getShowdown())
        listHand.append(objHand.getSummary())

        return C.sep.join( str(i) for i in listHand if 0 != len(i) )
