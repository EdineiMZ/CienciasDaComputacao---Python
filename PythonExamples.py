#Servidor do Discord
# https://www.discord.gg/4tYjBsnZ7a

#importação das bibliotecas utilizadas
import random
import time
import requests
import sqlite3

#mensagem de boas vindas
print("Hello Word!!!")

#Exemplos de utilização

def exemplo1(): #Exemplo de IF ELSE ELIF
    numero = random.randint(0, 300) #define na variavel numero um valor randomico entre 0 e 300
    if numero <= 50: #verifica se o numero é menor ou igual a 50
        print("O numero selecionado é: ", numero, " ele é menor ou igual a 50.")
    elif numero >= 51 and numero <= 100: #verifica se o numero é maior que 50 e menor que 100
        print("O numero selecionado é", numero, "e ele esta entre 51 e 100")
    else:
        print("Numero maior que 100", numero)


def exemplo2(): #Exemplo do While (Enquanto) para encontrar uma chave
    chave = random.randint(0, 50) #Dev=fine o valor da chave de segurança
    numero = 0
    print("Chave definida", chave)
    while numero != chave: #define que enquanto o numero for direfente da chave, imprime valor incoreto
        print("Valor Incoreto")
        time.sleep(0.2)
        numero = random.randint(0, 50)
    print("Chave encontrada", numero)

#EXERCICIOS


#	O sistema de avaliação de determinada disciplina é composto por três provas.
#	A primeira prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5.
#	Considerando que a média para aprovação é 7.0.
#	Construa um algoritmo para calcular a média final de um aluno desta disciplina e dizer se o aluno foi aprovado ou não.
#	Lembre-se que essa é uma média ponderada e não uma média aritmética
def atv1():
    prv1 = round(random.uniform(0, 10), 2)*2
    prv2 = round(random.uniform(0, 10), 2)*3
    prv3 = round(random.uniform(0, 10), 2)*5
    notaFinal = (prv1 + prv2 + prv3)/10
    media = f"{notaFinal:.2f}"

    if notaFinal >= 7:
        print("Aluno aprovado com media", media)
    else:
        print("Aluno precisa fazer a recuperação total. Sua media ficou", media)

#Elabore um algoritmo que indique se um número digitado está compreendido entre 20 e 90, ou não
def atv2():
    numero = random.randint(0, 150) #define na variavel numero um valor randomico entre 0 e 150
    if numero <= 19: #verifica se o numero é menor ou igual a 50
        print("Numero menor que 20:", numero)
    elif numero >= 20 and numero <= 90: #verifica se o numero é maior ou igual a 50 e menor ou igual a 90
        print("O numero selecionado é", numero, "e ele esta entre 20 e 90")
    else:
        print("Numero maior que 90:", numero)

#Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00;
#Caso contrário, o lucro será de 30%. Elabore um algoritmo que leia o valor do produto.
#Calcule e imprima o valor de venda do produto.
def atv3():
    valorCompra = round(random.uniform(0, 50), 2)
    if valorCompra <= 20:
        valorVenda = valorCompra+((valorCompra*40)/100)
        vendaFormat = f"{valorVenda:.2f}"
        print("Será vendido com um lucro de 40% pois o valor da venda foi de R$", valorCompra, " saindo com um total  R$", vendaFormat)
    else:
        valorVenda = valorCompra + ((valorCompra * 30) / 100)
        vendaFormat = f"{valorVenda:.2f}"
        print("Será vendido com um lucro de 30% pois o valor da venda foi de R$", valorCompra, " saindo com um total  R$", vendaFormat)

#Segundo uma tabela médica, o peso ideal está relacionado com a altura e o sexo.
#Elabore um algoritmo que leia a altura e o sexo de uma pessoa (M/F), calcule e imprima seu peso ideal, utilizando as seguintes fórmulas.
def atv4():
    SexosPos = ['M', 'F']
    sexo =random.choice(SexosPos)
    Altura = round(random.uniform(100, 200), 2)

    if sexo == 'M':
        Peso = ((72.7 * Altura) - 58) / 100
        PesoIdeal = f"{Peso:.2f}"
        print("O peso ideal para um homem como voce é", PesoIdeal)
    elif sexo == 'F':
        Peso = ((62.1 * Altura) - 44.7) / 100
        PesoIdeal = f"{Peso:.2f}"
        print("O peso ideal para uma garota como voce é:", PesoIdeal)
    else:
        print("Algo deu errado! Voce informou o valor correto?")

