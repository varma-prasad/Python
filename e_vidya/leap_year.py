def main():
    a=int(input('enter year'))
    lp(a)

def lp(n):
    if((n%4==0)and (n%100!=0))or(n%400==0):
        print('leap year')
    else:
        print('normal year')

main()
    
