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
