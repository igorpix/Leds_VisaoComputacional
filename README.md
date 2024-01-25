# Controle de LEDs por Detecção de Mãos

Este projeto utiliza a biblioteca MediaPipe para o rastreamento de mãos e comunicação com um Arduino para controlar LEDs. A ideia é contar quantos dedos estão levantados e, com base nisso, controlar os LEDs.

## Configuração

### Requisitos

- [Python](https://www.python.org/) (versão 3.x)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [MediaPipe](https://pypi.org/project/mediapipe/)
- [PySerial](https://pypi.org/project/pyserial/)

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/igorpix/Leds_VisaoComputacional.git
    cd Leds_VisaoComputacional
    ```

2. Instale as dependências:

    ```bash
    pip install opencv-python mediapipe pyserial
    ```

3. Conecte seu Arduino e ajuste a porta serial no arquivo Python:

    ```python
    porta_serial = 'COM5'  # Altere para a porta serial do seu Arduino
    ```

4. Execute o script Python:

    ```bash
    python nome_do_script.py
    ```

## Uso

1. Levante os dedos para controlar os LEDs.
2. Utilize o script Python para enviar comandos para o Arduino através da comunicação serial.

## Contribuição

Contribuições são bem-vindas! Se encontrar problemas ou tiver sugestões, por favor, abra uma [issue](https://github.com/igorpix/Leds_VisaoComputacional/issues).

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
