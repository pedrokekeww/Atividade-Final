#Nome: Pedro Vinicius Ernesto Barbosa
#Curso: P2 Informática
#Prof.: Allan Kelvin
idade = 0
cargo = ()
funcionarios = {}
func = {}
cargo_busca = ()
def adicionar_funcionario(funcionarios):
  nome = input("Digite o nome do funcionário: ")
  idade = int(input("Digite a idade do funcionário: "))
  cargo = input("Digite o cargo do funcionário: ")
  funcionarios[nome] = {"idade": idade, "cargo": cargo}
  print("Funcionário adicionado com sucesso!")
  return funcionarios
  
def listar_funcionarios(funcionarios):
  print(funcionarios)
  
def buscar_por_cargo(funcionarios, cargo_busca):
  cargo_busca = input("Digite o cargo que deseja buscar: ")
  encontrados = []
  for nome, dados in funcionarios.items():
    if dados['cargo'].lower() == cargo_busca.lower(): 
        encontrados.append(nome)
  print(f"Funcionários com o cargo {cargo_busca}-:")
  print(encontrados)
print("===== SISTEMA DE CADASTRO DE FUNCIONÁRIOS =====\n")
print("Escolha uma opção:")
while True:
  opcoes = int(input("1-Adicionar funcionário, 2-Listar funcionários, 3-Buscar funcionário por cargo, 4-Sair\n"))
  if opcoes == 1:
    adicionar_funcionario(funcionarios)
  elif opcoes == 2:
    listar_funcionarios(funcionarios)
  elif opcoes == 3:
    buscar_por_cargo(funcionarios, cargo_busca)
  elif opcoes == 4:
    print("Saindo do sistema...")
    break
  else:
    print("Opção inválida. Tente novamente.")
