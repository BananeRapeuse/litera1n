import tkinter as tk
from tkinter import Text
import subprocess

# Fonction pour lire la version depuis le fichier "version"
def read_version():
    try:
        with open("version", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "unknown"

# Fonction exécutée lors du clic sur le bouton "Jailbreak"
def jailbreak():
    window.title("Jailbreaking…")
    jailbreak_button.config(state=tk.DISABLED)
    # Exécute la commande pour le jailbreak
    subprocess.Popen(["python", "ipwndfu", "-p"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Fonction pour exécuter une commande dans le terminal intégré
def run_command():
    command = terminal_input.get("1.0", tk.END).strip()
    if command:
        terminal_output.insert(tk.END, f"> {command}\n")
        terminal_input.delete("1.0", tk.END)
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        terminal_output.insert(tk.END, result.stdout + result.stderr + "\n")

# Lecture de la version
version = read_version()

# Configuration de la fenêtre principale
window = tk.Tk()
window.title(f"litera1n Jailbreak: version {version}")
window.geometry("800x600")

# Bouton de jailbreak
jailbreak_button = tk.Button(window, text="Jailbreak", command=jailbreak)
jailbreak_button.pack(pady=20)

# Terminal intégré (affiche l'output)
terminal_output = Text(window, height=15, width=100)
terminal_output.pack(pady=10)

# Terminal intégré (input de commande)
terminal_input = Text(window, height=2, width=100)
terminal_input.pack(pady=5)
terminal_input.bind("<Return>", lambda event: run_command())

# Exécution initiale de la commande "python term.py"
result = subprocess.run(["python", "term.py"], capture_output=True, text=True)
terminal_output.insert(tk.END, result.stdout + result.stderr + "\n")

# Boucle principale de l'interface
window.mainloop()
