def my_split(text):    
    result = []
    czy_wyraz = True 
    wyraz = ""   
           
    for i in range(len(text)):
              
        if text[i] ==" ":
            czy_wyraz = False  

        if  text[i-1] ==" ": 
            czy_wyraz = True    

        if czy_wyraz == True:
            wyraz += text[i] 

        else:
            result.append(wyraz) 
            wyraz = ""
    result.append(wyraz)  
    return result
