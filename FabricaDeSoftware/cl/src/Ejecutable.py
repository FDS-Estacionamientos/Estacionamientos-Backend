# %%
import cv2
import os
from matplotlib import pyplot as plt
from time import time

# %%
cap = cv2.VideoCapture("rtsp://admin:admin@192.168.4.54:554")

count = 0
previous = time()
delta = 0
while cap.isOpened():
    ret, frame = cap.read()
    current = time()
    delta += current - previous
    previous = current
    if ret:
        if delta > 30:
            lastimg = cv2.imwrite('FabricaDeSoftware/cl/src/testingwebcam/frame{:d}.jpg'.format(count), frame)
            lastimg2 = cv2.imwrite('FabricaDeSoftware/cl/src/imagenactual/frame.jpg', frame)

            if delta > 31:
                string_exe = "python FabricaDeSoftware/cl/src/yolo/yolov5/detect.py --weights yolov5/yolov5s.pt --img 676 --conf 0.4 --source FabricaDeSoftware/cl/src/imagenactual"
                os.system(string_exe)
                count = count + 1
                delta = 0

    else:
        cap.release()
        break


# %%

# Ejecutar celda si se quiere terminar.
cap.release()

# %% md

### Lectura de imágenes de OpenCV

Deberían
usarse
varias
cámaras, por
lo
que
quizá
sea
buena
idea
un
array.

Tendrán
RGB
incorrecto, pero
no
es
importante.(Al
YOLO
no
le
importa
que
sea
un
auto
rojo
o
verde, sino
que
sea
un
auto
nomás)

...
O
puedo
ser
un
gil
y
en
realidad
sí
importa.

# %%

imagenes = []

img = cv2.imread('varios/Z7HeRxU.png', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('varios/grande.jpg', cv2.IMREAD_UNCHANGED)

imagenes.append(img)
imagenes.append(img2)

# %%

# Para graficar:

% matplotlib
inline

plt.imshow(imagenes[1])
plt.show

# %% md

### Resize
Porque
se
debe
usar
una
resolución
pequeña
para
darle
un
empujoncito
al
YOLO.

# %%

# Reajustar tamaño de frames

# Se usará un 16:9?
dim = (640, 360)

# O un 4:3?
# dim = (640, 480)

imgnueva = cv2.resize(imagenes[0], dsize=dim, interpolation=cv2.INTER_AREA)
imgnueva2 = cv2.resize(imagenes[1], dsize=dim, interpolation=cv2.INTER_AREA)

# %% md

Fijarse
en
los
números
de
la
imagen, con
eso
podrían
saber
más
o
menos
las
dimensiones.

# %%

% matplotlib
inline

plt.imshow(imgnueva)
plt.show

# %% md

Este
segundo
plot
es
para
ver
si
el
array
de
imágenes
funciona
aunque
sean
formatos
diferentes.

# %%

% matplotlib
inline

plt.imshow(imgnueva2)
plt.show

# %% md

### Recortar
Acá, el
punto
es
que
se
recortan
las
imagenes
obtenidas
por
las
cámaras, ya
que
es
posible
que
se
repitan
estacionamientos
y
eso
causaría
conflictos.
Los
pixeles
deben
ser
definidos
según
las
dimensiones, por
lo
que
hay
que
tener
cuidado.

Este
es
el
apartado
de
extracción
de
frames.

# %%

cropeada = imgnueva[50:200, 50:100]

cv2.imwrite('cropped/1.jpg', cropeada)

# %%

% matplotlib
inline

plt.imshow(cropeada)
plt.show

# %% md

## Ahora deberían estar listas la imágenes para el YOLO.
