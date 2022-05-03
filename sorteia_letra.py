from random import choice

def sorteia_letra(palavra, letrasrestritas):

    palavra = palavra.lower()
    possivel = False
    for letra in palavra:
        if letra not in letrasrestritas and letra not in ['.', ',', '-', ';', ' ']:
            possivel = True
    if possivel == True:    
        while True:
            sorteado = choice(palavra)
            if sorteado not in letrasrestritas and sorteado not in ['.', ',', '-', ';', ' ']:
                return sorteado
    else:
        return ''