#Elabore um algoritmo para testar se uma senha digitada é igual a “Patinho Feio”.
#Se a senha estiver correta mostre a mensagem “Acesso permitido”
#Do contrário mostre a mensagem “Você não tem acesso ao sistema”.
def atv5():
    senha = 'Patinho Feio'
    userpass = input("Digite a senha: ")

    if userpass == senha:
        print("Acesso autorizado! Bem vindo de volta!")
    else:
        print("Acesso Negado! Atividade suspeita detectada.")

#Elabore um algoritmo que leia dois números inteiros e efetue a sua adição.
#Caso a soma seja maior ou igual a 10, mostre a soma na tela, caso contrário informe que a soma é menor que dez.
def atv6():
    numero1 = random.randint(0, 10)
    numero2 = random.randint(0, 10)
    Resultado = numero2 + numero1
    if Resultado >= 10:
        print("Valor maior que 10: ", Resultado)
    else:
        print("Valor menor que 10")

#Desenvolva um algoritmo que classifique um número de entrada fornecido pelo usuário como PAR ou ÍMPAR.
def atv7():
    numero = random.randint(1, 30000000)
    ParImpar = numero%2
    if ParImpar == 0:
        print("Par", numero)
    else:
        print("Impar", numero)

#Elabore um algoritmo que leia um número e imprima uma das mensagens: é múltiplo de 3, ou, não é múltiplo de 3.
def atv8():
    numero = random.randint(1, 30000000)
    Multiplo = numero % 3
    if Multiplo == 0:
        print("Multiplo de 3", numero)
    else:
        print("Não é multiplo de 3", numero)

#Elabore um algoritmo que leia dois números e responda se a divisão do primeiro pelo segundo é exata (o resto da divisão deve ser igual a 0).
#Se for, o algoritmo deve imprimir a mensagem “A divisão de (1º numero) por (2º número) é exata”.
def atv9():
    numero = random.randint(0, 100)
    numero2 = random.randint(0, 100)
    divisao = numero % numero2
    if divisao != 0 :
        print("A divisão não é exata")
    else:
        print("A Divisão do numero", numero, "pelo numero", numero2, "é exata")

#Elabore um algoritmo que leia o nome e o peso de duas pessoas e imprima os dados da pessoa mais pesada. Os pesos delas serão diferentes.
def atv10():
    nomeP1 = input("Insira seu nome: ")
    peso1 = round(random.uniform(10, 150), 3)
    nomeP2 = input("Insira seu nome Pessoa 2: ")
    peso2 = round(random.uniform(10, 150), 3)
    if peso1 > peso2:
        print("A(o)", nomeP1, "é mais pesada que a(o)", nomeP2, "pesando", peso1, ".", nomeP2, "pesa", peso2)
    else:
        print("A(o)", nomeP2, "é mais pesada que a(o)", nomeP1, "pesando", peso2, ".", nomeP1, "pesa", peso1)

#	Elabore um algoritmo que leia dois números inteiros e imprima qual é maior, qual é menor, ou se os dois números são iguais.
def atv11():
    numero = random.randint(0, 10)  # define na variavel numero um valor randomico entre 0 e 150
    numero2 = random.randint(0, 10)  # define na variavel numero um valor randomico entre 0 e 150
    if numero > numero2:
        print("O numero 1:", numero, "é maior que o numero 2:", numero2,"!")
    elif numero == numero2:
        print("O numero 1:", numero, "é igual ao numero 2:", numero2, "!")
    else:
        print("O numero 1:", numero, "é menor que o numero 2:", numero2, "!")

