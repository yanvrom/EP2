from basenormalizada import *
from sorteia_letrafunc import sorteia_letra
from random import choice

def mercado(psorteado, dicaspossiveis, dicas, tentativasrestantes):
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
        dicaescolhida = int(input('Escolha uma opção entre 1 a 5 que ainda não foi escolhida ou 0 para sair: '))
        print()
    
    if dicaescolhida == 1 and tentativasrestantes >= 5:
        bandeira = bnorm[psorteado]['bandeira']
        coresbandeira = []
        for cor, valor in bandeira.items():
            if valor > 0:
                coresbandeira.append(cor)
        corsorteada = choice(coresbandeira)
        if 'Cores da bandeira' in dicas:
            while corsorteada in dicas['Cores da bandeira']:
                corsorteada = choice(coresbandeira)
        dicadada = corsorteada
    elif dicaescolhida == 2 and tentativasrestantes >= 4:
        capital = bnorm[psorteado]['capital']
        
        
    elif dicaescolhida == 3 and tentativasrestantes >= 7:
        dicadada = bnorm[psorteado]['area']
        
    elif dicaescolhida == 4 and tentativasrestantes >= 6:
        dicadada = bnorm[psorteado]['populacao']
        
    elif dicaescolhida == 5 and tentativasrestantes >= 8:
        dicadada = bnorm[psorteado]['continente']
    elif dicaescolhida == 0:
        return 0
    else:
        print('Se a dica fosse comprada, você perderia por estar sem dicas, nenhuma dica foi comprada.')
        return 0
    return dicadada, dicaescolhida