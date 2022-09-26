def main():
    x=dict(name='xyz',age=12,cl='four')
    y=('hello','you','love')
    p("darling",*y,**x)

def p(a,*args,**kwargs):
    print('Try coding  {}'.format(a))
    
    if len(args):
        for i in args:
            print(i)
    else:
        print('sorry')
        
    print("-"*10)
    
    for k in kwargs:
        print(k,":",kwargs[k])

main()
