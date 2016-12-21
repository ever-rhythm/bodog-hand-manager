
from main.const import Const as C
from main.util import Util as U

class Hand(object):

    def __init__(self):
        self.lobby = ''
        self.handId = ''
        self.game = ''
        self.date = ''
        self.table = ''
        
        self.sb = 0.0
        self.bb = 0.0
        self.pos = ''

        self.dictName = {}
        self.dictSeat = {}
        self.dictCard = {}
        self.dictStack = {}
        self.dictAction = {}

        for (k,v) in C.pairStreet:
            self.dictCard[v] = ''
            self.dictAction[v] = {}
            self.dictStack[v] = 0

            for (k2,v2) in C.pairPos:
                self.dictAction[v][v2] = []
                #self.dictStack[v][v2] = []
                
    # todo
    def getRake(self):
        return 0.01
                
    def getChip(self , flt):
        return '$' + str('%.2f'%float(flt))
    
    def getCard(self , listCard , bolDivide = False):
        if bolDivide :
            return '[' + U.ret(listCard[:-1],' ') + ']' + ' [' + listCard[-1:][0] + ']'
        else:
            return '[' + U.ret(listCard,' ') + ']'

    def getStreet(self , strStreet):
        listRes = []
        idx = 2 if strStreet == C.preflop else 0
        rounds = 0
        for i in self.dictAction[strStreet]:
            rounds = max(rounds,len(self.dictAction[strStreet][i]))
            
        #print(rounds)
        # todo raise val
        for i in list(range(0,rounds)):
            for j in list(range(idx,len(C.pairPos))):
                (k,pos) = C.pairPos[j]
                if i < len(self.dictAction[strStreet][pos]):
                    (act,val) = self.dictAction[strStreet][pos][i]
                    val = self.getChip(val) if len(val) > 0 else ''
                    name = self.dictName[pos]
                    strRes = name + ': ' + act.lower() + ' ' + val
                    if C.raises == act:
                        strRes += ' to ' + val
                    listRes.append(strRes)
            
            # next round
            idx = 0
        
        return U.ret(listRes)

    # todo date convert
    def getTable(self):
        listRes = []
        listRes.append( self.lobby + ' Hand #' + self.handId + ': ' + self.game + ' (' + self.getChip(self.sb) + '/' + self.getChip(self.bb) + ' USD) - ' + str.replace(self.date,'-','/') + ' ET' )
        listRes.append( 'Table ' + '\'' + self.table + '\'' + ' ' + str(len(self.dictSeat)) + '-max Seat #' + self.dictSeat[C.btn] + ' is the button' )

        listTmp = sorted(self.dictSeat.items() , key = lambda x:x[1])
        #print(self.dictStack)
        #print(self.dictName)
        for (pos,seat) in listTmp:
            listRes.append( C.seat + seat + ': ' + self.dictName[pos] + ' (' + self.getChip(self.dictStack[pos]) + ' in chips)')

        listRes.append( self.dictName[C.sb] + ': posts small blind ' + self.getChip(self.sb) )
        listRes.append( self.dictName[C.bb] + ': posts big blind ' + self.getChip(self.bb) )

        return U.ret(listRes)

    def getPreflop(self):
        listRes = []
        listRes.append(C.preflop)
        listRes.append( 'Dealt to ' + self.dictName[self.pos] + ' ' + self.getCard(self.dictCard[self.pos]) )
        listRes.append( self.getStreet(C.preflop) )
        return U.ret(listRes)

    def getFlop(self):
        strRes = self.getStreet(C.flop) 
        return U.ret([C.flop + ' ' + self.getCard(self.dictCard[C.flop]),strRes]) if len(strRes) > 0 else ''

    def getTurn(self):
        strRes = self.getStreet(C.turn) 
        return U.ret([C.turn + ' ' + self.getCard(self.dictCard[C.turn] , True),strRes]) if len(strRes) > 0 else ''

    def getRiver(self):
        strRes = self.getStreet(C.river) 
        return U.ret([C.river + ' ' + self.getCard(self.dictCard[C.river] , True),strRes]) if len(strRes) > 0 else ''
    
    # todo showdown order
    def getShowdown(self):
        listRes = []
        bolHasSd = False

        rounds = 0
        for (k,pos) in C.pairPos:
            rounds = max( rounds,len(self.dictAction[C.showdown][pos]) )
        #print(rounds)
        
        for i in list(range(0,rounds)):
            for (k,pos) in C.pairPos:
                if i < len(self.dictAction[C.showdown][pos]):
                    (act,val) = self.dictAction[C.showdown][pos][i] 

                    if C.sd == act:
                        if not bolHasSd:
                            listRes.append(C.showdown)
                            bolHasSd = True
                        listRes.append( self.dictName[pos] + ': shows ' + self.getCard(self.dictCard[pos]) )

                    elif C.nsd == act:
                        listRes.append( 'Uncalled bet (' + self.getChip(0) + ') returned to ' + self.dictName[pos])

                    elif C.handresult == act:
                        listRes.append( self.dictName[pos] + ' collected ' + self.getChip(val) + ' from pot')
                        if not bolHasSd:
                            listRes.append( self.dictName[pos] + ': doesn\'t show hand')
               
        return U.ret(listRes)

    # todo
    def getSummary(self):
        listRes = []
        listRes.append( C.summary )
        listRes.append( 'Total pot ' + self.getChip(self.dictStack[C.river]) + ' | Rake ' + self.getChip(self.getRake()) )
        for (k,v) in reversed(C.pairStreet):
            if len(self.dictCard[v]) != 0:
                listRes.append( 'Board ' + self.getCard(self.dictCard[v]) )
                break
        
        listTmp = sorted(self.dictSeat.items() , key = lambda x:x[1]) 
        for (pos,seat) in listTmp:
            strRes = C.seat + seat + ': ' + self.dictName[pos] + ' ' 
            if pos == C.sb:
                strRes += '(small blind)' + ' '
            elif pos == C.bb:
                strRes += '(big blind)' + ' '
            elif pos == C.btn:
                strRes += '(button)' + ' '

            if U.ret(self.dictAction[C.preflop][pos]).find(C.fold) != -1:
                strRes += 'folded before Flop (didn\'t bet)'
            elif U.ret(self.dictAction[C.flop][pos]).find(C.fold) != -1:
                strRes += 'folded on the Flop'
            elif U.ret(self.dictAction[C.turn][pos]).find(C.fold) != -1:
                strRes += 'folded on the Turn'
            elif U.ret(self.dictAction[C.river][pos]).find(C.fold) != -1:
                strRes += 'folded on the River'
            else:
                strRes += 'showed ' + self.getCard(self.dictCard[pos])
                
            listRes.append(strRes)

        return U.ret(listRes)

