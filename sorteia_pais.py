from random import choice

def sorteia_pais(dicionariodadospaises):
    paises = []
    for pais in dicionariodadospaises.keys():
        paises.append(pais)
    return choice(paises)