#!/usr/bin/env python3

from main.stat import Stat
from main.hand import Hand
from main.const import Const as C
from main.util import Util as U
import re

# input control
class Reader(object):
    
    def __init__(self):
        pass

    # while read eof and return listHand
    def read(self , strFile):
        listOut = []
        listOneHand = []
        oneStat = Stat()

        with open( strFile , 'r' ) as fp:
            for lineNum,strLine in enumerate(fp,1):
                strLine = strLine.strip()
                #print(strLine)
                if not len(strLine):
                    if len(listOneHand) > 0:
                        oneHand = Hand()
                        r = self.analyzeHand(listOneHand , oneHand)
                        if False == r:
                            #print(lineNum)
                            #print(strFile)
                            return False
                        listOut.append( oneHand)
                        
                        self.analyzeStat( listOneHand , oneStat )

                        # clean for next read
                        listOneHand = []
                else:
                    listOneHand.append(strLine)

        # first hand and last hand hero's stack ,and hand result
        handSt = listOut[0]
        handEd = listOut[-1]
        oneStat.stack += U.strToNum(handEd.dictStack[handEd.pos]) - U.strToNum(handSt.dictStack[handSt.pos])
        oneStat.stack += handEd.getPayout(handEd.pos)
        
        #print(U.strToNum(oneStat.stack))
        #print(listOneHand)
        return { 'hand':listOut , 'stat':oneStat }

    def readCard(self , strCard):
        return re.split( r'\s+' , strCard.replace('[','').replace(']','') )

    def analyzeStat(self , listHand , objStat):

        for oneLine in listHand:
            if oneLine.find(C.deposit) != -1 and oneLine.find(C.me) != -1:
                stack = U.search( r'\$[0-9\.]+' , oneLine ).strip('$')
                #print(stack)
                objStat.stack -= U.strToNum(stack)
        pass
        
    def analyzeHand(self , listHand , objHand):
        
        arrTable = re.split( r'\s+' ,listHand[0] )
        if len(arrTable) < 10:
            return False #test
            #print(listHand)
            #print(arrTable)
        objHand.lobby = C.ps
        objHand.handId = arrTable[2].strip('#')
        objHand.date = arrTable[8] + ' ' + arrTable[9]
        objHand.game = C.nlh
        objHand.table = C.table

        #print(arrTable)

        curStreet = ''
        curStack = 0.0
        curAct = ''
        
        for oneLine in listHand:
            
            # todo analyze 9-max pos
            # read seat
            if oneLine.find(C.seat) != -1 and oneLine.find('$') != -1:
                #print(oneLine)
                stack = U.search( r'\$[0-9\.]+' , oneLine ).strip('$')
                
                arr = re.split(r'\s+' , oneLine)
                name = arr[2]
                pos = arr[2]

                # todo rm 6-max param filter
                if not (pos,pos) in C.pairPos:
                   return False 

                if oneLine.find(C.me) != -1 :
                    name += '.' + C.hero
                    objHand.pos = pos
                    
                seat = arr[1].strip(':') 
                
                objHand.dictName[pos] = name
                objHand.dictStack[pos] = stack
                objHand.dictSeat[pos] = seat

            # read hand
            elif oneLine.find(C.dealt) != -1:
                objHand.dictCard[ re.split(r'\s+' , oneLine )[0] ] = self.readCard( U.search( r'\[[2-9TJQKAdchs ]*\]' , oneLine ) )

            # read showdown
            elif oneLine.find(C.sd) != -1: 
                pos = re.split(r'\s+' , oneLine)[0]
                objHand.dictAction[C.showdown][pos].append( (C.sd,0) )
            elif oneLine.find(C.nsd) != -1:
                pos = re.split(r'\s+' , oneLine)[0]
                objHand.dictAction[C.showdown][pos].append( (C.nsd,0) )
            elif oneLine.find(C.handresult) != -1:
                pos = re.split(r'\s+' , oneLine)[0]
                val = U.search( r'\$[0-9\.]+' , oneLine ).strip('$')
                objHand.dictAction[C.showdown][pos].append( (C.handresult,val) )
            elif oneLine.find(C.uncall) != -1:
                pos = re.split(r'\s+', oneLine)[0]
                val = U.search(r'\$[0-9\.]+', oneLine).strip('$')
                objHand.dictAction[C.showdown][pos].append((C.uncall, val))
            elif oneLine.find(C.posts) != -1:
                pos = re.split(r'\s+', oneLine)[0]
                val = U.search(r'\$[0-9\.]+', oneLine).strip('$')
                objHand.dictAction[C.showdown][pos].append((C.posts, val))

            else:
                # read sb/bb 
                for (k,v) in C.pairBlind:
                    if oneLine.lower().count(k) == 2 or (oneLine.find(C.btn) != -1 and oneLine.lower().find(k) != -1) :
                        #print(oneLine)
                        val = U.search( r'[0-9\.]+' , oneLine )
                        setattr(objHand,v,val)

                        pos = getattr(C,v)
                        if (oneLine.find(C.btn) != -1 and oneLine.lower().find(k) != -1):
                            pos = C.btn
                        objHand.dictAction[C.preflop][pos].append( (C.bet,val) )
                        curStack = round(curStack + float(val),2)
                        #print(curStack)

                # read board
                for (k,v) in C.pairStreet:
                    if oneLine.find(k) != -1:
                        curStreet = v
                        objHand.dictCard[v] = self.readCard( U.search( r'\[.*\]' , oneLine ) )
                        objHand.dictStack[v] = curStack

                # read action
                for (k,v) in C.pairAction:
                    if oneLine.find(k) != -1:
                        val = U.search( r'\$[0-9\.]+' , oneLine ).strip('$')
                        if not val:
                            val = '0'
                        if v == C.bet or v == C.raises or v == C.call or v == C.allin:
                            curStack = U.strToNum(curStack) + U.strToNum(val)
                        objHand.dictAction[curStreet][ re.split(r'\s+' , oneLine)[0] ].append( (v,val) ) 

                
        # set total pot
        objHand.dictStack[C.showdown] = curStack

        #print(curStack)
        #print(objHand.dictAction)
        #print(objHand.dictCard)
        #print(objHand.dictStack)

        pass
        
        
