# https://www.youtube.com/watch?v=eLTLtUVuuy4
import cv2
import numpy as np
import matplotlib.pyplot as plt
from iniciar_zed import capture_image

# Função para filtro cinza, gaussian blur e gradiente
def canny(image):
    # Passa um filtro cinza na imagem
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    #Blur ajuda a reduzir os "ruídos" da imagem, pega um pixel e faz com que se pareça mais com os mais próximos
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Calculas os gradientes da função dos pixels da imagem, se for alto quer dizer que há uma mudança brusca de cor (braco-preto)
    # (imagem, low_threshold, high_threshold)
    canny = cv2.Canny(blur, 50, 150)
    return canny


# Lê a imagem e retorna um array multidimensional contendo as intensidades de cada pixel
image = capture_image()
# Faz uma cópia da imagem para filtro cinza
lane_image = np.copy(image)
canny_image = canny(lane_image)

# Mostra a imagem na tela, a partir da região de interesse e da imagem otimizada
cv2.imshow('result', canny_image)
# Mantém até apertar qualquer tecla
cv2.waitKey(0)
# Use plt.imshow(canny) plt.show() para descobrir a região de interesse
