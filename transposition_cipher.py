def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, plaintext):
    order = {int(val): num for num, val in enumerate(key)}

    
    ciphertext = ''
    
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                print(f'index: {index}, order: {order}, part: {part}')
                ciphertext += part[order[index]]
            except IndexError:
                continue

    return ciphertext


print(encode('3214', 'hello world'))

'''
hello world

order: 
{
3 : 0
2 : 1
1 : 2
4 : 3
}

sorted(order):
{
1 : 2
2 : 1
3 : 0
4 : 3
}

split_len(plaintext, len(key)):
['hell', 'o wo', 'rld']

rows
-> 

1 2 3 4
h e l l
o   w o
r l d

3 2 1 4
l e h l
w   o o
d l r

lwde lhorlo

columns

ciphertext:

first:
{1:2} -> 1 (this is the key)
ciphertext += 'rld' + ''

'''