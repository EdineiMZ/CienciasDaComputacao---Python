#Servidor do Discord
# https://www.discord.gg/4tYjBsnZ7a

#importação das bibliotecas utilizadas
import random
import time
import requests
import sqlite3
from randomic import *
from colorama import Fore,Back,Style
from typing import Counter


#mensagem de boas vindas
print("Hello Wordy!!!")

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
    produto = randomProd()
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
    time_sorteado1 = randomTimesFut()
    time_sorteado2 = randomTimesFut()
    numeroGolsTime1 = randomInt(0, 5)
    numeroGolsTime2 = randomInt(0, 5)

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
    match mes:
        case 1:
            print("Janeiro")
        case 2:
            print("Fevereiro")
        case 3:
            print("Março")
        case 4:
            print("Abril")
        case 5:
            print("Maio")
        case 6:
            print("Junho")
        case 7|8|9|10|11|12:
            print("Segundo semestre")
        case _:
            print("Não existe um mês com essa numeração")


    # con = sqlite3.connect("products.db")
    # cur = con.cursor()
    # cur.execute("CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, preco, nome, local, codorigem)")
    # #
    # # cur.execute("""
    # # INSERT INTO produtos VALUES
    # # (1, 8.99,'Batata Inglesa','Europa',60)
    # # """)
    #
    # cur.execute("INSERT INTO produtos (preco, nome, local, codorigem) VALUES (?, ?, ?, ?)", (preco, nome, local, codorigem))
    # con.commit()
    # # id = 1
    # # cur.execute("SELECT * FROM produtos WHERE id = ?", (1,))
    # # produto = cur.fetchone()
    # # print(produto)
    #
    # cur.execute("SELECT * FROM produtos WHERE (id) VALUES (?)", (id))
    # registros = cur.fetchall()
    # for registros in registros:
    #     print(registros)

def atv26():
    preco = round(random.uniform(1, 500), 2)
    codorigem = random.randint(1, 20)

    match codorigem:
        case 1:
            local = "Sul"
        case 2:
            local = "Norte"
        case 3:
            local = "Leste"
        case 4:
            local = "Oeste"
        case 5|6:
            local = "Noroeste"
        case 7|8|9:
            local = "Sudeste"
        case 10|11|12:
            local = "Centro Oeste"
        case 13|14|15:
            local = "Noroeste"
        case _:
            local = "Importado"
    print("Produto de R$", preco, "Origem", local)

def atv27():
    codigo = random.randint(1, 4)
    def percenteualAumento(salario):
        if codigo == 2 or codigo == 4 :
            aumento = (salario*30)/100
        elif codigo == 1:
            aumento = (salario * 20) / 100
        else:
            aumento = (salario*15)/100
        return aumento
    match codigo:
        case 1:
            salario = 8000
            descricao = "Analista de Sistemas"
        case 2:
            salario =10000
            descricao = "Programador"
        case 3:
            salario = 15000
            descricao = "Gerente de Redes"
        case 4:
            salario = 20000
            descricao = "Gerente de TI"

    print("Cargo:", descricao, "- Salario:", salario, "- Aumento:", percenteualAumento(salario), " - Novo salário:", salario + percenteualAumento(salario))


def atv28():
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))
    operacao = input("Digite o caractere da operação desejada (* para multiplicação, / para divisão, + para adição, - para subtração): ")
    resultado = 0
    match operacao:
        case '*':
            resultado = numero1 * numero2
        case '/':
            resultado = numero1 / numero2 if numero2 != 0 else "Divisão por zero!"
        case '+':
            resultado = numero1 + numero2
        case '-':
            resultado = numero1 - numero2
        case _:
            resultado = "Operação inválida!"

    print("O resultado é ", resultado)



def jogo():
#Jogo Exemplo

#Feito Por GIOTTI e EU
    print('jogo legal')

    def jogo_legal():
        s = random.randint(1, 100)
        print(s)
        tentativas = 0
        contador = 0
        while True:
            tentativas = int(input('digite seu palpite: '))

            contador += 1

            if tentativas < s:
                print('o numero secreto e maior tente novamente')
            elif tentativas > s:
                print('o numero secreto e menor tente novamente')
            else:
                print(f'parabains voce acertou o numero secreto: {s} em {contador} tentativas')
                break
        jogarnovamente = input('deseja jogar novamente? S/N')
        if jogarnovamente.lower() == 'S':
            jogo_legal()
        else:
            print('obrigado por jogar')
    if __name__ == "__main__":
        jogo_legal()

