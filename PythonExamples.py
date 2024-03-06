import random
import time

print("Hello Word!!!")

def exemplo1(): #Exemplo de IF ELSE ELIF
    numero = random.randint(0, 300) #define na variavel numero um valor randomico entre 0 e 300
    if numero <= 50: #verifica se o numero é menor ou igual a 50
        print("O numero selecionado é: ", numero, " ele é menor ou igual a 50.")
    elif numero >= 51 and numero <= 100: #verifica se o numero é maior que 50 e menor que 100
        print("O numero selecionado é", numero, "e ele esta entre 51 e 100")
    else:
        print("Numero maior que 100", numero)

def exemplo2(): #Exemplo do While (Enquanto) para encontrar uma chave
    chave = random.randint(0, 50)
    numero = 0
    print("Chave definida", chave)
    while numero != chave:
        print("Valor Incoreto")
        time.sleep(0.2)
        numero = random.randint(0, 50)
    print("Chave encontrada", numero)


#	O sistema de avaliação de determinada disciplina é composto por três provas.
#	A primeira prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5.
#	Considerando que a média para aprovação é 7.0. Construa um algoritmo para calcular a média final de um aluno
#	desta disciplina e dizer se o aluno foi aprovado ou não.
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
atv1()



#exemplo2()
#exemplo1()
