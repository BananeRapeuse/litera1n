import tkinter as tk
from tkinter import ttk  # Importation de ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import subprocess

# URL du logo
LOGO_URL = "https://raw.githubusercontent.com/BananeRapeuse/litera1n/main/litera1n.png"

# URL des images et textes pour chaque modèle
ASSETS = {
    "5s-6s": {
        "step1": "https://github.com/BananeRapeuse/litera1n/blob/main/gui/5s-6s_assets/step1.jpeg?raw=true",
        "step2": "https://github.com/BananeRapeuse/litera1n/blob/main/gui/5s-6s_assets/step2.jpeg?raw=true",
        "texts": [
            "1. Get ready to enter DFU mode and click 'Enter DFU' to begin",
            "2. Press and hold Power button + Home button for 8 seconds",
            "3. Keep holding the Home button and release the Power button",
            "4. If you have a black screen, ENJOY YOU'RE IN DFU Mode!"
        ]
    },
    "7": {
        "step1": "https://github.com/BananeRapeuse/litera1n/blob/main/gui/7_assets/step1.jpeg?raw=true",
        "step2": "https://github.com/BananeRapeuse/litera1n/blob/main/gui/7_assets/step2.jpeg?raw=true",
        "texts": [
            "1. Get ready to enter DFU mode and click 'Enter DFU' to begin",
            "2. Press and hold Power button + Vol- button for 8 seconds",
            "3. Keep holding the Vol- button and release the Power button",
            "4. If you have a black screen, ENJOY YOU'RE IN DFU Mode!"
        ]
    },
    "8-X": {
        "step1": "https://github.com/BananeRapeuse/litera1n/blob/main/gui/8-X_assets/step1.jpeg?raw=true",
        "step2": "https://github.com/BananeRapeuse/litera1n/blob/main/gui/8-X_assets/step2.jpeg?raw=true",
        "step3": "https://github.com/BananeRapeuse/litera1n/blob/main/gui/8-X_assets/step3.jpeg?raw=true",
        "step4": "https://github.com/BananeRapeuse/litera1n/blob/main/gui/8-X_assets/step4.jpeg?raw=true",
        "step5": "https://github.com/BananeRapeuse/litera1n/blob/main/gui/8-X_assets/step5.jpeg?raw=true",
        "texts": [
            "1. Get ready to enter DFU mode and click 'Enter DFU' to begin",
            "2. Quickly press Vol+ and Vol- buttons",
            "3. Hold the Power button until the screen goes black",
            "4. Press and Hold both the Vol- button and Power button for 5 seconds",
            "5. Release the Power button",
            "6. If you have a black screen, ENJOY YOU'RE IN DFU Mode!"
        ]
    }
}

