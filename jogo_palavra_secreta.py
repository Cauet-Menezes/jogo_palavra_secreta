import os

palavras = ['perfume', 'computador', 'telefone', 'teclado']  # Lista de palavras
letras_acertadas = ''
numero_tentativas = 0
indice_palavra_atual = 0

while True:
    palavra_secreta = palavras[indice_palavra_atual]

    while numero_tentativas < 10:
        letra_digitada = input('Digite uma letra: ').lower()
        numero_tentativas += 1 

        if len(letra_digitada) != 1 or not letra_digitada.isalpha():
            print('Digite apenas uma letra válida!')
            continue

        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada
        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'

        print(palavra_formada)

        if palavra_formada == palavra_secreta:
            print('Você ganhou o jogo!')
            letras_acertadas = ''
            numero_tentativas = 0
            break

    else:
        print('Número de tentativas atingido!')
        letras_acertadas = ''
        numero_tentativas = 0

    indice_palavra_atual += 1
    if indice_palavra_atual >= len(palavras):
        print("Você jogou todas as palavras!")
        break
    else:
        print("Próxima palavra...\n")