#Uma empresa decidiu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:
def atv12():
    salario = round(random.uniform(-500, 5000), 2)
    print("Seu salário é de: R$", salario)
    if salario <= 0:
        print("Valor Invalido")
    elif salario <= 100:
        aumento = 25
    elif salario <= 2000:
        aumento = 20
    elif salario <= 3000:
        aumento = 15
    else:
        aumento = 10

    if salario > 0:
        print("O percentual de aumento do seu salário é de", aumento,"%")
        aumento = (salario * aumento) / 100
        novoSalario = f"{salario + aumento:.2f}"
        print("Seu salario sera de R$",novoSalario, "Com um aumento de R$",aumento)
    else:
        quit()

def atv13():
    numero = random.randint(0, 50000)
    divisao2 = numero % 2
    divisao3 = numero % 3
    divisao5 = numero % 5

    if divisao2 + divisao3 + divisao5 == 0:
        print("o numero", numero,"é divisivel por 2, 3 e 5")
    else:
        print("o numero", numero,"não é divisivel por 2, 3 e 5")

def TESTEAPI():
    response = requests.get('https://www.4devs.com.br/ferramentas.online.php',params={'acao': 'gerarnomes_produtos'})
    if response.status_code == 200:
        nome_produto = response.text
        print(nome_produto)
    else:
        print('Erro ao acessar')

def atv14():
    nomes_produtos = [
        'Computador', 'Tablet', 'Smartphone', 'Câmera', 'Fones de Ouvido',
        'Teclado', 'Mouse', 'Monitor', 'Impressora', 'Carregador',
        'Caixa de Som', 'Roteador', 'Cadeira', 'Mesa', 'Laptop',
        'Drone', 'Relógio', 'Headset', 'Microfone', 'Power Bank',
        'Geladeira', 'Liquidificador', 'Fogão', 'Aspirador de Pó',
        'Máquina de Lavar', 'Secador de Cabelo', 'Ventilador', 'Aparelho de Som',
        'Cafeteira', 'Panela Elétrica', 'Sanduicheira', 'Ferro de Passar',
        'Torradeira', 'Espremedor de Frutas', 'Freezer', 'Ar Condicionado',
        'Micro-ondas', 'Batedeira', 'Tábua de Passar', 'Fritadeira Elétrica',
        'Processador de Alimentos', 'Chuveiro Elétrico', 'Mixer', 'Cama',
        'Guarda-Roupa', 'Sofá', 'Escrivaninha', 'Estante', 'Cadeira de Escritório',
        'Poltrona', 'Mesa de Jantar', 'Cômoda', 'Criado-Mudo', 'Cortina',
        'Tapete', 'Lustre', 'Abajur', 'Persiana', 'Quadro Decorativo',
        'Moldura', 'Vaso Decorativo', 'Relógio de Parede', 'Espelho',
        'Almofada', 'Cesto de Roupa', 'Puff', 'Lixeira', 'Toalha de Banho',
        'Saboneteira', 'Porta Shampoo', 'Tapete de Banheiro', 'Cesto Organizador',
        'Porta-Retrato', 'Vela Aromática', 'Aromatizador de Ambiente', 'Jogo de Cama',
        'Colcha', 'Edredom', 'Travesseiro', 'Cobre-Leito', 'Lençol',
        'Almofada Decorativa', 'Protetor de Colchão', 'Manta', 'Capa de Almofada'
    ]
    valorProduto = round(random.uniform(0, 70), 2)
    if valorProduto < 10:
        lucro = 70
    elif valorProduto >= 10 and 30 > valorProduto:
        lucro = 50
    elif valorProduto >= 30 and valorProduto < 50:
        lucro = 40
    else:
        lucro = 30
    lucroVenda = valorProduto * lucro / 100
    produto = random.choice(nomes_produtos)
    print("O valor do produto", produto,"é de R$ ", valorProduto)
    print("Por isso a margem de lucro é de", f"{lucro:.2f}","%")
    print("Sendo vendido com um lucro de", f"{lucroVenda:.2f}")
    print("Totalizando um valor de", f"{lucroVenda + valorProduto:.2f}")

