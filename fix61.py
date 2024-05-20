# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 20/05/2024
# Descrição: Programa que calcula o IMC e verifica se o peso está ideal
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

def calcular_imc(peso, altura):
  imc = peso / (altura ** 2)
  return imc

def verificar_peso_ideal(imc, sexo):
  if sexo == 'M' or sexo == 'm':
    if imc < 20.7:
      return "Abaixo do peso"
    elif imc >= 20.7 and imc < 26.4:
      return "Peso normal"
    elif imc >= 26.4 and imc < 27.8:
      return "Marginalmente acima do peso"
    elif imc >= 27.8 and imc < 31.1:
      return "Acima do peso ideal"
    else:
      return "Obeso"
  elif sexo == 'F' or sexo == 'f':
    if imc < 19.1:
      return "Abaixo do peso"
    elif imc >= 19.1 and imc < 25.8:
      return "Peso normal"
    elif imc >= 25.8 and imc < 27.3:
      return "Marginalmente acima do peso"
    elif imc >= 27.3 and imc < 32.3:
      return "Acima do peso ideal"
    else:
      return "Obeso"
  else:
    return "Sexo inválido"

peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))
sexo = input("Digite o sexo (M/F): ")

imc = calcular_imc(peso, altura)
resultado = verificar_peso_ideal(imc, sexo)

print("IMC:", imc)
print("Resultado:", resultado)