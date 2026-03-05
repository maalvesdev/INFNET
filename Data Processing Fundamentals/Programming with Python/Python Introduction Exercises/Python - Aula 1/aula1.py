#0. Tranforme 130 minutos em H:M
tempo = 130
print("Horas:", tempo//60, "Minutos:", tempo%60)


#1. Calcule a média de três notas (7.5, 8.0, 6.5)
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
media = (nota1+nota2+nota3) / 3
print(media)


#2. Mostrar a palavra 'programa' sem a primeira e a última letra
texto = "programa"
print(texto[1:-1])


#3. Concatenar partes de uma string "abcdefghij"
# primeiras letras
# últimas letras
texto = "abcdefghij"
print(texto[:3], texto[-2:])


#4. Mostrar o nome completo juntando nome e sobrenome
#Nome: Ana
#Sobrenome: Silva
nome = "Ana"
sobrenome = "Silva"
print(nome,sobrenome)


#5. Simule censura de parte da frase com asteriscos
#frase = "Esse conteúdo é secreto"
#Trocar "conteúdo" por "*" por exemplo
frase = "Esse conteúdo é secreto"
censura = "*"
print(frase[:5], censura, frase[-10:])


#6. Crie um padrão alternando fatias diferentes
a = "abcd"
b = "1234"
#Saída esperada: "a1b2c3d4"
print(a[0]+b[0]+a[1]+b[1]+a[2]+b[2]+a[3]+b[3])


#7. Verificar se a soma de dois números é par
a = 8
b = 4
soma = a + b
print(soma%2)


#8. calculo do IMC
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura*altura)
print(imc)


#9. Transforme de celsius para fahrenheit
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius*9/5) + 32
print(fahrenheit)
