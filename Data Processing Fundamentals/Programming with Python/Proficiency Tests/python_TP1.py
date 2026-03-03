#==Exercício 1 - Importância da Programação e Comentários==
#No seu bloco de código Python no Deepnote, utilize o caractere `#` para escrever um comentário 
#explicativo sobre a importância da programação.

#A programação é importante porque permite criar tecnologias que facilitam tarefas do dia a dia e 
#resolvem problemas reais. Ela desenvolve o raciocínio lógico e o pensamento crítico. 
#Além disso, está presente em diversas áreas, ampliando oportunidades profissionais e 
#impulsionando a inovação tecnológica.


#==Exercício 2 - Processo de Escrita e Hello World==
#Escreva um programa no Deepnote que utilize a função `print()` para exibir a mensagem: 
#"Olá Mundo! Bem-vindo ao Cinema Digital".
print("Olá Mundo! Bem-vindo ao Cinema Digital")


#==Exercício 3 - Abordagem Programática e Atribuição==
#Declare uma variável chamada `disciplina` com o valor `""Python""` e uma variável chamada `turma` com o valor `101`. 
#Utilize dois comandos `print()` separados para exibir o conteúdo de cada variável no terminal.
disciplina = "Python"
turma = 101
print(disciplina)
print(turma)


#==Exercício 4 - Fluxo IPO: Entrada, Processamento e Saída==
#Crie um programa que siga o fluxo IPO:
#Entrada: Defina as variáveis `peso_unidade = 80` e `quantidade = 10`.
#Processamento: Crie a variável `peso_total` que multiplica o peso pela quantidade.
#Saída: Exiba o valor armazenado em `peso_total` usando o comando `print()`.
peso_unidade = 80
quantidade = 10
peso_total = peso_unidade * quantidade
print(peso_total)


#==Exercício 5 - Atribuição de Variáveis de Inventário==
#No Deepnote, atribua os seguintes valores: `quantidade_macas` recebe `150` e `preco_maca` recebe `5.99`. 
#Utilize a função `print()` para exibir primeiro a quantidade e depois o preço, em linhas separadas.
quantidade_macas = 150
preco_maca = 5.99
print(quantidade_macas)
print(preco_maca)


#==Exercício 6 - Tipos Básicos: Int e Float no Financeiro==
#Crie as variáveis `contratos = 12` e `faturamento = 2500.50`. Use a função `print()` 
#para exibir o tipo da variável `contratos` e o tipo da variável `faturamento` utilizando a função `type()`.
contratos = 12
faturamento = 2500.50
print(type(contratos),type(faturamento))


#==Exercício 7 - Tipos Básicos: Booleanos em Segurança==
#Crie uma variável chamada `sensor_ativo` e atribua a ela o valor booleano `True`. 
#Em seguida, exiba o valor da variável no terminal utilizando `print()`. 
#Altere seu valor para `False` e imprima novamente.
sensor_ativo = True
print(sensor_ativo)
sensor_ativo = False
print(sensor_ativo)


#==Exercício 8 - Operações Aritméticas: Soma de Receita
#Defina `venda_smartphones = 5400.00` e `venda_acessorios = 1250.50`. 
#Crie uma variável `receita_total` que realize a soma e exiba o resultado final.
venda_smartphones = 5400.00
venda_acessorios = 1250.50
receita_total = venda_smartphones + venda_acessorios
print(receita_total)


#==Exercício 9 - Operações de Subtração de Saldo==
#Crie as variáveis `saldo_atual = 10000` e `valor_fatura = 3500`. 
#Calcule o saldo restante e armazene em `saldo_final`. Exiba o valor de `saldo_final`.
saldo_atual = 10000
valor_fatura = 3500
saldo_final = saldo_atual - valor_fatura
print(saldo_final)


#==Exercício 10 - Multiplicação e Divisão de Preços==
#Defina `preco_fardo = 24.0` e `unidades = 6`. Calcule o `preco_unitario` e exiba o resultado.
preco_fardo = 24.0
unidades = 6
preco_unitario = preco_fardo / unidades
print(preco_unitario)


