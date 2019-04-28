def LetterChanges(str): 

    i = 0 
    
    while i <= len(str):
        
        temp = ord(str[i]) + 1
        str[i] = chr(temp)
        
        
        
        
        
    

    # code goes here 
    return str
    
# keep this function call here  
print(LetterChanges('Callum') ) 

