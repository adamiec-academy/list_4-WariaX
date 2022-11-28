def is_palindrome(text):
    text = text.lower().replace(" ", "")
    n = len(text)
    for i in range(n-1):
        if text[i] != text[n-1-i]: 
            return False 
    return True;
