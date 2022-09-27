def main():
    p(9,n=7)
    
def p(m,/,*,n,):
    print(m,n)
main()

