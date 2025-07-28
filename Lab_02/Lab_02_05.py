def bon(code):
    alphabet = ['A','B','C','D','E','F','G',
                'H','I','J','K','L','M','N',
                'O','P','Q','R','S','T','U',
                'V','W','X','Y','Z']
    
    code = code.upper()
    for letter in code:
        if code.count(letter) > 1:
            for i in alphabet:
                if i == letter:
                    return (alphabet.index(i) + 1) * 4
                
code = input("Enter secret code : ")
print(bon(code))

            