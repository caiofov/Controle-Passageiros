import pipeline_relatorio as prel
import json

with open('teste.json') as testes:
    dados = json.load(testes)

ano = int(input('\nDigite o ano para o qual quer o relatório: '))
mes = int(input('\nDigite o mês: '))


print('\nComo deseja gerar o relatório?\n\n1 - gerar na tela\n\n2 - gerar um arquivo de texto\n')

forma_de_gerar = int(input(''))
if forma_de_gerar == 1:
    #gerando no terminal
    print('------------------------RELATÓRIO---------------------------')
    print('\nValor arrecadado pelas linhas no mês escolhido:')
    valor_arrecadado_por_linha = prel.total_arrecadado(dados, 10, 2020)
    for elementos in valor_arrecadado_por_linha:    
        for linha, valor in elementos.items():
            print(f'\n{linha}: {valor}')
    print('\n---------Percentual de Passagens no mês escolhido----------')        
    print(f'Estudantes: {prel.percentual_estudantes(dados, mes, ano):.2f}%')
    print(f'Gratuidades: {prel.percentual_gratuidades(dados, mes, ano):.2f}%')
    print('\n------------------Ocupação Média Semanal-------------------')
    print(prel.exibir_matriz_ocupacao(prel.gerar_matriz_ocupacao(prel.ocupacao_media_semanal(dados))))

elif forma_de_gerar == 2:
    #gerando arquivo de texto
    with open('relatorio.txt', 'w+') as file:
        file.write('\n------------------------RELATÓRIO---------------------------')
        file.write('\nValor arrecadado pelas linhas:')
        valor_arrecadado_por_linha = prel.total_arrecadado(dados, 10, 2020)
        for elementos in valor_arrecadado_por_linha:    
            for linha, valor in elementos.items():
                file.write(f'\n{linha}: {valor}')
        file.write('\n---------Percentual de Passagens no mês escolhido----------')
        file.write(f'\nEstudantes: {prel.percentual_estudantes(dados, mes, ano):.2f}%')
        file.write(f'\nGratuidades: {prel.percentual_gratuidades(dados, mes, ano):.2f}%')
        file.write('\n------------------Ocupação Média Semanal-------------------')
        matriz = prel.gerar_matriz_ocupacao(prel.ocupacao_media_semanal(dados))
        for linha in matriz:
            file.write(f'\n{linha}')

        file.seek(0)      