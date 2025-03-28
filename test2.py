#عدد اول فقط به یک و خودش بخش پذیر است
def is_prime(number:int)->bool:
    i=2
    while i<number:
        if number%i==0:
            
            return False
        i+=1
    return True

def find_primes(number:int):
    for item in range(2,number):
        if is_prime(item):
            print(item,end=" ")

print("Www")        

while 1:
    num=input("Please enter a number ")
    find_primes(int(num))