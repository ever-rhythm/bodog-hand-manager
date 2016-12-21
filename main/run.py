
import os
from main.reader import Reader
from main.writer import Writer
from main.convertor import Convertor
from main.hand import Hand


def cli():
    
    strDir = os.path.abspath('.') + '/input/'
    listFile = os.listdir(strDir)
    strFile = strDir+listFile[0]
    objReader = Reader()
    objHand = objReader.read(strFile)
    #print(listOneHand)

    objConvertor = Convertor()
    strPsHand = objConvertor.convert(objHand)
    #print(strPsHand)

    objWriter = Writer()
    objWriter.write(strPsHand) 
    print('output done')

def main():
    cli()

if __name__ == '__main__':
    main()
