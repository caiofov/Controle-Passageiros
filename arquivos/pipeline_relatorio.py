import json
import datetime

with open('teste.json') as file:
    dados = json.load(file)


#a função recebe como parâmetro o dicionário, no qual estão as reservas, e o mês escolhido para fazer o relatório
def quantas_meias_por_linha(dados = list, nome_da_linha = str, mes_escolhido = int, ano = int):
    qtd_meias = 0
    #range(1, 32) pois não é inclusivo
    for dia in range(1, 32):
        #ou seja, a variação é de 31 dias, logo, a formatação da data no if aqui abaixo receberá do dia 1 ao dia 30 do mês escolhido
        for linhas in dados:
            
            if linhas['nome_linha'] == nome_da_linha:
                #if para delimitar qual linha quero acessar
                for reservas in linhas['reservas']:

                    if reservas['data'] == f'{ano}-{mes_escolhido}-{dia}':   
                    
                        qtd_meias = qtd_meias + reservas['meia']
    
    return qtd_meias



#a função recebe como parâmetro o arquivo em formato de lista, no qual estão as reservas, além do nome da linha, mês e ano escolhidos para gerar o relatório
def quantas_inteiras_por_linha(dados = list, nome_da_linha = str, mes_escolhido = int, ano = int):
    qtd_inteiras = 0
    for dia in range(1, 32):
        
        for linhas in dados:

            if linhas['nome_linha'] == nome_da_linha:

                for reservas in linhas['reservas']:
                    
                    if reservas['data'] == f'{ano}-{mes_escolhido}-{dia}':
                    
                        qtd_inteiras = qtd_inteiras + reservas['inteira']
    
    return qtd_inteiras



#a função recebe como parâmetro o arquivo em formato de lista, no qual estão as reservas, além do nome da linha, mês e ano escolhidos para gerar o relatório
def quantas_gratuitas_por_linha(dados = list, nome_da_linha = str, mes_escolhido = int, ano = int):
    qtd_gratuitas = 0
    for dia in range(1, 32):
        
        for linhas in dados:

            if linhas['nome_linha'] == nome_da_linha:

                for reservas in linhas['reservas']:
                    
                    if reservas['data'] == f'{ano}-{mes_escolhido}-{dia}':
                    
                        qtd_gratuitas = qtd_gratuitas + reservas['gratuita']
    
    return qtd_gratuitas


#não coloquei as gratuitas, pois não alteram o valor
def total_arrecadado(dados = list, mes_escolhido = int, ano = int):
    #passamos o mês escolhido e a função retorna o valor arrecadado nele.
    valor_arrecadado_por_linha = []
    #farei uma lista de dicionários com o nome da linha e o valor arrecadado por ela em um mês
    for linhas in dados:
        #loop para passar por cada linha do arquivo
        valor_por_linha = dict()
        #inicio o dicionario
        valor_por_linha['linha'] = linhas['nome_linha']    
        #key linha e valor nome_linha
        nome_da_linha = linhas['nome_linha']
        #variavel nome_da_linha para servir de parêmetro para as funções
        qtd_inteiras = quantas_inteiras_por_linha(dados, nome_da_linha, mes_escolhido, ano)
        
        qtd_meias = quantas_meias_por_linha(dados, nome_da_linha, mes_escolhido, ano)
            
        valor_por_linha['valor arrecadado'] = f'R${((qtd_inteiras*3.60) + (qtd_meias*1.60)):.2f}'
        
        valor_arrecadado_por_linha.append(valor_por_linha)

    return valor_arrecadado_por_linha



#função para calcular quantidade total de passagens inteiras vendidas por todas as linhas
#recebe como parâmetro o arquivo de linhas, o nome da linha, mês e ano para os quais se querem o relatório
def quantas_inteiras_mes(dados = list, mes_escolhido = int, ano = int):
    qtd_inteiras = 0
    for dia in range(1, 32):
        #loop para percorrer todo o mês
        for linhas in dados:
            #loop para pegar todas as linhas no arquivo de linhas
            for reservas in linhas['reservas']:
                    
                if reservas['data'] == f'{ano}-{mes_escolhido}-{dia}':
                    
                    qtd_inteiras = qtd_inteiras + reservas['inteira']
    
    return qtd_inteiras



def quantas_meias_mes(dados = list, mes_escolhido = int, ano = int):
    qtd_meias = 0
    for dia in range(1, 32):
        
        for linhas in dados:

            for reservas in linhas['reservas']:
                    
                if reservas['data'] == f'{ano}-{mes_escolhido}-{dia}':
                    
                    qtd_meias = qtd_meias + reservas['meia']
    
    return qtd_meias




def quantas_gratuitas_mes(dados = list, mes_escolhido = int, ano = int):
    qtd_gratuitas = 0
    for dia in range(1, 32):
        
        for linhas in dados:

                for reservas in linhas['reservas']:
                    
                    if reservas['data'] == f'{ano}-{mes_escolhido}-{dia}':
                    
                        qtd_gratuitas = qtd_gratuitas + reservas['gratuita']
    
    return qtd_gratuitas


#função para calcular quantidade total de passageiros num mês
def total_de_passageiros(dados = list, mes_escolhido = int, ano = int):
    qtd_inteiras = quantas_inteiras_mes(dados, mes_escolhido, ano) 
    qtd_meias = quantas_meias_mes(dados, mes_escolhido, ano) 
    qtd_gratuitas = quantas_gratuitas_mes(dados, mes_escolhido, ano)
    #soma das funções anteriores

    qtd_total = qtd_inteiras + qtd_meias + qtd_gratuitas
    
    return qtd_total



