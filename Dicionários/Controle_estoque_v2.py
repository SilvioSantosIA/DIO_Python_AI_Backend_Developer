# Definindo o dicionário para o controle de estoque
estoque = {
    '001': {'nome': 'Camiseta', 'preco': 29.90, 'quantidade': 100},
    '002': {'nome': 'Calça Jeans', 'preco': 79.90, 'quantidade': 50},
    '003': {'nome': 'Tênis', 'preco': 129.90, 'quantidade': 30}
}

# Função para adicionar um novo produto ao estoque
def adicionar_produto():
    while True:
        codigo = input("Digite o código do novo produto: ")
        if codigo in estoque:
            print("Código já existe. Por favor, insira um código único.")
        else:
            break
    
    nome = input("Digite o nome do novo produto: ")

    while True:
        try:
            preco = float(input("Digite o preço do novo produto (use ponto como separador decimal): "))
            break
        except ValueError:
            print("Valor inválido. Por favor, insira um valor numérico para o preço.")

    while True:
        try:
            quantidade = int(input("Digite a quantidade inicial do novo produto: "))
            break
        except ValueError:
            print("Quantidade inválida. Por favor, insira um valor numérico inteiro para a quantidade.")
    
    estoque[codigo] = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
    print(f"Produto '{nome}' adicionado ao estoque.")

# Função para atualizar a quantidade de um produto no estoque
def atualizar_quantidade():
    codigo = input("Digite o código do produto que deseja atualizar: ")
    if codigo in estoque:
        while True:
            try:
                nova_quantidade = int(input(f"Digite a nova quantidade para o produto '{estoque[codigo]['nome']}: "))
                break
            except ValueError:
                print("Quantidade inválida. Por favor, insira um valor numérico inteiro para a quantidade.")
        
        estoque[codigo]['quantidade'] = nova_quantidade
        print(f"Quantidade do produto '{estoque[codigo]['nome']}' atualizada para {nova_quantidade}.")
    else:
        print(f"Produto com código {codigo} não encontrado no estoque.")

# Função para remover um produto do estoque
def remover_produto():
    codigo = input("Digite o código do produto que deseja remover: ")
    if codigo in estoque:
        produto_removido = estoque.pop(codigo)
        print(f"Produto '{produto_removido['nome']}' removido do estoque.")
    else:
        print(f"Produto com código {codigo} não encontrado no estoque.")

# Função para exibir o menu de opções
def exibir_menu():
    print("\n================== Lojas Renner ========================")
    print("\n----------------- Menu de Opções -----------------------")
    print("1. Adicionar novo produto")
    print("2. Atualizar quantidade de um produto")
    print("3. Remover produto")
    print("4. Listar produtos no estoque")
    print("5. Sair")
    escolha = input("Escolha uma opção (1-5): ")
    return escolha

# Loop principal do programa
while True:
    opcao = exibir_menu()

    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        atualizar_quantidade()
    elif opcao == '3':
        remover_produto()
    elif opcao == '4':
        print("\n============== Produtos no Estoque ===============")
        for codigo, produto in estoque.items():
            print(f"Código: {codigo}, Nome: {produto['nome']}, Preço: R${produto['preco']}, Quantidade: {produto['quantidade']}")
    elif opcao == '5':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1-5).")
