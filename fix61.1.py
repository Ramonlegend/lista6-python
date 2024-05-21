# RA: 1051392411014
# Nome aluno: Ramon Godinho
# Data: 20/05/2024
# Descrição: Cadastro de emails
print("RA: 1051392411014, Nome: Ramon Godinho, Turma: 1 semestre DSM ")

# Register 3 email addresses
with open('email.txt', 'a') as file:
  emails = []
  for i in range(3):
    email = input("Enter an email address: ")
    emails.append(email)
    file.write(email + '\n')

print("Email addresses registered:")
for email in emails:
  print(email)