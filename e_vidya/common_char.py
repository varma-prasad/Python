def find_common_characters(msg1,msg2):
    var=''
    for x in msg1:
        if x in msg2:
            if x not in var:
                var=var+x
    if (var):
        return var.replace(' ','')
    else:
        return None
                
    
    
msg1='i like python'
msg2='java is popular language'
common=find_common_characters(msg1,msg2)
print(common)
