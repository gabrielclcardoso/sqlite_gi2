import sqlite3
import time


def main():
    con = sqlite3.connect("onda_do_trigo.db")
    cur = con.cursor()

    clients_who_ordered_items(cur)


def clients_who_ordered_items(cur):
    items = cur.execute("SELECT id, nome FROM item").fetchall()

    id = get_item_id(items)
    month = get_month()

    list_clients(cur, id, month)


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
    start = time.mktime(time.strptime(f'2023-{month}-1', '%Y-%m-%d'))
    end = time.mktime(time.strptime(f'2023-{month}-31', '%Y-%m-%d'))

    script = f"""
        SELECT c.telefone, c.nome FROM pedido AS p
        JOIN cliente AS c ON p.cliente = c.id
        JOIN item_no_pedido AS ip ON p.id = ip.pedido
        JOIN item AS i ON ip.item = i.id
        WHERE data >= {start} AND data <= {end} AND i.id = {item_id}
    """
    clients = cur.execute(script).fetchall()

    for telefone, name in clients:
        print(f'{name} | Telefone: {telefone}')


if __name__ == '__main__':
    main()
