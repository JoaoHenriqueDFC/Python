# Escreva um programa que leia tres numeros e que imprima o maior e o menor

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

maior = max(a, b, c)

menor = min(a, b, c)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print("\n")

# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input("Digite o salário do funcionário: R$ "))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print(f"O aumento foi de: R$ {aumento:.2f}")
print(f"O novo salário será de: R$ {novo_salario: .2f}")
print("\n")

# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

distancia = float(input("Qual é a distância a viagem em km? "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"O preço da passagem será de: R$ {preco: .2f}")
print("\n")

# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero!"
else:
    resultado = "Operação inválida!"

print(f"O resultado da operação é: {resultado}")
print("\n")

# Escreva um programa para aprovar o empréstimo bancario para compra de uma casa. O programa deve perguntar o valor da casa a comprar, salário e R quantidade de anos pagar. O Valor da prestação mensal não pode ser superior a 30% do salário. Calcule O o valor da prestação como sendo O valor da casa comprar dlvidido pelo número de meses a pagar.

valor_casa = float(input("Digite o valor da casa a ser comprada: R$ "))

salario = float(input("Digite o seu salário mensal: R$ "))

anos = int(input("Em quantos anos você deseja pagar? "))

meses = anos * 12
prestacao = valor_casa / meses
limite_prestacao = salario * 0.30

if prestacao <= limite_prestacao:
    print(f"Empréstimo aprovado, a prestação mensal será de R$ {prestacao:.2f}.")
else:
    print(f"Empréstimo negado, a prestação de R$ {prestacao:.2f} excede 30% do seu salário, que é R$ {limite_prestacao:.2f}.")
