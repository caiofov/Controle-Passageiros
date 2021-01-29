import math
import json
import datetime

def insere_linha(
    nome_linha : str, origem : str, 
    destino : str, primeiro_horario : int, 
    periodo: int, duracao_da_viagem : int,
    passagem : float, quantidade_de_assentos : int
                ):

    '''
    Ao cadastrar a linha, o usuário diz o primeiro horário de saida da linha, e de quanto
    em quanto tempo novos onibus saem.

    '''
    #Variável para limitar o preenchimento da lista com os horários disponíveis
    limite = datetime.timedelta(hours = 20)

    #Primeiro horário de partida do ônibus
    horario = datetime.timedelta(hours = primeiro_horario)

    #De quanto em quanto tempo o ônibus passa
    periodo = datetime.timedelta(minutes = periodo)

    #Lista que será adicionada ao dicionário com as informaçoes da linha
    horarios = []

    #Enquanto o horário não tiver atingido o limite(último horário considerado),
    #o loop irá adicionar o o horário atual à lista de horários e somando o periodo do onibus.
    while horario <= limite:
        segundos = horario.seconds
        hora = segundos//3600
        minutos = (segundos//60)%60
        horas = datetime.time(hour=hora, minute = minutos )
        horarios.append(str(horas))
        horario = horario + periodo

    '''

    Considera-se a distribuição comum de assentos de um ônibus municipal,
    dois assentos de cada lado do corredor, assim, considera-se uma matriz sempre
    com 4 colunas, 2 de cada lado do corredor, variando apenas a quantidade de linhas,
    de acordo com número total de assentos.

    '''

    #Matriz com assentos
    matriz_assentos = []

    #Serão consideradas sempre quatro colunas, dois assentos de cada lado do corredor
    colunas = 4

    #O número de linhas, será sempre o número total de assentos
    #dividido pelo número de linhas (arredondado para cima)
    linhas = math.ceil(quantidade_de_assentos/colunas)

    #O primeiro assento é o assento 1
    assento = 1
    
    #Enquando a variável de assentos for menor que o número total de assentos do ônibus
    #o loop irá preencher a matriz.
    while assento <= quantidade_de_assentos:

        for linha in range(linhas):
            linha = []

            for coluna in range(colunas):
                ##Dependendo da quantidade de assentos no ônibus, a matriz criada terá
                ##mais elementos do que assentos, para evitar a criação de assentos que não existem,
                ##se a variável 'assentos' ultrapassar o total de assentos, será colocado um X, para 
                ##representar que não há assentos.
                if assento <= quantidade_de_assentos:
                    linha.append(assento)
                elif assento > quantidade_de_assentos:
                    linha.append('X')
                assento = assento + 1
            matriz_assentos.append(linha)
    
    #Cria o dicionioário com as informações da lista, que será adicionado ao registro.
    linha = {
        'nome_linha' : nome_linha,
        'origem' : origem,
        'destino' : destino, 
        'horarios' : horarios,
        'duracao_da_viagem' : duracao_da_viagem, 
        'passagem' : passagem, 
        'assentos_disponiveis' : matriz_assentos,
        'reservas' : []
            }
    

    '''

    A maneira de armazenar os dicionários ao arquivo é em uma lista, pois facilita a leitura dos dados.
    Ao criar um novo arquivo, ele virá vazio, as palavras-chave try/except permitem tentar desempacotar
    o conteúdo do arquivo sem o risco do programa ser interrompido por um erro. Caso a linha que está sendo
    inserida seja a primeira linha a ser registrada, a clausula a ser executada será a do 'except', caso
    já hajam linhas registradas, a cláusula do 'try' será executada
    
    '''

    lista_para_adicionar = []
    try:
        with open('teste.json', 'r+') as teste:
            tentativa = json.load(teste)
            for conteudo in tentativa:
                lista_para_adicionar.append(conteudo)
            lista_para_adicionar.append(linha)
    except:
        lista_para_adicionar.append(linha)
    
    with open('teste.json', 'w+') as teste:
        json.dump(lista_para_adicionar, teste)