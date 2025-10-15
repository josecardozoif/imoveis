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
        print('= 3 - Listar imóveis do tipo Aluguel                     =')
        print('= 4 - Listar imóveis de valor menor que                   =')
        print('= 5 - Listar imóveis da cidade com o tipo (Venda/Aluguel)  =')
        print('= 6 - Corrigir IGP-M (REAJUSTE DE ALUGUEL)               =')
        print('= 7 - Atualizar um imovel por id                         =')
        print('= 8 - Remover um imovel por id                           =')
        print('= 0 - Sair')
        try:
            opcao = int(input('>> '))
        except:
            print('Opção Inválida!')
            continue
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
            corrigir_igpm(imoveis)
        elif opcao == 7:
            try:
                id = int(input("Entre com o ID do imóvel: "))
            except:
                print("ID inválido.")
                continue
            posicao = buscar_por_id(imoveis, id)
            if posicao == -1:
                print("Imóvel não encontrado.")
            else:
                atualizar_por_id(imoveis, posicao)
        elif opcao == 8:
            try:
                id = int(input("Entre com o ID do imóvel: "))
            except:
                print("ID inválido.")
                continue
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
    try:
        valorBuscado = int(input("Informe um valor: "))
    except:
        print("Valor inválido.")
        return
    for im in imoveis:
        if im["valor"] < valorBuscado:
            imprimir_imovel(im)
            
def imprimir_por_cidade(imoveis, imprimir_imovel):
    cidadeBuscada = input("Informe a cidade: ").strip().lower()
    tipoBuscado = input("Informe o tipo de negociação (Aluguel / Venda): ").strip().lower()
    if tipoBuscado in ('aluguel','a','s','sim','true','t'):
        tipo_bool = True
    elif tipoBuscado in ('venda','v','n','nao','não','false','f'):
        tipo_bool = False
    else:
        print("Tipo de negociação inválido. Use 'Aluguel' ou 'Venda'.")
        return
    encontrou = False
    for im in imoveis:
        if im.get("cidade", "").strip().lower() == cidadeBuscada and im.get("aluguel") == tipo_bool:
            imprimir_imovel(im)
            encontrou = True
    if not encontrou:
        print("Nenhum imóvel encontrado para os filtros informados.")
            
def buscar_por_id(imoveis, id):
    for im in range(len(imoveis)):
        if id == imoveis[im]["id"]: 
            return im
    return -1            

def atualizar_por_id(imoveis, posicao):
    imovel = imoveis[posicao]

    try:
        valor = int(input("Entre com o valor do imóvel em R$: "))
    except:
        print("Valor inválido.")
        return
    aluguel_input = input("O imóvel é do tipo aluguel? (S|N) ").upper()
    aluguel = True if aluguel_input == 'S' else False
    data = input("Entre com a data de inclusão do imóvel (Ex. 00/00/00) ")
    try:
        metragem = int(input("Entre com a metragem do imóvel: "))
    except:
        print("Metragem inválida.")
        return
    if aluguel == True:
        try:
            contrato = int(input("Entre com o valor do contrato: "))
        except:
            print("Contrato inválido.")
            return
    else:
        contrato = 1

    imovel_atualizado = dict(
        id = imovel["id"],
        tipo = imovel["tipo"],
        cidade = imovel["cidade"],
        valor = valor,
        aluguel = aluguel,
        data_inclusao = data,
        metragem = metragem,
        contrato = contrato
    )

    imoveis[posicao] = imovel_atualizado
    print("==== Imóvel Atualizado com Sucesso!")

def corrigir_igpm(imoveis):
    try:
        perc = float(input("Informe a porcentagem de reajuste (ex.: 5 para 5%): "))
    except:
        print("Porcentagem inválida.")
        return
    fator = 1 + (perc / 100)
    reajustados = 0
    for im in imoveis:
        if im.get('aluguel') == True:
            valor_antigo = im.get('valor', 0)
            novo_valor = int(valor_antigo * fator)
            im['valor'] = novo_valor
            reajustados += 1
            print("ID", im['id'], "-", im['tipo'], "reajustado de", valor_antigo, "para", novo_valor)
    if reajustados == 0:
        print("Não há imóveis de aluguel para reajustar.")
    else:
        print("Total de imóveis reajustados:", reajustados)

def remover_por_id(imoveis, posicao):
    imoveis.pop(posicao)
    print("==== Imóvel Removido com Sucesso!")
    
menu(imoveis)