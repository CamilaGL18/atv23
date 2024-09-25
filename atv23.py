# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.
def tabuada():
    try:
        numero = int(input("Digite um número para ver a tabuada: "))
        
        print(f"\nTabuada do {numero}:\n")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

tabuada()