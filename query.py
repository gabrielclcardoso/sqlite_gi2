import sqlite3
import time

import constants as const

menu = '''
1 - Ver clientes que pediram item em certo mês
2 - Ver quantidade de item vendido em um certo mês
3 - Sair do programa
'''


def main():
    con = sqlite3.connect("onda_do_trigo.db")
    cur = con.cursor()

    while True:
        try:
            u_input = input(f'{menu}\nSelecione o que você quer fazer: ')
            choice = int(u_input)
            if choice > 3 or choice <= 0:
                raise Exception
            call(choice, cur)
        except Exception:
            print('Entrada Invalida')
        except (KeyboardInterrupt, EOFError):
            exit(0)


def call(choice, cur):
    if choice == 1:
        clients_who_ordered_items(cur)
    elif choice == 2:
        count_items(cur)
    else:
        exit(0)


def clients_who_ordered_items(cur):
    items = cur.execute("SELECT id, nome FROM item").fetchall()

    id = get_item_id(items)
    month = get_month()

    list_clients(cur, id, month)


def count_items(cur):
    items = cur.execute("SELECT id, nome FROM item").fetchall()

    id = get_item_id(items)
    month = get_month()

    count(cur, id, month)


def get_item_id(items):
    prompt = "\n".join([f"{id} - {name}" for id, name in items])

    while True:
        u_input = input(
            prompt + '\nSelecione o item que você quer consultar: ')
        try:
            id = int(u_input)
            if id > len(items) or id <= 0:
                raise Exception
            break
        except Exception:
            print('Entrada Invalida')
    return id


def get_month():
    while True:
        u_input = input(
            'Digite o número correspondente ao mês que você quer consultar: ')
        try:
            month = int(u_input)
            if month > 12 or month <= 0:
                raise Exception
            break
        except Exception:
            print('Entrada Invalida')
    return month


def list_clients(cur, item_id, month):
    day = const.FINAL_DAY[month - 1]
    start = time.mktime(time.strptime(f'2023-{month}-1', '%Y-%m-%d'))
    end = time.mktime(time.strptime(f'2023-{month}-{day}', '%Y-%m-%d'))

    script = f'''
        SELECT c.telefone, c.nome FROM pedido AS p
        JOIN cliente AS c ON p.cliente = c.id
        JOIN item_no_pedido AS ip ON p.id = ip.pedido
        JOIN item AS i ON ip.item = i.id
        WHERE data >= {start} AND data <= {end} AND i.id = {item_id}
    '''
    clients = cur.execute(script).fetchall()

    for telefone, name in clients:
        print(f'{name} | Telefone: {telefone}')


def count(cur, item_id, month):
    day = const.FINAL_DAY[month - 1]
    start = time.mktime(time.strptime(f'2023-{month}-1', '%Y-%m-%d'))
    end = time.mktime(time.strptime(f'2023-{month}-{day}', '%Y-%m-%d'))

    script = f'''
    SELECT SUM(ip.quantidade) FROM item_no_pedido AS ip
    JOIN pedido AS p ON ip.pedido = p.id
    JOIN item AS i on ip.item = i.id
    WHERE data >= {start} AND data <= {end} AND i.id = {item_id}
    '''
    amount = cur.execute(script).fetchone()[0]
    if amount is None:
        amount = 0
    print(f'\nQuantidade de itens pedidos no mês selecionado: {amount}')


if __name__ == '__main__':
    main()