#repetição

def repeticaoEx():
    for count in range (1, 11):
        print('Contagem', count)

    for count in range (10, 0, -1):
        print('Contagem', count)

    # Exemplo do While (Enquanto) para encontrar uma chave
    chave = random.randint(0, 50)  # Dev=fine o valor da chave de segurança
    numero = 0
    print("Chave definida", chave)
    while numero != chave:  # define que enquanto o numero for direfente da chave, imprime valor incoreto
        print("Valor Incoreto")
        time.sleep(0.2)
        numero = random.randint(0, 50)
    print("Chave encontrada", numero)


def atv29():
    for count in range (1, 101):
        print('Contagem', count)

def atv30():
    for count in range (100, 0, -1):
        print('Contagem', count)

def atv31():
    for count in range (250, 501):
        print('Contagem', count)

#4)	Elabore um algoritmo que leia um número de entrada que indicará a quantidade de números a serem lidos.
# Em seguida, leia n números (conforme o valor informado anteriormente) e imprima o triplo de cada um.
def atv32():
    QuantLeitura = random.randint(1, 500)
    for n in range (1, QuantLeitura):
        triplo = n * 3
        print('Numero lido', n, 'triplo dele', triplo)

def atv33():
    pessoa = randonPessoas()
    for count in range (1, 21):
        pessoa = randonPessoas()
        sobrenome = randomSobrenomes()
        idade = randomInt(1, 90)
        if idade > 18:
            print('Parabéns', pessoa, sobrenome, 'voce ja fez 18 anos')
        else:
            print('Menor de idade')
def atv34():
    for count in range(1, 101):
        if count % 2 == 0:
            print(count)


def atv35():
    for count in range(301, 402):
        if count % 3 == 0:
            print('Multiplo de 3',count)
        else:
            if count %  5 == 0:
                print('Multiplo de 5', count)

def exemploCores():
    class color:
        BLACK = '\33[30m'
        WHITE = '\33[40m'

        RED = '\33[91m'  # ou 31
        GREEN = '\033[92m'  # ou 32
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        PURPLE = '\033[95m'
        CYAN = '\033[96m'

        BLACK_BACK = '\33[40m'
        RED_BACK = '\33[41m'
        GREEN_BACK = '\33[42m'
        YELLOW_BACK = '\33[43m'
        BLUE_BACK = '\33[44m'
        GRAY_BACK = '\33[47m'

        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

    print("Usar cores no terminal é " + color.BLUE_BACK + "divertido" + color.END + ", concorda?")
    print("Eu " + color.BLACK + color.RED_BACK + color.UNDERLINE + "gosto" + color.END + " muito!")



def colorama():
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    print('back to normal now')
    print(Back.RED + "Texto colorido" + Back.RESET + Fore.GREEN + " pela Colorama")
    print(Style.RESET_ALL)

def atv36():
    frase = '1, 2, 3... testando'
    for valor in range(1, 31):
        if valor % 2 !=0:
            print(Fore.RED + frase, valor)
        else:
            print(Fore.GREEN + frase, valor)

def atv37():
    for i in range(200, 221):
        print(i, end="-") if i < 220 else print(i, end="")

def atv38():
#Escrever um programa que mostre os números múltiplos de 3 e de 5 existentes entre 301 e 401.
# Os números múltiplos de 3 devem ser mostrados em azul
# e os múltiplos de 5 em amarelo.
# Quando o número for múltiplo de 3 e de 5, ele deverá ser mostrado em rosa (purple).
# Se não for múltiplo nem de 3 e nem de 5, deverá ser mostrada em branco.
    for i in range(301, 402):
        if (i % 3 == 0) and (i % 5 == 0):
            print(Fore.MAGENTA + str(i))
        elif i % 5 == 0:
            print(Fore.YELLOW + str(i))
        elif i % 3 == 0:
            print(Fore.BLUE + str(i))
        else:
            print(Fore.RESET + str(i))

