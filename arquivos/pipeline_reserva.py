import pergunta_sim_ou_nao as sn
import input_horario as ih
import altera_linha as al
import input_ponto as ip
import input_linha as il
import input_data as id
import regista_falhas as rf
import datetime
import json

'''
A função permite que o usuário pesquise quais linhas na base de dados vão até a parada desejada e,
caso existam, perguntar se o usuário deseja realizar uma reserva. Caso o usuário deseje reservar um assento,
a função reservar_assento será executada. Por usa vez, a função reservando_assento ira chamar essa mesma função,
com o parâmetro 'reservando' == True, fazendo com que ela apenas retorne uma lista.

'''
#O parâmetro 'reservando' é utilizado para controle, idealmente deve ser omitido
#pelo usuário, sendo utilizado apenas pela função 'reservando_assento'
def checa_linha(destino : str):
    
    #Abre o bando de dados e cria uma lista com as linhas
    #que vão para o destino desejado.
    lista_linhas = []
    with open('teste.json') as teste:
        for linha in json.load(teste):
            if linha['destino'] == destino:
                lista_linhas.append(linha)

    #Caso nenhuma lista para o destino esteja disponível
    #o usuário é informado
    if len(lista_linhas) == 0:
                print('Não há linhas com esse destino cadastradas')

    #As linhas disponíveis são exibidas ao usuário,
    #e é perguntado se deseja fazer uma reserva.
    else:
            for linha in lista_linhas:
                print(linha['nome_linha'])
            
            reserva = sn.pergunta_sim_ou_nao('Você gostaria de verificar a disponibilidade de assentos? ')


            #Caso o usuário deseje realizar uma reserva
            #a função responsável é chamada.
            if reserva == 'sim':
                linhas_disponiveis(lista_linhas)

#CAIO - Funcao para verificar as linhas disponiveis para um certa data e hora

def linhas_disponiveis(lista_linhas):
    diferenca_minima_agendamento_horas = 24
    while True:
        lista_disponiveis = [] #lista das linhas disponiveis
        
        #pedir o ponto de partida
        ponto_partida = ip.input_ponto(lista_linhas, msg="Ponto de partida: ", msg_de_erro='Ponto de partida não encontrado. Por favor, tente novamente')
        
        while True: #loop data e horario
            #pedir a data de partida
            data_partida = id.input_data("Data de partida: ")
                
            #pedir o horario de partida
            horario_partida = ih.input_horario("Horario de partida: ")
            
            data_e_hora_partida = data_partida + datetime.timedelta(hours=horario_partida.hour, minutes=horario_partida.minute)
            
            if datetime.datetime.now() + datetime.timedelta(hours=diferenca_minima_agendamento_horas) > data_e_hora_partida:
                print("Por favor, reserve/consulte as linhas com no minimo 24h de antecedencia")
        
            else:
                break
            
            
        data_partida=str(data_partida)[:10] #para deixar no padrao
        horario_partida=str(horario_partida)
       
        #adicionar as linhas disponiveis na lista_disponiveis
        for linha in lista_linhas:
            disponivel=True
            
            #se o horario ou a origem nao for o da linha que esta sendo analisada
            if horario_partida not in linha['horarios'] or linha['origem'] != ponto_partida:
                disponivel = False
            
            #se nao houver assentos disponiveis
            elif len( assentos_disponiveis(linha, horario_partida, data_partida) ) == 0:
                disponivel = False
                    
            
            #imprimir as linhas disponiveis e adicionar a lista das disponiveis
            if disponivel:
                lista_disponiveis.append(linha)
                
        #se nao houver linhas disponiveis
        if len(lista_disponiveis) == 0:
            print("Nao ha linhas disponiveis com os dados inseridos. Por favor, tente novamente.")
        
       
        else:
            print('As linhas com assentos disponiveis nessa data e horario sao: ')
            
            #imprimir as linhas disponiveis
            for linha in lista_disponiveis:
                print('\n >> %s << \n    Assentos: %s \n' %(linha['nome_linha'],str(assentos_disponiveis(linha,horario_partida,data_partida)[0])[1:-1]) )
            
            reserva = sn.pergunta_sim_ou_nao("Deseja efetuar uma reserva?")
            if reserva == 'nao':
                break
            
            elif reserva == 'sim':
                
                if len (lista_disponiveis) == 1:
                        
                    escolha_linha = lista_disponiveis[0]
                    print('\nLinha: ', escolha_linha['nome_linha'])
                
                else:
                    escolha_linha = il.input_linha(lista_disponiveis,'\nLinha: ','Por favor, insira uma linha dentre as disponiveis')
                
                reservar_assento(escolha_linha,data_partida,horario_partida,lista_linhas)
                break


#CAIO - Funcao de reservar assento

