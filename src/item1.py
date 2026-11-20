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
import cv2

video = cv2.VideoCapture("assets/exercicio1.mp4")

if not video.isOpened():
    print('Erro ao abrir o vídeo')
else:
    print('Vídeo carregado com sucesso')

frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = video.get(cv2.CAP_PROP_FPS)
frame_cont = 1
ultimo_tick =cv2.getTickCount()

while frame_cont <= frames:
    ret, frame= video.read()
    if not ret:
        print('Erro ao carregar o frame')

    shape = frame.shape

    print(f'Resolução: {shape[0]}x{shape[1]}')
    print(f'Frame: {frame_cont}')
    frame_cont += 1
    tick_atual = cv2.getTickCount()
    taxa_fps = 1000/(tick_atual - ultimo_tick)
    tick_atual = ultimo_tick
    print(f'Taxa de fps: {taxa_fps}')

    cv2.imshow('frame atual', frame)
    if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
# Item B:q

# Estenda o script do item A: capture um único frame e salve-o em disco com cv2.imwrite.
# Recarregue a imagem salva, converta para escala de cinza com cv2.cvtColor e exiba as duas versões (colorida e cinza) lado a lado usando cv2.hconcat.
# Demonstre que o array NumPy resultante tem shapes e dtypes corretos imprimindo esses valores no terminal.
# Validação: duas janelas ou painel único exibindo original e cinza; terminal com shape (H, W, 3) para colorida e (H, W) para cinza, dtype uint8 para ambas