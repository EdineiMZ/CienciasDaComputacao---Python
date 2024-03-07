#importação das bibliotecas utilizadas
import random
import time

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

# 5)Elabore um algoritmo que leia o nome e o peso de duas pessoas e imprima os dados da pessoa mais pesada. Os pesos delas serão diferentes.
def atv10():
    nomeP1 = input("Insira seu nome: ")
    peso1 = round(random.uniform(10, 150), 3)
    nomeP2 = input("Insira seu nome Pessoa 2: ")
    peso2 = round(random.uniform(10, 150), 3)
    if peso1 > peso2:
        print("A(o)", nomeP1, "é mais pesada que a(o)", nomeP2, "pesando", peso1, ".", nomeP2, "pesa", peso2)
    else:
        print("A(o)", nomeP2, "é mais pesada que a(o)", nomeP1, "pesando", peso2, ".", nomeP1, "pesa", peso1)


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
