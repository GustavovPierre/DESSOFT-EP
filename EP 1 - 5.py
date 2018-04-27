# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 00:34:42 2018

@author: gppie
"""



import json
with open ("Lojas.json","r") as arquivo:
    texto = arquivo.read()

Lojas = json.loads(texto)
escolha0=10
while escolha0 != 0:
    print("0 - Sair")
    print("1 - Adicionar loja")
    print("2 - Remover loja")
    print("3 - Alterar loja")
    print("4 - Imprimir lojas cadastradas")
    print('5 - Entrar no menu da loja')
    escolha0 = int(input('Escolha um comando acima:'))
    if escolha0 == 0:
        print(('Até mais! Nosso programa agradece!'))
    if escolha0 == 1:
        loja = str(input('Nome da loja:'))
        if loja not in Lojas:
            Lojas[loja]={}
        else:
            print('Loja já cadastrada')
        print(Lojas)
    if escolha0 == 2:
        print(Lojas)
        loja = str(input('Qual loja deseja remover?'))
        if loja not in Lojas:
            print('loja não encontrada')
        if loja in Lojas:
            del Lojas[loja]
        print(Lojas)
    if escolha0 == 3:
        print(Lojas)
        loja = str(input("Escolha a loja:"))
        if loja in Lojas:
            nova_loja=str(input('Diga o nome da nova loja:'))
            del Lojas[loja]
            Lojas[nova_loja]={}
        else:
            print('Loja não encontrada')
        print(Lojas)
    if escolha0 == 4:
        print(Lojas)
    if escolha0 == 5:
        print(Lojas)
        loja = str(input('Nome da loja a ser analizada:'))
        if loja not in Lojas:
            print('Loja não cadastrada')