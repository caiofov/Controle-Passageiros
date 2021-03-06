Dos aquivos aqui anexados, os únicos que devem ser utilizados pelo usuário são menu.py e relatorio.py, todos os demais
são os códigos fonte do programa, e devem ser mantidos intocados.

Abaixo segue uma breve documentação das atuais funcionalidades do programa:



O programa, consistem em funções relacionadas à reserva de assentos e cadastro de linhas e funções auxiliares.

insere_linha(
    nome_linha : str, origem : str, 
    destino : str, primeiro_horario : int, 
    periodo: int, duracao_da_viagem : int,
    passagem : float, quantidade_de_assentos : int
                ):

Recebe as informações da linha a ser criada, nome, origem/destino, horário da primeira
saída, de quanto em quanto tempo passa, quanto tempo dura a viagem,  preço da passagem e quantidade de assentos.
Como a função altera o banco de dados de linhas, o propósito é que só seja utilizada por administradores.

altera_linha(nome_linha : str, destino: str, parametro : str, novo_valor):

Essa função altera dados de uma linha específica, diretamente no banco de dados. Assim, é uma
função a ser utilizada por administradores ou por outras funções.


checa_linha(destino : str)

Com o input apenas do destino, essa função fornece ao usuário informações sobre as linhas
disponiveis a um determinado destino, e desencadeia as funções responsáveis por realizar 
as reservas.


>> assentos_disponiveis(linha : dict, data_partida : str, hora_partida : str) <<

- Objetivo: Achar os assentos disponíveis de uma determinada linha em uma certa data e hora.
- Parâmetros: Linha (para obter os assentos disponiveis), data e hora.
- Retorno: Para obter os assentos disponíveis, basta chamar "assentos_disponiveis(linha,data,horario)[0]". Precisa do índice "[0]" pois ela retorna uma lista: o primeiro elemento é uma lista com os assentos disponiveis (que é o objetivo da função) e o segundo elemento é a variável "index" que será usada apenas pela função "reservar_assento".

> Passo a passo:
- Primeiro, adiciona todos os assentos da matriz padrão da linha na lista de disponiveis. Após isso, irá verificar se há reservas na linha para o horário e data recebido como parâmetro.
- Se sim, irá remover todos os assentos na lista de reservado da lista de disponiveis.
- Se não, irá adicionar um novo dicionário de reserva na lista de reservas da linha.
- Então, efetuará o retorno.


>> linhas_disponiveis(lista_linhas : list) <<

- Objetivo: Achar as linhas disponíveis para um certo destino, ponto de partida, data e hora.
- Parâmetros: Lista de linhas existentes para um certo destino (gerada pela função checa_linha)
- Retorno: Não possui.

> Passo a passo:
- Apesar de possuir apenas um parâmetro, irá pedir ao usuário o ponto de partida (usando a função "input_ponto"), data (utilizando a função "input_data") e horário (utilizando a função "input_horario") para a exibição das linhas disponíveis seguindo esses dados. Juntamente  ao nome de cada linha, irá exibir os assentos disponíveis em cada uma, usando a função "assentos_disponiveis".

- Após cumprir seu objetivo, irá perguntar ao usuário se deseja reservar (o input será recebido pela função "pergunta_sim_ou_nao"). Caso positivo, irá pedir ao usuário a linha na qual deseja efetuar a reserva usando a função "input_linha".

- Recebendo a linha, irá chamar a função "reservar_assento" para começar a reserva.




>> reservar_assento(linha : dict, data_partida : str, horario_partida : str, lista_linhas : list) <<
- Objetivo: Realizar a reserva de um assento.

