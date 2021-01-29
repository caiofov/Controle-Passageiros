import json

'''
Algumas linha vão a mais de um campus, portanto, para modificar uma linha
é necessário informat tanto o nome da linha, quanto o destino
'''

def registra_falhas(lista_falhas):

        try:
            with open('falhas.json', 'r+') as falhas:
                falhas_lista = json.load(falhas)
                falhas.extend(lista_falhas)
        except:
            falhas_lista = lista_falhas
        
        with open('falhas.json', 'w+') as falhas:
            json.dump(falhas_lista, falhas)