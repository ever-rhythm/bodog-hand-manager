
import os

class Writer(object):

    def __init__(self):
        pass

    def write(self , strIn):

        strFile = os.path.abspath('.') + '/output/output.txt'

        with open( strFile , 'w' ) as fp:
            fp.write(strIn+'\n')
