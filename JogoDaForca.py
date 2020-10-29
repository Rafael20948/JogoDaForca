import random

def intersecao(conjuntoA, conjuntoB):
        inter = []
        for x in conjuntoA:
            for y in conjuntoB:
                if x == y:
                    inter.append(x)
        return print(inter)

palavras="Baleia,Cachorro,Cavalo,Crocodilo,Elefante,Galinha,Gamba,Gato,\
Golfinho,Girafa,Lobo,Macaco,Ovelha,Papagaio,Pombo,Rinoceronte,Tartaruga,\
Touro,Urso,Vaca"
lista = palavras.lower().split(',')
print("***************************************************************")
print("Jogo da Forca, tente adivinhar o animal, você tem 10 tentativas")
print("***************************************************************\n")
palavraAleatoria = random.choice(lista)
listPalavraAleatoria=list(palavraAleatoria)
tamanhoPalavra=len(palavraAleatoria)
listaCaracterUnico=len(sorted(set(listPalavraAleatoria)))
listaAcertos=[]
listaErros=[]
listaAllLetras=[]
numTentativas=9
while numTentativas >= 0:
    print(f'Tamanho da Palavra {len(palavraAleatoria) * "-"}')
    tamanhoListaAcertos=len(listaAcertos)
    letra = input('Digite uma letra: ').lower()
    try:
        if letra == '' or letra == ' ':
            print("\n****************")
            print(f'DIGITE UMA LETRA')
            print("****************\n")
        elif listaAllLetras.index(letra):
            print("\n***********************")
            print('Erro, Letra já DIGITADA')
            print("***********************\n")
            numTentativas += 1
        elif listaAllLetras[0] == letra:
            print("\n***********************")
            print('Erro, Letra já DIGITADA')
            print("***********************\n")
            numTentativas += 1
    except:
        if letra == '' or letra == ' ' or letra == '\n':
                pass
        elif letra in palavraAleatoria:
                  print("\n************************")
                  print(f'Parabéns você acertou: {letra}')
                  print("************************\n")
                  listaAllLetras.append(letra)
                  listaAcertos.append(letra)
                  intersecao(listPalavraAleatoria,listaAcertos)
        else:
            listaErros.append(letra)
            listaAllLetras.append(letra)
            print("\n*********************")
            print(f'Você Errou {listaErros}')
            print("*********************\n")
            if numTentativas == 0:
                  print("*********")
                  print('GAME OVER')
                  print("*********")
                  print(f'A palavra era: {palavraAleatoria}')
    if tamanhoListaAcertos == (listaCaracterUnico - 1):
        print("*********************")
        print(f'Parabéns você ganhou')
        print("*********************")
        break
    if letra in palavraAleatoria:
            numTentativas-=1
    else:
            numTentativas-=1
    if letra == '' or letra == ' ' or letra == '/n':
            numTentativas+=1
    print(f'Tentativas Restantes {numTentativas + 1} \n')
        