def atv39():
#Elabore um algoritmo que leia 20 números inteiros.
# Ao final deve ser informado quantos maiores que 10 foram lidos e a sua média.
    valor = set()
    for i in range(0, 10):
        valores = randomInt(0, 30)
        if valores > 10:
            valor.add(valores)
    media = sum(valor) / len(valor)
    print('media dos numeros maiores que 10:', f"{media:.2f}")
    print('Os numeros erram:', valor)

def atv40():
#Elabore um algoritmo que leia 200 números
#imprima quantos são pares e quantos são ímpares.
    impar = set()
    par = set()
    for i in range(0, 200):
        numero = randomInt(0,1000)
        if numero % 2 == 0:
            par.add(i)
        else:
            impar.add(i)
    print('Quantidade numeros pares:', len(par))
    print('Quantidade numeros impar:', len(impar))

def atv41():
    #Construir um programa para ler 20 números inteiros e encontrar o maior valor informado
    conjunto = set()
    for i in range(0, 20):
        numero = randomInt(1, 100)
        conjunto.add(numero)
    print('maior valor do conjunto', max(conjunto))


def atv42():
    #Construir um programa para mostrar a tabuada de um número inteiro informado pelo usuário.
    tabuada = int(input('Informe a tabuada desejada de 1 a 10: '))
    if tabuada >= 1 and tabuada <= 10:
        for i in range(1, 11):
            print(tabuada, 'x' , i , '=' , tabuada * i )
    else:
        print('Valor inserido invalido! ')

def atv43():
    #Elabore um algoritmo que leia um número de entrada que indicará a quantidade de números a serem lidos.
    #Em seguida, leia n números inteiros e positivos, e ao final, imprima o maior número digitado.
    conjunto = set()
    qtnumsort = randomInt(1, 100)

    for i in range(1, qtnumsort):
        numero = randomInt(1, 500)
        conjunto.add(numero)
    print('maior valor do conjunto', max(conjunto))

def atv44():
    #Elabore um algoritmo que leia um número de entrada n que indicará a quantidade de números a serem lidos.
    #Em seguida, leia n números (conforme o valor informado anteriormente) e, ao final imprima o menor número digitado.
    #Note que nesse caso não sabemos o intervalo dos valores possíveis, assim vamos usar outra informação: o maior número que pode ser armazenado em uma variável em Python é ‘inf’, portanto, se esse é o maior número possível, qualquer número será menor que ele.
    n = randomInt(1, 500)
    menor = float('inf')
    for i in range(1, n):
        numero = randomInt(-5000, 5000)
        if numero < menor:
            menorvalor = numero

    print('Menor valor do conjunto', menorvalor)

def atv45():
    #Escrever um programa que gere 1 número randômico entre 1 e 100 e mostre os números contidos nesse intervalo.
    # Por exemplo, se for sorteado o número 5, deve mostrar os números do 1 até o 5.  Mostar 10 números por linha.
    conjunto = []
    intervalo = randomInt(1, 100)
    contadorl = 1
    print("Os numeros no intervalo de 1 a", intervalo, "são: " )
    for i in range(1, intervalo + 1):
        conjunto.append(i)
        if contadorl == 10:
            conjunto.sort()
            print(conjunto)
            conjunto.clear()
            contadorl = 1
        elif contadorl != 10:
            if i == intervalo:
                conjunto.sort()
                print(conjunto)
            else:
                contadorl = contadorl + 1

def atv46():
    #Escrever um programa que gere 20 números aleatórios (randômicos) entre 0 e 100 e conte quantos desses são pares e quantos são impares.
    contagem_par = 0
    for i in range(0, 20):
        random = randomInt(0, 100)
        if random & 1:
            break
        else:
            contagem_par = contagem_par + 1
    print(contagem_par)

def atv47():
    #Escrever um programa que gere e mostre 10 números aleatórios (randômicos) entre 50 e 100.
    #Em seguida mostre qual foi o maior valor gerado.
    #Note que nesse exercício o maior valor possível será 100 e o menor valor possível será 50.
    conjunto = set()
    for i in range(1, 11):
        random = randomInt(50, 100)
        conjunto.add(random)
    print('Maior valor sorteado:', max(conjunto))

