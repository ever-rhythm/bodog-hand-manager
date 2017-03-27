
import configparser

c = configparser.ConfigParser()
c.read( '../conf/global.conf' )

print( c.sections())
