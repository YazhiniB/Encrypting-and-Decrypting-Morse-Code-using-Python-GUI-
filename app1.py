import tkinter as tk

# Define Morse code dictionary
morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# Define functions for encryption and decryption
def encrypt_text():
    plaintext = plaintext_entry.get().upper()
    ciphertext = ''
    for char in plaintext:
        if char == ' ':
            ciphertext += ' '
        elif char in morse_code:
            ciphertext += morse_code[char] + ' '
        else:
            ciphertext += char
    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(0, ciphertext)

def decrypt_text():
    ciphertext = ciphertext_entry.get()
    plaintext = ''
    morse_chars = ciphertext.split(' ')
    for char in morse_chars:
        if char == '':
            plaintext += ' '
        else:
            for letter, code in morse_code.items():
                if code == char:
                    plaintext += letter
                    break
            else:
                plaintext += char
    plaintext_entry.delete(0, tk.END)
    plaintext_entry.insert(0, plaintext)

# Create GUI
root = tk.Tk()
root.title('Morse Code Encryptor/Decryptor')

plaintext_label = tk.Label(root, text='Plaintext:')
plaintext_label.grid(row=0, column=0, padx=5, pady=5)

plaintext_entry = tk.Entry(root)
plaintext_entry.grid(row=0, column=1, padx=5, pady=5)

encrypt_button = tk.Button(root, text='Encrypt', command=encrypt_text)
encrypt_button.grid(row=0, column=2, padx=5, pady=5)

ciphertext_label = tk.Label(root, text='Ciphertext:')
ciphertext_label.grid(row=1, column=0, padx=5, pady=5)

ciphertext_entry = tk.Entry(root)
ciphertext_entry.grid(row=1, column=1, padx=5, pady=5)

decrypt_button = tk.Button(root, text='Decrypt', command=decrypt_text)
decrypt_button.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
