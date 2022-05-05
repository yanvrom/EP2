from haversinefunc import haversine
from esta_na_listafunc import esta_na_lista
from adiciona_em_ordemfunc import adiciona_em_ordem
from sorteia_letrafunc import sorteia_letra
from sorteia_paisfunc import sorteia_pais
from basenormalizada import *
from random import choice

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
    
    #Sorteando o país da base normalizada
    psorteado = sorteia_pais(bnorm)
    tentativasrestantes = 20
    print("Um país foi escolhido, tente adivinhar!")
    
    jogarnovamente = input('Deseja jogar novamente? [s|n] ')
    while jogarnovamente != 's' and jogarnovamente != 'n':
        print('Infelizmente sua resposta não é s ou n, tire um descanso e tome um café para voltar melhor e me responder corretamente!')
        jogarnovamente = input('Deseja jogar novamente? [s|n] ')

print()
print('Até a próxima!')