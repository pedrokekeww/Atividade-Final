# Nome: Pedro Vinicius Ernesto Barbosa
# Curso: P2 InformC!tica
# Prof.: Allan Kelvin
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
    if len(temps) < 10:
        True
    else:
        break
tempmedia = sum(temps) / len(temps)
for temperaturas in temps:
    if temperaturas < tempmedia:
        abaixodamedia.append(temperaturas)

print(f"maior temperatura: {max(temps)}")
print(f"menor temperatura: {min(temps)}")
print(f"temperatura mC)dia: {tempmedia}")
print(f"dias com temperaturas abaixo da mC)dia: {len(abaixodamedia)}")
