# ============================
# IMPORTS
# ============================
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk

from Crypto.Cipher import DES, DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

import os


# ============================
# GLOBAL VARIABLES
# ============================

selected_file = ""        # Path of file user selects
selected_key_file = ""    # Path of key file (for decryption)


# ============================
# FILE SELECTION FUNCTIONS
# ============================

def browse_file():
    """
    Opens file dialog and allows user to pick any file.
    Stores file path globally and updates label.
    """
    global selected_file
    selected_file = filedialog.askopenfilename()

    if selected_file:
        file_label.config(text=selected_file)


def browse_key_file():
    """
    Opens dialog to select a .key file (used for decryption).
    """
    global selected_key_file
    selected_key_file = filedialog.askopenfilename()

    if selected_key_file:
        key_label.config(text=selected_key_file)


# ============================
# ALGORITHM DESCRIPTION
# ============================

def update_description():
    """
    Updates the description box when algorithm changes.
    """
    choice = algo_var.get()

    if choice == "DES":
        desc = "DES:\n64-bit block size\n56-bit key\nLegacy algorithm (insecure today)"
    elif choice == "2TDEA":
        desc = "2TDEA:\n64-bit block size\n112-bit effective key\nUses 2 keys (K1, K2) in EDE mode"
    else:
        desc = "3DES:\n64-bit block size\n168-bit key\nMore secure but slower, being phased out"

    description_box.delete("1.0", END)
    description_box.insert("1.0", desc)


# ============================
# KEY GENERATION
# ============================

def generate_key(algo):
    """
    Generates a cryptographic key depending on algorithm.
    """
    if algo == "DES":
        return get_random_bytes(8)   # 8 bytes = 64 bits (56 used)
    elif algo == "2TDEA":
        return DES3.adjust_key_parity(get_random_bytes(16))  # 16 bytes
    else:
        return DES3.adjust_key_parity(get_random_bytes(24))  # 24 bytes


# ============================
# ENCRYPTION FUNCTION
# ============================

def encrypt_file():
    """
    Handles full encryption process:
    - Reads file
    - Generates key + IV
    - Encrypts using CBC
    - Saves encrypted file + key file
    """
    if not selected_file:
        messagebox.showerror("Error", "No file selected")
        return

    algo = algo_var.get()

    try:
        # Read file as bytes
        with open(selected_file, "rb") as f:
            data = f.read()

        key = generate_key(algo)            # Generate key
        iv = get_random_bytes(8)            # 8-byte IV (DES block size)

        # Select cipher
        if algo == "DES":
            cipher = DES.new(key, DES.MODE_CBC, iv)
        else:
            cipher = DES3.new(key, DES3.MODE_CBC, iv)

        # Pad data to multiple of 8 bytes
        padded_data = pad(data, 8)

        # Encrypt
        ciphertext = cipher.encrypt(padded_data)

        # ============================
        # SAVE FILES
        # ============================

        base = os.path.basename(selected_file)

        # Encrypted file (.bin)
        enc_filename = f"{base}_{algo}_encrypted.bin"
        with open(enc_filename, "wb") as f:
            f.write(iv + ciphertext)   # Store IV + ciphertext

        # Key file (.key)
        key_filename = f"{base}_{algo}.key"
        with open(key_filename, "wb") as f:
            f.write(key + iv)          # Store key + IV

        status_label.config(text="Encryption successful")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ============================
# DECRYPTION FUNCTION
# ============================

def decrypt_file():
    """
    Handles decryption:
    - Loads encrypted file
    - Loads key file
    - Decrypts using same algorithm
    - Removes padding
    """
    if not selected_file or not selected_key_file:
        messagebox.showerror("Error", "Missing file or key file")
        return

    algo = algo_var.get()

    try:
        # Read encrypted file
        with open(selected_file, "rb") as f:
            file_data = f.read()

        # Extract IV and ciphertext
        iv = file_data[:8]
        ciphertext = file_data[8:]

        # Read key file
        with open(selected_key_file, "rb") as f:
            key_data = f.read()

        # Extract key (ignore IV stored in key file)
        if algo == "DES":
            key = key_data[:8]
        elif algo == "2TDEA":
            key = key_data[:16]
        else:
            key = key_data[:24]

        # Select cipher
        if algo == "DES":
            cipher = DES.new(key, DES.MODE_CBC, iv)
        else:
            cipher = DES3.new(key, DES3.MODE_CBC, iv)

        # Decrypt + unpad
        plaintext = unpad(cipher.decrypt(ciphertext), 8)

        # Save output
        base = os.path.basename(selected_file)
        output_name = f"{base}_decrypted"

        with open(output_name, "wb") as f:
            f.write(plaintext)

        status_label.config(text="Decryption successful")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ============================
# GUI SETUP
# ============================

root = Tk()
root.title("File Encryption Tool")
root.geometry("700x500")
root.configure(bg="#006400")

# File selection
Button(root, text="Select File", command=browse_file).pack()
file_label = Label(root, text="No file selected")
file_label.pack()

# Algorithm selection
algo_var = StringVar(value="DES")

Label(root, text="Select Algorithm").pack()

Radiobutton(root, text="DES", variable=algo_var, value="DES", command=update_description).pack()
Radiobutton(root, text="2TDEA", variable=algo_var, value="2TDEA", command=update_description).pack()
Radiobutton(root, text="3DES", variable=algo_var, value="3DES", command=update_description).pack()

# Description box
description_box = Text(root, height=5, width=60)
description_box.pack()
update_description()

# Operation selection
operation_var = StringVar(value="Encrypt")

def toggle_key_button():
    """
    Shows key selection only when decrypting.
    """
    if operation_var.get() == "Decrypt":
        key_button.pack()
        key_label.pack()
    else:
        key_button.pack_forget()
        key_label.pack_forget()

Radiobutton(root, text="Encrypt", variable=operation_var, value="Encrypt", command=toggle_key_button).pack()
Radiobutton(root, text="Decrypt", variable=operation_var, value="Decrypt", command=toggle_key_button).pack()

# Key file selection (hidden initially)
key_button = Button(root, text="Select Key File", command=browse_key_file)
key_label = Label(root, text="No key file selected")

# Action button
def run_operation():
    """
    Decides whether to encrypt or decrypt.
    """
    if operation_var.get() == "Encrypt":
        encrypt_file()
    else:
        decrypt_file()

Button(root, text="Run", command=run_operation).pack(pady=10)

# Status label
status_label = Label(root, text="Status: Waiting")
status_label.pack()

root.mainloop()