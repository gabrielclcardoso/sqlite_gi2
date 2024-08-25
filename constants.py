SQL_TABLE_SCRIPTS = """
CREATE TABLE cliente(
id INTEGER PRIMARY KEY,
telefone VARCHAR(13) NOT NULL UNIQUE,
nome VARCHAR(50) NOT NULL UNIQUE,
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
        "id": None, "nome": "Pão na chapa", "categoria": "Salgados",
        "preço": 4, "ativo": True
    },
    {
        "id": None, "nome": "Pão c/ ovo", "categoria": "Salgados", "preço": 6,
        "ativo": True
    },
    {
        "id": None, "nome": "Misto quente", "categoria": "Salgados",
        "preço": 8.95, "ativo": True
    },
    {
        "id": None, "nome": "Misto c/ ovo", "categoria": "Salgados",
        "preço": 9.95, "ativo": True
    },
    {
        "id": None, "nome": "Pão de queijo", "categoria": "Salgados",
        "preço": 2.5, "ativo": True
    },
    {
        "id": None, "nome": "Croissant", "categoria": "Salgados",
        "preço": 7.9, "ativo": True
    },
    {
        "id": None, "nome": "Mini sonho de creme", "categoria": "Doces",
        "preço": 4.55, "ativo": True
    },
    {
        "id": None, "nome": "Mini sonho de doce de leite",
        "categoria": "Doces", "preço": 4.55, "ativo": True
    },
    {
        "id": None, "nome": "Cookie", "categoria": "Doces", "preço": 5.85,
        "ativo": True
    },
    {
        "id": None, "nome": "Bomba de chocolate", "categoria": "Doces",
        "preço": 7.7, "ativo": True
    },
    {
        "id": None, "nome": "Bomba de creme", "categoria": "Doces",
        "preço": 7.7, "ativo": True
    },
    {
        "id": None, "nome": "Donut", "categoria": "Doces",
        "preço": 9, "ativo": True
    },
)
