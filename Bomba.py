import serial, random

while True:
    try:
        arduino = serial.Serial('COM8', 9600)
        break
    except:
        pass

def jogo():
	nums = list(range(10))
	random.shuffle(nums)
	n1, n2, n3, n4 = nums[:4]

	password = str(n1) + str(n2) + str(n3) + str(n4)
	par = 0

	if n1 % 2 == 0:
		par += 1

	if n2 % 2 == 0:
		par += 1

	if n3 % 2 == 0:
		par += 1

	if n4 % 2 == 0:
		par += 1

	print("\nVoce conseguiu acessar o controle da bomba!\nPara desarma-la, digite a senha de 4 digitos corretamente.\nVoce tem 60 segundos!")
	print(f"Dica: A senha possui {par} numero(s) par(es)\n")
	
	while True:
		guess = input("Digite uma senha de 4 digitos: ")
		presente = 0

		nums = [n1, n2, n3, n4]

		if str(n1) in guess:
			presente += 1
		if str(n2) in guess:
			presente += 1
		if str(n3) in guess:
			presente += 1
		if str(n4) in guess:
			presente += 1

		if(guess[0]==password[0]):
			print("\nO primeiro numero esta certo!")
		if(guess[1]==password[1]):
			print("\nO segundo numero esta certo!")
		if(guess[2]==password[2]):
			print("\nO terceiro numero esta certo!")
		if(guess[3]==password[3]):
			print("\nO quarto numero esta certo!")

		if presente == 4:
			print("\nAinda NAO acabou, para salvar Erick conecte o fio vermelho ao polo positivo energizado!\n")
			#a='a'
			#return(a)
			break

		elif presente == 4 :
			print(f"\nTodos os numeros fazem parte da senha.\n")

		else:
			print(f"\n{presente} numeros fazem parte da senha.")

while True:
    cmd = input("comecar o jogo")
    if cmd == 's':
        arduino.write('s'.encode())
        cmd = jogo()
        arduino.flush()
        if cmd == 'a':
            jogo.arduino.write('a'.encode())
    else:
        print("Xau! Nunca quis brincar mesmo...")
    
