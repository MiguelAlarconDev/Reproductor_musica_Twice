import tkinter as tk
from tkinter import ttk
import threading
from player import MusicPlayer
from songs import songs

def reproducir_cancion():
    seleccion = lista_canciones.curselection()
    if seleccion:
        indice = seleccion[0]
        cancion = songs[indice]
        threading.Thread(target=player.play, args=(cancion["archivo"],)).start()

ventana = tk.Tk()
ventana.title("Reproductor de Twice")

player = MusicPlayer()

lista_canciones = tk.Listbox(ventana, width=40, height=10)
for song in songs:
    lista_canciones.insert(tk.END, song["titulo"])
lista_canciones.pack(pady=10)

boton_play = ttk.Button(ventana, text="Reproducir", command=reproducir_cancion)
boton_play.pack(pady=10)

ventana.mainloop()
