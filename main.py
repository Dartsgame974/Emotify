from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar



def redimensionner_image(chemin_image, taille):
    image = Image.open(chemin_image)
    image_redimensionnee = image.resize((taille, taille), Image.LANCZOS)
    return image_redimensionnee

def redimensionner_images_png(repertoire, options_selectionnees):
    if not os.path.exists(repertoire):
        messagebox.showerror("Erreur", "Le répertoire spécifié n'existe pas.")
        return
    
    # Liste des tailles pour chaque option
    tailles = {}

    if options_selectionnees["Twitch"]:
        tailles["Twitch"] = [72, 36, 18]

    if options_selectionnees["Discord"]:
        tailles["Discord"] = [256]

    if options_selectionnees["ChannelPoints"]:
        tailles["ChannelPoints"] = [28, 56, 112]

    if not tailles:
        messagebox.showerror("Erreur", "Aucune option de redimensionnement sélectionnée.")
        return

    total_fichiers = len([fichier for fichier in os.listdir(repertoire) if fichier.lower().endswith('.png')]) * sum(len(t) for t in tailles.values())
    progres = 0
    barre_progression['maximum'] = total_fichiers

    for option, sizes in tailles.items():
        dossier_destination = os.path.join(repertoire, option)
        os.makedirs(dossier_destination, exist_ok=True)

        fichiers_png = [fichier for fichier in os.listdir(repertoire) if fichier.lower().endswith('.png')]

        for fichier in fichiers_png:
            chemin_fichier = os.path.join(repertoire, fichier)
            for size in sizes:
                image_redimensionnee = redimensionner_image(chemin_fichier, size)
                image_redimensionnee.save(os.path.join(dossier_destination, f'{fichier[:-4]}_{size}x{size}.png'))

                progres += 1
                label_texte.config(text=f"{fichier} - Redimensionné ({progres}/{total_fichiers})")
                barre_progression['value'] = progres
                fenetre.update()

    messagebox.showinfo("Terminé", "Les images ont été redimensionnées avec succès.")

def parcourir_dossier():
    chemin_repertoire = filedialog.askdirectory()
    entry_chemin.delete(0, tk.END)
    entry_chemin.insert(0, chemin_repertoire)

fenetre = tk.Tk()
fenetre.title("Emotify")
fenetre.geometry("400x400")

#fenetre.option_add('*Font', 'Segoe UI')

frame_titre = tk.Frame(fenetre)
frame_titre.pack(pady=10)
label_titre = tk.Label(frame_titre, text="Emotify", font=("Arial", 20))
label_titre.pack(side="left", padx=10)

button_parcourir = tk.Button(fenetre, text="Parcourir", command=parcourir_dossier, font=("Arial", 10))
button_parcourir.pack()

label_chemin = tk.Label(fenetre, text="Entrez le chemin du répertoire contenant les images PNG à redimensionner:", font=("Arial", 10))
label_chemin.pack()
entry_chemin = tk.Entry(fenetre, width=50)
entry_chemin.pack()

options_selectionnees = {"Twitch": tk.BooleanVar(), "Discord": tk.BooleanVar(), "ChannelPoints": tk.BooleanVar()}
label_options = tk.Label(fenetre, text="Options de redimensionnement:", font=("Arial", 10))
label_options.pack()

for option in options_selectionnees:
    checkbutton = tk.Checkbutton(fenetre, text=option, variable=options_selectionnees[option], font=("Arial", 10))
    checkbutton.pack(anchor="w")

label_custom = tk.Label(fenetre, text="Résolution personnalisée (facultatif) :", font=("Arial", 10))
label_custom.pack()
entry_custom = tk.Entry(fenetre, width=50)
entry_custom.pack()

button_redimensionner = tk.Button(fenetre, text="Redimensionner", command=lambda: redimensionner_images_png(entry_chemin.get(), options_selectionnees), font=("Arial", 10))
button_redimensionner.pack()

barre_progression = Progressbar(fenetre, orient=tk.HORIZONTAL, length=200, mode='determinate')
barre_progression.pack(pady=20)

label_texte = tk.Label(fenetre, text="", font=("Arial", 10))
label_texte.pack()

fenetre.mainloop()
