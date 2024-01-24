import cv2
import mediapipe as mp
import serial
import time

# Definindo a porta serial do Arduino
porta_serial = 'COM5'
ser = serial.Serial(porta_serial, 9600, timeout=1)
time.sleep(2)

# Configurando do MediaPipe
mp_dedos = mp.solutions.hands
dedos = mp_dedos.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Função para contar dedos
def contar_dedos(results):
    dedos_contados = 0

    if results.multi_hand_landmarks:
        # Aqui usamos apenas os landmarks dos dedos
        landmarks_dedos = [4, 8, 12, 16, 20]
        pontos_dedos = [results.multi_hand_landmarks[0].landmark[i] for i in landmarks_dedos]

        # Identifique a ponta do dedo (dedo levantado) com base na posição Y
        for ponto in pontos_dedos:
            if ponto.y < 0.2:  # Ajuste este valor conforme necessário
                dedos_contados += 1

    return dedos_contados

# Configuração da webcam
cap = cv2.VideoCapture(0)

# Função para verificar se a tecla 'q' foi pressionada
def verificar_tecla_q():
    return cv2.waitKey(1) & 0xFF == ord('q')

# Lógica de estabilização
tempo_estabilizacao = 2  # 2 segundos de estabilização
tempo_inicial = time.time()

while cap.isOpened():
    ret, frame = cap.read()

    # Detecção de mãos
    results = dedos.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Lógica para contar dedos
    dedos_contados = contar_dedos(results)

    # Exibe a quantidade de LEDs ligados no console
    print(f'LEDs ligados: {dedos_contados}')

    # Adiciona um retângulo indicando a quantidade de LEDs na tela
    cv2.rectangle(frame, (10, 10), (120, 40), (0, 255, 0), cv2.FILLED)
    cv2.putText(frame, f'LEDs: {dedos_contados}', (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Envio de comandos pela comunicação serial
    if dedos_contados == 1:
        ser.write(b'1')  # Comando para ligar LED 1
    elif dedos_contados == 2:
        ser.write(b'2')  # Comando para ligar LED 2
    elif dedos_contados == 3:
        ser.write(b'3')  # Comando para ligar LED 3
    else:
        ser.write(b'0')  # Comando para desligar todos os LEDs

    cv2.imshow("Webcam", frame)

    # Verifica se a tecla 'q' foi pressionada para parar o looping
    if verificar_tecla_q():
        break

    # Verifica se o tempo de estabilização foi atingido
    if time.time() - tempo_inicial > tempo_estabilizacao:
        # Reinicia o tempo de estabilização
        tempo_inicial = time.time()

cap.release()
cv2.destroyAllWindows()
ser.close()
