SQL_TABLE_SCRIPTS = """
CREATE TABLE cliente(
id INTEGER PRIMARY KEY,
telefone VARCHAR(13) NOT NULL UNIQUE,
nome VARCHAR(50) NOT NULL,
aniversario DATE,
data_de_registro DATE NOT NULL
);

CREATE TABLE pedido(
id INTEGER PRIMARY KEY,
cliente INT NOT NULL,
data DATE NOT NULL,
FOREIGN KEY (cliente) REFERENCES cliente (id)
);

CREATE TABLE item(
id INTEGER PRIMARY KEY,
nome VARCHAR(70) NOT NULL,
categoria VARCHAR(20) NOT NULL,
preço REAL,
ativo BOOL
);

CREATE TABLE item_no_pedido(
id INTEGER PRIMARY KEY,
pedido INT NOT NULL,
item INT NOT NULL,
quantidade SMALLINT NOT NULL CHECK (quantidade > 0),
FOREIGN KEY (item) REFERENCES item (id),
FOREIGN KEY (pedido) REFERENCES pedido (id)
);
CREATE UNIQUE INDEX idx_nome_ativo ON item (nome) WHERE ativo = 1;
"""

MENU_ITEMS = (
    {
        "id": None, "nome": "Suco de laranja", "categoria": "Bebida",
        "preço": 10, "ativo": True
    },
    {
        "id": None, "nome": "Suco de limão", "categoria": "Bebida",
        "preço": 10, "ativo": True
    },
    {
        "id": None, "nome": "Nescau P", "categoria": "Bebida", "preço": 5.9,
        "ativo": True
    },
    {
        "id": None, "nome": "Nescau M", "categoria": "Bebida", "preço": 7.9,
        "ativo": True
    },
    {
        "id": None, "nome": "Café coado P", "categoria": "Bebida",
        "preço": 3.5, "ativo": True
    },
    {
        "id": None, "nome": "Café coado M c/ leite", "categoria": "Bebida",
        "preço": 5.9, "ativo": True
    },
    {
        "id": None, "nome": "Café coado M", "categoria": "Bebida",
        "preço": 6.9, "ativo": True
    },
    {
        "id": None, "nome": "Expresso P", "categoria": "Bebida",
        "preço": 4.3, "ativo": True
    },
    {
        "id": None, "nome": "Expresso M c/ leite", "categoria": "Bebida",
        "preço": 6.9, "ativo": True
    },
    {
        "id": None, "nome": "Expresso M", "categoria": "Bebida",
        "preço": 7.9, "ativo": True
    },
    {
        "id": None, "nome": "Cappucino P", "categoria": "Bebida",
        "preço": 7, "ativo": True
    },
    {
        "id": None, "nome": "Cappucino M", "categoria": "Bebida",
        "preço": 10.5, "ativo": True
    },
    {
        "id": None, "nome": "Pão na chapa", "categoria": "Salgado",
        "preço": 4, "ativo": True
    },
    {
        "id": None, "nome": "Pão c/ ovo", "categoria": "Salgado", "preço": 6,
        "ativo": True
    },
    {
        "id": None, "nome": "Misto quente", "categoria": "Salgado",
        "preço": 8.95, "ativo": True
    },
    {
        "id": None, "nome": "Misto c/ ovo", "categoria": "Salgado",
        "preço": 9.95, "ativo": True
    },
    {
        "id": None, "nome": "Pão de queijo", "categoria": "Salgado",
        "preço": 2.5, "ativo": True
    },
    {
        "id": None, "nome": "Croissant", "categoria": "Salgado",
        "preço": 7.9, "ativo": True
    },
    {
        "id": None, "nome": "Mini sonho de creme", "categoria": "Doce",
        "preço": 4.55, "ativo": True
    },
    {
        "id": None, "nome": "Mini sonho de doce de leite",
        "categoria": "Doce", "preço": 4.55, "ativo": True
    },
    {
        "id": None, "nome": "Cookie", "categoria": "Doce", "preço": 5.85,
        "ativo": True
    },
    {
        "id": None, "nome": "Bomba de chocolate", "categoria": "Doce",
        "preço": 7.7, "ativo": True
    },
    {
        "id": None, "nome": "Bomba de creme", "categoria": "Doce",
        "preço": 7.7, "ativo": True
    },
    {
        "id": None, "nome": "Donut", "categoria": "Doce",
        "preço": 9, "ativo": True
    },
)

