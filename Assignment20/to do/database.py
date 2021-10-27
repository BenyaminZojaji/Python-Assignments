import sqlite3

con = sqlite3.connect('db.db')
my_cursor = con.cursor()

def add(id, title, description, time):
    my_cursor.execute(f'INSERT INTO tasks(id, title, description, time, done, priority) VALUES("{id}", "{title}", "{description}", "{time}", "{0}", "{0}")')
    con.commit()

def get_all():
    my_cursor.execute('SELECT * FROM tasks')
    result = my_cursor.fetchall()
    return result

def get_detail(id):
    my_cursor.execute(f'SELECT * FROM tasks WHERE id={id}')
    result = my_cursor.fetchall()
    return result

def delete(id):
    my_cursor.execute(f'DELETE FROM tasks WHERE id={id}')
    con.commit()

def update_priority(id, state):
    my_cursor.execute(f'UPDATE tasks SET priority = {state} WHERE id={id}')
    con.commit()

def update_done(id, state):
    my_cursor.execute(f'UPDATE tasks SET done = {state} WHERE id={id}')
    con.commit()