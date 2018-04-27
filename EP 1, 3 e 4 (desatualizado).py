#menu de iniciação
estoque = {}
escolha = 10
while escolha != 0:
    
    print("0 - sair")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - alterar item")
    print("4 - imprimir estoque")
    escolha = int(input('Faça sua escolha:'))
    if escolha == 0:
        print('Até mais!')
    if escolha == 1:
        x = str(input('nome do produto:'))
        
        if x not in estoque:
            estoque[x] = {}         #se o produto não estiver no estoque, ele deve ser colocado
            a = int(input('quantidade inicial:'))
            while a < 0:
                print('A quantidade inicial não pode ser negativa.')
                a = int(input('quantidade inicial:'))
            b = float(input('valor do produto:'))
            estoque[x]["quantidade"] = a
            estoque[x]["valor"] = b
                b = float(input('valor do produto:'))
                estoque[x]["quantidade"] = a
                estoque[x]["valor"] = b
    
        else:
            print('Produto já cadastrado')       #Se já estiver no estoque,avisa que ele já está cadastrado
       
    if escolha == 2:
        w = str(input('Qual produto deseja remover?'))
        if w not in estoque:
            print('produto não encontrado')
        if w in estoque:
            del estoque[w]
        
        
    if escolha == 3:
        print("1 - alterar quantidade")
        print("2 - alterar valor")
        escolhaAlterar = int(input("Faca sua escolha: "))
        
        if escolhaAlterar == 1:
           produto = str(input("Escolha o produto:"))
           print(estoque)
           if produto in estoque:
               nova_quantidade = int(input("Nova quantidade:"))
               estoque[produto]["quantidade"] = nova_quantidade + a
               a = estoque[produto]["quantidade"]
           if produto not in estoque:
                print('Elemento não encontrado.')     
        if escolhaAlterar == 2:
            produto = str(input("Escolha o produto:"))
            if produto in estoque:
                novo_valor = int(input("Novo valor:"))
                estoque[produto]["valor"] = novo_valor
        
    if escolha == 4:
        print(estoque)

for produto in estoque:
    if estoque[produto]["quantidade"]< 0:
        negativo.append(produto)
        print ('Os produtos com quantidade de estoque negativo são: {0}'.format(negativo))

valor=0
for produto in estoque:
    valor=valor + estoque[produto]['quantidade'] * estoque[produto]['valor']
print('O valor monetário total no estoque é de {0} reais'.format(valor))

