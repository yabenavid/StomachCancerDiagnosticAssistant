import image_form, segmentation_skimage, sam

# leer el dataset y realiza el entrenamiento
images = image_form.seleccionar_imagenes()

X = segmentation_skimage.segment(images)

# Y = sam.segment(images)