#==Exercício 11 - Otimização de Carga e Estabilidade de Frete==
#Com base na capacidade de 550kg e no peso unitário de 65kg, desenvolva um código que 
#calcule o número máximo de sacas que podem ser embarcadas em um caminhão sem exceder o limite
#bem como a porcentagem de ocupação do peso do caminhão.
#O resultado deve ser armazenado em uma variável que represente a capacidade real
#e outra com a porcentagem, ambas exibidas no console.
capacidade_caminhao = 550
peso_unitario = 65
numero_sacas = capacidade_caminhao // peso_unitario
porcentagem_ocupacao = (numero_sacas * peso_unitario) / capacidade_caminhao * 100
print(numero_sacas)
print(porcentagem_ocupacao)


#==Exercício 12 - Sincronização de Turnos e Manutenção Preventiva==
#Considerando o total de 125 dias decorridos e a periodicidade de 8 dias, escreva um programa que 
#determine a fase atual da operação dentro do ciclo e com quantos dias decorridos ao todo poderemos 
#ter a parada técnica. Exiba com duas variáveis o valor resultante que indica o dia atual do ciclo e 
#a quantidade total de dias decorridos até a parada.
total_dias = 125
periodicidade = 8
dia_atual = total_dias % periodicidade
dias_parada = periodicidade - dia_atual
print(dia_atual)
print(dias_parada)


#==Exercício 13 - Engenharia Reversa de Tributação e Logística
#Defina os valores para custo base (2500), alíquota (0.05) e suporte (150). Calcule, em apenas uma 
#linha utilizando parênteses, o valor final que o cliente deverá pagar, garantindo que a ordem das 
#operações respeite a regra de negócio descrita. Exiba o total final.
custo_base = 2500
aliquota = 0.05
suporte = 150
valor_final = (custo_base * aliquota) + custo_base + suporte
print(valor_final)


#==Exercício 14 - Auditoria de Desempenho e Eficiência de Ativos
#Crie um sistema que receba o registro de 345 minutos e realize a transformação para a grandeza de horas decimais. 
#O resultado deve refletir a fração exata do tempo de uso para que o custo por hora seja aplicado posteriormente. 
#Exiba o valor convertido.
minutos = 345
print(minutos / 60)


#==Exercício 15 - Telemetria Aeroespacial e Autonomia de Voo==
#A partir do tempo de ambos os voos, desenvolva o raciocínio lógico para converter o total integralmente para 
#a unidade de segundos, e obter quanto de energia foi gasto nos voos. Em seguida, considere a margem de segurança 
#e armazene o resultado final em uma variável apropriada e exiba no terminal.
#Dados dos voos
voo1_horas = 3.77
voo2_minutos = 214

#Conversão para segundos
voo1_segundos = voo1_horas * 3600
voo2_segundos = voo2_minutos * 60

#Tempo total em segundos
tempo_total_segundos = voo1_segundos + voo2_segundos

#Consumo de energia (2,7 joules por segundo)
energia_gasta = tempo_total_segundos * 2.7

#15% de margem de segurança
energia_total = energia_gasta * 1.15

print("Tempo total em segundos:", tempo_total_segundos)
print("Energia total:", energia_total)


#==Exercício 16 Decomposição de Jornada para Fechamento de Folha==
#A partir do total de 1527 minutos, calcule a quantidade de horas inteiras trabalhadas 
#e a quantidade de minutos restantes. Em seguida calcule o valor total referente às horas
#e o valor total referente aos minutos excedentes.
#total de minutos
total_minutos = 1527

#valores do contrato
valor_hora = 60.00
valor_minuto = 1.20

#separação do tempo
horas_completas = total_minutos // 60
minutos_excedentes = total_minutos % 60

#cálculos de pagamento
pagamento_horas = horas_completas * valor_hora
pagamento_minutos = minutos_excedentes * valor_minuto
valor_total = pagamento_horas + pagamento_minutos

print("Horas completas:", horas_completas, "Minutos excedentes:", minutos_excedentes)
print("Valor total:", valor_total)
