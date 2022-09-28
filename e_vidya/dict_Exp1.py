def main():
    print(dic_Exp1('I love my country very much and thank you a'))

def dic_Exp1(stat):
    stat=stat.lower().split()
    sample_dictionary={}
    for word in stat:
        words=len(word)
        if words in sample_dictionary:
            sample_dictionary[words].add(word)
        else:
            sample_dictionary[words]={word}
    return sample_dictionary
main()
        

        
        
    
