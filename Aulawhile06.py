v = 1

#enquanto V for menor ou igual a 3, esses comandos vão 
# se repetir, ou seja, enquanto a condição for true

while v <=3:
    print("O valor de V é",v)
    #somo mais 1 ao valor de V para que esse
    # seja infinito, já que ele para quando for maior que 3
v = v + 1 

print("_" * 100)

'''
Imagine que você está criando um contador numérico e esse contador deve perguntar ao usuário em qual valor ele deve parar.
'''

parada = int(input("Digite o valor que deseja contar:"))
contador = 1

while contador <= parada:
    print(contador)
    contador = contador + 1

'''
Imagine que você ta criando uma aposta para ver quem vai ser o time que vai ganhar o mundial 
'''

time = input("Digite o nome do time que deseja apostar:").upper()

while time == 'PALMEIRAS':
    print("Palmeiras não tem mundial😂, escolha outro time!")
    time = input("Digite novamente:").upper()
else:
    print('Boa sorte na sua aposta!')
