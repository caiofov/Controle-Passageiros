import datetime
import json

with open('teste.json') as teste:
    teste = json.load(teste)


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
                    ocupacao_media_semanal['nome_linha'] = linha['nome_linha']
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
                linha[dia] = round(media*100, 2)
            #Armazena as informações da média de ocupação dos assentos para cada dia da semana
            #junto com o nome da linha
    return medias_semanais



print(ocupacao_media_semanal(teste))
