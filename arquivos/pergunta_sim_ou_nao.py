def pergunta_sim_ou_nao(msg):
  sim = 'sim'
  nao = 'nao'
  tradutor_sim_nao = {'sim':sim, 's':sim, 'si':sim, 'sm':sim,
                      'nao':nao, 'n':nao, 'não':nao, 'na':nao, 'no':nao}
  while True:
    resposta = (input(msg+' (sim/nao): ')).lower()
    if resposta in tradutor_sim_nao.keys():
      return tradutor_sim_nao[resposta]
    else:
      print('Resposta inválida, tente novamente.')