# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 21:32:59 2018

@author: lucasmuchaluat
"""

from firebase import firebase
firebase=firebase.FirebaseApplication('https://ep-lucas-e-gustavo-288d7.firebaseio.com/',None)
if firebase.get('informacoes',None) is None:
    Lojas = {}
else:
    Lojas = firebase.get('informacoes',None)

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
            print('Loja não encontrada')
        if loja in Lojas:
            del Lojas[loja]
            firebase.delete('informacoes', loja)
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
        else:
            escolha = 10
            negativo = []
            while escolha != 0:
                print("0 - Sair")
                print("1 - Adicionar item")
                print("2 - Remover item")
                print("3 - Alterar item")
                print("4 - Analisar estoque")
                escolha = int(input('Escolha um comando acima:'))
                if escolha == 0:
                    print('Redirecionando para o menu principal...')
                if escolha == 1:
                    x = str(input('Nome do produto:'))
                    
                    if x not in Lojas[loja]:
                        Lojas[loja][x] = {}
                        a = int(input('Quantidade inicial:'))
                        while a < 0:
                            print('A quantidade inicial não pode ser negativa.')
                            a = int(input('Quantidade inicial: '))
                        b = float(input('Valor unitário do produto: '))
                        while b < 0:
                            print('O valor do produto não pode ser negativo.')
                            b = float(input('Valor unitário do produto: '))
                        Lojas[loja][x]["quantidade"] = a
                        Lojas[loja][x]["valor unitário"] = b
                        
                    else:
                        print('Produto já cadastrado')
                    print(Lojas[loja])
                if escolha == 2:
                    w = str(input('Qual produto deseja remover?'))
                    if w not in Lojas[loja]:
                        print('Produto não encontrado')
                    if w in Lojas[loja]:
                        del Lojas[loja][w]
                        firebase.delete('informacoes/{0}'.format(loja), w)
                    print(Lojas[loja])
                    
                if escolha == 3:
                    print("1 - Alterar quantidade")
                    print("2 - Alterar valor unitário")
                    escolha_alterar = int(input("Faça sua escolha: "))
                    
                    if escolha_alterar == 1:
                        print(Lojas[loja])
                        produto = str(input("Escolha o produto:"))
                        if produto in Lojas[loja]:
                            nova_quantidade = int(input("Quantidade a adicionar:"))
                            quantidade_inicial = Lojas[loja][produto]["quantidade"]
                            Lojas[loja][produto]["quantidade"] = nova_quantidade + quantidade_inicial
                            quantidade_inicial = Lojas[loja][produto]["quantidade"]
                        else:
                            print('Elemento não encontrado.')
                    if escolha_alterar == 2:
                        produto = str(input("Escolha o produto:"))
                        if produto in Lojas[loja]:
                            novo_valor = float(input("Novo valor unitário: "))
                            while novo_valor < 0:
                                print('O valor do produto não pode ser negativo.')
                                novo_valor = float(input('Novo valor unitário: '))
                            Lojas[loja][produto]["valor unitário"] = novo_valor
                    print(Lojas[loja])
                if escolha == 4:
                    print("1 - Imprimir estoque")
                    print("2 - Imprimir valor monetário total")
                    print("3 - Verificar se há produtos com quantidade negativa")
                    escolha_impressao = int(input("Faça sua escolha: "))
                    
                    if escolha_impressao == 1:
                        print(Lojas[loja])
                    if escolha_impressao == 2:
                        valor=0
                        for produto in Lojas[loja]:
                            valor=valor + Lojas[loja][produto]['quantidade'] * Lojas[loja][produto]['valor unitário']
                        print('O valor monetário total em {0} é de {1} reais'.format(loja,valor))
                    if escolha_impressao == 3:
                        for produto in Lojas[loja]:
                            if Lojas[loja][produto]["quantidade"]< 0:
                                negativo.append(produto)
                                print ('Os produtos com quantidade de estoque negativo em {0} são: {1}'.format(loja, negativo))
                        if negativo == []:
                            print('Não há produtos com quantidade de estoque negativa em {0}.'.format(loja))

firebase.patch('https://ep-lucas-e-gustavo-288d7.firebaseio.com/informacoes', Lojas)
