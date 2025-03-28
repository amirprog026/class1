PI=3.14
rad= input("Please Enter Raious value ")

try:
    result=PI*(int(rad)**2)
    print("RESULT is {}.".format(result))
except ValueError:
    raise TypeError("ERROR. Value is not correct")
except:
    print("Unknown error")
#comment
print("s")



