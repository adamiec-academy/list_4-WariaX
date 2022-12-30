def my_split(text):    
    result = []
    czy_wyraz = True 
    wyraz = ""   
            # " Hobbit   ma kota"
    for i in range(len(text)):
        
        if text[i] ==" ":
            czy_wyraz = False  

        elif  text[i-1] ==" ": 
            czy_wyraz = True    

        if czy_wyraz == True:
            wyraz += text[i] 

        elif wyraz != "":
            result.append(wyraz) 
            wyraz = ""

    if wyraz != "":       
        result.append(wyraz)  
    return result
