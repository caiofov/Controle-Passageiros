import json

'''
Algumas linha vão a mais de um campus, portanto, para modificar uma linha
é necessário informat tanto o nome da linha, quanto o destino
'''

def altera_linha(nome_linha : str, destino: str, parametro : str, novo_valor):

    
    with open('teste.json') as teste:
        #Abre o arquivo, e armazena seu conteúdo em uma lista
        lista_linhas = json.load(teste)
        
        #Confere o nome da linha e o destino, para garantir que a linha correta está sendo alterada
        for linha in lista_linhas:
            if  (linha['nome_linha'] == nome_linha) and (linha['destino'] == destino):
                index = lista_linhas.index(linha)
                linha = lista_linhas.pop(index)
                
                #Por causa do funcionamento dos dicionários, caso o usuário
                #insina um parametro inexistente, se não houver checagem, a função 
                #irá criar um novo paraâmetro
                if parametro not in linha.keys():
                    parametro = input('O parâmetro que você deseja alterar não existe, verifique se o nome está correto e insira novamente')
                    
                linha[parametro] = novo_valor
                lista_linhas.append(linha)

    with open('teste.json', 'w+') as teste:       
        json.dump(lista_linhas, teste)
    
