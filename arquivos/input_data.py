import datetime


def input_data(msg='Data: ', data_atual=datetime.datetime.now(), delta=15):
    #dd/mm/aaaa
    while True:
        #pede input no formato dd/mm/aaaa mas aceita somente dd/mm ou dd
        data_input = input(msg).split('/')
        try:
            #quando dia e mes eh dado adiciona ano
            if len(data_input)==2:
                data_input.append(data_atual.year)
            #quando so dia eh dado, adiciona mes e ano
            elif len(data_input)==1:
                data_input += [data_atual.month, data_atual.year]
            #cria datetime com essas informacoes
            data = datetime.datetime(int(data_input[2]), int(data_input[1]), int(data_input[0]))
            #checa se aconteceu no passado ou hoje
            if data<=data_atual:
                print('Nao temos onibus nessa data.')
            #checa se ta dentro do periodo maximo de cadastramento
            elif data_atual + datetime.timedelta(days = delta)<data:
                print('Voce so pode reservar no maximo a {} dias de distancia'.format(delta))
            else:
                return data
        except:
            print('Data invalida')