#função para calcular o percentual de estudantes
def percentual_estudantes(dados = list, mes_escolhido = int, ano = int):
    #função anterior para calcular a quantidade de passagens de estudante vendidas
    qtd_meias = quantas_meias_mes(dados, mes_escolhido, ano)
    qtd_passageiros = total_de_passageiros(dados, mes_escolhido, ano)
    if qtd_passageiros > 0:
        porcentagem_de_estudantes = qtd_meias*100 / qtd_passageiros
    else:
        porcentagem_de_estudantes = 0   
    #calcula o percentual de estudantes em relação ao total de passageiros
    return porcentagem_de_estudantes



#função para calcular o percentual de gratuidades
def percentual_gratuidades(dados = list, mes_escolhido = int, ano = int):
    qtd_gratuitas = quantas_gratuitas_mes(dados, mes_escolhido, ano)
    #chamo a função anterior de calcular quantas gratuidades e trato-a como passageiros
    qtd_passageiros = total_de_passageiros(dados, mes_escolhido, ano)
    if qtd_passageiros > 0:
        porcentagem_de_gratuidades = qtd_gratuitas*100 / qtd_passageiros
    #calcula o percentual de gratuidades em relação ao total de passageiros
    else:
        porcentagem_de_gratuidades = 0
    return porcentagem_de_gratuidades






#Dicionário para converter a representação do dia da semana da biblioteca datetime
#nos nomes dos dias da semana
semana = {
    'Segunda-Feira' : 0, 'Terça-Feira' : 1, 
    'Quarta-Feira' : 2, 'Quinta-Feira' : 3, 
    'Sexta-Feira' : 4, 'Sábado' : 5,
    'Domingo' : 6
}

ocupacao_media = {
    'Segunda-Feira' : [],
    'Terça-Feira' : [],
    'Quarta-Feira' : [],
    'Quinta-Feira' : [],
    'Sexta-Feira' : [],
    'Sábado' : [],
    'Domingo' : []
}

def input_data_dia_semana(data_input):
    #Recebe a data (string) constante na reserva, e converte num objeto datetime
    data_input = str(data_input)
    data_input = data_input.split('-')
    data = datetime.date(int(data_input[0]), int(data_input[1]), int(data_input[2]))
    return data.weekday()



def ocupacao_media_semanal(dados):

    semana = {
    'Segunda-Feira' : 0, 'Terça-Feira' : 1, 
    'Quarta-Feira' : 2, 'Quinta-Feira' : 3, 
    'Sexta-Feira' : 4, 'Sábado' : 5,
    'Domingo' : 6
    }
    #Lista onde os dicionários com as medias de ocupação para cada dia da semana 
    #para cada linha serão armazenados
    medias_semanais = []

    #Dicionário onde as médias de ocupação para cada dia da semana serão armazenadas

    for linha in dados:
        ocupacao_media_semanal = {'Segunda-Feira' : [], 'Terça-Feira' : [],
                                    'Quarta-Feira' : [], 'Quinta-Feira' : [],
                                    'Sexta-Feira' : [], 'Sábado' : [], 'Domingo' : []}
        #Verifica se há alguma reserva na linha em questão, para avaliar se há como calcular a media de ocupação
        if len(linha['reservas']) > 0:
            for reserva in linha['reservas']:
                #Converte o valor numérico do dia da semana em texto
                dia = input_data_dia_semana(reserva['data'])
                for key, value in semana.items():
                    if dia == value:
                        dia = key
                #Calcula a media de ocupação dos assentos para cada dia da semana e armazena no dicionário
                        ocupacao = len(reserva['assentos']) / 30
                        ocupacao_media_semanal[dia].append(ocupacao)
                    ocupacao_media_semanal['linha'] = linha['nome_linha']
                medias_semanais.append(ocupacao_media_semanal)
        

    for linha in medias_semanais:
        for dia in linha.keys():
            if type(linha[dia]) == list and len(linha[dia]) > 0:
                soma = 0
                #Verifica se a ocupação media diária para um dia tem algum elemento,
                #ou seja, se houve alguma reserva naquele dia, para não tentar calcular
                #a media de uma lista sem elementos
                for media in linha[dia]:
                    soma = soma + media
                    media = soma/len(linha[dia])
                linha[dia] = f'{round(media*100, 2)}%'
            #Armazena as informações da média de ocupação dos assentos para cada dia da semana
            #junto com o nome da linha
    return medias_semanais

#print(ocupacao_media_semanal(dados))


def gerar_matriz_ocupacao(medias_semanais = list):
    #lista onde será armazenada a lista de ocupação média por dias da semana
    matriz = []
    for medias in medias_semanais:
        #loop para percorrer a lista de médias semanais geradas pela função anterior
        linha_matriz = []
        for keys, values in medias.items():
            linha_matriz.append(f'{keys}: {values}')
            #linha dá um append nas keys e valores dos dicionários contidos na lista de ocupação
        matriz.append(linha_matriz)
    return matriz        

#função para exibir matriz de forma que print a linha da matriz em cada linha do terminal
def exibir_matriz_ocupacao(matriz):
    for linha in matriz:
        print(linha)

#exibir_matriz_ocupacao(gerar_matriz_ocupacao(ocupacao_media_semanal(dados)))
