def main():
    for i in my_range(2,4,1):
        print(i,end=" ")

def my_range(*args):
    n=len(args)
    start=0
    step=1
    if n<1:
        print('error')
        return
    elif n==1:
        stop=args[0]
    elif n==2:
        (start,stop)=args
    elif n==3:
        (start,stop,step)=args
    else:
        print('error')
        return
    i=start
    while i<=stop:
        yield i
        i=i+step
        
    

main()