def exemplo3():
    numero = 1
    qtd = 0

    while numero <= 50000:
        divisao2 = numero % 2
        divisao3 = numero % 3
        divisao5 = numero % 5

        if divisao2 + divisao3 + divisao5 == 0:
            print("o numero", numero,"é divisivel por 2, 3 e 5")
            qtd = qtd + 1
        else:
            print("o numero", numero,"não é divisivel por 2, 3 e 5")

        numero = numero + 1
        print("Total", qtd)

def atv15():
    q1 = True
    q2 = True
    q3 = False

    if q1:
        print('A')
        if q2:
            print('B')
            print('C')
        elif q3:
            print('D')
        else:
            print('E')
    else:
        print('F')
    print('G')

def atv16():
    x = 30
    y = 5
    w = False
    z = False
    k = 'teste'
    if (x > y) and (w is False):
        print('A')
        if (k == 'teste') and (x <= 20):
            print('B')
    else:
        if (w == True):
            print('C')
        elif (z is True) or (k != 'teste'):
            print('D')
            print('E')
        else:
            print('F')
            print('G')
    print('H')

def atv17():
    salario = round(random.uniform(-500, 5000), 2)
    print("Seu salário é de: R$", salario)
    if salario <= 0:
        print("Valor Invalido")
    elif salario <= 2000:
        aumento = 10
    elif salario <= 3000:
        aumento = 20
    elif salario <= 4000:
        aumento = 25
    else:
        aumento = 30

    if salario > 0:
        print("O percentual do credito especial de seu salário é de", aumento,"%")
        aumento = (salario * aumento) / 100
        novoSalario = f"{salario + aumento:.2f}"
        print("Seu salario com crédito especial será de R$",novoSalario, "O valor do credito será de R$", f"{aumento:.2f}")
    else:
        quit()

def atv18():
    valor1 = round(random.uniform(-500, 50000), 2)
    valor2 = round(random.uniform(-500, 50000), 2)
    valor3 = round(random.uniform(-500, 50000), 2)
    print("Os valores selecionados foram: ", valor1 , valor2 , valor3)

    ordenacao = sorted([valor1, valor2, valor3], reverse=True)
    print("Os valores ordenados de forma decressente são: ", ordenacao)

def atv19():
    times_de_futebol = {
        "Real Madrid", "Barcelona", "Manchester United", "Liverpool", "Bayern de Munique",
        "Paris Saint-Germain", "Juventus", "Borussia Dortmund", "Chelsea", "Arsenal",
        "Flamengo", "Corinthians", "São Paulo", "Palmeiras", "Santos", "Vasco da Gama",
        "Grêmio", "Internacional", "Atlético Mineiro", "Cruzeiro", "Manchester City",
        "Tottenham", "AC Milan", "Inter de Milão", "Roma", "Napoli", "Lazio", "Benfica",
        "Porto", "Sporting Lisboa", "Ajax", "PSV Eindhoven", "Feyenoord", "Boca Juniors",
        "River Plate", "Racing Club", "América de Cali", "Club América", "Seattle Sounders",
        "LA Galaxy", "New York City FC", "Toronto FC", "Bayer Leverkusen", "RB Leipzig",
        "Wolfsburg", "Schalke 04", "Hamburger SV", "Eintracht Frankfurt", "Atalanta",
        "Lyon", "Marseille", "Monaco", "Bordeaux", "PSG", "Celtic", "Rangers", "Fulham",
        "West Ham United", "Leicester City", "Everton", "Ajax", "Feyenoord",
        "PSV Eindhoven"
    }

    time_sorteado1 = random.choice(list(times_de_futebol))
    time_sorteado2 = random.choice(list(times_de_futebol))
    numeroGolsTime1 = random.randint(0, 5)
    numeroGolsTime2 = random.randint(0, 5)

    if numeroGolsTime1 or numeroGolsTime2 < 0:
        print("Valor invalido para o numero de gols")
    else:

        if numeroGolsTime1 > numeroGolsTime2:
            print("Time ", time_sorteado2, "perdeu com", numeroGolsTime1, "gols para o time ", time_sorteado1, "com ", numeroGolsTime2, "gols")
        elif numeroGolsTime1 == numeroGolsTime2:
            print("Time ", time_sorteado1, "empatou com o time ", time_sorteado2, " com ", numeroGolsTime2)
        else:
            print("Time ", time_sorteado1, "perdeu com", numeroGolsTime1, "gols para o time ", time_sorteado2, "com ", numeroGolsTime2, "gols")

