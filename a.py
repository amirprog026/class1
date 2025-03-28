import sys,math
import colorama
colorama.init()
def jazr(number):
    return math.sqrt(number)
print(colorama.Back.GREEN+str(jazr(int(sys.argv[1]))))
