
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base     

class DaoHand(declarative_base()):

    __tablename__ = 'hand'

    id = Column(String(20) ,primary_key=True)
    card = Column(String(20) ,primary_key=True)
    session = Column(String(20) ,primary_key=True)
    level = Column(String(20) ,primary_key=True)
    pot = Column(Float(20) ,primary_key=True)
    serialize = Column(Text(20) ,primary_key=True)

    def __init__(self):
        pass

    def add(self , dictIn):
        
        pass

    def stat(self):

        pass

if __name__ == '__main__':
    o = DaoHand()
    print(dir(o))
    #o.add()
    

    
