import tkinter as tk
from tkinter import font
from validator import password_check

def check_password(event=None):
    password = password_entry.get()
    result = password_check(password)
    status_label.config(text=result)

def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)

def close_app(event=None):
    root.destroy()

# Initialize main window
root = tk.Tk()
root.title("Secure Entry Portal")
root.attributes("-fullscreen", True)

# Set soft-pink background
bg_color = "#FFC0CB" # Soft pink
root.configure(bg=bg_color)

# Bind escape key to exit fullscreen or close app
root.bind("<Escape>", exit_fullscreen)
root.protocol("WM_DELETE_WINDOW", close_app)

# Create a container frame to center content
container = tk.Frame(root, bg=bg_color)
container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Title Label
title_font = font.Font(family="Helvetica", size=32, weight="bold")
title_label = tk.Label(
    container,
    text="Secure Entry Portal",
    font=title_font,
    bg=bg_color,
    fg="#333333"
)
title_label.pack(pady=(0, 30))

# Password Entry Field (Masked)
entry_font = font.Font(family="Helvetica", size=20)
password_entry = tk.Entry(
    container,
    font=entry_font,
    show="*",
    width=20,
    justify="center",
    bd=2,
    relief="groove"
)
password_entry.pack(pady=10)
password_entry.bind("<Return>", check_password)

# Verify Button
btn_font = font.Font(family="Helvetica", size=16, weight="bold")
verify_button = tk.Button(
    container,
    text="Verify",
    font=btn_font,
    command=check_password,
    bg="#ff99a8",
    activebackground="#ff8095",
    fg="white",
    bd=0,
    padx=20,
    pady=10,
    cursor="hand2"
)
verify_button.pack(pady=20)

# Status Label
status_font = font.Font(family="Helvetica", size=18)
status_label = tk.Label(
    container,
    text="Enter your password to verify",
    font=status_font,
    bg=bg_color,
    fg="#555555"
)
status_label.pack(pady=20)

# Instructions Label
instruction_font = font.Font(family="Helvetica", size=12)
instruction_label = tk.Label(
    root,
    text="Press ESC to exit fullscreen",
    font=instruction_font,
    bg=bg_color,
    fg="#777777"
)
instruction_label.pack(side=tk.BOTTOM, pady=20)

# Start the application
if __name__ == "__main__":
    password_entry.focus_set()
    root.mainloop()
