def main():
    print(string_dictionary('qwertyuiopasdfghjklzxcvbnm'))

def string_dictionary(sent):
    sent=sent.lower()
    d={'vowel':0,'consonant':0,'other':0}
    vowel_set=('aeiou')
    consonant_set=('bcdfghjklmnpqrstvwxyz')
    v,c,o=0,0,0
    for i in sent:
        if i in vowel_set:
            v+=1
        elif i in consonant_set:
            c+=1
        else:
            o+=1
    d['vowel']=v
    d['consonant']=c
    d['other']=o
    return d
main()
        

    
