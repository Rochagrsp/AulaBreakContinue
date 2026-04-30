contador=1

while contador <=10:
    print(contador)
    if contador == 5:
        break
    contador +=1

    senha= ""

    while True:
        senha=input("Digite a senha:")

        if senha == "1234":
            print("Acesso liberado")
            break
        print("Senha incorreta")

numero = 1

while numero<=5:
    if numero ==2:
        numero += 1
        continue
    print(numero)
    numero +=1

# Questão 1
# Mostre números de 1 a 10, mas pare no 6.
 
contador=1
while contador<=10: 
    print(contador)
    if contador == 6:
        break
    contador +=1

# Questão 2
# Mostre números de 1 a 10, pulando o número 5.

numero=1

while numero <= 10:
    if numero == 5:
        numero += 1
        continue
    print(numero)
    numero += 1

# Questão 3
# Mostre números de 1 a 20, pulando pares e encerrando no 15.

numero=1

while numero <=20:
    if numero  ==17:
        break
    if numero %2==0:
        numero+=1
        continue
    print(numero)
    numero+=1

# Questão 4
# Uma loja deseja cadastrar produtos até o funcionário digitar fim.
# Pedir nome do produto
# Se digitar fim, encerrar cadastro
# Mostrar cada produto cadastrado
# Usar break

while True:
    produto=input("Digite o nome do produto!")

    if produto =="fim":
        print("cadastro finalizado")
        break
    print("prodruto cadastrado")

# Questão 5
# Parar quando soma chegar em 20

soma=0
while True:
    numero=int(input("digite um numero:"))
    soma+= numero
    if soma>=20:
        break
    print("Total",soma)



# Atividade 6 – Parada por Limite
# Crie um sistema que receba números digitados pelo usuário e vá somando os
# valores informados.
# Quando a soma total atingir ou ultrapassar 50, o programa deverá encerrar
# automaticamente utilizando o comando break.

soma=0
while True:
    numero=int(input("Digite um numero"))
    soma+=numero
    if soma>=50:
        print("limite atingido!")
        print("Total:",soma)
        break

# Atividade 7 – Sistema de Senha
# Crie um programa que peça uma senha ao usuário até ele acertar.
# A senha correta será:
# Teste
# Quando acertar, mostrar:
# Acesso liberado

while True:
    senha=input("Digite a senha:")
    if senha =="teste":
        print("Acesso liberado")
        break
    else:
        print('senha incorreta')