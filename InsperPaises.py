from haversinefunc import haversine
from adiciona_em_ordemfunc import adiciona_em_ordem
from sorteia_paisfunc import sorteia_pais
from basenormalizada import *
from random import choice
from mercadodedicas import *

#guardando paises da base bnorm em uma lista
listapaises = list(bnorm.keys())
EARTH_RADIUS = 6371

#Dados terminados de carregar, inicia-se a abertura do jogo:
print(" \33[33m============================")
print("|                            |")
print("| Bem-vindo ao Insper Países |")
print("|                            |")
print(" ==== Design de Software ====\33[m")
print()
print(" Comandos:")
print()
print("     \33[32mdica       - entra no mercado de dicas")
print("     \33[31mdesisto    - desiste da rodada")
print("     \33[35minventario - exibe sua posição\33[m")
print()

jogarnovamente = 's'

while jogarnovamente != 'n':
    
    #Sorteando o país da base e guardando suas informações
    psorteado = sorteia_pais(bnorm)
    dados = bnorm[psorteado]
    capital = dados['capital'].lower()
    letrascapital = []
    for letra in capital:
        if letra not in letrascapital:
            letrascapital.append(letra)
    simbolos = ['.', ',', '-', ';', ' ']
    for simbolo in simbolos:
        if simbolo in letrascapital:
            letrascapital.remove(simbolo)
    bandeira = []
    for cor, valor in dados['bandeira'].items():
        if valor > 0:
            bandeira.append(cor)
    if 'outras' in bandeira:
        bandeira.remove('outras')
    
    
    #redefinindo os dados
    tentativasrestantes = 20
    dicas = {}
    dicaspossiveis = [0, 1, 2, 3, 4, 5]
    custodasdicasemordem = {1:4, 2:3, 3:6, 4:5, 5:7}
    distancias = []
    print("Um país foi escolhido, tente adivinhar!")
    print(f'Você tem \33[1;36m{tentativasrestantes}\33[m tentativa(s)')
    print()
    pescolhido = 'Nome de nenhum país aqui'
    
    #Aqui começa o jogo em sí, que roda até que acabem as tentativas ou que o while pare pelo pais ter sido acertado.
    while tentativasrestantes > 0 and pescolhido != psorteado:
        pescolhido = input('Qual seu palpite? ')
        if pescolhido == psorteado:
            tentativasrestantes -= 1
            break
        while pescolhido not in listapaises and pescolhido not in ['dica', 'desisto', 'inventario']:
            print('País desconhecido.')
            pescolhido = input('Qual seu palpite? ')
            
        if pescolhido == 'desisto':
            temcerteza = input('Tem certeza que deseja desistir da rodada? [s|n] ')
            print()
            if temcerteza == 's':
                break
        elif pescolhido == 'dica' and len(list(custodasdicasemordem.values())) == 0:
            print('Não há mais dicas disponíveis!')
        #Se for selecionado dica e o numero de tentativas restantes for maior do que a quantidade mínima que será gasta no mercado de dicas:
        elif pescolhido == 'dica' and tentativasrestantes > min(list(custodasdicasemordem.values())):
            retorno = (mercado(psorteado, dicaspossiveis, custodasdicasemordem, dicas, tentativasrestantes, bandeira, letrascapital))
            if retorno != 0:
                dicaspossiveis, custodasdicasemordem, dicas, tentativasrestantes, bandeira, letrascapital = retorno
            
        elif pescolhido == 'inventario':
            print('Exibindo inventário:')
            print()
        
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
            if distanc > 10000:
                print(f'\33[31m     {distanc//1} km -> {paiss}\33[m')
            elif distanc > 5000:
                print(f'\33[35m     {distanc//1} km -> {paiss}\33[m')
            elif distanc > 2500:
                print(f'\33[33m     {distanc//1} km -> {paiss}\33[m')
            elif distanc > 1250:
                print(f'\33[34m     {distanc//1} km -> {paiss}\33[m')
            elif distanc > 625:
                print(f'\33[36m     {distanc//1} km -> {paiss}\33[m')
            else:
                print(f'\33[32m     {distanc//1} km -> {paiss}\33[m')
        print()
        print('Dicas:')
        for nomedica, infodada in dicas.items():
            if nomedica == 'Área':
                print(f'   -{nomedica}: {infodada} km2')
            elif nomedica == 'Letras da capital':
                print(f'   -{nomedica}: ', end = '')
                letras = f'{infodada}'
                letras = letras.replace('[', '').replace(']', '').replace("'", '')
                print(letras)
                print()
            elif nomedica == 'Cores da bandeira':
                print(f'   -{nomedica}: ', end = '')
                for cor in infodada:
                    print(cor, end =', ')
                print()
            elif nomedica == 'População':
                pop = f'{infodada:,.0f}'
                pop = pop.replace(',', '.')
                print(f'   -{nomedica}: {pop}')
            else:
                print(f'   -{nomedica}: {infodada}')
        print()
        print(f'Você tem \33[1;36m{tentativasrestantes}\33[m tentativa(s)')

    
    #Comunicando se o jogo foi ganhado ou perdido.
    if pescolhido == psorteado:
        print(f'*** Parabéns! Você acertou após \33[1;36m{20 - tentativasrestantes}\33[m tentativas!')
    elif pescolhido != psorteado:
        print(f'>>> Você perdeu, o país era: {psorteado}')
    
    #verifica se o jogador quer começar outro jogo
    jogarnovamente = input('Deseja jogar novamente? [s|n] ')
    while jogarnovamente != 's' and jogarnovamente != 'n':
        print('Infelizmente sua resposta não é s ou n, tire um descanso e tome um café para voltar melhor e me responder corretamente!')
        jogarnovamente = input('Deseja jogar novamente? [s|n] ')

print()
print('Até a próxima!')