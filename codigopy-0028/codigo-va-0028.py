# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import os
# ruta de imagen
ruta = os.path.join(
    "img-original-0028",
    "microondas.webp"
)
# Imagen
# Vamos a crear nuestra matriz principal
microondas = cv2.imread(ruta)
# print(microondas) muestra las matrices de la imagen
# # convertir de BGR a RGB color rojo COLOR_BGR2RGB
micro = cv2.cvtColor(microondas, cv2.COLOR_BGR2RGB)
# cv2.imshow("microondas",microondas )
cv2.imshow("microondas color",micro )
cv2.waitKey(0) # tiempo de espera 
cv2.destroyAllWindows() # destruye todas las ventanas en memoria