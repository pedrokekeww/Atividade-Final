#Nome: Pedro Vinicius Ernesto Barbosa
#Curso: P2 Informática
#Prof.: Allan Kelvin
bus = {1: 'sim', 2: 'sim', 3: 'sim', 4: 'sim', 5: 'sim'}
lugar = 0
print("======= SISTEMA DE RESERVA =======")
while True:
  if bus == {}:
    print("Todos os lugares estão ocupados")
    break
  print(f'Assentos disponiveis - {list(bus.keys())}')
  lugar = int(input("Deseja reservar qual assento?\n"))
  print("-"*30)
  if lugar not in bus:
     print("Assento indisponível / Já está ocupado\n")
  else:
    del bus[lugar]
    print(f"Assento {lugar} reservado com sucesso!\n")
print("FIM")
