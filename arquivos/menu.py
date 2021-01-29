import pipeline_reserva as pr
import altera_linha as al
import insere_linha as il
#menu para o inicio do programa

print("Bem-vindo(a)!")
while True: #loop do menu principal
    print("MENU PRINCIPAL: \nO que deseja fazer?")

    print("(1) - Reservar assento ou verificar disponibilidade de linhas \n(2) - Area do administrador \n(3) - Encerrar o programa")
    fazer = input("Digite sua opcao: ")

    if fazer == '1':
    
        destino = input("Qual o campus de destino?: ")
        pr.checa_linha(destino)

    elif fazer =='2':
    
        while True: #loop do admin
            print('Esta e a area do administrador. O que deseja fazer? \n (1) - Alterar linhas ja existentes \n (2) Adicionar novas linhas \n (3) - Voltar ao menu principal')
            admin = input("Escolha sua opcao: ")
    
            if admin == "1":
        
            #pedir as informacoes
                nome_linha = input("Nome da linha que sera alterada: ")
                destino = input("Destino da linha: ")
                parametro = input("O que voce deseja alterar? Opcoes:\n-passagem\n-origem\n-destino\n-duracao_da_viagem\n-quantidade_de_assentos ") #COLOCAR O NOME DOS PARAMETROS QUE PODEM SER ALTERADOS
                novo_valor = input('Qual o novo valor do parâmetro?: ')
            #chamar a funcao
                al.altera_linha(nome_linha, destino, parametro, novo_valor)
                break
        
            elif admin =='2':
                #pedir as informacoes para a nova linha
                nome_linha = input("Nome da nova linha: ")
                origem = input("Origem da nova linha: ")
                destino = input("Destino da nova linha: ")
                duracao = input( "Duracao da viagem: ")
                primeiro_horario = input("Que horas a linha comecara seu trajeto? ")
                periodo = input("Periodo: ") #O que eh isso?
                passagem = input("Valor da passagem: ")
                qtd_assentos = input("Quantidade de assentos: ")
        
                #chamar a funcao
                il.insere_linha(nome_linha,origem,destino,primeiro_horario,periodo,duracao,passagem,qtd_assentos)
                break

            elif admin =="3":
                break

            else:
                print("Por favor, insira um numero valido (1, 2 ou 3)")
    
    elif fazer == '3':
        break

    else:
        print("Por favor, insira um numero valido (1, 2 ou 3)")

print("Feito por Equipe Open-Source: \n- Caio Oliveira \n- Joao Pedro Isaias \n- Paulo Rodrigues \n- Pedro Amaral ")