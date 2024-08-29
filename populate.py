import sqlite3
import random
import time

import constants as const


def main():
    con = sqlite3.connect("onda_do_trigo.db")
    cur = con.cursor()

    create_tables(cur)
    create_menu_items(cur)
    create_mock_clients(cur, 1200)
    create_mock_orders(cur, 30 * 80 * 12)
    create_order_relations(cur)

    con.commit()
    con.close()


def create_tables(cur):
    cur.executescript(const.SQL_TABLE_SCRIPTS)


def create_menu_items(cur):
    cur.executemany(
        "INSERT INTO item VALUES(:id, :nome, :categoria, :preço, :ativo)",
        const.MENU_ITEMS)


def create_mock_clients(cur, n):
    clients = []
    birth_start = time.mktime(time.strptime("1945-01-01", "%Y-%m-%d"))
    birth_end = time.mktime(time.strptime("2006-12-31", "%Y-%m-%d"))
    reg_start = time.mktime(time.strptime("2020-01-01", "%Y-%m-%d"))
    reg_end = time.mktime(time.strptime("2023-12-31", "%Y-%m-%d"))

    for i in range(n):
        cli = {'id': None}
        cli['telefone'] = str(i)
        cli['nome'] = random.choice(const.NAMES)
        cli['aniversario'] = random.randint(int(birth_start), int(birth_end))
        cli['data_de_registro'] = random.randint(int(reg_start), int(reg_end))
        clients.append(cli)

    cur.executemany("INSERT INTO cliente VALUES(:id, :telefone, :nome, \
                    :aniversario, :data_de_registro)", clients)


def create_mock_orders(cur, n):
    clients = cur.execute("SELECT id FROM cliente").fetchall()
    start = time.mktime(time.strptime("2023-01-01", "%Y-%m-%d"))
    end = time.mktime(time.strptime("2023-12-31", "%Y-%m-%d"))
    orders = []

    for i in range(n):
        order = {'id': None}
        order['cliente'] = random.choice(clients)[0]
        order['data'] = random.randint(int(start), int(end))
        orders.append(order)

    cur.executemany("INSERT INTO pedido VALUES(:id, :cliente, :data)", orders)


def create_order_relations(cur):
    orders = cur.execute("SELECT id FROM pedido").fetchall()
    drinks, food, dessert = get_items(cur)
    relations = []

    for order in orders:
        relations.append(add_item(cur, order[0], drinks))
        relations.append(add_item(cur, order[0], food))
        relations.append(add_item(cur, order[0], dessert))

    cur.executemany("INSERT INTO item_no_pedido VALUES(:id, :pedido, :item, \
        :quantidade)", relations)


def get_items(cur):
    res = cur.execute(
        "SELECT id FROM item WHERE categoria = 'Bebida' AND ativo = 1;")
    drinks = res.fetchall()
    res = cur.execute(
        "SELECT id FROM item WHERE categoria = 'Salgado' AND ativo = 1;")
    food = res.fetchall()
    res = cur.execute(
        "SELECT id FROM item WHERE categoria = 'Doce' AND ativo = 1;")
    dessert = res.fetchall()

    return drinks, food, dessert


def add_item(cur, order, items):
    relation = {
        'id': None,
        'pedido': order,
        'item': random.choice(items)[0],
        'quantidade': random.randint(1, 4)
    }
    return relation


if __name__ == '__main__':
    main()
