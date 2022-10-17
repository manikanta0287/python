#from asyncore import loop

"""
print("Hello world!!!")


a = 5

b = 15

c = a+b


print(c)

"""
#---complextype------

a = complex(4,5)
#print(a)

b=complex(3.4,5.4)
#print(b)


c= 25
#print(type(c),c)
d = 25.01
#print(type(d),d)


#print("I'm 20 years old")

#print('My favorite book is "Sense and Sensibility"')  #observe the difference in single and double quotes

freecodecamp = "freeCodeCamp"

#print(freecodecamp[2:8])

name = 'manikanta'
print(name[3:9:2])           # need more clarity on this cocept, lititle bit consfusing 
print(name[5:2:-4])
print(name[4::3])
print(name[:8:2])
print(name[::-2])
print(name[::-1])





print(freecodecamp.capitalize())                #'Freecodecamp'

print(freecodecamp.count("C"))                  #   2

print(freecodecamp.find("e"))                   # 2

print(freecodecamp.index("p"))                  # 11

print(freecodecamp.isalnum())                          # True

print(freecodecamp.isalpha())                    #  True

print(freecodecamp.isdecimal())                 #  False

print(freecodecamp.isdigit())                   #  False

print(freecodecamp.isidentifier())              #  True

print(freecodecamp.islower())                   # False

print(freecodecamp.isnumeric())                 # False

print(freecodecamp.isprintable())               # True

print(freecodecamp.isspace())                   # False

print(freecodecamp.istitle())                   # False

print(freecodecamp.isupper())                   # False

print(freecodecamp.lower())                      #'freecodecamp'

print(freecodecamp.lstrip("f"))                 #'reeCodeCamp'

print(freecodecamp.rstrip("p"))                       # 'freeCodeCam'

print(freecodecamp.replace("e", "a"))             # 'fraaCodaCamp'

print(freecodecamp.split("C"))                   # ['free', 'ode', 'amp']

print(freecodecamp.swapcase())                    # 'FREEcODEcAMP'

print(freecodecamp.title())                       #  'Freecodecamp'

print(freecodecamp.upper())                        #'FREECODECAMP'