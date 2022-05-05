def adiciona_em_ordem(nomepais, distpais, paisesdist):
    dicpaises = {}
    if [nomepais, distpais] not in paisesdist:
        paisesdist.append([nomepais, distpais])
    
    for dadopais in paisesdist:
        dicpaises[dadopais[1]] = dadopais[0]
    
    ordemdistancias = sorted(dicpaises.keys())
    
    saida = []
    for distancia in ordemdistancias:
        saida.append([dicpaises[distancia], distancia])
    
    return saida
