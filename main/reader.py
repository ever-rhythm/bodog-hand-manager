#!/usr/bin/env python3

from main.hand import Hand
from main.const import Const as C
from main.util import Util as U
import re

class Reader(object):
    
    def __init__(self):
        pass

    def read(self , strFile):

        listOneHand = []
        with open( strFile , 'r' ) as fp:
            for strLine in fp:
                strLine = strLine.strip()
                #print(strLine)
                if not len(strLine):
                    break 
                else:
                    listOneHand.append(strLine)

        #print(listOneHand)
        return self.analyze(listOneHand)


    # not robust
    def readCard(self , strCard):
        return strCard.replace('[','').replace(']','').split(' ')

    def analyze(self , listHand):

        objHand = Hand()
        
        arrTable = listHand[0].split(' ')
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
            
            # read seat
            if oneLine.find(C.seat) != -1:
                #print(oneLine)
                stack = U.search( r'\$[0-9\.]+' , oneLine ).strip('$')
                
                arr = oneLine.split(' ')
                name = arr[2]
                pos = arr[2]
                if oneLine.find(C.me) != -1 :
                    #name += ' ' + C.hero
                    objHand.pos = pos
                    
                seat = arr[1].strip(':') 
                
                objHand.dictName[pos] = name
                objHand.dictStack[pos] = stack
                objHand.dictSeat[pos] = seat
                #print(arr)

            # read hand
            elif oneLine.find(C.dealt) != -1:
                objHand.dictCard[ oneLine.split(' ')[0] ] = self.readCard( U.search( r'\[[2-9TJQKAdchs ]*\]' , oneLine ) )

            # read showdown
            elif oneLine.find(C.sd) != -1: 
                pos = oneLine.split(' ')[0]
                objHand.dictAction[C.showdown][pos].append( (C.sd,'') )
            elif oneLine.find(C.nsd) != -1:
                pos = oneLine.split(' ')[0]
                objHand.dictAction[C.showdown][pos].append( (C.nsd,'') )
            elif oneLine.find(C.handresult) != -1:
                pos = oneLine.split(' ')[0]
                val = U.search( r'\$[0-9\.]+' , oneLine ).strip('$')
                objHand.dictAction[C.showdown][pos].append( (C.handresult,val) )

            else:
                # read sb/bb 
                for (k,v) in C.pairBlind:
                    if oneLine.find(k) != -1:
                        val = U.search( r'[0-9\.]+' , oneLine )
                        setattr(objHand,v,val)
                        objHand.dictAction[C.preflop][getattr(C,v)].append( (C.bet,val) )
                        curStack = round(curStack+float(val),2)

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
                        if v == C.bet or v == C.raises or v == C.call:
                            curStack = round(curStack+float(val),2)
                        objHand.dictAction[curStreet][ oneLine.split(' ')[0] ].append( (v,val) ) 

                
        #print(objHand.dictAction)
        #print(objHand.dictCard)
        #print(objHand.dictStack)

        return objHand
        
        
