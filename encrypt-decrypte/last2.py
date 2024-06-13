# dernier code 13/06
#avec une interface_graphique
import math
import random 
import tkinter as tk
from tkinter import messagebox

element = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!,"

def generate_rsa_keys(p, q):
    if not (prime(p) and prime(q)):
        messagebox.showerror("Erreur", "Les deux nombres doivent être premiers.")
        return None, None, None, None, None
    
    n = p * q
    E = (p - 1) * (q - 1)
    
    public_key = next(i for i in range(2, 10000) if E % i != 0)
    secret_key = next((1 + j * E) // public_key for j in range(10000) if (1 + j * E) % public_key == 0)
    
    return p, q, public_key, secret_key, n

def prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_keys():
    try:
        p = int(entry_p.get())
        q = int(entry_q.get())
    except ValueError:
        messagebox.showerror("Erreur", "Entrée invalide. Veuillez entrer deux entiers.")
        return

    global public_key, secret_key, n
    p, q, public_key, secret_key, n = generate_rsa_keys(p, q)
    if public_key and secret_key:
        lbl_public_key_val.config(text=str(public_key))
        lbl_secret_key_val.config(text=str(secret_key))
        lbl_n_val.config(text=str(n))

def encrypt_message():
    if not (public_key and n):
        messagebox.showerror("Erreur", "Générez d'abord les clés RSA.")
        return

    plain_text = entry_plain_text.get()
    encrypted_text = ""
    for k in plain_text:
        m = 0
        for l in element:
            if k == l:
                encrypted_text += str((m ** public_key) % n) + " "
                break
            m += 1
    entry_encrypted_text.delete(0, tk.END)
    entry_encrypted_text.insert(0, encrypted_text)

def decrypt_message():
    if not (secret_key and n):
        messagebox.showerror("Erreur", "Générez d'abord les clés RSA.")
        return

    encrypted_text = entry_encrypted_text.get()
    plain_text = ""
    for s in encrypted_text.split(" "):
        if s:
            m = int(s)
            for k, l in enumerate(element):
                if m == (k ** secret_key) % n:
                    plain_text += l
                    break
    entry_plain_text.delete(0, tk.END)
    entry_plain_text.insert(0, plain_text)

root = tk.Tk()
root.title("Encrypt/Decrypt")
root.geometry("800x500")
root.configure(bg="#34495e")  

# Style des boutons
button_style = {
    "font": ("Arial", 14, "bold"),
    "fg": "white",
    "activeforeground": "white",
    "bd": 0,
    "highlightthickness": 0,
    "relief": "flat",
    "width": 15, 
    "height": 2  
}

# Frame pour l'entrée des nombres premiers
frame_primes = tk.Frame(root, padx=10, pady=10, bg="#34495e")
frame_primes.pack(pady=10)

lbl_p = tk.Label(frame_primes, text="p:", font=("Arial", 14), bg="#34495e", fg="white")
lbl_p.grid(row=0, column=0, sticky='e')
entry_p = tk.Entry(frame_primes, font=("Arial", 14))
entry_p.grid(row=0, column=1, padx=5, pady=5)

lbl_q = tk.Label(frame_primes, text="q:", font=("Arial", 14), bg="#34495e", fg="white")
lbl_q.grid(row=1, column=0, sticky='e')
entry_q = tk.Entry(frame_primes, font=("Arial", 14))
entry_q.grid(row=1, column=1, padx=5, pady=5)

btn_generate = tk.Button(frame_primes, text="les clés", command=generate_keys, **button_style, bg="#2980b9", activebackground="#3498db")
btn_generate.grid(row=2, columnspan=2, pady=10)

# Frame pour l'affichage des clés
frame_keys = tk.Frame(root, padx=10, pady=10, bg="#34495e")
frame_keys.pack(pady=10)

lbl_public_key = tk.Label(frame_keys, text="public_key:", font=("Arial", 14), bg="#34495e", fg="white")
lbl_public_key.grid(row=0, column=0, sticky='e')
lbl_public_key_val = tk.Label(frame_keys, text="", font=("Arial", 14), bg="#34495e", fg="white")
lbl_public_key_val.grid(row=0, column=1, padx=5, pady=5)

lbl_secret_key = tk.Label(frame_keys, text="secret_key:", font=("Arial", 14), bg="#34495e", fg="white")
lbl_secret_key.grid(row=1, column=0, sticky='e')
lbl_secret_key_val = tk.Label(frame_keys, text="", font=("Arial", 14), bg="#34495e", fg="white")
lbl_secret_key_val.grid(row=1, column=1, padx=5, pady=5)

lbl_n = tk.Label(frame_keys, text="n =:", font=("Arial", 14), bg="#34495e", fg="white")
lbl_n.grid(row=2, column=0, sticky='e')
lbl_n_val = tk.Label(frame_keys, text="", font=("Arial", 14), bg="#34495e", fg="white")
lbl_n_val.grid(row=2, column=1, padx=5, pady=5)

# Frame pour le Encrypt/Decrypt
frame_cipher = tk.Frame(root, padx=10, pady=10, bg="#34495e")
frame_cipher.pack(pady=10)

lbl_plain_text = tk.Label(frame_cipher, text="message  :", font=("Arial", 14), bg="#34495e", fg="white")
lbl_plain_text.grid(row=0, column=0, sticky='e')
entry_plain_text = tk.Entry(frame_cipher, width=50, font=("Arial", 14))
entry_plain_text.grid(row=0, column=1, padx=5, pady=5)

lbl_encrypted_text = tk.Label(frame_cipher, text="message chiffré:", font=("Arial", 14), bg="#34495e", fg="white")
lbl_encrypted_text.grid(row=1, column=0, sticky='e')
entry_encrypted_text = tk.Entry(frame_cipher, width=50, font=("Arial", 14))
entry_encrypted_text.grid(row=1, column=1, padx=5, pady=5)

btn_encrypt = tk.Button(frame_cipher, text="Encryption", command=encrypt_message, **button_style, bg="#27ae60", activebackground="#2ecc71")
btn_encrypt.grid(row=2, column=0, pady=10, padx=10)

btn_decrypt = tk.Button(frame_cipher, text="Décryption", command=decrypt_message, **button_style, bg="#e74c3c", activebackground="#c0392b")
btn_decrypt.grid(row=2, column=1, pady=10, padx=10)

root.mainloop()
