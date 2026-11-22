# Manipulação de cor e realce de imagem

# Tarefa

# Em sistemas de percepção robótica, a manipulação de espaços de cor é fundamental para segmentação de 
# objetos e detecção de características. 
# Erros sutis na conversão ou na manipulação de canais podem comprometer toda a pipeline de visão. 
# Este exercício exige que você converta imagens entre espaços de cor, inspecione canais individualmente 
# e aplique técnicas de realce de nitidez, demonstrando domínio da relação entre espaço de cor, 
# canais e qualidade de imagem para aplicações robóticas.

# Requisitos Técnicos e Saídas Esperadas

# Item A:

# Carregue uma imagem colorida (mínimo 480×480 px).
# Converta para os espaços HSV e LAB e exiba cada canal separadamente - 
# 7 imagens no total: BGR original + 3 canais HSV + 3 canais LAB.
# Altere programaticamente a saturação da imagem HSV para 0%, 50% e 150% do valor original e 
# exiba os três resultados.
# Comente no código o que cada canal representa em cada espaço de cor.
# Validação: janela ou grid com 7 imagens de canais + 3 imagens com saturação alterada; 
# comentários explicativos no código.
import cv2
import numpy as np

imagem = cv2.imread('./assets/exercicio2.jpg')

imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
imagem_lab = cv2.cvtColor(imagem, cv2.COLOR_BGR2LAB)

#HSV
imagem_hsv_H = imagem_hsv[:,:,0]
imagem_hsv_S = imagem_hsv[:,:,1]
imagem_hsv_V = imagem_hsv[:,:,2]

#LAB
imagem_lab_L = imagem_lab[:,:,0]
imagem_lab_A = imagem_lab[:,:,1]
imagem_lab_B = imagem_lab[:,:,2]



cv2.imshow('original', imagem)
cv2.imshow('hsv', imagem_hsv)
cv2.imshow('hsv_H', imagem_hsv_H)
cv2.imshow('hsv_S', imagem_hsv_S)
cv2.imshow('hsv_V', imagem_hsv_V)
cv2.imshow('lab', imagem_lab)
cv2.imshow('lab_L', imagem_lab_L)
cv2.imshow('lab_A', imagem_lab_A)
cv2.imshow('lab_B', imagem_lab_B)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Item B:

# Aplique sharpening à imagem original usando dois métodos: (1) kernel de sharpening manual via cv2.filter2D e (2) unsharp masking por subtração de blur gaussiano.
# Compare visualmente os resultados exibindo as imagens lado a lado.
# Calcule e imprima a variância do Laplaciano de cada versão como métrica de nitidez.
# Indique no terminal qual método produziu maior nitidez para a imagem escolhida.
# Validação: três imagens exibidas lado a lado (original, sharpening manual, unsharp masking); terminal com valores de variância do Laplaciano para cada versão.