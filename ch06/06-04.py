month = {1: 'Uanuary', 2: 'February', 3: 'March', 4: 'April'}
month[5] ='may'
month[6] ='June'
month[7] ='July'
month[8] ='August'
month[9] ='September'
print(month)
print()

from random import randint
for i in range(5):
    r = randint(1,9)
    print('%d: %s'%(r, month[r]))