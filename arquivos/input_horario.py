import datetime
def input_horario(msg='Horario: '):
    #hh:mm
    while True:
      horario = input(msg).split(':')
      try:
        return datetime.time(int(horario[0]), int(horario[1]))
      except ValueError:
        print('Horario invalido')
      except IndexError:
        print('Horario invalido')
      except TypeError:
        print('Horario invalido')