- Parâmetros: Linha, data, horario, lista_linhas (a que foi usada na função "linhas_disponiveis" e foi gerada pela função "checa_linha".

- Retorno: Não possui.

> Passo a passo:
- Chama a função "assentos_disponiveis" para receber a lista dos assentos disponiveis e a variável "index" que será usada no futuro. Irá exibir ao usuário a lista dos assentos e pedir o input de qual assento ele quer reservar, nesse momneto, poderá ocorrer falhas** na reserva, que serão todas registradas em um arquivo de texto.

- Após o usuário escolher um assento e uma passagem válida, irá exibir uma mensagem de confirmação (o input será recebido pela função "pergunta_sim_ou_nao"):
 	
	- Caso a resposta seja "nao", irá registrar mais uma falha** e irá perguntar se o usuário quer recomeçar (também com a função "pergunta_sim_ou_nao"). Se sim, irá novamente usar a função "pergunta_sim_ou_nao" para identificar se irá querer um novo destino para a nova reserva. Se sim, irá pedir o destino e chamar a função "checa_linha". Se não, irá chamar a função "linhas_disponiveis".
	
	- Caso positivo, irá identificar os assentos adjacentes seguindos as regras de distanciamento do COVID-19 e então fazer as alterações necessárias no arquivo de texto que armazena as linhas. Após isso, irá perguntar ao usuário se desea realizar uma nova reserva (novamente a função "pergunta_sim_ou_nao"). Caso a resposta seja "sim", irá seguir o mesmo procedimento dito anteriormente (perguntar se deseja alterar o destino e etc).

**FALHAS:
1ª - Motivo: "Assento ocupado" -> assento existe na matriz padrão dos assentos mas não está na lista de disponíveis.

2ª - Motivo: "Assento inexistente" -> assento não existe na matriz padrão dos assentos.

3ª - Motivo: "Reserva nao confirmada" -> usuário não confirmou a efetuação da reserva.



def quantas_meias_por_linha(dados = list, nome_da_linha = str, mes_escolhido = int, ano = int):
 - objetivo: calcular quantas passagens meias foram vendidas em uma linha escolhida em um mês.
 - parâmetros: dados (arquivo de reservas feitas), nome da linha, mês escolhido e o ano.
 - retorno: quantidade de passagens meias vendidas. 

def quantas_inteiras_por_linha(dados = list, nome_da_linha = str, mes_escolhido = int, ano = int):
 - objetivo: calcular quantas passagens inteiras foram vendidas em uma linha escolhida em um mês.
 - parâmetros: dados (arquivo de reservas feitas), nome da linha, mês escolhido e o ano.
 - retorno: quantidade de passagens inteiras vendidas. 

def quantas_gratuitas_por_linha(dados = list, nome_da_linha = str, mes_escolhido = int, ano = int):
 - objetivo: calcular quantas passagens gratuitas foram vendidas em uma linha escolhida em um mês.
 - parâmetros: dados (arquivo de reservas feitas), nome da linha, mês escolhido e o ano.
 - retorno: quantidade de passagens gratuitas vendidas. 

def total_arrecadado(dados = list, mes_escolhido = int, ano = int):
 - objetivo: calcular valor total arrecadados por uma linhas num mês específico
 - parâmetros: dados (arquivo de reservas feitas), mês escolhido e o ano.
 - retorno: valor arrecadado por linha num mês

def quantas_meias_mes(dados = list, mes_escolhido = int, ano = int):
 - objetivo: calcular quantas passagens meias foram vendidas por todas as linhas em um mês.
 - parâmetros: dados (arquivo de reservas feitas), mês escolhido e o ano.
 - retorno: quantidade de passagens meias vendidas.

def quantas_inteiras_mes(dados = list, mes_escolhido = int, ano = int):
 - objetivo: calcular quantas passagens inteiras foram vendidas por todas as linhas em um mês.
 - parâmetros: dados (arquivo de reservas feitas), mês escolhido e o ano.
 - retorno: quantidade de passagens inteiras vendidas.

def quantas_gratuitas_mes(dados = list, mes_escolhido = int, ano = int):
 - objetivo: calcular quantas passagens gratuitas foram vendidas por todas as linhas em um mês.
 - parâmetros: dados (arquivo de reservas feitas), mês escolhido e o ano.
 - retorno: quantidade de passagens gratuitas vendidas. 

def total_de_passageiros(dados = list, mes_escolhido = int, ano = int):
 - objetivo: Calcular a quantidade total de passageiros de todas as linhas num mês específico.
 - parâmetros: dados (arquivo de reservas feitas), mês escolhido e o ano.
 - retorno: quantidade total de passageiros

def percentual_estudantes(dados = list, mes_escolhido = int, ano = int):
 - objetivo: Calcular o percentual de estudantes em todas as linhas num mês escolhido.
 - parâmetros: dados (arquivo de reservas feitas), mês escolhido e o ano.
 - retorno: percentual de estudantes.

def percentual_gratuidades(dados = list, mes_escolhido = int, ano = int):
 - objetivo: Calcular o percentual de gratuidades em todas as linhas num mês escolhido.
 - parâmetros: dados (arquivo de reservas feitas), mês escolhido e o ano.
 - retorno: percentual de gratuidades.

def input_data_dia_semana(data_input):
 - objetivo: transformar uma data string num objeto datetime.
 - parâmetros: data.
 - retorno: data em datetime.

def ocupacao_media_semanal(dados):
 - objetivo: Calcular a ocupação média por linha em porcentagem entre dias da semana que houveram reservas.
 - parâmetros: dados (arquivo de reservas feitas).
 - retorno: medias semanais de ocupação por linha em uma lista de dicionários. 

def gerar_matriz_ocupacao(medias_semanais = list):
 - objetivo: gerar a matriz com os dados oferecidos pela função "ocupacao_media_semanal".
 - parâmetros: lista de médias de ocupação semanal.
 - retorno: matriz de médias de ocupação semanal.

def exibir_matriz_ocupacao(matriz):
 - objetivo: printar cada linha da matriz em uma linha do terminal.
 - parâmetros: matriz gerada pela função "gerar_matriz_ocupacao".
 - retorno: não há

 
>> input_horario(str msg) << (função auxiliar do programa)

- Objetivo: Perguntar ao usuário um horário no formato hh:mm e retornar um método time com esse horário.
- Parâmetros: msg (para saber o que perguntar ao usuário quando for pedir o horário).
- Retorno: um método time da biblioteca datetime.

 > Passo a passo:
 - Pede o horário para o usuário e divide a resposta pelo ':' caso exista.
 - Tenta retornar um metodo time usando cada elemento respectivo da lista horário,
 se der erro, significa que o usuário deu um horário invalido, manda uma mensagem
 de erro e pede novamente por um horário, voltando para o início.

>> input_data(msg='Data: ', data_atual=datetime.now(), delta=15) << (função auxiliar do programa)
- Objetivo: perguntar ao usuário por uma data no formato dd/mm/yyyy ou dd/mm ou dd e retornar
um método datetime com essa data.
- Parâmetros: msg (mensagem para perguntar ao usuário por uma data), data_atual (para obter o
dia atual), delta (para saber o tempo máximo de agendamento).
- Retorno: um método datetime da biblioteca datetime

 > Passo a passo:
 - Pede uma data para o usuário e a divide pela '/' caso exista.
 - Tenta complementar com o mês atual ou o ano atual caso não tenham sido especificados.
 - Tenta transformar em datetime essa lista com as informações da data.
 - Checa se essa data é menor ou igual ao dia de hoje, se for não é válida pois não pode
 ter cadastramento no passado nem no mesmo dia.
 - Checa se essa data passa do período permitido de cadastramento.
 - Se passar por todas essas checagens e não der erro, retorna um método datetime com a data, se não,
 manda uma mensagem de erro, volta ao início do código e pede uma data novamente.

>> pergunta_sim_ou_nao(msg) << (função auxiliar do programa)
- Objetivo: perguntar ao usuário uma pergunta de sim e nao e retornar qual foi a resposta se for válida.
- Parâmetros: msg (Pergunta de sim ou não que será perguntada ao usuário)
- Retorno: uma string 'sim' ou 'nao'

 > Passo a passo:
 - cria um tradutor que tem as strings que podem ser respondidas pelo usuário e as atribui a resposta esperada
 - pergunta ao usuário uma pergunta de sim ou não, se a resposta tiver no dicionário criado, retorna a atribuição
 desta resposta ao dicionário, se não, responde uma mensagem de erro e recomeça o pedido de resposta.

>> remove_caracteres_especiais(palavra) << (função auxiliar do programa)
- Objetivo: substituir os caracteres especiais pela forma normal em uma string.
- Parâmetros: palavra (palavra que vai ser normalizada).
- Retorno: uma string sem caracteres especiais

 > Passo a passo:
 - retorna a função normalize da biblioteca unicodedata de forma a substituir os caracteres
especiais como á por a e ç por c.

>> input_ponto(lista_linhas, msg='Ponto: ', msg_de_erro='Nenhum ponto encontrado.')
- Objetivo: Perguntar ao usuário por um ponto de onibus e retornar esse ponto.
- Parâmetros: lista_linhas (lista de dicionários com listas válidas), msg (mensagem para ser perguntada ao
usuário), msg_de_erro (mensagem de erro caso seja inserido uma linha inválida)
- Retorno: string com o nome do ponto

 > Passo a passo:
 - cria set e coloca a origem da linha no set.
 - cria lista com os pontos normalizados do set.
 - faz o print dos pontos disponíveis
 - pede o ponto para o usuário e normaliza ele
 - se o ponto tiver inscrito na string do ponto dado pelo usuário, ele retorna o ponto

>> input_linha(dicionario_linhas, msg='Linha: ', msg_erro='Linha não encontrada.'):
- Objetivo: Perguntar ao usuário por uma linha de ônibus e retorna essa linha.
- Parâmetros: dicionario_linhas (lista de dicionários de linhas), msg (mensagem que vai ser 
perguntata ao usuário), msg_erro (mensagem dada caso seja dado uma linha inválida)
- Retorno: o dicionário da linha escolhida

 > Passo a passo:
 - Pergunta ao usuário por uma linha.
 - itera pela lista de linhas de normaliza o nome da linha do dicionário atual
 - divide o nome da linha em nome e número
 - checa se a resposta é igual ao nome inteiro da linha, ou ao número da linha ou aos pontos da linha,
 se sim, retorna o dicionário dessa linha, se não, manda mensagem de erro e recomeça o código.














