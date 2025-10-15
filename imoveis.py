imoveis = [
{'id': 1,'tipo': 'casa', 'valor':450000, 'aluguel':False, 'cidade':'Nova Andradina', 'data_inclusao':'12/11/2024', 'metragem':80, 'contrato': 1},
{'id': 2,'tipo': 'apartamento', 'valor':900000, 'aluguel':False, 'cidade':'São Paulo', 'data_inclusao':'11/12/2023', 'metragem':100, 'contrato': 1},
{'id': 3,'tipo': 'casa', 'valor':15000, 'aluguel':True, 'cidade':'Xique-Xique', 'data_inclusao':'12/10/202', 'metragem':20, 'contrato': 200},
{'id': 4,'tipo': 'sobrado', 'valor':150000, 'aluguel':False, 'cidade':'Osasco', 'data_inclusao':'30/05/2025', 'metragem':90, 'contrato': 1},
{'id': 5,'tipo': 'casa', 'valor':60000, 'aluguel':True, 'cidade':'Nova Andradina', 'data_inclusao':'24/12/2024', 'metragem':60, 'contrato': 50},
{'id': 6,'tipo': 'apartamento', 'valor':650000, 'aluguel':False, 'cidade':'Porto Alegre', 'data_inclusao':'11/09/2023', 'metragem':80, 'contrato': 1},
{'id': 7,'tipo': 'casa', 'valor':310000, 'aluguel':False, 'cidade':'Nova Andradina', 'data_inclusao':'20/10/2025', 'metragem':70, 'contrato': 1}
]

def menu(imoveis):
    opcao = 1
    while opcao != 0:
        print('=======================MENU IMÓVEIS=======================')
        print('= 1 - Listar todos imóveis                               =')
        print('= 2 - Listar imóveis do tipo Venda                        =')
        print('= 3 - Listar imóveis do tipo Aluguel                     =') #QUANDO FOR DO TIPO ALUGUEL MULTIPLICAR PELO CONTRATO 
        print('= 4 - Listar imóveis de valor menor que                   =')
        print('= 5 - Listar imóveis da cidade com o tipo (Venda/Aluguel)  =') #USUARIO INFORMA CIDADE E TIPO DE IMOVEL
        print('= 6 - Corrigir IGP-M (REAJUSTE DE ALUGUEL)               =') #CORRIGE ALUGUEL DADO A PORCENTAGEM (ATUALIZA O VALOR APENAS DE TODOS IMOVEIS DE ALUGUEL)
        print('= 7 - Atualizar um imovel por id                         =') #ATUALIZAR SOMENTE: VALOR, ALUGUEL, DATA, METRAGEM, CONTRATO
        print('= 8 - Remover um imovel por id                           =')
        print('= 0 - Sair')
        opcao = int(input('>>'))
        if opcao == 1:
            imprimir_todos_imoveis(imoveis)
        elif opcao == 2:
            imprimir_imoveis_venda(imoveis, imprimir_imovel)
        elif opcao == 3:
            imprimir_imoveis_aluguel(imoveis, imprimir_imovel)
        elif opcao == 4:
            imprimir_valor_menorque(imoveis, imprimir_imovel)
        elif opcao == 5:
            imprimir_por_cidade(imoveis, imprimir_imovel)
        elif opcao == 6:
            print('Não Implementado')
        elif opcao == 7:
            id = int(input("Entre com o ID do imóvel: "))
            posicao = buscar_por_id(imoveis, id)
            if posicao == -1:
                print("Imóvel não encontrado.")
            else:
                atualizar_por_id(imoveis, posicao)
        elif opcao == 8:
            id = int(input("Entre com o ID do imóvel: "))
            posicao = buscar_por_id(imoveis, id)
            if posicao == -1:
                print("Imóvel não encontrado.")
            else:
                remover_por_id(imoveis, posicao)
        elif opcao == 0:
            print('Saindo!!!')
        else:
            print('Opção Inválida!')

def imprimir_imovel(imovel):
    print('Tipo:', imovel["tipo"])
    print('Metragem:', imovel["metragem"], 'm²')
    print('Data Inclusão:', imovel["data_inclusao"])
    print('Cidade:', imovel["cidade"])
    print('Disponível para ' , 'Venda' if imovel["aluguel"] == False else 'Aluguel')
    print('Valor:', imovel["valor"])
    if imovel["aluguel"] == True:
        print("Valor total de contrato: ", imovel['valor']*imovel['contrato'])    
    print('--------------------------------')

def imprimir_todos_imoveis(imoveis):
    for im in imoveis:
        imprimir_imovel(im)
        
def imprimir_imoveis_venda(imoveis, imprimir_imovel):
    for im in imoveis:
        if im["aluguel"] == False:
            imprimir_imovel(im)
            
def imprimir_imoveis_aluguel(imoveis, imprimir_imovel):
    for im in imoveis:
        if im["aluguel"] == True:
            imprimir_imovel(im)
    
def imprimir_valor_menorque(imoveis, imprimir_imovel):
    valorBuscado = int(input("Informe um valor: "))
    for im in imoveis:
        if im["valor"] < valorBuscado:
            imprimir_imovel(im)
            
def imprimir_por_cidade(imoveis, imprimir_imovel):
    cidadeBuscada = input("Informe a cidade: ").lower()
    tipoBuscado = input("Informe o tipo de negociação (Aluguel - True / Venda - False): ")
    for im in imoveis:
        if im["aluguel"] == tipoBuscado:
            imprimir_imovel(im)
            
def buscar_por_id(imoveis, id):
    for im in range(len(imoveis)):
        if id == imoveis[im]["id"]: 
            return im
    return -1            

def atualizar_por_id(imoveis, posicao):
    imovel = imoveis[posicao] #variável que pega o dicionário atual no índice desejado na lista

    valor = int(input("Entre com o valor do imóvel em R$: "))
    aluguel = input("O imóvel é do tipo aluguel? (S|N) ").upper()
    aluguel = True if aluguel == 'S' else False
    data = input("Entre com a data de inclusão do imóvel (Ex. 00/00/00) ")
    metragem = int(input("Entre com a metragem do imóvel: "))
    if aluguel == True:
        contrato = int(input("Entre com o valor do contrato: "))
    

    imovel_atualizado = dict(
        id = imovel["id"],
        tipo = imovel["tipo"],
        cidade = imovel["cidade"],
        valor = valor,
        aluguel = aluguel,
        data = data,
        metragem = metragem,
        contrato = contrato
        if imovel["aluguel"] == True:
            contrato = contrato
    )

    imoveis[posicao] = imovel_atualizado
    print("==== Imóvel Atualizado com Sucesso!")

def remover_por_id(imoveis, posicao):
    imoveis.pop(posicao)
    print("==== Imóvel Removido com Sucesso!")
    
menu(imoveis)