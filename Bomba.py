import serial
from jogoSenha import jogo

while True:
    try:
        arduino = serial.Serial('COM5', 9600)

        break
    except:
        pass

while True:
    cmd = input("começar o jogo")
    if cmd == 's':
        arduino.write('s'.encode())
        cmd = jogo()
        arduino.flush()
        if cmd == 'a':
            arduino.write('a'.encode())
    else:
        print("Xau! Nunca quis brincar mesmo...")
    