NAMES = ["Helena", "Alice", "Laura", "Maria Alice", "Cecília", "Maitê", "Liz",
         "Aurora", "Antonella", "Heloísa", "Maria Cecília", "Maria Clara",
         "Manuela", "Maya", "Sophia", "Valentina", "Elisa", "Maria Helena",
         "Isabella", "Eloá", "Ayla", "Lara", "Lívia", "Maria Júlia", "Lorena",
         "Melissa", "Sofia", "Isabela", "Luísa", "Beatriz", "Júlia",
         "Mariana", "Isadora", "Maria Luiza", "Ana Liz", "Rebeca", "Isis",
         "Maria Eduarda", "Aylla", "Esther", "Manuella", "Sarah", "Ísis",
         "Maria Liz", "Olívia", "Lavínia", "Ana Laura", "Catarina", "Maria",
         "Luna", "Ana Clara", "Luiza", "Yasmin", "Marina", "Emanuelly",
         "Giovanna", "Jade", "Eloah", "Julia", "Clara", "Maria Luísa",
         "Ana Júlia", "Ester", "Anna Liz", "Agatha", "Stella", "Alícia",
         "Gabriela", "Maria Laura", "Sara", "Maria Flor", "Heloisa",
         "Hellena", "Clarice", "Maria Isis", "Bella", "Isabelly", "Melina",
         "Mirella", "Rafaela", "Vitória", "Maria Julia", "Cecilia", "Allana",
         "Olivia", "Alana", "Zoe", "Mariah", "Ana Luiza", "Lunna", "Bianca",
         "Hadassa", "Maria Vitória", "Maria Fernanda", "Luara", "Milena",
         "Ágatha", "Laís", "Ana Cecília", "Ana Beatriz", "Miguel", "Heitor",
         "Gael", "Arthur", "Bernardo", "Davi", "Ravi", "Noah", "Samuel",
         "Théo", "Gabriel", "Anthony", "Pedro", "Benício", "Joaquim", "Isaac",
         "Lorenzo", "João Miguel", "Lucas", "Levi", "Henrique", "Rafael",
         "Henry", "Theo", "Nicolas", "Murilo", "Guilherme", "Benjamin",
         "Lucca", "Matheus", "Matteo", "Pedro Henrique", "Bento", "Gustavo",
         "Leonardo", "Vicente", "Daniel", "João Pedro", "Emanuel", "Pietro",
         "Davi Lucca", "Bryan", "Felipe", "Enzo Gabriel", "Antony", "Mateus",
         "Anthony Gabriel", "João Lucas", "Augusto", "João Guilherme",
         "Benjamim", "Thomas", "João", "Eduardo", "Antônio", "Yuri", "Enzo",
         "Oliver", "Rael", "Otávio", "Francisco", "Rhavi", "João Gabriel",
         "Nathan", "Mathias", "Caio", "Arthur Miguel", "Brayan", "Isaque",
         "José", "Ryan", "Ravi Lucca", "Enrico", "Davi Lucas", "Josué",
         "Benicio", "José Miguel", "Luan", "Luiz Miguel", "Ravy", "Vinícius",
         "Apollo", "Otto", "Theodoro", "Yan", "Dom", "Pedro Lucas", "Léo",
         "Davi Miguel", "Valentim", "Caleb", "José Pedro", "Liam", "Dante",
         "Gael Henrique", "Henry Gabriel", "Kevin", "Arthur Gabriel", "Asafe",
         "Erick"]
