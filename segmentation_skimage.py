import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from skimage import data, filters, segmentation as skimage_segmentation
from PIL import Image, ImageTk


def segment(images):
    for img_path in images:
        imgn = Image.open(img_path)
        img = np.array(imgn)

        # print('Type: ', type(images))
        # print('dtype: ', images.dtype)
        # print('shape:', images.shape)

        # Mostrar imagen inicial
        plt.title("Imagen Inicial Escala de Grises")
        plt.imshow(img, cmap="gray")
        plt.axis("off")  # Opcional: Oculta los ejes
        plt.show()

        # Crear marcadores
        markers = np.zeros_like(img)
        markers[img < 30] = 1
        markers[img > 150] = 2

        # Calcular el mapa de elevación
        elevation_map = filters.sobel(img)

        # Mostrar mapa de elevación
        plt.title("Mapa de Elevación (Sobel)")
        plt.imshow(elevation_map, cmap="gray")
        plt.axis("off")
        plt.show()

        # Mostrar marcadores
        plt.title("Marcadores")
        plt.imshow(markers, cmap="viridis")
        plt.axis("off")
        plt.show()

        # Realizar la segmentación
        segmentation = skimage_segmentation.watershed(elevation_map, markers)

        # Mostrar segmentación obtenida
        plt.title("Segmentación")
        plt.imshow(segmentation, cmap="gray")
        plt.axis("off")
        plt.show()

        # Llenar agujeros en la segmentación
        segmentation = sp.ndimage.binary_fill_holes(segmentation - 1)
        labeled_images, _ = sp.ndimage.label(segmentation)

        # Mostrar la imagen segmentada superpuesta sobre la imagen original
        plt.figure(figsize=(10, 5))
        plt.imshow(img, cmap="gray")  # Imagen original
        plt.title("Resultado: Imagen Inicial con Segmentación")
        plt.axis("off")

        # Usar contours para superponer las etiquetas
        plt.imshow(
            labeled_images, alpha=0.5, cmap="nipy_spectral"
        )  # Superponer con transparencia
        plt.show()
