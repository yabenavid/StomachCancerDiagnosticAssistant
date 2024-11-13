import image_form, segmentation_skimage

images = image_form.seleccionar_imagenes()

segmentation_skimage.segment(images)