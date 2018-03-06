###Cargar Imagen original### 

import matplotlib.pyplot as plt
import numpy as np
from pylab import imread, imshow

img = imread('D:\Esteban\Desktop\Ezatara\EZ\EZ-Images\grim.jpg').astype(np.float32)  #Se lee archivo con la funcion imread de pylab

image = img / 255
imshow(image)		#Se muestra la imagen con la funcion ishow de la libreria matplotlib


#Cargar y Leer CSV 

import numpy as np

data = np.genfromtxt('D:/Esteban/Desktop/Ezatara/EZ-U/Aseguramiento/POC/train.csv', delimiter = ',', skip_header=1, dtype=None) #Se utiliza numpy y su funcion 
																																#de genfromtxt para leer el archivo
for row in data:
	print(row)						#Se imprimen las row del archivo en forma de array
	#print(row[0], row[1], row[2])	#Para cargar el csv pero no desplegar de forma de array


###Cargar la imagen y ponerle y manejar el contraste a la misma###

from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np
from pylab import imread, imshow, gray, mean

img = imread('D:\Esteban\Desktop\Ezatara\EZ\EZ-Images\grim.jpg').astype(np.float32)	#Se lle el archivo con imread de pylab 

image = mean(img,2)
plt.imshow(image, cmap=plt.cm.gray, vmin=30, vmax=200)	#Se usa la libreria matplotlib para hacer un remapeo de la imagen en gris y manejar su contraste 
plt.axis('off')	#Se eliminan los axes 

plt.show()	#Se muestra la imagen con la modificación