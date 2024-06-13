import math 
import random






p = 0
q = 0 
element = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!, "
public_key = 0
secret_key = 0
plain_text = ""
encrypted_text = ""
word = ""
key_word = ""
key_number = 1
R = True



while R:
    p, q = input("enter two key numbers seperated by space, it should be a prime number:\n#> ").split(" ")
    p = int(p)
    q = int(q)
    n = p * q
    E = (p-1) * (q-1)

    for i in range(1, 10000):
        if 0 != E % i:
            public_key = round(i)
            break

    for j in range(0, 10000):
        d = 1 + (j * E)
        d2 = d / public_key
        if 0 == d % public_key:
            secret_key = round(d2)
            break

    demarer = True
    while demarer:
        print("\n")
        print("p=",p)
        print("q=",q)
        print("modulo=",n)
        print("public key=",public_key)
        print("secret key=",secret_key)
        print("choise")
        print("E encrypt plain text")
        print("D decrypt encrypted text")
        print("F exit the program\n")
        word = input("--->")

        if "F" in word:
            demarer = False

        if "E" in word:
            plain_text = input("Enter the text: ")
            encrypted_text = ""
            for k in plain_text:
                m = 0
                for l in element :
                    if k == l:
                        if m < 10:
                            m = m + 00
                        encrypted_text = encrypted_text + (str((m ** public_key) % n)) + " "
                        break
                    m += 1
            print("encrypted text: ",encrypted_text)
            input("press enter to do another operation")

        if "D" in word:
            encrypted_text = input("Enter encrypted text: ")
            plain_text = ""
            for s in encrypted_text.split(" "):
                for k in element :
                    m = 0
                    for l in element :
                        if k == l:
                            if s == (str((m ** public_key) % n)):
                                plain_text = plain_text + l
                            break
                        m += 1
            print("plain text: ",plain_text)
            input("press enter")

        if "F " in word:
            R = False

