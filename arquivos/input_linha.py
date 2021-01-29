import remove_caracteres_especiais as rc
def input_linha(dicionario_linhas, msg='Linha: ', msg_erro='Linha não encontrada.'):
    while True:
        linha_input = rc.remove_caracteres_especiais(input(msg)).lower()
        for dicionario in dicionario_linhas:
            linha = dicionario['nome_linha']
            linha_normalizada = rc.remove_caracteres_especiais(linha.lower())
            nomes, numero = linha_normalizada.replace(')','').split('(')
            if linha_input==linha_normalizada or linha_input==nomes.lower() or linha_input==numero:
                return dicionario
        print(msg_erro)