
'''
d = [1,2,3]

#print(d[-1])

a = [(1,1),(2,2)]

if not (1,1) in a:
    print(123)
else:
    print(456)
'''

class A(object):

    @staticmethod
    def switchRange(x):
        return {
            'AK':'AK',
        }.get(x,'Other')


print( A.switchRange('AK'))

print(dir(dict))
