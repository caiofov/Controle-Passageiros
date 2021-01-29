import insere_linha as il
import math
import json
import datetime


'''
Nesse documento, o banco de dados foi preenchido com todos as linhas em questão, porém
caso deseje explorar a funcionalidade de criação de linhas, segue um exemplo que não consta atualmente
no banco de dados.
'''
il.insere_linha('Linha Fantasia', 'benfica', 'pici', 5, 30, 1, 2.5, 100)

'''
Caso queira, também é possivel apagar o aquivo teste.json, e executar esse código novamente.
Porém, é importante saber, que caso o arquivo teste.json seja reiniciado, todas as reservas
constantes nele serão apagadas, e para se aproveitar das funções que geram os relatórios das reservas
será preciso realizar manualmente novas reservas.

'''





passagem = 3.6
primeiro_horario = 6
periodo = 60
quantidade_assentos = 30


#porangabucu -> Pici
il.insere_linha('Borges de Melo II(032)', 'porangabucu', 'pici', primeiro_horario, periodo, 9, passagem, quantidade_assentos)
il.insere_linha('Francisco Sa/Parangaba(080)', 'porangabucu', 'pici', primeiro_horario, periodo, 8, passagem, quantidade_assentos)
#Pici -> porangabucu
il.insere_linha('Borges de Melo I(031)', 'pici', 'porangabucu', primeiro_horario, periodo, 12, passagem, quantidade_assentos)
il.insere_linha('Francisco Sa/Parangaba(080)', 'pici', 'porangabucu', primeiro_horario, periodo, 10, passagem, quantidade_assentos)
#Pici -> Benfica
il.insere_linha('Paupina/Pici(703)', 'pici', 'benfica', primeiro_horario, periodo, 12, passagem, quantidade_assentos)
il.insere_linha('Bezerra de Menezes/Washington Soares(855)', 'pici', 'benfica', primeiro_horario, periodo, 15, passagem, quantidade_assentos)
#Benfica -> Pici
il.insere_linha('Paupina/Pici(703)', 'benfica', 'pici', primeiro_horario, periodo, 12, passagem, quantidade_assentos)
il.insere_linha('Jovita Feitosa/Shopping Benfica(389)', 'benfica', 'pici', primeiro_horario, periodo, 11, passagem, quantidade_assentos)
il.insere_linha('Antonio Bezerra/Albert Sabin(088)', 'benfica', 'pici', primeiro_horario, periodo, 34, passagem, quantidade_assentos)
il.insere_linha('Campus do PICI/Unifor(075)', 'benfica', 'pici', primeiro_horario, periodo, 9, passagem, quantidade_assentos)
#Pici -> Labomar
il.insere_linha('Antonio Bezerra/Mucuripe(071)', 'pici', 'labomar', primeiro_horario, periodo, 47, passagem, quantidade_assentos)
il.insere_linha('Conjunto Ceará/Aldeota/Papicu(076)', 'pici', 'labomar', primeiro_horario, periodo, 41, passagem, quantidade_assentos)
#Labomar -> Pici
il.insere_linha('Conjunto Ceara/Aldeota/Papicu(076)', 'labomar', 'pici', primeiro_horario, periodo, 35, passagem, quantidade_assentos)
#Labomar -> Benfica
il.insere_linha('Parangaba/Mucuripe(077)', 'labomar', 'benfica', primeiro_horario, periodo, 25, passagem, quantidade_assentos)
#Benfica -> Labomar
il.insere_linha('Parangaba/Mucuripe(077)', 'benfica', 'labomar', primeiro_horario, periodo, 27, passagem, quantidade_assentos)
il.insere_linha('Parangaba/Nautico(029)', 'benfica', 'labomar', primeiro_horario, periodo, 36, passagem, quantidade_assentos)
#Benfica -> porangabucu
il.insere_linha('Granja Lisboa/Goiabeiras(754)', 'benfica', 'porangabucu', primeiro_horario, periodo, 5, passagem, quantidade_assentos)
il.insere_linha('Conjunto Ceara/Centro(709)', 'benfica', 'porangabucu', primeiro_horario, periodo, 4, passagem, quantidade_assentos)
il.insere_linha('Conjunto Ceara/Centro/2 Etapa(343)', 'benfica', 'porangabucu', primeiro_horario, periodo, 6, passagem, quantidade_assentos)
#porangabucu -> Benfica
il.insere_linha('Democrito Rocha(308)', 'porangabucu', 'benfica', primeiro_horario, periodo, 5, passagem, quantidade_assentos)
il.insere_linha('Conjunto Ceara/Centro(709)', 'porangabucu', 'benfica', primeiro_horario, periodo, 5, passagem, quantidade_assentos)
il.insere_linha('Jardim Jatoba/Centro(387)', 'porangabucu', 'benfica', primeiro_horario, periodo, 6, passagem, quantidade_assentos)
il.insere_linha('Conjunto Ceara/Bonsucesso/Centro(710)', 'porangabucu', 'benfica', primeiro_horario, periodo, 6, passagem, quantidade_assentos)
#porangabucu -> Labomar
il.insere_linha('Parangaba/Mucuripe(077)', 'porangabucu', 'labomar', primeiro_horario, periodo, 32, passagem, quantidade_assentos)
il.insere_linha('Parangaba/Nautico(029)', 'porangabucu', 'labomar', primeiro_horario, periodo, 42, passagem, quantidade_assentos)
#Labomar -> Parangabuçu
il.insere_linha('Parangaba/Mucuripe(77)', 'labomar', 'porangabucu', primeiro_horario, periodo, 32, passagem, quantidade_assentos)
