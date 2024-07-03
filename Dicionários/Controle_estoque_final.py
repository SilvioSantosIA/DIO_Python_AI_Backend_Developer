
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

# Função para realizar a saída de estoque (venda ou transferência)
def saida_estoque():
    codigo = input("Digite o código do produto que teve saída: ")
    if codigo in estoque:
        while True:
            try:
                quantidade = int(input(f"Digite a quantidade de '{estoque[codigo]['nome']}' que saiu do estoque: "))
                if quantidade < 0:
                    raise ValueError("A quantidade não pode ser negativa.")
                if quantidade > estoque[codigo]['quantidade']:
                    raise ValueError("Quantidade superior ao estoque disponível.")
                break
            except ValueError as e:
                print(f"Erro: {e}")

        estoque[codigo]['quantidade'] -= quantidade
        print(f"Saida de '{quantidade}' unidades do produto '{estoque[codigo]['nome']}' realizada com sucesso.")
    else:
        print(f"Produto com código {codigo} não encontrado no estoque.")

# Função para exibir o menu de opções
def exibir_menu():
    print("\n================== Lojas Renner ========================")
    print("\n----------------- Menu de Opções -----------------------")
    print("1. Adicionar novo produto")
    print("2. Realizar saída de estoque (venda ou transferência)")
    print("3. Listar produtos no estoque")
    print("4. Sair")
    escolha = input("Escolha uma opção (1-4): ")
    return escolha

# Loop principal do programa
while True:
    opcao = exibir_menu()

    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        saida_estoque()
    elif opcao == '3':
        print("\n============== Produtos no Estoque ===============")
        if not estoque:
            print("Nenhum produto cadastrado.")
        else:
            for codigo, produto in estoque.items():
                print(f"Código: {codigo}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")
    elif opcao == '4':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1-4).")
