import sqlite3

import constants as const


def main():
    con = sqlite3.connect("onda_do_trigo.db")
    cur = con.cursor()

    cur.executescript(const.SQL_TABLE_SCRIPTS)

    create_menu_items(cur)

    con.commit()
    con.close()

    # new_con.close()


def create_menu_items(cur):
    cur.executemany(
        "INSERT INTO item VALUES(:id, :nome, :categoria, :preço, :ativo)",
        const.MENU_ITEMS)


if __name__ == '__main__':
    main()
