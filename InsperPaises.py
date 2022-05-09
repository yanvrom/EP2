from haversinefunc import haversine
from adiciona_em_ordemfunc import adiciona_em_ordem
from sorteia_paisfunc import sorteia_pais
from basenormalizada import *
from random import choice
from mercadodedicas import *
import math

#guardando paises da base bnorm em uma lista
listapaises = list(bnorm.keys())
EARTH_RADIUS = 6371

print(" ============================")
print("|                            |")
print("| Bem-vindo ao Insper Países |")
print("|                            |")
print(" ==== Design de Software ====")
print()
print(" Comandos:")
print()
print("     dica       - entra no mercado de dicas")
print("     desisto    - desiste da rodada")
print("     inventario - exibe sua posição")
print()

jogarnovamente = 's'

while jogarnovamente != 'n':
    
    #Sorteando o país da base e guardando suas informações
    psorteado = sorteia_pais(bnorm)
    dados = bnorm[psorteado]
    
    #redefinindo os dados
    tentativasrestantes = 20
    dicas = {}
    dicaspossiveis = [0, 1, 2, 3, 4, 5]
    distancias = []
    print("Um país foi escolhido, tente adivinhar!")
    print(f'Você tem {tentativasrestantes} tentativa(s)')
    print()
    pescolhido = input('Qual seu palpite? ')
    
    #Aqui começa o jogo em sí, que roda até que acabem as tentativas ou que o break aconteça pelo pais ter sido acertado.
    while tentativasrestantes > 0 and pescolhido != psorteado:
        while pescolhido not in listapaises and pescolhido not in ['dica', 'desisto', 'inventario']:
            print('País desconhecido.')
            pescolhido = input('Qual seu palpite? ')
            
        if pescolhido == 'desisto':
            temcerteza = input('Tem certeza que deseja desistir da rodada? [s|n] ')
            print()
            if temcerteza == 's':
                break
        elif pescolhido == 'dica' and tentativasrestantes >= 3:
            retorno = (mercado(psorteado, dicaspossiveis, dicas, tentativasrestantes))
            if retorno != 0:
                dicadada, numerodicaescolhida = retorno
                if numerodicaescolhida == 1:
                    if 'Cores da bandeira' not in list(dicas.keys()):
                        dicas['Cores da bandeira'] = [dicadada]
                    else:
                        dicas['Cores da bandeira'].append(dicadada)
                    tentativasrestantes -= 4
                elif numerodicaescolhida == 2:
                    if 'Letras da capital' not in list(dicas.keys()):
                        dicas['Letras da capital'] = [dicadada]
                    else:
                        dicas['Letras da capital'].append(dicadada)
                    tentativasrestantes -= 3
                elif numerodicaescolhida == 3:
                    dicas['Área'] = dicadada
                    tentativasrestantes -= 6
                elif numerodicaescolhida == 4:
                    dicas['População'] = dicadada
                    tentativasrestantes -= 5
                elif numerodicaescolhida == 5:
                    dicas['Continente'] = dicadada
                    tentativasrestantes -= 7
                if numerodicaescolhida not in [1, 2]:
                    dicaspossiveis.remove(numerodicaescolhida)
        elif pescolhido == 'dica' and tentativasrestantes < 3:
            print('Você não possui tentativas suficientes para comprar dicas.')
        # elif pescolhido == 'inventario':
        
        else:
            dadosescolhido = bnorm[pescolhido]
            distancianova = haversine(EARTH_RADIUS, dados['geo']['latitude'], dados['geo']['longitude'], dadosescolhido['geo']['latitude'], dadosescolhido['geo']['longitude'])
            distancias = adiciona_em_ordem(pescolhido, distancianova, distancias)
            tentativasrestantes -= 1
        
        #exibindo status
        print('Distâncias:')
        for elemento in distancias:
            paiss = elemento[0]
            distanc = elemento[1]
            print(f'     {distanc//1} km -> {paiss}')
        print()
        print('Dicas:')
        for nomedica, infodada in dicas.items():
            if nomedica == 'Área':
                print(f'   -{nomedica}: {infodada} km2')
            elif nomedica == 'Cores da bandeira':
                print(f'   -{nomedica}: ', end = '')
                for cor in infodada:
                    print(cor, end =', ')
                print()
            else:
                print(f'   -{nomedica}: {infodada}')
        print()
        print(f'Você tem {tentativasrestantes} tentativa(s)')

        pescolhido = input('Qual seu palpite? ')
    
    #Comunicando se o jogo foi ganhado ou perdido.
    if pescolhido == psorteado:
        print(f'*** Parabéns! Você acertou após {20 - tentativasrestantes} tentativas!')
    elif pescolhido != psorteado:
        print(f'>>> Você perdeu, o país era: {psorteado}')
    
    #verifica se o jogador quer começar outro jogo
    jogarnovamente = input('Deseja jogar novamente? [s|n] ')
    while jogarnovamente != 's' and jogarnovamente != 'n':
        print('Infelizmente sua resposta não é s ou n, tire um descanso e tome um café para voltar melhor e me responder corretamente!')
        jogarnovamente = input('Deseja jogar novamente? [s|n] ')

print()
print('Até a próxima!')