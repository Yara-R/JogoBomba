import os
os.system("cls")

import random
import time

n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)
n4 = random.randint(0, 9)

password = str(n1) + str(n2) + str(n3) + str(n4)
count = 0

if n1 % 2 == 0:
    count += 1

if n2 % 2 == 0:
    count += 1

if n3 % 2 == 0:
    count += 1

if n4 % 2 == 0:
    count += 1

print("Você conseguiu acessar o controle da bomba!\nPara desarma-la, digite a senha de 4 dígitos corretamente.\nVocê tem 60 segundos!")
print(f"Dica: A senha possui {count} numero(s) par(es)\n")

while True:
	guess = input("Digite uma senha de 4 digitos:")
	presente = 0
	certo = 0

	rand_nums = [n1, n2, n3, n4]

	if str(n1) in guess:
		presente += 1
	if(guess[0]==password[0]):
		certo +=1
	if str(n2) in guess:
		presente += 1
	if(guess[1]==password[1]):
		certo +=1
	if str(n3) in guess:
		presente += 1
	if(guess[2]==password[2]):
		certo +=1
	if str(n4) in guess:
		presente += 1
	if(guess[3]==password[3]):
		certo +=1


	if presente == 4:

		if guess == password:
			print("Parabéns! Você conseguiu desmontar a bomba")
			break

		else:
			print(f"Todos os numeros estão certos e {certo} estão na posição certa!")


	else:
		print(f"{presente} números fazem parte da senha.\n{certo} números estão na posição certa")
