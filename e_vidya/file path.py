def main():
    x=p('my computer','cdrive','varma')
    print(x)
    
def p(*args,sep='/'):
    return sep.join(args)
    
    
        
main()
