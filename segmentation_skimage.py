import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from skimage import data, filters, segmentation as skimage_segmentation, color
from PIL import Image, ImageTk

def segment(images):
    for img_path in images:
        # Cargar la imagen
        imgn = Image.open(img_path)
        
        # Convertir a RGB si tiene canal alfa (RGBA)
        if imgn.mode == 'RGBA':
            imgn = imgn.convert('RGB')
            
        img = np.array(imgn)
        
        # Convertir a escala de grises si es una imagen a color
        if len(img.shape) == 3:
            img_gray = color.rgb2gray(img)
        else:
            img_gray = img / 255.0 if img.max() > 1 else img
            
        # Mostrar imagen inicial
        plt.figure(figsize=(8, 6))
        plt.title("Imagen Histológica Original")
        plt.imshow(img)
        plt.axis("off")
        plt.show()
        
        # Preprocesamiento - mejora de contraste
        p2, p98 = np.percentile(img_gray, (2, 98))
        img_rescale = np.clip((img_gray - p2) / (p98 - p2), 0, 1)
        
        # Mostrar imagen preprocesada
        plt.figure(figsize=(8, 6))
        plt.title("Imagen Preprocesada")
        plt.imshow(img_rescale, cmap="gray")
        plt.axis("off")
        plt.show()
        
        # Crear marcadores adaptados a histología
        # Ajustar estos umbrales según la imagen específica
        markers = np.zeros_like(img_gray, dtype=np.uint8)
        
        # Marcar estructuras oscuras (núcleos, estructuras epiteliales)
        markers[img_gray < 0.4] = 1
        
        # Marcar estructuras claras (fondo, espacios vacíos)
        markers[img_gray > 0.8] = 2
        
        # Marcar tejido conectivo (valores intermedios)
        mask_conectivo = (img_gray >= 0.5) & (img_gray <= 0.7)
        markers[mask_conectivo] = 3
        
        # Mostrar marcadores
        plt.figure(figsize=(8, 6))
        plt.title("Marcadores para Tejidos")
        plt.imshow(markers, cmap="nipy_spectral")
        plt.colorbar(label='Tipo de Tejido')
        plt.axis("off")
        plt.show()
        
        # Calcular el mapa de elevación con un filtro más adecuado para tejidos
        elevation_map = filters.scharr(img_gray)
        
        # Mostrar mapa de elevación
        plt.figure(figsize=(8, 6))
        plt.title("Mapa de Bordes (Filtro Scharr)")
        plt.imshow(elevation_map, cmap="magma")
        plt.axis("off")
        plt.show()
        
        # Realizar la segmentación watershed
        segmentation = skimage_segmentation.watershed(elevation_map, markers, watershed_line=True)
        
        # Mostrar segmentación obtenida
        plt.figure(figsize=(8, 6))
        plt.title("Segmentación de Tejidos")
        plt.imshow(segmentation, cmap="nipy_spectral")
        plt.colorbar(label='Regiones')
        plt.axis("off")
        plt.show()
        
        # Superponer resultado sobre la imagen original
        plt.figure(figsize=(10, 8))
        plt.title("Resultado: Imagen Original con Segmentación")
        plt.imshow(img)
        plt.imshow(segmentation, alpha=0.5, cmap="nipy_spectral")
        plt.axis("off")
        plt.show()
        
        # Para compatibilidad con el código original - regresar segmentación
        return segmentation