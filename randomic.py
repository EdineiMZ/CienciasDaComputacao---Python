import random
def randomProdAlim():
    conjunto_produtosAlim = {"Seleção de Temperos Internacionais", "Variedade de Geleias Artesanais",
                            "Barra de Granola Orgânica", "Chá de Especiarias Exóticas", "Chocolate Artesanal Premium",
                            "Café Gourmet", "Mix de Frutas Secas", "Biscoitos Artesanais", "Mel Puro",
                            "Azeite Extra Virgem", "Queijo Artesanal", "Vinho Tinto Reserva", "Cerveja Artesanal",
                            "Pacote de Massa Integral", "Molho de Tomate Caseiro", "Farinha de Trigo Orgânica",
                            "Snack de Castanhas", "Suco Natural de Frutas", "Lancheira Térmica",
                            "Garrafa de Água Reutilizável", "Copo de Bambu", "Tábua de Corte de Madeira",
                            "Conjunto de Facas de Cozinha", "Pote Hermético de Vidro", "Livro de Receitas Saudáveis",
                            "Assinatura de Clube de Degustação", "Kombucha Artesanal",
                            "Pão Integral de Fermentação Natural", "Sal Marinho Grosso", "Semente de Chia Orgânica",
                            "Sorvete Artesanal", "Barra de Chocolate Amargo", "Kit para Fazer Sushi em Casa",
                            "Tempero para Carne", "Ervas Finas Desidratadas", "Cookies de Aveia e Passas",
                            "Mix de Cogumelos Secos", "Mix de Ervas para Chá", "Xarope de Bordo Puro",
                            "Geleia de Frutas Vermelhas", "Pack de Cervejas Artesanais", "Kit para Fazer Pão Caseiro",
                            "Cesta de Café da Manhã", "Kit para Fazer Pizza em Casa", "Vinho Branco Seco",
                            "Aperitivo de Grão-de-Bico", "Chips de Batata Doce", "Salada de Quinoa Pronta",
                            "Manteiga de Amendoim Orgânica", "Canela em Pau", "Framboesas Frescas", "Salada de Lentilhas",
                            "Mix de Sementes Crocantes", "Bolachas de Arroz Integral", "Pasta de Amêndoas",
                            "Kit para Fazer Cerveja em Casa", "Garrafa Térmica de Café", "Moedor de Pimenta",
                            "Kit de Vinhos Internacionais", "Molho de Soja Orgânico", "Bebida de Amêndoa",
                            "Sorvete Vegano", "Cesta de Frutas Frescas", "Pack de Snacks Saudáveis",
                            "Barra de Proteína Vegana", "Pasta de Tomate Seco", "Melão Cantalupo", "Limões Sicilianos",
                            "Folhas de Manjericão Fresco", "Pacote de Cacau em Pó", "Cenouras Orgânicas",
                            "Bebida Energética Natural", "Biscoitos de Gengibre", "Salada de Frutas da Estação",
                            "Pão de Centeio Integral", "Gelatina de Algas Marinhas", "Chá Gelado de Hibisco",
                            "Baguete de Pão Francês", "Picles Artesanais", "Cereal Matinal Multigrãos",
                            "Sopa de Lentilhas e Vegetais", "Mix de Frutas Tropicais", "Brownies de Chocolate Sem Glúten",
                            "Pack de Água de Coco", "Feijão Preto Orgânico", "Tomates Cereja", "Pepinos em Conserva",
                            "Kit para Fazer Queijo Fresco", "Pacote de Sementes de Abóbora",
                            "Salada de Beterraba e Queijo Feta", "Torradas de Pão Integral",
                            "Granulado de Chocolate Amargo", "Pacote de Grãos de Café Arábica", "Chips de Banana-da-Terra",
                            "Molho de Pimenta Artesanal", "Kefir de Leite", "Suco Detox de Vegetais", "Muffins de Mirtilo",
                            "Mix de Nozes e Castanhas", "Pacote de Arroz Integral", "Cesta de Vegetais Orgânicos",
                            "Marmelada Caseira", "Pão de Queijo Tradicional", "Sopa de Abóbora com Gengibre",
                            "Pack de Cervejas Importadas", "Manteiga de Coco Orgânica", "Mix de Frutas Cristalizadas",
                            "Pack de Vinhos Nacionais"}

    produtoAlim = random.choice(list(conjunto_produtosAlim))
    return produtoAlim

