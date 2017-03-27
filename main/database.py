
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker     # 可理解为1次链接
from sqlalchemy.ext.declarative import declarative_base     # orm基类

# init database and table
class Database(object):

    def __init__(self):
        pass

    def init(self):
        
        # todo read dir from conf
        engine = create_engine('sqlite:///../db/hm.db');
        
        meta = MetaData()

        table = Table('hand' , meta , \
            Column('id' , String(20) ,primary_key=True), \
            Column('card' , String(20) ) ,\
            Column('session' , String(20) ) ,\
            Column('level' , String(20) ) ,\
            Column('pot' , Float(20) ) ,\
            Column('serialize' , Text(20) ) \
            )

        meta.create_all(engine)


if __name__ == '__main__':
    o = Database()
    o.init()
                
        
        