class Litera1nApp:
    def __init__(self, root):
        self.root = root
        self.root.title("litera1n - Version beta 0.3")
        self.root.geometry("1280x720")  # Taille de la fenêtre en 720p (1280x720 pixels)
        self.root.resizable(False, False)  # Désactiver la redimension de la fenêtre
        self.root.configure(bg='white')  # Fond de la fenêtre blanc

        # Charger le logo
        self.logo_image = self.load_image_from_url(LOGO_URL, (200, 200))  # Augmenté pour mieux être visible

        # Créer des écrans
        self.main_screen()

    def main_screen(self):
        """Affiche l'écran principal avec les éléments spécifiés"""
        self.clear_screen()

        # Ajouter le logo au centre
        self.logo_label = tk.Label(self.root, image=self.logo_image, bg='white')
        self.logo_label.place(relx=0.5, rely=0.5, anchor='center')

        self.title_label = tk.Label(self.root, text="litera1n - Version beta 0.3", font=("Helvetica", 20, "bold"), bg='white')
        self.title_label.pack(pady=10)

        self.welcome_label = tk.Label(self.root, text="Welcome to litera1n", font=("Helvetica", 16), bg='white')
        self.welcome_label.pack(pady=10)

        self.info_label = tk.Label(self.root, text="Connect your iDevice to begin.", font=("Helvetica", 12), bg='white')
        self.info_label.pack(pady=10)

        self.made_by_label = tk.Label(self.root, text="Made by Ph0qu3_111", font=("Helvetica", 12), bg='white')
        self.made_by_label.pack(pady=5)

        self.thanks_label = tk.Label(self.root, text="Thanks to: axi0mX (for the checkm8 exploit and ipwndfu), Kim Jong Cracks (for checkra1n), walac (for pyusb)", font=("Helvetica", 10), bg='white')
        self.thanks_label.pack(pady=5)

        self.note_label = tk.Label(self.root, text="NOTE: Please make a backup of your device in iTunes before performing the jailbreak.", font=("Helvetica", 10), bg='white')
        self.note_label.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Start", command=self.device_selection_screen, width=30, height=2)
        self.start_button.pack(side=tk.BOTTOM, pady=10)

    def device_selection_screen(self):
        """Affiche l'écran pour choisir le modèle d'iPhone"""
        self.clear_screen()

        self.device_label = tk.Label(self.root, text="Select your iPhone model", font=("Helvetica", 14), bg='white')
        self.device_label.pack(pady=10)

        self.device_5s_6s_button = tk.Button(self.root, text="iPhone 5s-6s", command=lambda: self.show_dfu_steps("5s-6s"), width=30, height=2)
        self.device_5s_6s_button.pack(pady=5)

        self.device_7_button = tk.Button(self.root, text="iPhone 7", command=lambda: self.show_dfu_steps("7"), width=30, height=2)
        self.device_7_button.pack(pady=5)

        self.device_8_x_button = tk.Button(self.root, text="iPhone 8-X", command=lambda: self.show_dfu_steps("8-X"), width=30, height=2)
        self.device_8_x_button.pack(pady=5)

    def show_dfu_steps(self, device):
        """Affiche les étapes pour entrer en mode DFU après la sélection du modèle"""
        self.clear_screen()

        # Afficher l'instruction "Follow the next steps"
        self.instructions_label = tk.Label(self.root, text="Follow the next steps", font=("Helvetica", 14), bg='white')
        self.instructions_label.place(x=20, y=10)

        # Afficher le bouton "Enter DFU"
        self.enter_dfu_button = tk.Button(self.root, text="Enter DFU", command=self.display_dfu_images)
        self.enter_dfu_button.place(x=1050, y=650)

        # Afficher les textes des instructions à droite
        self.texts = ASSETS[device]["texts"]
        self.step_images = [ASSETS[device].get(f"step{i+1}") for i in range(len(self.texts))]

        self.text_labels = []
        for i, text in enumerate(self.texts):
            label = tk.Label(self.root, text=text, font=("Helvetica", 12), wraplength=300, bg='white')
            label.place(x=800, y=50 + i*60)  # Ajuster la position des textes pour la visibilité
            self.text_labels.append(label)

        # Initialiser le texte en gras
        self.current_step = 0
        self.update_text_style(self.current_step, True)

    def update_text_style(self, step_index, is_bold):
        """Met à jour le style du texte pour l'étape actuelle"""
        if step_index < len(self.text_labels):
            for i, label in enumerate(self.text_labels):
                font = ("Helvetica", 12, "bold") if i == step_index and is_bold else ("Helvetica", 12)
                label.config(font=font)

    def display_dfu_images(self):
        """Affiche les images étape par étape pour le mode DFU"""
        # Afficher l'image Step 1 redimensionnée à 300x520
        step1_image = self.load_image_from_url(self.step_images[0], (300, 520))
        self.dfu_image_label = tk.Label(self.root, image=step1_image, bg='white')
        self.dfu_image_label.image = step1_image  # Garde une référence pour éviter que l'image soit garbage collected
        self.dfu_image_label.place(relx=0.5, rely=0.5, anchor='center')

        # Mettre en gras le texte de l'étape 1 et démarrer le compte à rebours
        self.update_text_style(0, True)
        self.root.after(2000, self.show_step2_image)

    def show_step2_image(self):
        """Affiche la deuxième étape après 1 seconde pour iPhone 8-X ou 8 secondes pour les autres"""
        step2_image = self.load_image_from_url(self.step_images[1], (300, 520))
        self.dfu_image_label.config(image=step2_image)
        self.dfu_image_label.image = step2_image  # Garde une référence

        # Mettre en gras le texte correspondant à l'étape 2
        self.update_text_style(1, True)

        # Passer à l'étape suivante après 1 seconde pour iPhone 8-X, sinon 8 secondes
        if len(self.step_images) == 5:  # iPhone 8-X
            self.root.after(1000, self.show_step3_image)
        else:
            self.root.after(8000, self.show_step3_image)

    def show_step3_image(self):
        """Affiche la troisième étape après 1 seconde pour iPhone 8-X ou 8 secondes pour les autres"""
        step3_image = self.load_image_from_url(self.step_images[2], (300, 520))
        self.dfu_image_label.config(image=step3_image)
        self.dfu_image_label.image = step3_image  # Garde une référence

        # Mettre en gras le texte correspondant à l'étape 3
        self.update_text_style(2, True)

        # Passer à l'étape suivante après 1 seconde pour iPhone 8-X, sinon 8 secondes
        if len(self.step_images) == 5:  # iPhone 8-X
            self.root.after(1000, self.show_step4_image)
        else:
            self.root.after(8000, self.show_step4_image)

    def show_step4_image(self):
        """Affiche la quatrième étape après le temps spécifié"""
        step4_image = self.load_image_from_url(self.step_images[3], (300, 520))
        self.dfu_image_label.config(image=step4_image)
        self.dfu_image_label.image = step4_image  # Garde une référence

        # Mettre en gras le texte correspondant à l'étape 4
        self.update_text_style(3, True)

        # Passer à l'étape suivante après 1 seconde pour iPhone 8-X, sinon 8 secondes
        if len(self.step_images) == 5:  # iPhone 8-X
            self.root.after(1000, self.show_step5_image)
        else:
            self.root.after(8000, self.show_step5_image)

    def show_step5_image(self):
        """Affiche la cinquième étape après le temps spécifié"""
        step5_image = self.load_image_from_url(self.step_images[4], (300, 520))
        self.dfu_image_label.config(image=step5_image)
        self.dfu_image_label.image = step5_image  # Garde une référence

        # Mettre en gras le texte correspondant à l'étape 5
        self.update_text_style(4, True)

        # Passer au menu "Jailbreak" après un court délai
        self.root.after(2000, self.show_jailbreak_screen)

    def show_jailbreak_screen(self):
        """Affiche l'écran de jailbreak avec une barre de progression"""
        self.clear_screen()
        self.root.title("litera1n - Jailbreaking...")

        # Écran de progression
        self.jailbreak_label = tk.Label(self.root, text="Jailbreaking...", font=("Helvetica", 20, "bold"), bg='white')
        self.jailbreak_label.pack(pady=10)

        self.progress = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress, maximum=100, length=400)  # Utiliser ttk.Progressbar
        self.progress_bar.pack(pady=20)

        self.info_label = tk.Label(self.root, text="For more jailbreak info, check your command line", font=("Helvetica", 12), bg='white')
        self.info_label.pack(pady=10)

        # Démarrer la mise à jour de la barre de progression
        self.progress_value = 0
        self.update_progress_bar()

        # Exécuter la commande après 3 secondes
        self.root.after(3000, self.run_jailbreak_command)

    def update_progress_bar(self):
        """Met à jour la barre de progression toutes les 2 secondes"""
        self.progress_value += 25
        if self.progress_value > 100:
            self.progress_value = 100

        self.progress.set(self.progress_value)

        if self.progress_value < 100:
            self.root.after(2000, self.update_progress_bar)

    def run_jailbreak_command(self):
        """Exécute la commande de jailbreak"""
        try:
            subprocess.run(["python", "ipwndfu", "-p"], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Command failed: {e}")

    def clear_screen(self):
        """Efface le contenu de la fenêtre"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def load_image_from_url(self, url, size):
        """Charge une image depuis une URL et la redimensionne"""
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)

if __name__ == "__main__":
    root = tk.Tk()
    app = Litera1nApp(root)
    root.mainloop()
