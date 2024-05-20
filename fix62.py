# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 20/05/2024
# Descrição: Cadastro de senhas
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

# Open the file in append mode
with open('senha.txt', 'a') as file:
  # Prompt the user to enter 5 passwords
  for _ in range(5):
    password = input("Enter a password: ")
    # Write the password to the file
    file.write(password + '\n')

print("Passwords added successfully!")