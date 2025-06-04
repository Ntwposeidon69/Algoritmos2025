
import os

tamanho = 0 
while(tamanho <= 5):

    usuario = input("Informe seu usuário de E-mail sem o @: ")
    tamanho = len(usuario)
    if (tamanho <= 5):
        print("Informe um email maior que 5 caracteres")

if (tamanho > 5 ):
    print("Qual seu E-mail")
    print("1 - @ifpr.edu.br")
    print("2 - @gmail.com")
    print("3 - @hotmail.com")
    print("4 - Outras")

    opcao = int(input("Digite a opção desejada: "))

    if (opcao == 1):
        email = usuario + "@ifpr.edu.br"

    elif (opcao == 2):
         email = usuario + "@gmail.com"
        
    elif (opcao == 3):
         email = usuario + "@hotmail.com"

    else: 
        provedor = ""
        while(not("@" in provedor and ".com" in provedor)):
            provedor = input("Digite seu provedor de E-mail")
        email = usuario + provedor

print(f"Seu e-mail é: {email}")

msg_commit = input("Digite sua mensagem de commit: ")
while (len (msg_commit) <= 10 ):
    print("Detalhe mais sua mensagem!")
    msg_commit = input("Mensagem do Commit: ")

c = f"git config user.email \"{email}\""

os.system(c)

c = f"git add *"
os.system(c)

c = f"git commit -m \"{msg_commit}\""
os.system(c)


c = "git push"
os.system(c)


