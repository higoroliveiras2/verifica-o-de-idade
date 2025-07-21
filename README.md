# verifica-o-de-idade

# 1. Verifica a idade do usuário
idade = int(input("Qual a sua idade? "))
if idade >= 18:
    print("Acesso liberado! Bem-vindo ao jogo.")
else:
    print("Acesso negado. Você precisa ter 18 anos ou mais.")

print("-" * 50)

# 2. Verifica se o usuário tem ingresso
ingresso = input("Você tem ingresso? (sim/não) ").strip().lower()
if ingresso == "sim":
    print("Pode entrar, aproveite o filme!")
elif ingresso == "não":
    print("Desculpe, você precisa de um ingresso para entrar.")
else:
    print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

print("-" * 50)

# 3. Verifica o estado da luz
luz = input("A luz está acesa? (sim/não) ").strip().lower()
if luz == "sim":
    print("Desligue a luz para economizar energia.")
elif luz == "não":
    print("Boa! A luz está apagada.")
else:
    print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

print("-" * 50)

# 4. Escolha de bebida
bebida = input("O que você deseja beber? (refrigerante/água) ").strip().lower()
if bebida == "refrigerante":
    print("Cuidado com o excesso de açúcar!")
elif bebida == "água":
    print("Ótima escolha! Hidratação é importante.")
else:
    print("Opção inválida. Escolha 'refrigerante' ou 'água'.")
