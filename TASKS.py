# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:30:13 2021

@author: SELAB
"""

def encrypt(text,s):
   result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + s -65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
   return result
         
#check the above function
text = "DEFENDTHEFORT"
s = 7 #the key to be encrypted 

print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
print ("Cipher: " + encrypt(text,s))
z = encrypt(text, s)
def decrypt(text,s):
   result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) -s -65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) - s - 97) % 26 + 97)
   return result
#check the above function
print("DSECRYPTION:",decrypt(z,s))
print("encryption tasks")
