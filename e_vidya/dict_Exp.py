def main():
    print(dic_Exp('I love my country very much and thankyou'))

def dic_Exp(stat):
    d=dict({})
    a=stat.split(' ')
    print(a)
    l=[]
    i=0
    while(i<len(a)):
        l.append(len(a[i]))
        i+=1
    print(l)
    v=max(l)
    n=1
    i=0
    while (i<len(l)):
        while(n<=v):
            if n in l:
                count=l.count(n)
                d.update({n:count})
            n+=1
        i+=1
    return d
main()
        

        
        
    
