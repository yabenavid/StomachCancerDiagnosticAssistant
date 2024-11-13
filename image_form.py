import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np

# Crear una función para seleccionar múltiples imágenes


def seleccionar_imagenes():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    archivos = filedialog.askopenfilenames(title="Seleccionar imágenes", filetypes=[
                                           ("Archivos de imagen", ".png;.jpg;.jpeg;.gif")])
    return list(archivos)


# Seleccionar imágenes

# imagenes = seleccionar_imagenes()

# # Mostrar cada imagen
# for img_path in imagenes:
#     img = Image.open(img_path)
#     plt.imshow(img)
#     plt.axis('off')  # Ocultar los ejes
#     plt.show()