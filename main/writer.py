
import os

# output control
class Writer(object):

    def __init__(self):
        pass

    def clean(self):
        
        strFile = os.path.abspath('.') + '/output/output.txt'
        with open( strFile , 'w' ) as fp:
            fp.write('')
        
    def write(self , strIn):

        strFile = os.path.abspath('.') + '/output/output.txt'

        with open( strFile , 'a' ) as fp:
            fp.write(strIn+'\n'+'\n')