def randomTimesFut():
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
    time = random.choice(list(times_de_futebol))
    return time

def randomInt(inicial, final):
    valor = random.randint(inicial, final)
    return valor


def randomProd():
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
    produto = random.choice(list(nomes_produtos))
    return produto


def randonPessoas():
    nomes_pessoass = ["Maria", "João", "Ana", "Pedro", "Carolina", "André", "Mariana", "José", "Juliana", "Lucas", "Fernanda",
               "Rafael", "Isabela", "Gabriel", "Amanda", "Thiago", "Camila", "Bruno", "Larissa", "Matheus", "Letícia",
               "Leonardo", "Beatriz", "Vinícius", "Jéssica", "Gustavo", "Vanessa", "Marcelo", "Renata", "Rodrigo",
               "Paula", "Felipe", "Natália", "Ricardo", "Bianca", "Caio", "Carolina", "Carlos", "Luana", "Victor",
               "Fernanda", "Eduardo", "Patrícia", "Alexandre", "Priscila", "Guilherme", "Bruna", "Daniel", "Marina",
               "Henrique", "Débora", "William", "Luiza", "Fábio", "Taís", "Diego", "Lívia", "Igor", "Bárbara", "Marcos",
               "Renata", "André", "Fabiana", "Leandro", "Letícia", "Thiago", "Gabriela", "Rafael", "Ana", "Lucas",
               "Juliana", "Matheus", "Larissa", "Vinícius", "Jéssica", "Gustavo", "Vanessa", "Marcelo", "Renata",
               "Rodrigo", "Paula", "Felipe", "Natália", "Ricardo", "Bianca", "Caio", "Carolina", "Carlos", "Luana",
               "Victor", "Fernanda", "Eduardo", "Patrícia", "Alexandre", "Priscila", "Guilherme", "Bruna", "Daniel",
               "Marina", "Henrique"
               ]
    pessoa = random.choice(list(nomes_pessoass))
    return pessoa

def randomSobrenomes():
    lista_sobrenomes = [
        "Silva", "Santos", "Oliveira", "Pereira", "Ferreira", "Almeida", "Rocha", "Martins", "Carvalho", "Reis",
        "Rodrigues", "Costa", "Sousa", "Fernandes", "Pinto", "Melo", "Barbosa", "Araújo", "Nascimento", "Gomes",
        "Lima", "Dias", "Castro", "Monteiro", "Alves", "Lopes", "Gonçalves", "Dantas", "Cardoso", "Sá",
        "Correia", "Vieira", "Cruz", "Mendes", "Freitas", "Campos", "Siqueira", "Leal", "Ribeiro", "Amaral",
        "Farias", "Marques", "Cavalcanti", "Neves", "Teixeira", "Carneiro", "Domingues", "Moreira", "Bezerra",
        "Sales", "Moraes", "Borges", "Azevedo", "Jesus", "Freire", "Xavier", "Aguiar", "Lemos", "Garcia",
        "Correia", "Vargas", "Oliveira", "Nogueira", "Abreu", "Aragão", "Santana", "Coutinho", "Franco",
        "Ramos", "Macedo", "Cunha", "Peixoto", "Cavalcante", "Moura", "Barros", "Paula", "Diniz", "Albuquerque",
        "Tavares", "Barbosa", "Macedo", "Braga", "Caldeira", "Veiga", "Miranda", "Loureiro", "Fonseca",
        "Lacerda", "Assis", "Magalhães", "Sampaio", "Pacheco", "Castelo", "Machado", "Duarte", "Rocha"
    ]
    sobrenome = random.choice(list(lista_sobrenomes))
    return sobrenome

