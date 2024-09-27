#Nome: Pedro Vinicius Ernesto Barbosa
#Curso: P2 Informática
#Prof.: Allan Kelvin
#Obs: Use o comando "python main.py" para executar o programa no Shell
#Unico jeito q consegui fazer essas comparações entre maior ou menor, desculpa se ta feio
temps = []
abaixodamedia = []
while True:
  for i in range(10):
    temperaturas = int(input(f"Entre com a {i+1}a temperatura: "))
    if temperaturas < 15:
      print("erro")
      break
    elif temperaturas > 40:
      print("erro")
      break
    else:
      temps.append(temperaturas)
  break
tempmedia = sum(temps) / len(temps)
for temperaturas in temps:
  if temperaturas < tempmedia:
    abaixodamedia.append(temperaturas)
    
print(f"maior temperatura: {max(temps)}")
print(f"menor temperatura: {min(temps)}")
print(f"temperatura média: {tempmedia}")
print(f"dias com temperaturas abaixo da média: {len(abaixodamedia)}")