def atv48():
    #Modifique o programa anterior para mostrar também o menor valor gerado.
    #Escrever um programa que gere e mostre 10 números aleatórios (randômicos) entre 50 e 100.
    #Em seguida mostre qual foi o maior valor gerado.
    #Note que nesse exercício o maior valor possível será 100 e o menor valor possível será 50.
    conjunto = set()
    for i in range(1, 11):
        random = randomInt(50, 100)
        conjunto.add(random)
    print('Maior valor sorteado:', max(conjunto))
    print('Menor valor sorteado:', min(conjunto))

#Construa um programa que sorteie 50 números inteiros entre 0 e 500 e no final informe quantas vezes o valor 100 foi sorteado.
def atv49():
    conjunto = []
    for i in range(0, 50):
        random = randomInt(0, 500)
        conjunto.append(random)
    print('Numero 100 aparceu:', conjunto.count(100), ' vezes')

def atv50():
    #um algoritmo que imprima os números de 1 até 100 na tela.
    #Divida-os em 20 números por linha.
    conjunto = []
    contadorl = 1
    valor = 1
    while valor <= 100:
        conjunto.append(valor)
        valor = valor + 1
        if contadorl == 20:
            conjunto.sort()
            print(conjunto)
            conjunto.clear()
            contadorl = 1
        else:
            contadorl = contadorl + 1
def atv51():
    #Elabore um algoritmo que leia números inteiros e imprima o triplo de cada um.
    #O algoritmo acaba quando número 999 for digitado (incluindo o triplo de 999).
    numero = 0
    while numero != 999 or numero != 2997:
        numero = randomInt(998, 999)
        valor = numero * 3
        print('Numero', numero, '* 3 =', valor)

def atv52():
    #Elabore um algoritmo que leia números inteiros enquanto os valores informados forem positivos ou zero.
    # Quando um número negativo for informado devem ser mostrados quantos números que foram digitados (incluindo o último número).
    numinfor = 0
    valor = randomInt(-50, 5000)
    while valor >=0:
        numinfor = numinfor + 1
        valor = randomInt(-50, 5000)
        print(valor)

    numinfor = numinfor + 1
    print(numinfor)

def atv53():
    #Construir um programa que gere números aleatórios ou randômicos entre 0 e 100, até que o valor zero seja sorteado.
    # Em seguida mostre o maior e o menor valores sorteados.
    # conjunto = []
    # valor = 9
    # while valor != 0:
    #     valor = randomInt(0, 100)
    #     if valor == 0:
    #         print("Algo")
    #     else:
    #         conjunto.append(valor)
    # conjunto.append(valor)
    #
    # print("O maior valor sorteado foi:", max(conjunto))
    # print("O menor valor sorteado foi:", min(conjunto))
    valormenor= float('inf')
    valormaior = float('-inf')
    valor = 8
    while valor != 0:
        valor = randomInt(0, 100)
        if valor >=0 :
            if valor > valormaior:
                valormaior = valor
            elif valor < valormenor:
                valormenor = valor
    print('Valor Maior', valormaior)
    print('valor Menor', valormenor)

def atv54():
    #2. Construir um programa que solicite o nome, a idade e quantidade de filhos de uma quantidade indeterminada de pessoas enquanto o usuário responder ‘Sim’ (‘S’) a pergunta “Deseja continuar (S/N)?”.  Ao final apresente um relatório contendo:
    #   a. O nome e idade da pessoa mais velha
    #   b. O nome e quantidade de filhos da pessoa mais velha
    #   c. O nome da pessoa com maior quantidade de filho

    def relatorio_pessoas(pessoas):
        mais_velha = max(pessoas, key=lambda x: x['idade'])
        mais_filhos = max(pessoas, key=lambda x: x['quantidade_filhos'])
        print("a. Pessoa mais velha:")
        print("   Nome:", mais_velha['nome'])
        print("   Idade:", mais_velha['idade'])
        print("b. Pessoa mais velha com quantidade de filhos:")
        print("   Nome:", mais_velha['nome'])
        print("   Quantidade de filhos:", mais_velha['quantidade_filhos'])
        print("c. Pessoa com maior quantidade de filhos:")
        print("   Nome:", mais_filhos['nome'])

    pessoas = []
    continuar = 'S'

    while continuar == 'S':
        nome = input("Digite o nome da pessoa: ")
        while True:
            idade = input("Digite a idade da pessoa: ")
            if idade.isdigit():
                idade = int(idade)
                break
            else:
                print("Por favor, insira apenas números para a idade.")
        while True:
            quantidade_filhos = input("Digite a quantidade de filhos da pessoa: ")
            if quantidade_filhos.isdigit():
                quantidade_filhos = int(quantidade_filhos)
                break
            else:
                print("Por favor, insira apenas números para a quantidade de filhos.")

        pessoas.append({'nome': nome, 'idade': idade, 'quantidade_filhos': quantidade_filhos})
        while True:
            continuar = input("Deseja continuar (S/N)? ").upper()
            if continuar in ['S', 'N']:
                break
            else:
                print("Por favor, responda apenas com 'S' ou 'N'.")

    relatorio_pessoas(pessoas)


