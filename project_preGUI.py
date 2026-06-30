import os
import random

to_number = {chr(i + 97): i for i in range(26)}
to_letter = {v: k for k, v in to_number.items()}
atbash = {
    'a':'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u',
    'g':'t', 'h':'s', 'i':'r', 'j':'q', 'k':'p', 'l':'o',
    'm':'n', 'n':'m', 'o':'l', 'p':'k', 'q':'j', 'r':'i',
    's':'h', 't':'g', 'u':'f', 'v':'e', 'w':'d', 'x':'c',
    'y':'b', 'z':'a'
}

def caesar_e():
    plaintext=input("Please enter the plaintext: ")
    plaintext = plaintext.lower().replace(" ", "")
    key=int(input("Please enter the key: "))
    ciphertext=""
    for i in plaintext:
        if i.isalpha():
            x=to_number[i]
            x=(x+key)%26
            x=to_letter[x]
            ciphertext+=x
        else:
            ciphertext+=i
    print(plaintext)
    print(ciphertext)

def affine_e():
    plaintext=input("Please enter the plaintext: ")
    plaintext = plaintext.lower().replace(" ", "")
    a=int(input("Please enter the a value: "))
    b=int(input("Please enter the b value: "))
    ciphertext=""
    for i in plaintext:
        if i.isalpha():
            x=to_number[i]
            x=(a*x+b)%26
            x=to_letter[x]
            ciphertext+=x
        else:
            ciphertext+=i
    print(plaintext)
    print(ciphertext)
    
def vigenère_e():
    plaintext=input("Please enter the plaintext: ")
    plaintext = plaintext.lower().replace(" ", "")
    keyword=input("Please enter the key: ").lower().replace(" ", "")
    key=[]
    for i in keyword:
        x=to_number[i]
        key.append(x)
    ciphertext=""
    for i in range(len(plaintext)):
        if i.isalpha():
            x = to_number[plaintext[i]]
            x = (x + key[i % len(key)]) % 26
            x = to_letter[x]
            ciphertext += x
        else:
            ciphertext+=i
    print(plaintext)
    print(ciphertext)

def rail_fence_e():
    plaintext=input("Please enter the plaintext: ")
    plaintext=plaintext.lower().replace(" ", "")
    rail=int(input("Please enter the number of rails: "))
    ciphertext=""
    rails=[[] for i in range(rail)]
    direction=1
    row=0
    for letter in plaintext:
        rails[row].append(letter)
        if row==0:
            direction=1
        elif row==rail-1:
            direction=-1
        row+=direction
    for r in rails:
        for c in r:
            ciphertext+=c
    print(plaintext)
    print(ciphertext)

def atbash_e():
    plaintext=input("Please enter the plaintext: ")
    plaintext = plaintext.lower().replace(" ", "")
    ciphertext=""
    for i in plaintext:
        if i.isalpha():
            x=atbash[i]
            ciphertext+=x
        else:
            ciphertext+=i
    print(plaintext)
    print(ciphertext)

def row_transposition_e():
    plaintext=input("Please enter the plaintext: ")
    plaintext=plaintext.lower().replace(" ", "")
    key=input("Please enter the key: ")
    keylist=[]
    for i in key:
        keylist.append(int(i))
    ciphertext=""
    keys=[[] for i in range(len(keylist))]
    keys2=[[] for i in range(len(keylist))]
    max_key=max(keylist)
    iteration=0
    for i in plaintext:
        keys[iteration].append(i)
        iteration+=1
        if iteration==max_key:
            iteration=0
    for i in range (max_key):
        while len(keys[i]) < len(keys[0]):
            x=random.randint(0, 25)
            x=to_letter[x]
            keys[i].append(x)
    for i in range(len(keylist)):
        keys2[keylist[i]-1]=keys[i]
    for i in keys2:
        for j in i:
            ciphertext+=j
    print(plaintext)
    print(ciphertext)
    
def caesar_d():
    ciphertext=input("Please enter the ciphertext: ")
    ciphertext = ciphertext.lower().replace(" ", "")
    key=int(input("Please enter the key: "))
    plaintext=""
    for i in ciphertext:
        if i.isalpha():
            x=to_number[i]
            x=(x-key)%26
            x=to_letter[x]
            plaintext+=x
        else:
                plaintext+=i
    print(ciphertext)
    print(plaintext)

def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i