def atv20():
    idade = random.randint(0, 100)
    if idade <= 12:
        print("Criaça com", idade, "anos de idade")
    elif idade >12 and idade <= 18:
        print("Adolecente com", idade, "anos de idade")
    elif idade > 18 and idade <=60:
        print("Adulto com", idade, "anos de idade")
    else:
        print("Idoso com", idade, "anos de idade")

def exemplo4():
    Times = input("Digite nomes de times separados por virgulas: ")
    time1, time2 = Times.split(',')

    time1 = time1.strip()
    time2 = time2.strip()

    print("Time 1", time1)
    print("Time 2", time2)

def atv21():
    equilatero = 0
    isosceles = 0
    escaleno = 0
    while equilatero == 0:
        lado1 = random.randint(1, 50)
        lado2 = random.randint(1, 50)
        lado3 = random.randint(1, 50)

        if lado1 < lado2 + lado3 or lado2 < lado1 + lado3 or lado3 < lado1 + lado2:
            print("É um triangulo com as medidas", lado1, lado2, lado3)
            if lado1 == lado2 == lado3:
                print("Equilatero")
                equilatero = equilatero + 1
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print("Isosceles")
                isosceles = isosceles + 1
            else:
                print("Escaleno")
                escaleno = escaleno + 1
        else:
            print("Valores Invalidos", lado1, lado2, lado3)
    print("Isosceles", isosceles, "Escaleno", escaleno, "Equilateros", equilatero)

def exemplo5():
    numeros = input(f"Digite numeros separados por virgulas: ")
    numerosstr = numeros.split(',')
    numeros1= int(numerosstr[0])
    numeros2 = int(numerosstr[1])
    print(numeros1 + numeros2)

def atv22():
    numeros = input(f"Digite nomes de times separados por virgulas: ")
    numerosstr = numeros.split(',')
    numeros1= int(numerosstr[0])
    numeros2 = int(numerosstr[1])

    print("########################################################################")
    print("#                                                                      #")
    print("#                Informe uma das seguintes opções                      #")
    print("#                   1) Media entre os valores                          #")
    print("#          2) Diferença Maior pelo menor se fores diferentes           #")
    print("#                      3) Sair do Programa                             #")
    print("#                                                                      #")
    print("########################################################################")
    opcao = int(input(f"Informe a opção desejada: "))
    if opcao == 1:
        resposta = (numeros2 + numeros1) / 2
        print("A média entre os valores é de", resposta)
    elif opcao == 2:
        if numeros1 > numeros2:
            resposta = numeros1 - numeros2
            print("A Diferença entre eles é de", resposta)
        else:
            resposta = numeros2 - numeros1
            print("A Diferença entre eles é de", resposta)
    elif opcao == 3:
        print("Saindo do Programa...")
    else:
        print("Opção Inválida")

def atv23():
    trabalho1 = float(input("Informe a nota do Trabalho 1: "))
    prova1 = float(input("Informe a nota da Prova 1: "))
    prova2 = float(input("Informe a nota da Prova 2: "))
    trabalhos_individuais = float(input("Informe a nota dos Trabalhos Individuais: "))
    atividades_ensino_extensao = float(input("Informe a nota das Atividades de Ensino e Extensão: "))
    frequencia = float(input("Informe a frequência do acadêmico em %: "))

    media = (trabalho1 * 0.25) + (prova1 * 0.25) + (prova2 * 0.30) + (trabalhos_individuais * 0.10) + (
                atividades_ensino_extensao * 0.10)

    if frequencia >= 75:
        situacaoF = "Aprovado na frequência"
    else:
        situacaoF = "Reprovado por frequência"

    if media >= 7:
        situacaoM = "Aprovado em média"
    elif media < 4:
        situacaoM = "Reprovado por média"
    else:
        situacaoM = "Em A2"

    print("A média final do acadêmico é:", media)
    print("Situação:", situacaoM)
    print("Situação:", situacaoF)

