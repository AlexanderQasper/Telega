import sqlite3 as sq

base = sq.connect('pizza_cool.db')
cur = base.cursor()

def sql_start():
    global base, cur
    if base:
        print('Sql DB starts!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()