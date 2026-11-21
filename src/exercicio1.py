# Exercício 1 Ambiente, câmera e pipeline básico

# Tarefa

# Em fases iniciais de desenvolvimento de sistemas robóticos, a rotina mais básica de validação consiste em confirmar que o ambiente de visão computacional está configurado corretamente e que a câmera responde conforme esperado. Este exercício isola problemas de ambiente, drivers, resolução e convenções de captura antes que qualquer processamento de imagem seja iniciado. Seu objetivo é implementar um script Python com OpenCV que capture um stream de vídeo, exiba o feed em tempo real e registre metadados de execução, finalizando de forma controlada ao pressionar Q.

# Requisitos Técnicos e Saídas Esperadas

# Item A:

# Capture um stream de vídeo de câmera real ou arquivo .mp4.
# Exiba o feed em janela com cv2.imshow.
# A cada frame, imprima no terminal: resolução atual, número do frame e taxa estimada de FPS usando cv2.getTickCount().
# O script deve encerrar corretamente ao pressionar Q, liberando todos os recursos com cap.release() e cv2.destroyAllWindows().
# Validação: terminal deve exibir resolução, número de frame e FPS em tempo real; janela deve fechar sem erros ao pressionar Q.
from typing import Sequence

import cv2
from cv2.typing import MatLike

video = cv2.VideoCapture("assets/exercicio1.mp4")

if not video.isOpened():
    print('Erro ao abrir o vídeo')
else:
    print('Vídeo carregado com sucesso')

frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = video.get(cv2.CAP_PROP_FPS)
frame_cont = 1

frame_selecionado = None

janela_video = "Vídeo"
cv2.namedWindow(janela_video, cv2.WINDOW_NORMAL)
cv2.resizeWindow(janela_video, 800, 600)
frame_salvo = 0
while frame_cont <= frames:
    inicio_frame = cv2.getTickCount()
    ret, frame= video.read()
    if not ret:
        print('Erro ao carregar o frame')

    shape = frame.shape

    
    print(f'Resolução: {shape[0]}x{shape[1]}')
    print(f'Frame: {frame_cont}')
    
    if frame_cont <= 100:
        frame_salvo = frame_cont
        frame_selecionado = frame
    
    cv2.imshow(janela_video, frame)
    if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
        break

    fim_frame = cv2.getTickCount()
    frame_cont += 1
        
    segundos = (fim_frame - inicio_frame)/cv2.getTickFrequency()
    taxa_fps = 1 / segundos
    print(f'Taxa de fps: {int(taxa_fps)}')
video.release()
cv2.destroyWindow(janela_video)
# Item B:q
# Estenda o script do item A: capture um único frame e salve-o em disco com cv2.imwrite.
# Recarregue a imagem salva, converta para escala de cinza com cv2.cvtColor e exiba as duas versões 
# (colorida e cinza) lado a lado usando cv2.hconcat.
# Demonstre que o array NumPy resultante tem shapes e dtypes corretos imprimindo esses valores no 
# terminal.
# Validação: duas janelas ou painel único exibindo original e cinza; terminal com shape (H, W, 3) 
# para colorida e (H, W) para cinza, dtype uint8 para ambas

imagem_output_nome = f'exercicio1-{frame_salvo}.jpeg'
cv2.imwrite(f'./assets/outputs/{imagem_output_nome}',frame_selecionado)


imagem_carregada = cv2.imread(f'./assets/outputs/{imagem_output_nome}')
imagem_cinza = cv2.cvtColor(imagem_carregada, cv2.COLOR_BGR2GRAY)
imagem_cinza_bgr = cv2.cvtColor(imagem_cinza, cv2.COLOR_GRAY2BGR)

imagem_array = cv2.hconcat([imagem_carregada, imagem_cinza_bgr])

print(f'Imagem colorida shape: {imagem_carregada.shape}')
print(f'Imagem escala de cinza shape: {imagem_cinza.shape}')

print(f'Imagem colorida dtype: {imagem_carregada.dtype}')
print(f'Imagem cinza dtype: {imagem_cinza.dtype}')

janela_imagem = "Imagem"
cv2.namedWindow(janela_imagem, cv2.WINDOW_NORMAL)
cv2.resizeWindow(janela_imagem, 1200, 800)

cv2.imshow(janela_imagem, imagem_array)

cv2.waitKey(0)
cv2.destroyWindow(janela_imagem)

