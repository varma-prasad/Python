bal=1000
amount='300'
def take_card():
    print('take the card out of ATM')
try:
    if(bal>=int(amount)):
        print('withdraw')
    else:
        print('invalid amount')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except:
    print('some error occured')
finally:
    take_card()
    