def affine_d():
    ciphertext=input("Please enter the ciphertext: ")
    ciphertext = ciphertext.lower().replace(" ", "")
    a=int(input("Please enter the a value: "))
    b=int(input("Please enter the b value: "))
    plaintext=""
    a_inv = mod_inverse(a, 26)
    for i in ciphertext:
        if i.isalpha():
            x=to_number[i]
            x=(a_inv*(x-b))%26
            x=to_letter[x]
            plaintext+=x
        else:
                plaintext+=i
    print(ciphertext)
    print(plaintext)
    
def vigenère_d():
    ciphertext=input("Please enter the ciphertext: ")
    ciphertext = ciphertext.lower().replace(" ", "")
    keyword=input("Please enter the key: ").lower().replace(" ", "")
    key=[]
    for i in keyword:
        x=to_number[i]
        key.append(x)
    plaintext=""
    for i in range(len(ciphertext)):
        if i.isalpha():
            x = to_number[ciphertext[i]]
            x = (x - key[i % len(key)]) % 26
            x = to_letter[x]
            plaintext += x
        else:
                plaintext+=i
    print(ciphertext)
    print(plaintext)

def rail_fence_d():
    ciphertext=input("Please enter the ciphertext: ")
    ciphertext=ciphertext.lower().replace(" ", "")
    rail =int(input("Please enter the number of rails: "))
    pattern=[]
    row=0
    direction=1
    for i in range(len(ciphertext)):
        pattern.append(row)
        if row==0:
            direction=1
        elif row==rail-1:
            direction=-1
        row+=direction
    rails=[[] for i in range(rail)]
    index=0
    for r in range(rail):
        count=pattern.count(r)
        rails[r]=list(ciphertext[index:index+count])
        index+=count
    plaintext=""
    rail_index=[0]*rail
    for r in pattern:
        plaintext+=rails[r][rail_index[r]]
        rail_index[r]+=1
    print(ciphertext)
    print(plaintext)

def atbash_d():
    ciphertext=input("Please enter the ciphertext: ")
    ciphertext = ciphertext.lower().replace(" ", "")
    plaintext=""
    for i in ciphertext:
        if i.isalpha():
            x=atbash[i]
            plaintext+=x
        else:
                plaintext+=i
    print(ciphertext)
    print(plaintext)

def row_transposition_d():
    ciphertext=input("Please enter the ciphertext: ")
    ciphertext=ciphertext.lower().replace(" ", "")
    key=input("Please enter the key: ")
    keylist=[]
    for i in key:
        keylist.append(int(i))
    plaintext=""
    keys=[[] for i in range(len(keylist))]
    keys2=[[] for i in range(len(keylist))]
    max_key=max(keylist)
    cols=len(keylist)
    rows=len(ciphertext)//cols
    iteration=0
    for i in range(cols):
        keys2[i]=list(ciphertext[iteration:iteration+rows])
        iteration+=rows
    for i in range(len(keylist)):
        keys[i]=keys2[keylist[i]-1]
    for r in range(rows):
        for c in range(len(keys)):
            plaintext+=keys[c][r]
    print(ciphertext)
    print(plaintext)

while True:
    x=input("Press '1' to encrypt, '2' to decrypt, or anything else to quit: ")
    if x=='1':
        os.system('cls')
        print("Encryptions:")
        print("Press '1' for the ceaser cipher")
        print("Press '2' for the affine cipher")
        print("Press '3' for the vigenère cipher")
        print("Press '4' for the rail fence cipher")
        print("Press '5' for the atbash cipher")
        print("Press '6' for the row transposition cipher")
        print("Press anything else to return to the menu")
        x=input()
        
        if x=='1':
            caesar_e()
        elif x=='2':
            affine_e()
        elif x=='3':
            vigenère_e()
        elif x=='4':
            rail_fence_e()
        elif x=='5':
            atbash_e()
        elif x=='6':
            row_transposition_e()
        else:
            continue
        
    elif x =='2':
        os.system('cls')
        print("Decryptions:")
        print("Press '1' for the ceaser cipher")
        print("Press '2' for the affine cipher")
        print("Press '3' for the vigenère cipher")
        print("Press '4' for the rail fence cipher")
        print("Press '5' for the atbash cipher")
        print("Press '6' for the row transposition cipher")
        print("Press anything else to return to the menu")
        x=input()
        
        if x=='1':
            caesar_d()
        elif x=='2':
            affine_d()
        elif x=='3':
            vigenère_d()
        elif x=='4':
            rail_fence_d()
        elif x=='5':
            atbash_d()
        elif x=='6':
            row_transposition_d()
        else:
            continue
        
    else:
        break
    