
import re
from main.const import Const as C

class Util(object):

    @staticmethod
    def ret(listRes , sep = C.sep):
       return sep.join( str(i) for i in listRes ) 

    @staticmethod
    def search(pattern , string):
        obj = re.search(pattern,string)
        return '' if None == obj else obj.group()

