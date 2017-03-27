
import re
from main.const import Const as C

class Util(object):

    @staticmethod
    def getChip(flt):
        return '$' + str('%.2f'%float(flt))

    @staticmethod
    def strToNum(string):
        return round(float(string),2)

    @staticmethod
    def ret(listRes , sep = C.sep):
       return sep.join( str(i) for i in listRes ) 

    @staticmethod
    def search(pattern , string):
        obj = re.search(pattern,string)
        return '' if None is obj else obj.group()

    '''
    classfy , order and range
    [Ac,Kc] => AK , s , AK
    [Ac,Ah] => AA , o , AA
    [8c,8h] => 88 , o , SmallPair

    '''
    @staticmethod
    def classifyHand(listCard):

        arrTmp = Util.sortCard([ listCard[0][0],listCard[1][0] ])

        c = arrTmp[0] + arrTmp[1]
        s = True if listCard[0][1] == listCard[1][1] else False
        r = Util.switchRange(c)

        return { 'card':c,'suit':s,'range':r }

    '''
    sort card desc
    '''
    @staticmethod
    def sortCard(listCard):

        dictCmp = {
            'A':14,
            'K':13,
            'Q':12,
            'J':11,
            'T':10,
        }

        for i in range(2,10):
            dictCmp[str(i)] = i

        if dictCmp[listCard[0]] > dictCmp[listCard[1]]:
            return listCard
        else:
            return [listCard[1] , listCard[0]]

    # todo add range
    @staticmethod
    def switchRange(x):
        return {
            'AK':'AK',
            'AQ':'AQ',
            'AJ':'AJ',
            'AT':'AT',

            'AA':'AA',
            'KK':'KK',
            'QQ':'QQ',

            'KQ':'KQ',
            'KJ':'KJ',
            'QJ': 'QJ',
            'JT': 'JT',

            '88':'SmallPair',
            '77':'SmallPair',
            '66':'SmallPair',
            '55':'SmallPair',
            '44':'SmallPair',
            '33': 'SmallPair',
            '22': 'SmallPair',

            '99': 'MidPair',
            'TT': 'MidPair',
            'JJ': 'MidPair',
        }.get(x,'Other')
