def get_plaintext()->str:
    return input("Please Enter Plaintext\t")
def get_key()->int:
    return int(input("Please enter a number as cipher Key\t"))
def divide_characters(plaintext)->list:
    return list(plaintext)
def encrypt_cesar(plaintext:list,key=2)->list:
    result=[]
    for character in plaintext:
        result.append(chr(ord(character)-key))
    return result

def decrypt_cesar(cipher:list,key=2):
    result=[]
    for character in cipher:
        result.append(chr(ord(character)+key))
    return result
plaintxt=get_plaintext()
key=get_key()
cipher=encrypt_cesar(plaintxt,key)

for character in cipher:
    print(character,end="")
print("\n")
decrypted=decrypt_cesar(cipher,key)
for char in decrypted:
    print(char, end="")