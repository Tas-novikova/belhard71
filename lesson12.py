from sqlite3 import connect

conn = connect("db.sqlite3")
cur = conn.cursor()
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS statuses(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name VARCHAR (10) NOT NULL UNIQUE
    );
"""
)
conn.commit()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS users(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name VARCHAR (24) NOT NULL CHECK(name !=''),
       email VARCHAR (24) NOT NULL UNIQUE CHECK(email LIKE '%@%')
    );
"""
)
conn.commit()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS categories(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name VARCHAR (24) NOT NULL UNIQUE CHECK(name !='')
    );
"""
)
conn.commit()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        title VARCHAR(36) NOT NULL CHECK(name !=''),
        description VARCHAR(140),
        FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE RESTRICT
    );
"""
)
conn.commit()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        status_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE RESTRICT,
        FOREIGN KEY (status_id) REFERENCES statuses(id) ON DELETE RESTRICT
    );
"""
)
conn.commit()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS order_items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE RESTRICT,
        FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT
    );
"""
)
conn.commit()

cur.execute(
    """
    CREATE INDEX category_id_index ON products(category_id);
"""
)
conn.commit()

cur.execute(
    """
    CREATE INDEX status_id_index ON orders(status_id);
"""
)
conn.commit()
