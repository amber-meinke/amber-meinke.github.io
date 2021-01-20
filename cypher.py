import os

#
# call "encrypt()" or "decrypt()" in the command line to run
#

def encrypt():
    # read the file (to be encrypted) and write it into a temporary file
    fileName = input("Enter the name of your file: ")
    file = open(fileName,"r")
    temp = open("temp.txt","w")
    temp.write("")
    temp.close()

    for line in file:
        temp = open("temp.txt","a")
        temp.write(line)
        temp.close()


    file.close()
    file = open(fileName,"w")
    file.write("") # empty the file
    file.close()

    temp = open("temp.txt","r")
     
    # read from the temp file, and write back into the
    #     original file, incrementing each character
    #     by one ascii value
    for line in temp:
        for char in line:
            #print(char)
            char = chr(ord(char) + 1)
            file = open(fileName,"a")
            file.write(char)
            file.close()
             
    # close the file and delete the temp file
    file.close()
    os.remove("temp.txt")
    
def decrypt():
    # read the file (to be decrypted) write it into a temporary file
    fileName = input("Enter the name of your file: ")
    file = open(fileName,"r")
    temp = open("temp.txt","w")
    temp.write("")
    temp.close()

    for line in file:
        temp = open("temp.txt","a")
        temp.write(line)
        temp.close()


    file.close()
    file = open(fileName,"w")
    file.write("") # empty the file
    file.close()

    temp = open("temp.txt","r")
     
    # read from the temp file, and write back into the
    #     original file, decrementing each character
    #     by one ascii value
    for line in temp:
        for char in line:
            #print(char)
            char = chr(ord(char) - 1)
            file = open(fileName,"a")
            file.write(char)
            file.close()
           
    # close the file and delete the temp file
    file.close()
    os.remove("temp.txt")
