# Correções:
# [1] Remover opção 2, está redundante. 
# [2] Antes de remover um produto, eles devem ser listados, para que usuário escolha o código do produto a ser removido.




# Iniciando o programa com o estoque vazio
estoque = {}

# Variável global para controlar o próximo código de produto
proximo_codigo = 1

# Função para adicionar um novo produto ao estoque
def adicionar_produto():
    global proximo_codigo

    nome = input("Digite o nome do novo produto: ")

    while True:
        preco_str = input("Digite o preço do novo produto (use ponto como separador decimal, ex. 00.00): ")
        try:
            preco = float(preco_str)
            # Verifica se o preço possui dois decimais
            if preco_str.count('.') != 1 or len(preco_str.split('.')[1]) != 2:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido. Por favor, insira um valor numérico no formato correto (ex. 00.00).")

    while True:
        try:
            quantidade = int(input("Digite a quantidade inicial do novo produto: "))
            break
        except ValueError:
            print("Quantidade inválida. Por favor, insira um valor numérico inteiro para a quantidade.")
    
    codigo = str(proximo_codigo).zfill(3)  # Gerando o código sequencial formatado
    estoque[codigo] = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
    proximo_codigo += 1  # Incrementando o próximo código disponível

    print(f"Produto '{nome}' adicionado ao estoque com código '{codigo}'.")

# Função para adicionar ou remover quantidade de um produto no estoque
def adicionar_remover_quantidade():
    codigo = input("Digite o código do produto que deseja modificar a quantidade: ")
    if codigo in estoque:
        operacao = input(f"Deseja adicionar (+) ou remover (-) quantidade do produto '{estoque[codigo]['nome']}': ")
        while operacao not in ('+', '-'):
            operacao = input("Operação inválida. Digite '+' para adicionar ou '-' para remover: ")

        while True:
            try:
                quantidade = int(input("Digite a quantidade a ser modificada: "))
                if operacao == '-':
                    quantidade *= -1  # Se for remoção, converte para negativo
                break
            except ValueError:
                print("Quantidade inválida. Por favor, insira um valor numérico inteiro para a quantidade.")

        estoque[codigo]['quantidade'] += quantidade
        print(f"Quantidade do produto '{estoque[codigo]['nome']}' atualizada para {estoque[codigo]['quantidade']}.")
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
    print("2. Adicionar ou remover quantidade de um produto")
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
        adicionar_remover_quantidade()
    elif opcao == '3':
        remover_produto()
    elif opcao == '4':
        print("\n============== Produtos no Estoque ===============")
        if not estoque:
            print("Nenhum produto cadastrado.")
        else:
            for codigo, produto in estoque.items():
                print(f"Código: {codigo}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")
    elif opcao == '5':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1-5).")
