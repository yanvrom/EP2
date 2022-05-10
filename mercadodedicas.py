from basenormalizada import *
from random import choice

def mercado(psorteado, dicaspossiveis, custodasdicasemordem, dicas, tentativasrestantes, bandeira, letrascapital):
    dicasnomes = [0, '1. Cor da bandeira  - custa 4 tentativas', '2. Letra da capital - custa 3 tentativas',
            '3. Área             - custa 6 tentativas', '4. População        - custa 5 tentativas',
            '5. Continente       - custa 7 tentativas']
    print('Mercado de Dicas')
    print('----------------------------------------')
    for dicapossivel in dicaspossiveis[1::]:
        print(dicasnomes[dicapossivel])
    print('0. Sem dica')
    print('----------------------------------------')

    dicaescolhida = int(input('Escolha sua opção [0|1|2|3|4|5]: '))
    while dicaescolhida not in dicaspossiveis:
        print()
        dicaescolhida = int(input('Escolha uma opção possível ou 0 para sair: '))
        print()
    
    if dicaescolhida == 0:
        return 0
    
    if dicaescolhida == 1:
        corsorteada = choice(bandeira)
        bandeira.remove(corsorteada)
        if len(bandeira) == 0:
            dicaspossiveis.remove(1)
            del custodasdicasemordem[1]
        tentativasrestantes -= 4
        if 'Cores da bandeira' not in list(dicas.keys()):
            dicas['Cores da bandeira'] = [corsorteada]
        else:
            dicas['Cores da bandeira'].append(corsorteada)
    
    if dicaescolhida == 2:
        letrasorteada = choice(letrascapital)
        letrascapital.remove(letrasorteada)
        if len(letrascapital) == 0:
            dicaspossiveis.remove(2)
            del custodasdicasemordem[2]
        tentativasrestantes -= 3
        if 'Letras da capital' not in list(dicas.keys()):
            dicas['Letras da capital'] = [letrasorteada]
        else:
            dicas['Letras da capital'].append(letrasorteada)
    
    if dicaescolhida == 3:
        dicas['Área'] = bnorm[psorteado]['area']
        dicaspossiveis.remove(3)
        del custodasdicasemordem[3]
        tentativasrestantes -= 6
    
    if dicaescolhida == 4:
        dicas['População'] = bnorm[psorteado]['populacao']
        dicaspossiveis.remove(4)
        del custodasdicasemordem[4]
        tentativasrestantes -= 5
    
    if dicaescolhida == 5:
        dicas['Continente'] = bnorm[psorteado]['continente']
        dicaspossiveis.remove(5)
        del custodasdicasemordem[5]
        tentativasrestantes -= 7
    
    #analisando as dicas possiveis e retirando aquelas mais caras que as tentativas restantes:
    dicas_para_eliminar = []
    for numdica, valordela in custodasdicasemordem.items():
        if tentativasrestantes <= valordela:
            dicas_para_eliminar.append(numdica)
    for dica_para_elim in dicas_para_eliminar:
        dicaspossiveis.remove(dica_para_elim)
        del custodasdicasemordem[dica_para_elim]
    
    return  dicaspossiveis, custodasdicasemordem, dicas, tentativasrestantes, bandeira, letrascapital