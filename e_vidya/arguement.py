def main():
    greet('hi','welcome','bye')

def greet(*args):
    if len(args):
        for i in args:
            print(i)
    else:
        print("no arguement")

main()
