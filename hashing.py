import hashlib
def get_file():
    return input("Please enter file address\t")
def readfile_bytes(fileaddr:str)->bytes:
    file1=open(fileaddr,'rb')
    return file1.read()
def calculate_hash(filebytes:bytes)->str:
    return hashlib.md5(filebytes).hexdigest()
fileaddr=get_file()
fbytes=readfile_bytes(fileaddr)
print(calculate_hash(fbytes))


