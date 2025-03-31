from gtts import gTTS
import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def text_to_speech():
    text = entry.get()
    language = language_var.get()
    speed = speed_var.get()
    
    if not text.strip():
        messagebox.showwarning("Warning", "Please enter some text!")
        return
    
    slow = speed == "Slow"
    
    try:
        tts = gTTS(text=text, lang=languages.get(language, "en"), slow=slow)
        tts.save("output.mp3")
        os.system("start output.mp3" if os.name == "nt" else "afplay output.mp3")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong! {str(e)}")

# GUI Setup
root = tk.Tk()
root.title("Text-to-Speech Converter")
root.geometry("800x600")
root.configure(bg="#e6f2ff")

# Language Dictionary
languages = {
    "English": "en", "Hindi": "hi", "Spanish": "es", "French": "fr", 
    "German": "de", "Chinese": "zh-cn", "Japanese": "ja", "Russian": "ru"
}

# Title Label
title_label = ttk.Label(root, text="🗣️ Text-to-Speech Converter", font=("Arial", 24, "bold"), background="#e6f2ff", foreground="#1b4f72")
title_label.pack(pady=20)

# Entry Widget
entry_frame = tk.Frame(root, bg="#e6f2ff")
entry_frame.pack(pady=10)
entry_label = ttk.Label(entry_frame, text="Enter Text:", font=("Arial", 14, "bold"), background="#e6f2ff")
entry_label.pack(side=tk.LEFT, padx=10)
entry = ttk.Entry(entry_frame, width=50, font=("Arial", 14))
entry.pack(side=tk.LEFT, padx=10)

# Language Selection
language_var = tk.StringVar(value="English")
lang_frame = tk.Frame(root, bg="#e6f2ff")
lang_frame.pack(pady=10)
ttk.Label(lang_frame, text="🌍 Select Language:", font=("Arial", 14, "bold"), background="#e6f2ff").pack(side=tk.LEFT, padx=10)
language_menu = ttk.Combobox(lang_frame, textvariable=language_var, values=list(languages.keys()), state="readonly", font=("Arial", 12))
language_menu.pack(side=tk.LEFT)

# Speed Selection
speed_var = tk.StringVar(value="Normal")
speed_frame = tk.Frame(root, bg="#e6f2ff")
speed_frame.pack(pady=10)
ttk.Label(speed_frame, text="⚡ Select Speed:", font=("Arial", 14, "bold"), background="#e6f2ff").pack(side=tk.LEFT, padx=10)
speed_menu = ttk.Combobox(speed_frame, textvariable=speed_var, values=["Normal", "Slow"], state="readonly", font=("Arial", 12))
speed_menu.pack(side=tk.LEFT)

# Convert Button
convert_button = tk.Button(root, text="🎤 Convert to Speech", command=text_to_speech, font=("Arial", 16, "bold"), bg="#28a745", fg="white", padx=20, pady=10, relief="raised", borderwidth=4)
convert_button.pack(pady=20)

# Footer
footer_label = ttk.Label(root, text="Developed by Ayush Pallaw", font=("Arial", 12, "italic"), background="#e6f2ff", foreground="#1b4f72")
footer_label.pack(side=tk.BOTTOM, pady=15)

# Run Application
root.mainloop()
