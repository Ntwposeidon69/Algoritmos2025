#cont = int(input("Digite um valor: "))
#for num in range (1, 11):
#    print(f"{cont} X {num} = {cont*num}")

numero = int (input("Digite um numero: "))
x = int(input("Digite o valor inicial X: "))
y = int(input("Digite o valor final Y: " ))

if x > y:
    print("O valor inicial (X) deve ser menor ou igual ao final (Y).")
else:
    print(f"\nTabuada do número {numero}, de {x} a {y}:\n")
    for i in range(x, y + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")