import tkinter as tk
from tkinter import messagebox
import socket
import hashlib
import re

# ------------------- Functions -------------------

def scan_ports():
    ip = entry_ip.get()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Scanning open ports for {ip}...\n\n")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]

    for port in common_ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            res = s.connect_ex((ip, port))
            if res == 0:
                result_text.insert(tk.END, f"Port {port} is OPEN\n")
            s.close()
        except:
            result_text.insert(tk.END, "Error scanning ports\n")
            break


def check_password():
    pwd = entry_password.get()
    score = 0

    if len(pwd) >= 8:
        score += 1
    if re.search("[A-Z]", pwd):
        score += 1
    if re.search("[a-z]", pwd):
        score += 1
    if re.search("[0-9]", pwd):
        score += 1
    if re.search("[@#$%^&*!]", pwd):
        score += 1

    if score <= 2:
        strength = "Weak ❌"
    elif score == 3 or score == 4:
        strength = "Medium ⚠️"
    else:
        strength = "Strong ✅"

    messagebox.showinfo("Password Strength", f"Password Strength: {strength}")


def generate_hash():
    text = entry_hash.get()
    algo = hash_var.get()

    if algo == "MD5":
        hashed = hashlib.md5(text.encode()).hexdigest()
    else:
        hashed = hashlib.sha256(text.encode()).hexdigest()

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"{algo} Hash:\n{hashed}")


def check_url():
    url = entry_url.get().lower()
    suspicious_words = ["free", "login", "verify", "bank", "offer", "click"]

    score = 0
    for word in suspicious_words:
        if word in url:
            score += 1

    if score >= 2:
        messagebox.showwarning("URL Safety", "This URL looks SUSPICIOUS ⚠️")
    else:
        messagebox.showinfo("URL Safety", "This URL looks SAFE ✅")


# ------------------- UI -------------------

app = tk.Tk()
app.title("Cybersecurity All-in-One Toolkit")
app.geometry("420x650")
app.config(bg="#020617")

title = tk.Label(app, text="CYBERSECURITY TOOLKIT", font=("Arial", 16, "bold"), fg="#38bdf8", bg="#020617")
title.pack(pady=10)

# IP Scanner
tk.Label(app, text="Port Scanner (Enter IP):", fg="white", bg="#020617").pack()
entry_ip = tk.Entry(app)
entry_ip.pack()
tk.Button(app, text="Scan Ports", command=scan_ports, bg="#22c55e").pack(pady=5)

# Password Checker
tk.Label(app, text="Password Strength Checker:", fg="white", bg="#020617").pack()
entry_password = tk.Entry(app, show="*")
entry_password.pack()
tk.Button(app, text="Check Password", command=check_password, bg="#facc15").pack(pady=5)

# Hash Generator
tk.Label(app, text="Hash Generator (Text):", fg="white", bg="#020617").pack()
entry_hash = tk.Entry(app)
entry_hash.pack()

hash_var = tk.StringVar(value="MD5")
tk.Radiobutton(app, text="MD5", variable=hash_var, value="MD5", bg="#020617", fg="white").pack()
tk.Radiobutton(app, text="SHA-256", variable=hash_var, value="SHA-256", bg="#020617", fg="white").pack()

tk.Button(app, text="Generate Hash", command=generate_hash, bg="#a78bfa").pack(pady=5)

# URL Checker
tk.Label(app, text="URL Safety Checker:", fg="white", bg="#020617").pack()
entry_url = tk.Entry(app)
entry_url.pack()
tk.Button(app, text="Check URL", command=check_url, bg="#fb7185").pack(pady=5)

# Result Box
result_text = tk.Text(app, height=10, width=45)
result_text.pack(pady=10)

footer = tk.Label(app, text="Developed by Balaji P | For Educational Use Only", fg="gray", bg="#020617")
footer.pack(pady=5)

app.mainloop()