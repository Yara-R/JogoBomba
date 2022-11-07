import serial
import jogoSenha

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
        cmd = input("Andre começa com que letra?")
        arduino.flush()
        if cmd == 'a':
            arduino.write('a'.encode())
        else:
            arduino.write('b'.encode())
            print('Morreu!')
    else:
        print("Xau! Nunca quis brincar mesmo...")
    