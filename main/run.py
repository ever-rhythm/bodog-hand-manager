
import os
from main.reader import Reader
from main.writer import Writer
from main.convertor import Convertor
from main.hand import Hand
from main.const import Const as C
from main.util import Util as U


# oneAcc/oneFile = oneStat = listHand
def cli():
    
    strDir = os.path.abspath('.') + '/input/'
    listAccount = os.listdir(strDir)
    #print(listAccount)
    cntDone = 0

    objWriter = Writer()
    objWriter.clean()

    objReader = Reader()
    
    objCvtor = Convertor()

    for oneAccount in listAccount:
        for oneFile in os.listdir(strDir + '/' + oneAccount):
            strFile = strDir + '/' + oneAccount + '/' + oneFile
            #print(strFile)
            '''
            if '/Users/qinmengyao/PythonProjects/python3/git_bodog/input//2248820/HH20170103-191742 - 4994888 - RING - $0.10-$0.25 - HOLDEM - NL - TBL No.11256624.txt' != strFile:
                continue
            '''
            outRead = objReader.read(strFile)
            #print(outRead)
            if False == outRead:
                continue

            listHand = outRead['hand']
            one = listHand[3]

            stat = outRead['stat']
            #print(one.dictAction)
            #print(one.pos)
            #break

            sum = 0
            idx = 0

            for one in listHand:
                tmp = (round(one.getPayout(one.pos),2))
                l = []
                l.append(one.dictStack[one.pos])
                l.append(tmp)

                l.append(one.pos)

                for k,v in C.pairStreet:
                    #print( one.dictAction[k][one.pos])
                    pass
                sum += tmp
                l.append(U.getChip(sum))
                #print(U.ret(l, ' '))

            print(U.getChip(sum))
            print(U.getChip(stat.stack))

            #print(listHand[0].getPayout(listHand[0].pos))
            #print(one.pos)

            #print(U.getChip(stat.stack))
            #break
        break
'''
            for oneHand in listHand:
                if filter(oneHand):
                    cntDone +=1
                    #print(oneHand.dictAction[C.preflop])
                    #print(oneHand.dictCard[oneHand.pos])
                    #print(oneHand.dictAction[C.preflop])
                    #print(oneHand.dictAction[C.preflop][oneHand.pos])

                    strPsHand = objCvtor.convert(oneHand)
                    objWriter.write(strPsHand)
                    #break


    print(str(cntDone) + ' done')
'''
def main():
    cli()

# test get 3bet pot
def filter(objHand):

    numPfr = 0
    for pos in objHand.dictAction[C.preflop]:
        for act,val in objHand.dictAction[C.preflop][pos]:
            #print(act)
            if act == C.raises or act == C.allin:
                numPfr += 1
        
    if numPfr >= 2 and U.strToNum(objHand.bb) == 0.5 and not (C.fold,'') in objHand.dictAction[C.preflop][objHand.pos]:
        return True
    
    return False
    

if __name__ == '__main__':
    main()