def atv55():
    #Elaborar um algoritmo que solicite ao usuário um número entre 1 e 10. Caso o número esteja fora do intervalo definido, o sistema deve voltar a pedir o número (while). Em seguida deve ser mostrada a tabuada do número informado (for).
    numero = 0
    while numero < 1 or numero > 10:
        numero = int(input("Digite um número entre 1 e 10: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def atv56():
    #Construir um programa que apresente os números impares existentes entre 1 e 499, inclusive, sua média e seu somatório.
    impares = []
    for i in range(1, 500):
        if i % 2 != 0:
            impares.append(i)
    media = sum(impares) / len(impares)
    somatorio = sum(impares)
    print("Números ímpares:", impares)
    print("Média:", media)
    print("Somatório:", somatorio)

def atv57():
    #Construir um programa que lê as notas da prova de Algoritmos de uma turma de alunos e ao final apresenta um relatório contendo:
    #a. A melhor nota
    #b. A pior nota
    #c. A média de todas das notas

    notas = []
    continuar = 'S'
    while continuar == 'S':
        nota = float(input("Digite a nota do aluno: "))
        notas.append(nota)
        continuar = input("Deseja continuar (S/N)? ").upper()
    melhor_nota = max(notas)
    pior_nota = min(notas)
    media = sum(notas) / len(notas)
    print("a. Melhor nota:", melhor_nota)
    print("b. Pior nota:", pior_nota)
    print("c. Média:", media)

def atv58():
    #. Construir um programa para registrar os dados referentes a preferência por canais de TV de pessoas entrevistadas.
    #O usuário deve informar os seguintes dados de cada cliente entrevistado:
    #a) Canal de TV que assiste mais (sendo 1-Globo, 2-SporTV, 3-Outra)
    #b) Canal de streaming que assiste mais (sendo 1-Netflix, 2-Disney, 3-Outra)
    #c) Idade da pessoa
    #d) Nível de instrução (1 – ensino fundamental, 2- ensino médio, 3- ensino superior)
    #Quando terminar de entrevistar as pessoas (respondendo à pergunta “Deseja continuar
    #(S/N)?” ), deve ser apresentadas as seguintes informações:
    #Canais de TV aberto e streaming mais assistidos
    #Idade média das pessoas que assistem SporTV
    #Nível de instrução das pessoas que responderam à pesquisa (percentual de cada)

    def relatorio_entrevistados(entrevistados):
        canais_tv = {1: 'Globo', 2: 'SporTV', 3: 'Outra'}
        canais_streaming = {1: 'Netflix', 2: 'Disney', 3: 'Outra'}
        canais_tv_mais_assistidos = Counter([entrevistado['canal_tv'] for entrevistado in entrevistados]).most_common(1)
        canais_streaming_mais_assistidos = Counter([entrevistado['canal_streaming'] for entrevistado in entrevistados]).most_common(1)
        idade_media_sportv = sum([entrevistado['idade'] for entrevistado in entrevistados if entrevistado['canal_tv'] == 2]) / len([entrevistado for entrevistado in entrevistados if entrevistado['canal_tv'] == 2])
        nivel_instrucao = Counter([entrevistado['nivel_instrucao'] for entrevistado in entrevistados])
        total_entrevistados = len(entrevistados)
        print("Canais de TV aberto e streaming mais assistidos:")
        print("  TV aberto:", canais_tv[canais_tv_mais_assistidos[0][0]])
        print("  Streaming:", canais_streaming[canais_streaming_mais_assistidos[0][0]])
        print("Idade média das pessoas que assistem SporTV:", idade_media_sportv)
        print("Nível de instrução das pessoas que responderam à pesquisa:")
        for nivel, quantidade in nivel_instrucao.items():
            print(f"  Nível {nivel}: {quantidade / total_entrevistados * 100:.2f}%")

    entrevistados = []
    continuar = 'S'

    while continuar == 'S':
        canal_tv = int(input("Canal de TV que assiste mais (1-Globo, 2-SporTV, 3-Outra): "))
        canal_streaming = int(input("Canal de streaming que assiste mais (1-Netflix, 2-Disney, 3-Outra): "))
        idade = int(input("Idade da pessoa: "))
        nivel_instrucao = int(input("Nível de instrução (1-ensino fundamental, 2-ensino médio, 3-ensino superior): "))
        entrevistados.append({'canal_tv': canal_tv, 'canal_streaming': canal_streaming, 'idade': idade, 'nivel_instrucao': nivel_instrucao})
        continuar = input("Deseja continuar (S/N)? ").upper()

    relatorio_entrevistados(entrevistados)

def atv59():
    #Construir um programa que solicite o nome, a idade e quantidade de livros de uma quantidade indeterminada de escritores. Utilize a estratégia que preferir para fazer a leitura de todos os dados. Ao final apresente um relatório contendo:
    #a. O nome e idade do escritor mais novo.
    #b. O nome e quantidade de livros do escritor mais velho.
    #c. O nome do escritor com maior quantidade de livros.

    def relatorio_escritores(escritores):
        mais_novo = min(escritores, key=lambda x: x['idade'])
        mais_velho = max(escritores, key=lambda x: x['idade'])
        mais_livros = max(escritores, key=lambda x: x['quantidade_livros'])
        print("a. Escritor mais novo:")
        print("   Nome:", mais_novo['nome'])
        print("   Idade:", mais_novo['idade'])
        print("b. Escritor mais velho:")
        print("   Nome:", mais_velho['nome'])
        print("   Quantidade de livros:", mais_velho['quantidade_livros'])
        print("c. Escritor com maior quantidade de livros:")
        print("   Nome:", mais_livros['nome'])

    escritores = []
    continuar = 'S'

    while continuar == 'S':
        nome = input("Digite o nome do escritor: ")
        while True:
            idade = input("Digite a idade do escritor: ")
            if idade.isdigit():
                idade = int(idade)
                break
            else:
                print("Por favor, insira apenas números para a idade.")
        while True:
            quantidade_livros = input("Digite a quantidade de livros do escritor: ")
            if quantidade_livros.isdigit():
                quantidade_livros = int(quantidade_livros)
                break
            else:
                print("Por favor, insira apenas números para a quantidade de livros.")

        escritores.append({'nome': nome, 'idade': idade, 'quantidade_livros': quantidade_livros})
        while True:
            continuar = input("Deseja continuar (S/N)? ").upper()
            if continuar in ['S', 'N']:
                break
            else:
                print("Por favor, responda apenas com 'S' ou 'N'.")

    relatorio_escritores(escritores)


#Implemente um algoritmo que leia as notas de 10 alunos armazenando-as em um vetor (matriz)
#de 10 posições. Ao final, escreva na tela somente as notas maiores que 5.0.
def atv60():
    notas = []
    for i in range(1, 11):
        nota = float(input(f"Digite a nota do aluno {i}: "))
        notas.append(nota)
    print("Notas maiores que 5.0:", [nota for nota in notas if nota > 5.0])

#Desenvolva um algoritmo que leia um conjunto de 15 números inteiros e armazene-os em um
#vetor A. Após a leitura dos dados o algoritmo deve multiplicar todos os números do vetor A por 3
#e armazenar o resultado em um segundo vetor B. No final, mostrar o conteúdo dos 2 vetores




#atv60()
#atv59()
#atv58()
#atv57()
#atv56()
#atv55()
#atv54()
#atv53()
#atv52()
#atv51()
#atv50()
#atv49()
#atv48()
#atv47()
#atv46()
#atv45()
#atv44()
#atv43()
#atv42()
#atv41()
#atv40()
#atv39()
#atv38()
#atv37()
#atv36()
#colorama()
#exemploCores()
#atv35()
#atv34()
#atv33()
#atv32()
#atv31()
#atv30()
#atv29()
#repeticaoEx()
#jogo()
#atv28()
#atv27()
#atv26()
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
