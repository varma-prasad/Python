BL="Good Evening, this is final call to AI passengersfor flight AI 466 whichis planned to take off at 8.40 A.M."
if (BL.startswith('Good Evening')):
    print(BL.replace('Good Evening','Good Morning'))
if(BL.find('AI')>0):
    print('Welcomr to Air India')
if(BL.endswith('A.M.')):
   print('Passengers are requested to have break fast')
a=BL.split(' ')
print(a)
for i in a:
   if (i.isdigit()):
       print('Flight number is {}'.format(i))
print('The number of timees airline anounced is:',BL.count('AI'))
message='ThaNk yOu All'

print(message.upper())
print(message.lower())
   
   

   
    
