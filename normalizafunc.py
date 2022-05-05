def normaliza(basepaises):
    basenor = {}
    for continente, paises in basepaises.items():
        for dadopais in paises.values():
            dadopais['continente'] = continente
        for pais, dados in paises.items():
            basenor[pais] = dados
    return basenor