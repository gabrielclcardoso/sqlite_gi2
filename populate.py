import sqlite3

import constants as const


def main():
    con = sqlite3.connect("onda_do_trigo.db")
    cur = con.cursor()

    cur.executescript(const.SQL_TABLE_SCRIPTS)
    con.commit()
    con.close()


if __name__ == '__main__':
    main()