def atv24():
    def eh_bissexto(ano):
        return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0
    def calcular_proximo_dia(dia, mes, ano):
        meses_30 = [4, 6, 9, 11]
        meses_31 = [1, 3, 5, 7, 8, 10, 12]
        # Verificar se o ano é bissexto
        bissexto = eh_bissexto(ano)
        # Validar se a data é válida
        if (mes < 1 or mes > 12 or
                (mes in meses_30 and dia > 30) or
                (mes in meses_31 and dia > 31) or
                (mes == 2 and ((bissexto and dia > 29) or (not bissexto and dia > 28)))):
            print("Data inválida!")
            return
        # Calcular o próximo dia
        if mes in meses_30:
            if dia == 30:
                dia = 1
                mes += 1
            else:
                dia += 1
        elif mes in meses_31:
            if dia == 31:
                if mes == 12:
                    dia = 1
                    mes = 1
                    ano += 1
                else:
                    dia = 1
                    mes += 1
            else:
                dia += 1
        else:  # Fevereiro
            if bissexto:
                if dia == 29:
                    dia = 1
                    mes += 1
                else:
                    dia += 1
            else:
                if dia == 28:
                    dia = 1
                    mes += 1
                else:
                    dia += 1
        print(f"O próximo dia é: {dia}/{mes}/{ano}")
    def calcular_dia_anterior(dia, mes, ano):
        meses_30 = [4, 6, 9, 11]
        meses_31 = [1, 3, 5, 7, 8, 10, 12]

        # Verificar se o ano é bissexto
        bissexto = eh_bissexto(ano)

        # Calcular o dia anterior
        dia -= 1
        # Verificar se o dia é negativo, o que significa que precisamos retroceder para o mês anterior
        if dia <= 0:
            mes -= 1
            if mes < 1:
                mes = 12
                ano -= 1
            # Determinar o último dia do mês anterior
            if mes in meses_30:
                dia = 30
            elif mes in meses_31:
                dia = 31
            else:  # Fevereiro
                if bissexto:
                    dia = 29
                else:
                    dia = 28
        print(f"O dia anterior é: {dia}/{mes}/{ano}")

    dia = random.randint(1, 31)
    mes = random.randint(1, 12)
    ano = random.randint(2024, 2025)

    calcular_dia_anterior(dia, mes, ano)
    print(f"O dia atual é: {dia}/{mes}/{ano}")
    calcular_proximo_dia(dia, mes, ano)


#Elabore um algoritmo que leia um número inteiro entre 1 e 6 e imprima o mês correspondente.
# Caso seja digitado um valor entre 7 e 12, informar que é um mês localizado no segundo semestre do ano.
# Caso seja digitado um valor fora desse intervalo, deverá ser exibida uma mensagem informando que não existe mês com esse número.

def atv25():
    mes = random.randint(-1, 13)
    print(mes)
    if mes <= 6 and mes >= 1:
        if mes == 1:
            print("Janeiro")
        elif mes == 2:
            print("Fevereiro")
        elif mes == 3:
            print("Março")
        elif mes == 4:
            print("Abril")
        elif mes == 5:
            print("Maio")
        else:
            print("Junho")
    elif mes >=7 and mes <= 12:
        print("Segundo semestre do ano")
    else:
        print("Não existe mês com esse numero")





#atv25()
#atv24()
#atv23()
#atv22()
#exemplo5()
#atv21()
#exemplo4()
#atv20()
#atv19()
#atv18()
#atv17()
#atv16()
#atv15()
#exemplo3()
#atv14()
#TESTEAPI()
#atv13()
#atv12()
#atv11()
#atv10()
#atv9()
#atv8()
#atv7()
#atv6()
#atv5()
#atv4()
#atv3()
#atv2()
#atv1()
#exemplo2()
#exemplo1()
