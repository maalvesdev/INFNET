#Exercício 1 — Contar vogais em uma frase Dada uma string, conte quantas vogais minúsculas (a, e, i, o, u) existem no texto.
frase = input("Digite uma frase: ").lower()
vogais = frase.count("a") + frase.count("e") + frase.count("i") + frase.count("o") + frase.count("u")
print("Quantidade de vogais:",vogais)

#Exercício 2 — Contar quantas vezes uma palavra aparece Dada uma frase e uma palavra, conte quantas vezes a palavra aparece na frase.
frase = input("Digite uma frase: ").lower()
palavra = input("Digite uma palavra: ").lower()
quantidade = frase.count(palavra)
print(f"A palavra aparece {quantidade} vezes")

#Exercício 3 — Verificar se uma palavra está na frase Leia uma frase e uma palavra e diga se ela aparece na frase. Mostre apenas o valor lógico (True ou False).
frase = input("Digite uma frase: ").lower()
palavra = input("Digite uma palavra: ").lower()
print(palavra in frase)

#Exercício 4 — Substituir todas as ocorrências de uma palavra Dada uma frase, troque uma palavra por outra. Exemplo: trocar "bolo" por "torta" na frase "eu gosto de bolo de chocolate".
frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra para substituir: ")
print(frase.replace(palavra, "pizza"))

#Exercício 5 — Contar quantos espaços existem em uma frase. Dada uma frase, conte quantos espaços em branco existem.
frase = input("Digite uma frase: ")
print(f"Quantidade de espaços: {frase.count(' ')}")

#Exercício 6 — Deixar só a primeira letra de cada palavra maiúscula Dada uma frase em letras minúsculas, transforme-a para o formato “Título”, com a primeira letra de cada palavra em maiúscula.
frase = input("Digite uma frase: ").title()
print(frase)

#Exercício 7 — Remover todos os espaços da frase Dada uma frase, crie uma nova string sem nenhum espaço.
frase = input("Digite uma frase: ")
print(frase.replace(" ",""))

#Exercício 8 — Quantidade de caracteres sem espaços. Dada uma frase, calcule quantos caracteres não são espaços. Use a ideia: tamanho total − quantidade de espaços.
frase = input("Digite uma frase: ")
print(len(frase) - frase.count(" "))

#Exercício 9 — Letras 'a' e proporção no texto Dada uma string, conte quantas letras "a" minúsculas existem e calcule a proporção em relação ao tamanho total do texto.
frase = input("Digite uma frase: ")
qntd_a = frase.count('a')
prop = frase.count('a') // len(frase)
#print(f"Quantidade de 'a': {frase.count('a')}\nProporção: {frase.count('a') // len(frase)}")
print(f"Quantiade de 'a': {qntd_a}\nProporção: {prop}")

#Exercício 10 — Formatar número de telefone. Dada uma string com 11 dígitos representando um celular no formato DDNNNNNNNNN, monte a versão formatada:
#Exemplo: Entrada: "21987654321" → Saída: "(21) 98765-4321"
numero = input("Digite um numero: ")[:11]
ddd = numero[:2]
num1 = numero[3:7]
num2 = numero[6:]
print(f"({ddd}) {num1}-{num2}")

#Exercício 11 — Formatar uma data (DDMMAAAA → DD/MM/AAAA) Dada uma string contendo uma data somente em números no formato "DDMMAAAA", transforme-a em "DD/MM/AAAA".
data = input("Digite uma data: ")[:8]
dia = data[:2]
mes = data[2:4]
ano = data[3:]
print(f"{dia}/{mes}/{ano}")

#Exercício 12 — Extrair usuário e domínio de um e‑mail. Dado um e-mail no formato "usuario@dominio.com", separe a parte antes e depois do "@", exibindo:
#Usuário: ... Domínio: ...
email = input("Digite seu e-mail: ")
usuario, dominio = email.split("@")
print(f"Usuário: {usuario}\nDomínio: {dominio}")

#Exercício 13 — Remover todas as vogais do texto. Peça ao usuário um texto e remova todas as vogais minúsculas (a, e, i, o, u). A nova string deve manter todos os outros caracteres.
frase = input("Digite uma frase: ")
#remove as vogais
remove_vogais = ( 
    frase.replace("a", "")
         .replace("e", "")
         .replace("i", "")
         .replace("o", "")
         .replace("u", "")
)

print(f"Frase sem vogais: {remove_vogais}")

#Exercício 14 — Criar um “bordão” com a primeira e última letra. Peça ao usuário uma palavra e construa uma nova string assim:
#primeira letra + (várias *) + última letra
#A quantidade de * deve ser igual a (tamanho da palavra − 2).
palavra = input("Digite uma palavra: ")
bordao = palavra[0] + "*" * (len(palavra) - 2) + palavra[-1]
print(bordao)

#Exercício 15 — Frase abreviada com a palavra do meio Peça ao usuário uma frase com 3 palavras e gere a forma abreviada:
#primeira (x.) terceira
#Onde x é a inicial da palavra do meio.
#Use apenas find() e fatiamento ([:]).
frase = input("Digite uma frase com 3 palavras: ")

espaco1 = frase.find(" ")
espaco2 = frase.find(" ", espaco1 + 1)

primeira = frase[:espaco1]
meio = frase[espaco1 + 1]
terceira = frase[espaco2 + 1:]

print(f"{primeira} ({meio}.) {terceira}")