import tkinter as tk
from tkinter import ttk
from ytdl import *

def download_content():
    content = entry.get("1.0", tk.END)  # Récupère le contenu de la zone de texte
    selected_extension = "." + extension_combobox.get()  # Récupère l'extension sélectionnée
    t1 = timestamp_start.get("1.0", tk.END)
    t0 = timestamp_end.get("1.0", tk.END)
    download_video(content, selected_extension,t0,t1)

# Crée la fenêtre principale
app = tk.Tk()
app.title("YoutubeDL")

# Crée une zone de texte
entry = tk.Text(app, height=5, width=50)
entry.grid(row=0, column=0, padx=10, pady=10)

label_format = tk.Label(app, text='Écrit les heures dans se format : "22:11"')
label_format.grid(row=0, column=1, padx=2, pady=2)


#---------------Row 1---------------#
#-----Timestamp buttons-----#
timestamp_container = ttk.Frame(app)
timestamp_container.grid(row=1, column=0, padx=5, pady=5)

label_timestamp_start = tk.Label(timestamp_container, text='start')
label_timestamp_start.grid(row=0, column=1)
timestamp_start = tk.Text(timestamp_container, height=1, width=5)
timestamp_start.grid(row=1, column=1, padx=2, pady=2)

label_timestamp_end = tk.Label(timestamp_container, text='end')
label_timestamp_end.grid(row=0, column=2)
timestamp_end = tk.Text(timestamp_container, height=1, width=5)
timestamp_end.grid(row=1, column=2, padx=2, pady=2)

#-----Extensions-----#
extensions = ["mp3", "mp4"]
extension_combobox = ttk.Combobox(timestamp_container, values=extensions, state="readonly")
extension_combobox.set("mp4")  # Sélectionne mp4 par défaut
extension_combobox.grid(row=1, column=0, padx=2, pady=2)
#----------------------------------#

# Crée un bouton de téléchargement
download_button = tk.Button(app, text="Download", command=download_content)
download_button.grid(row=1, column=1, pady=2, padx=2)






#-----Display of the window-----#
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x_coordinate = (screen_width - app.winfo_reqwidth()) // 2
y_coordinate = (screen_height - app.winfo_reqheight()) // 2

# Définit les coordonnées de la fenêtre
app.geometry("+{}+{}".format(x_coordinate, y_coordinate))

# Lance la boucle principale de l'interface graphique
app.mainloop()
