
import random
import string


#grab constants from the module string
chars = " " + string.punctuation + string.digits + string.ascii_letters
#change the string into a list
#typecasting
chars = list (chars)
key = chars.copy ( )

random.shuffle(key)
print (f"chars : {chars}")
print (" ")
print (f"keys : {key}")
print (" ")

credential = input ("Enter your password to login - ")
encrypt = " "


for letter in credential :
    index = chars.index (letter)
    encrypt += key[index]

print( f"plain : {credential}")
print ( f"encrypt : {encrypt}")


decrypt = input ("Enter message to decrypt - ")
credential = " "

#decrypt
for letter in encrypt :
    index = key.index (letter)
    credential += chars[index]

print( f"plain : {credential}")
print (decrypt)