def main():
    encrypt_message('the sun rises in the east')

def encrypt_message(sen):
    sen=sen.lower()
    vowel_set=set('aeiou')
    final_list=[]
    word=sen.split()
    for i in range(0,len(word)):
        if(i%2==0):
            final_list.append(word[i][::-1])
        else:
            c=[c for c in word[i] if c not in vowel_set]
            v=[v for v in word[i] if v in vowel_set]
            final_list.append("".join(c+v) )
    print(final_list)

main()
