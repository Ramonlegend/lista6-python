# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 20/05/2024
# Descrição: Determinar o tamanho do arquivo mensagem.txt e criar uma lista de palavras a partir dele
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")
import os

# a) Determining the size of the file mensagem.txt
file_path = "mensagem.txt"
file_size = os.path.getsize(file_path)
print(f"Tamanho do arquivo mensagem.txt is {file_size} bytes.")

# b) Creating a list of words from the file mensagem.txt
with open(file_path, "r") as file:
  words = file.read().split()
print(f"Lista de palavras do arquivo mensagem.txt is: {words}")