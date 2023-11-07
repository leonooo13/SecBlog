---
title: SQLlite For Python
categories: Python
tags:
- Python
- SQLlite
---
# HOW to Use it
```python
conn = sqlite3.connect('./data/eth_gas_price.sqlite3')
cur = conn.cursor()
cur.execute("create table test_tmp as select * from gas_price;")
cur.execute("drop table gas_price;")
cur.execute("""create table gas_price (
                id integer primary key autoincrement,
                coin_name varchar(15) not null,
                low integer not null,
                avg integer not null,
                high integer not null,
                c_time integer not null
            );""")

cur.execute("insert into gas_price select * from test_tmp;")
cur.execute("drop table test_tmp;")
conn.commit()

# 查看所有表
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())
# 查看表结构
cur.execute("PRAGMA table_info(gas_price)")
print(cur.fetchall())
```
