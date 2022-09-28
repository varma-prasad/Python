from collections import OrderedDict
def encode(message):
    dict=OrderedDict.fromkeys(message,0)
    for ch in message:
        dict[ch]+=1
    output= ''
    for key,value in dict.items():
        output=output+key+str(value)
    return output

if __name__ == "__main__":
    input="wwwwaaadexxxxxx"
    print (encode(input))