def reservar_assento(linha,data_partida,horario_partida,lista_linhas):
    
    while True:
    
        #retorno da funcao dos assentos disponiveis
        retorno_funcao_assentos = assentos_disponiveis(linha, horario_partida, data_partida)
        
        disponiveis = retorno_funcao_assentos[0]
        index = retorno_funcao_assentos[1]
        
        #imprimir os assentos disponiveis
        print("\nOs assentos disponiveis sao: ", str(disponiveis)[1:-1])
        
        while True: #loop da escolha do assento
            
            reservado = input("Qual voce deseja reservar? ") #deixar em string para aceitar mais respostas e dar menos erro
            
            try:
                reservado = int(reservado) #mudar para inteiro
            except:
                pass
            
            if reservado not in disponiveis:
                print("Por favor, escolha um assento dentre os disponi­veis")
                
                #falhas na reserva:
                if reservado in linha['assentos_disponiveis']:
                    reservas_falhas = [{'linha':linha['nome_linha'],'data':data_partida,'horario':horario_partida,'motivo':"Assento ocupado"}]
                    rf.registra_falhas(reservas_falhas)
               
                elif reservado not in linha['assentos_disponiveis']:
                    reservas_falhas = [{'linha':linha['nome_linha'],'data':data_partida,'horario':horario_partida,'motivo':"Assento inexistente"}]
                    rf.registra_falhas(reservas_falhas)
                    
            
            else:
                
                break
        
        
        while True: #loop do pagamento - tem que ser loop, porque existe a possibilidade do usuario errar o input
                #pergunta o tipo da passagem
                pagar = input("Qual a passagem? \n(1)-Inteira \n(2)-Meia Estudante \n(3)-Idoso ou crianca \nDigite o numero correspondente: ")
                
                if pagar == '1': #inteira
                   
                    preco=linha['passagem']
                    linha['reservas'][index]['inteira'] += 1
                    
                    break
                
                elif pagar == '2': #meia
                   
                    preco = linha['passagem']/2
                    linha['reservas'][index]['meia'] += 1
                    
                    break
               
                elif pagar == '3': #gratuita
                    
                    preco = 0
                    linha['reservas'][index]['gratuita'] += 1
                    
                    break
               
                else:
                    print("Por favor, insira um numero valido (1, 2 ou 3)")
            
        #imprimir a reserva
        print("\n - - - Sua reserva sera: - - - \n \n¬ Linha: %s \n¬ Data: %s \n¬ Horario: %s \n¬ Rota: %s -> %s \n¬ Assento: %d \n¬ Preco: R$ %.2f" %(linha['nome_linha'],data_partida,horario_partida,linha['origem'].upper(),linha['destino'].upper(),reservado,preco))
        
        #confirmar a reserva
        confirma = sn.pergunta_sim_ou_nao("Voce confirma?")
       
        if confirma == 'nao':
            reservas_falhas=[{'linha':linha['nome_linha'],'data':data_partida,'horario':horario_partida,'motivo':"Reserva nao confirmada"}]
            rf.registra_falhas(reservas_falhas)
                    
            recomecar= sn.pergunta_sim_ou_nao("Deseja recomecar a reserva? ")
           
            if recomecar == 'nao':
                break
            
            elif recomecar == 'sim':
                mudar_destino = sn.pergunta_sim_ou_nao("Gostaria de alterar o destino? ")
               
                if mudar_destino == 'sim':
                    destino = input("Novo destino: ")
                    checa_linha(destino)
                    break
                
                else:
                    linhas_disponiveis(lista_linhas)
                    break
        
        elif confirma == "sim":
            #adicionar o assento reservado a lista das reservas
            linha['reservas'][index]['assentos'].append(reservado) 
        
        
            #ver os assentos que serao "ocupados por tabela" (seguindo as restricoes) depois de reservado aquele
            
            if reservado%2 == 0:
                restricao = reservado-1
                
                if restricao in disponiveis:
                    linha['reservas'][index]['assentos'].append(restricao)
           
            
            else:
                restricao = reservado+1
               
                if restricao in disponiveis:
                    linha['reservas'][index]['assentos'].append(restricao)
            
            
            restricao = reservado+4
            if restricao in disponiveis:
                linha['reservas'][index]['assentos'].append(restricao)
            
            
            restricao = reservado-4
            if restricao in disponiveis:
                linha['reservas'][index]['assentos'].append(restricao)
                    
            
            #registrar as alteracoes
            al.altera_linha(linha['nome_linha'],linha['destino'],'reservas',linha['reservas'])
            
            continuar = sn.pergunta_sim_ou_nao("Deseja reservar mais um assento?")
            
            
            if continuar == 'nao':
                break
            
            elif continuar == 'sim':
                mudar_destino = sn.pergunta_sim_ou_nao("Gostaria de alterar o destino? ")

                if mudar_destino == 'sim':
                    destino = input("Novo destino: ")
                    checa_linha(destino)
                    break
                
                else:
                    linhas_disponiveis(lista_linhas)
                    break
    

    print("\n----- FIM DA RESERVA ------")

#CAIO - Funcao para ver os assentos disponiveis
def assentos_disponiveis(linha, horario_partida, data_partida):
    disponiveis = [] #lista dos assentos disponiveis
    index = 0 #index que sera usado nas reservas (vai mudar)
        
    
    #preencher a lista "disponiveis" com todos os assentos pela matriz do padrao dos assentos da linha
    for linha_matriz in range( len (linha['assentos_disponiveis']) ):
        for coluna_matriz in range( len (linha['assentos_disponiveis'][0]) ):
            
            if type(linha['assentos_disponiveis'][linha_matriz][coluna_matriz]) is int:
                disponiveis.append(linha['assentos_disponiveis'][linha_matriz][coluna_matriz])
            
            
    
    if len( linha['reservas'] ) != 0: #se ja houver reservas na linha
        tem_reserva = False #ira ser True se existir alguma reserva com o mesmo dia e horario
        
        for reserva in linha['reservas']: 
            
            #se ja houver uma reserva com o mesmo dia e horario
            if reserva['data'] == data_partida and reserva['horario'] == horario_partida:
                
                index = linha['reservas'].index(reserva)
                tem_reserva = True 
                
                
                #remover da lista "disponiveis" os assentos ja reservados
                for assento in reserva['assentos']:
                    disponiveis.remove(assento)
                    
                break
        
    #se nao houver reservas na linha ou a variavel 'tem_reserva' for False
    if len( linha['reservas'] ) == 0 or not tem_reserva: 
        
        nova_reserva = {'data':data_partida,'horario':horario_partida,'assentos':[],'inteira':0,'meia':0,'gratuita':0}
        linha['reservas'].append(nova_reserva)
        index = -1
            
           
    return [disponiveis, index]