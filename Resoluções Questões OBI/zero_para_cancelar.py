# Zero para cancelar

# Seu chefe está ao telefone, nervoso. Ele quer que você compute a soma de uma sequência de números que ele vai falar para você ao telefone, para saber o total das vendas em sua mais recente viagem de negócios.

# Infelizmente, de vez em quando seu chefe fala números errados para você ao telefone.

# Felizmente, seu chefe rapidamente percebe que falou um número errado e diz "zero", que como combinado previamente quer dizer ignore o último número corrente.

# Infelizmente, seu chefe pode cometer erros repetidos, e diz "zero" para cada erro.

# Para não deixar seu chefe ainda mais nervoso, escreva um programa que determine a soma total dos números falados por seu chefe ao telefone.

# A lógica é assim:

# Quando o chefe fala um número normal, você adiciona na lista.

# Quando ele fala 0, você remove o último número (se houver).

# No final, você soma tudo o que ficou na lista.

pilha = []

print('Digite números. Digite "fim" para encerrar:')

while True:
    entrada = input()

    if entrada.lower() == "fim":
        break

    x = int(entrada)

    if x == 0:
        if pilha:
            pilha.pop()
    else:
        pilha.append(x)

print("Resultado:", sum(pilha))


# pilha começa vazia

# Se x não é zero → append(x)

# Se x é zero → pop()

# No final → sum(pilha)