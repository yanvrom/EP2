def esta_na_lista(pais, listapaises):
    paises = []
    for dadopais in listapaises:
        if dadopais[0] not in paises:
            paises.append(dadopais[0])
    if pais in paises:
        return True
    else:
        return False

#não utilizar