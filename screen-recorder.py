# pip install pyautogui opencv-python

import cv2
import pyautogui

# Configurações para a gravação de tela
SCREEN_SIZE = (1920, 1080)  # Tamanho da tela (altere conforme necessário)
FPS = 30.0  # Quadros por segundo

# Nome do arquivo de saída
output_file = "screen_recording.avi"

# Codec de vídeo e inicialização do gravador de vídeo
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_file, fourcc, FPS, SCREEN_SIZE)

try:
    while True:
        # Captura um frame da tela
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Grava o frame no vídeo
        out.write(frame)

        # Encerra a gravação quando o usuário pressiona 'q'
        if cv2.waitKey(1) == ord("q"):
            break
finally:
    # Libera os recursos
    out.release()
    cv2.destroyAllWindows()
