#from string import maketrans

def rot13(intab, outtab, text):
    trantab = str.maketrans(intab, outtab)
    return text.translate(trantab)
    
intab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
outtab = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
txt = "this is string example...wow!!!"
print(rot13(intab, outtab, txt))