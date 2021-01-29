import remove_caracteres_especiais as rce


def input_ponto(lista_linhas, msg='Ponto: ', msg_de_erro='Nenhum ponto encontrado.'):
    pontos_de_partida = set()
    for linha in lista_linhas:
        pontos_de_partida.add(linha['origem'])
    pontos_de_partida_normalizados = [rce.remove_caracteres_especiais(ponto).lower() for ponto in pontos_de_partida]
    print('Pontos disponíveis:')
    print(', '.join(pontos_de_partida))
    while True:
        input_ponto = rce.remove_caracteres_especiais(input(msg).lower())
        for ponto_de_partida_normalizado in pontos_de_partida_normalizados:
            if ponto_de_partida_normalizado in input_ponto:
                return ponto_de_partida_normalizado
        print(msg_de_erro)